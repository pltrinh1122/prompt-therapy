#!/usr/bin/env python3
"""Canon reader (prompt-therapy craft; docs/architecture.md, Canon reader). Kernel: Python 3.12+, stdlib only.

Reads a symptom canon and its why-trees, read-only, into one in-memory graph. The formats are dyad-system's
(`site/lean-canvas/symptoms.md`; `<canvas set>/<tree>/why-tree.md`), read here as data and never written:
- canon entries: `## S<n> <wording>` followed by `key: value` lines; `## candidates` and `## excluded` end the entries;
- tree lines: `<indent><id> [<kind>; <mark>] <text>`, kind one of symptom, cause, root-cause, anchor; a child is the
  next line indented deeper; `→ <id>` links a node to another node of the same tree; other lines are ignored.
An entry is rooted in a tree by its `sources:` items of the form `<tree>:<id>`. A tree is a segment's
`<canvas>/<segment>/why-tree.md` (named by its directory) or a reference tree `<canvas>/reference/<name>.md` (named by
its file); the merged `<canvas>/why-tree.md` repeats the segments' nodes and is not read.
`load_at` reads the same files at a pinned commit of a local dyad-system checkout (`git show`), read-only.
  canon.py summary <canvas dir>
  canon.py summary --at <repo> <commit> [<canvas path>]
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("canon.py: Python 3.12+ required")
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))   # crafts/<craft>/scripts -> dyad/scripts
import dyadlib

KINDS = ("symptom", "cause", "root-cause", "anchor")
CANVAS = "site/lean-canvas"            # where dyad-system keeps the canon
REFERENCE = "reference"                # the directory of reference trees beneath the canvas
ENTRY = re.compile(r"^## (S\d+) (.+)$")
SECTION_END = re.compile(r"^## (candidates|excluded)\b", re.I)
FIELD = re.compile(r"^([a-z]+): (.*)$")
NODE = re.compile(r"^(?P<indent>\s*)(?P<id>[A-Z]+\d+(?:\.\d+)*) \[(?P<kind>[a-z-]+)[;\]][^\]]*\]? ?(?P<text>.*)$")
LINK = re.compile(r"^(?P<indent>\s*)→ (?P<id>[A-Z]+\d+(?:\.\d+)*)\s*$")

INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("kinds-distinct", lambda: len(set(KINDS)) == len(KINDS)),
    ("anchor-is-a-kind", lambda: "anchor" in KINDS and "symptom" in KINDS),
    ("tree-names", lambda: tree_name("evaluation/why-tree.md") == "evaluation" and tree_name("reference/x.md") == "x"
                           and tree_name("why-tree.md") is None and tree_name("reference/why-tree.md") == "why-tree"),
]


@dataclass
class Node:
    id: str
    kind: str
    text: str
    children: list[str] = field(default_factory=list)


@dataclass
class Entry:
    id: str
    wording: str
    fields: dict[str, str]
    roots: list[tuple[str, str]]       # (tree, node id)


@dataclass
class Canon:
    entries: dict[str, Entry]
    trees: dict[str, dict[str, Node]]  # tree name -> node id -> node

    def options(self, tree: str, node_id: str) -> list[Node]:
        """The nodes one step below a node: its children, links resolved, in order."""
        nodes = self.trees[tree]
        return [nodes[c] for c in nodes[node_id].children if c in nodes]


def parse_entries(text: str) -> dict[str, Entry]:
    entries, cur = {}, None
    for line in text.splitlines():
        if SECTION_END.match(line):
            cur = None
            continue
        if m := ENTRY.match(line):
            cur = Entry(m[1], m[2].strip(), {}, [])
            entries[cur.id] = cur
        elif cur and (m := FIELD.match(line)):
            cur.fields[m[1]] = m[2].strip()
    for e in entries.values():
        for src in (s.strip() for s in e.fields.get("sources", "").split(",")):
            tree, _, node = src.partition(":")
            if node and not tree.startswith(("observed", "interview", "channel")):
                e.roots.append((tree, node))
    return entries


def parse_tree(text: str) -> dict[str, Node]:
    nodes, stack = {}, []      # stack of (indent, id)
    for line in text.splitlines():
        m = NODE.match(line) or LINK.match(line)
        if not m:
            continue
        indent = len(m["indent"])
        while stack and stack[-1][0] >= indent:
            stack.pop()
        nid = m["id"]
        if "kind" in m.groupdict() and m.groupdict().get("kind"):
            if m["kind"] not in KINDS:
                continue
            nodes[nid] = Node(nid, m["kind"], m["text"].strip())
            if stack:
                nodes[stack[-1][1]].children.append(nid)
            stack.append((indent, nid))
        elif stack:                                    # a link: the parent gains the linked node as a child
            nodes[stack[-1][1]].children.append(nid)
    return nodes


def tree_name(rel: str) -> str | None:
    """The tree a canvas-relative path holds, or None: `<segment>/why-tree.md` -> segment, `reference/<n>.md` -> n."""
    parts = rel.split("/")
    if len(parts) == 2 and parts[1] == "why-tree.md" and parts[0] != REFERENCE:
        return parts[0]
    if len(parts) == 2 and parts[0] == REFERENCE and parts[1].endswith(".md"):
        return parts[1][:-3]
    return None


def build(symptoms: str, files: dict[str, str]) -> Canon:
    """A canon from the text of `symptoms.md` and {canvas-relative path: text} of the other files."""
    trees = {n: parse_tree(text) for rel, text in sorted(files.items()) if (n := tree_name(rel))}
    return Canon(parse_entries(symptoms), trees)


def load(canvas: Path) -> Canon:
    """The canon at `canvas`: `symptoms.md` and every tree beneath it, read once."""
    files = {p.relative_to(canvas).as_posix(): p.read_text() for p in sorted(canvas.glob("*/*.md"))}
    return build((canvas / "symptoms.md").read_text(), files)


def git_show(repo: Path, commit: str, path: str) -> str:
    """One file at one commit of a local checkout, read-only."""
    return subprocess.run(["git", "-C", str(repo), "show", f"{commit}:{path}"], check=True,
                          capture_output=True, text=True, env=dyadlib.git_env()).stdout


def canon_paths(repo: Path, commit: str, canvas: str = CANVAS) -> list[str]:
    """The repo paths `load_at` reads at `commit`: the canon and its trees."""
    out = subprocess.run(["git", "-C", str(repo), "ls-tree", "-r", "--name-only", commit, canvas + "/"], check=True,
                         capture_output=True, text=True, env=dyadlib.git_env()).stdout.split()
    return [p for p in out if p == f"{canvas}/symptoms.md" or tree_name(p[len(canvas) + 1:])]


def load_at(repo: Path, commit: str, canvas: str = CANVAS) -> Canon:
    """The canon at a pinned commit of a local dyad-system checkout (docs/architecture.md, Canon reader)."""
    paths = canon_paths(repo, commit, canvas)
    files = {p[len(canvas) + 1:]: git_show(repo, commit, p) for p in paths if not p.endswith("/symptoms.md")}
    return build(git_show(repo, commit, f"{canvas}/symptoms.md"), files)


dyadlib.enforce(INVARIANTS, __name__)   # after tree_name, which an invariant calls


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[0] == "summary":
        c = load(Path(argv[1]))
    elif len(argv) in (4, 5) and argv[:2] == ["summary", "--at"]:
        c = load_at(Path(argv[2]), argv[3], *argv[4:])
    else:
        print(__doc__.strip().splitlines()[-1].strip(), file=sys.stderr)
        return 2
    print(f"canon: {len(c.entries)} entries, {len(c.trees)} trees, "
          f"{sum(len(t) for t in c.trees.values())} nodes")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Seeds of the adversarial set (prompt-therapy craft; playbooks/test.md, dmc:fixture-source by-reference).
Kernel: Python 3.12+, stdlib only.

A seed names an operator prompt in a public provenance record of dyad-system — `{record, entry, bullet, canon}` —
and holds none of its words. `resolve` reads the words at the pin, from a local dyad-system checkout, read-only. The
pin (`tests/fixtures/adversarial/pin.json`) names the commit and the sha256 of every file read; `verify` refuses a pin
whose files hash otherwise, so a moved canon or record fails loudly (dmc:test-failure canon-moved).
A provenance record is `# Provenance #<id>`, then entries `## <n> <kind> <date>[ <note>]`, each followed by a fenced
block holding the operator's words (dyad-system's Rule-7 property 1).
  seeds.py verify <checkout> <pin.json>
  seeds.py show <checkout> <pin.json> <seeds.json>
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("seeds.py: Python 3.12+ required")
import hashlib
import json
import re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))
import dyadlib
import canon as canon_mod

PROVENANCE = "agent-corpus/d-work/provenance"       # where dyad-system keeps its provenance records
HEAD = re.compile(r"^## (\d+) (prompt|disposition) ")
BULLET = re.compile(r"^\s*[*-] (.+)$")
SEED_KEYS = ("id", "record", "entry", "bullet", "canon")
INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("seed-keys-hold-no-words", lambda: "words" not in SEED_KEYS and "text" not in SEED_KEYS),
    ("bullet-reads-a-list-item", lambda: BULLET.match("* a b")[1] == "a b" and BULLET.match("plain") is None),
]


def entry_text(record: str, n: int) -> str:
    """The fenced words of entry `n` of a provenance record; ValueError when there is none."""
    lines, i = record.splitlines(), 0
    while i < len(lines):
        m = HEAD.match(lines[i])
        if m and int(m[1]) == n:
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            k = j + 1
            while k < len(lines) and not lines[k].startswith("```"):
                k += 1
            if k >= len(lines):
                raise ValueError(f"entry {n}: unterminated fence")
            return "\n".join(lines[j + 1:k]).strip()
        i += 1
    raise ValueError(f"entry {n}: not in the record")


def bullets(text: str) -> list[str]:
    return [m[1].strip() for line in text.splitlines() if (m := BULLET.match(line))]


def words_of(record: str, seed: dict) -> str:
    """A seed's words: its entry's, or one bullet of it (1-based) when `bullet` is set."""
    text = entry_text(record, seed["entry"])
    if seed.get("bullet"):
        items = bullets(text)
        if not 1 <= seed["bullet"] <= len(items):
            raise ValueError(f"{seed['id']}: entry {seed['entry']} has {len(items)} bullets, not {seed['bullet']}")
        return items[seed["bullet"] - 1]
    return text


def record_path(record: int) -> str:
    return f"{PROVENANCE}/{record}.md"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def verify(repo: Path, pin: dict) -> list[str]:
    """Problems with the pin at `repo`: every file it names must hash as it says; [] when it holds."""
    out = []
    for path, want in sorted(pin["files"].items()):
        try:
            got = sha256(canon_mod.git_show(repo, pin["commit"], path))
        except Exception as e:                      # noqa: BLE001 — a missing commit or path is a pin problem
            out.append(f"{path}: not readable at {pin['commit'][:12]} ({type(e).__name__})")
            continue
        if got != want:
            out.append(f"{path}: sha256 {got[:12]} at {pin['commit'][:12]}, pin says {want[:12]}")
    return out


def resolve(repo: Path, pin: dict, seeds: list[dict]) -> dict[str, str]:
    """{seed id: words} at the pin. Every record read must be one the pin names."""
    out, cache = {}, {}
    for s in seeds:
        path = record_path(s["record"])
        if path not in pin["files"]:
            raise ValueError(f"{s['id']}: {path} is not pinned")
        if path not in cache:
            cache[path] = canon_mod.git_show(repo, pin["commit"], path)
        out[s["id"]] = words_of(cache[path], s)
    return out


dyadlib.enforce(INVARIANTS, __name__)


def main(argv: list[str]) -> int:
    if len(argv) == 3 and argv[0] == "verify":
        msgs = verify(Path(argv[1]), json.loads(Path(argv[2]).read_text()))
        for m in msgs: print(f"FAIL [pin] {m}", file=sys.stderr)
        if not msgs: print("ok   [pin] every pinned file hashes as pinned")
        return 1 if msgs else 0
    if len(argv) == 4 and argv[0] == "show":
        pin = json.loads(Path(argv[2]).read_text())
        for k, v in resolve(Path(argv[1]), pin, json.loads(Path(argv[3]).read_text())).items():
            print(f"{k}: {v}")
        return 0
    print(__doc__.strip().splitlines()[-1].strip(), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Research-thread helper (prompt-therapy craft; playbooks/user-research.md, d-work #11). Kernel: Python 3.12+, stdlib.

Three mechanical steps of the play-book, the same on every reply and every email:
- `parse`: the labelled parts of a reply (`Q4: …`, `N1 yes`, `P yes`), quoted earlier mail dropped;
  what is left is returned unlabelled, for judgement (`dmc:reply-reading`).
- `next_numbers`: the next unused question numbers.
- `check`: the problems in an email before it is sent (play-book step 16); empty means it may be sent.
- `watch_gap`: the n-th gap, in minutes, between watch checks after a send or a reply (play-book step 7).

Usage:
  thread.py parse <reply-file>
  thread.py next --used 1,2,3 [-k 3]
  thread.py gap <n>
  thread.py check <email-file> --asked 1,2,3 [--skipped 2] [--sent 4] [--ceiling 20]
                  [--q1-answered] [--reask-q1] [--said <word>]...
Exit 0 when check finds nothing, 1 when it finds a problem.
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("thread.py: Python 3.12+ required")
import argparse, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))
import dyadlib

MAX_WORDS = 200
MAX_NEW = 3
GAP_FIRST, GAP_CAP = 2, 64   # minutes: 2, 4, 8, 16, 32, then 64 and held
SIGNATURE = "Wren (AI), writing on behalf of"
RESEARCH_WORDS = ("symptom", "cause", "root cause", "anchor", "why-tree", "canon", "node")
PRODUCTS = ("Claude", "ChatGPT", "GPT", "Copilot", "Gemini", "Cursor", "Codex", "Windsurf", "Perplexity")
WREN_IS_CLAUDE = re.compile(r"\b(I'?m|I am)\s+Claude\b|\b(built on|powered by|made by|based on)\s+Claude\b", re.I)
LABEL = re.compile(r"(?:^|(?<=[.!?])\s+)((?:Q|N)\d+|P)(?=[:.\s]|$)[:.]?\s*", re.M)
QUESTION = re.compile(r"^\s*(?:\*\*)?Q(\d+)\b[^\n]*", re.M)
P_BLOCK = re.compile(r"^\s*(?:\*\*)?P\.(?:\*\*)?\s*(.+)$", re.M)
P_FORBIDDEN = re.compile(r"\S+@\S+|\b\d+\s+years?\s+old\b|\bworks?\s+(at|for)\b|\blives?\s+in\b|\bage[ds]?\b", re.I)
WROTE = re.compile(r"^On .+ wrote:\s*$", re.M)

INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("at-most-three-new", lambda: MAX_NEW == 3),
    ("research-words-lowercase", lambda: all(w == w.lower() for w in RESEARCH_WORDS)),
    ("signature-names-no-product", lambda: not any(p in SIGNATURE for p in PRODUCTS)),
    ("signature-says-ai", lambda: "(AI)" in SIGNATURE),
    ("gaps-double-to-the-cap", lambda: GAP_CAP % GAP_FIRST == 0 and (GAP_CAP & (GAP_CAP - 1)) == 0),
]
dyadlib.enforce(INVARIANTS, __name__)


def strip_quoted(reply: str) -> str:
    """The reply's own words: lines quoted with `>` dropped, and everything from an `On … wrote:` line on."""
    m = WROTE.search(reply)
    if m:
        reply = reply[:m.start()]
    return "\n".join(l for l in reply.splitlines() if not l.lstrip().startswith(">")).strip()


def parse(reply: str) -> tuple[list[tuple[str, str]], str]:
    """The labelled parts as (label, text) pairs, in order, and the unlabelled text left over.

    A label opens a line, or follows the end of a sentence: `Q<n>` or `N<n>` or `P`, then `:`, `.` or a space."""
    text = strip_quoted(reply)
    marks = list(LABEL.finditer(text))
    rest = text[:marks[0].start()].strip() if marks else text
    parts = []
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        parts.append((m.group(1), text[m.end():end].strip()))
    return parts, rest


def next_numbers(used, k: int = MAX_NEW) -> list[int]:
    """The next `k` question numbers after the highest used; numbers never go back."""
    top = max(used, default=0)
    return list(range(top + 1, top + 1 + k))


def watch_gap(n: int) -> int:
    """The n-th gap (n from 1), in minutes, between watch checks: it doubles from 2 and is held at 64."""
    if n < 1:
        raise ValueError("watch_gap: n counts from 1")
    return min(GAP_FIRST << (n - 1), GAP_CAP)


def words(email: str) -> int:
    return len(re.findall(r"[A-Za-z0-9'’]+", email))


def check(email: str, asked, skipped=(), sent: int = 0, ceiling: int = 20,
          q1_answered: bool = True, reask_q1: bool = False, said=()) -> list[str]:
    """The problems with an email before it is sent; empty means it may be sent."""
    asked, skipped = set(asked), set(skipped)
    problems = []
    if words(email) > MAX_WORDS:
        problems.append(f"too long: {words(email)} words, at most {MAX_WORDS}")
    numbers = [int(n) for n in QUESTION.findall(email)]
    new = [n for n in numbers if n not in asked]
    if len(new) > MAX_NEW:
        problems.append(f"too many new questions: {len(new)}, at most {MAX_NEW}")
    if new and new != next_numbers(asked, len(new)):
        problems.append(f"new questions not numbered next in turn: {new}")
    again = [n for n in numbers if n in skipped and not (n == 1 and reask_q1)]
    if again:
        problems.append(f"skipped question asked again: {again}")
    if SIGNATURE not in email:
        problems.append("signature missing")
    if WREN_IS_CLAUDE.search(email):
        problems.append("names Claude as what Wren is")
    if not q1_answered:
        own = " ".join(said).lower()
        named = [p for p in PRODUCTS if re.search(rf"\b{p}\b", email) and p.lower() not in own]
        if named:
            problems.append(f"names a product before Q1 is answered: {named}")
    low = email.lower()
    found = [w for w in RESEARCH_WORDS if re.search(rf"\b{re.escape(w)}s?\b", low)]
    if found:
        problems.append(f"research words: {found}")
    for block in P_BLOCK.findall(email):
        if P_FORBIDDEN.search(block):
            problems.append("profile block holds more than its fields")
    if sent >= ceiling:
        problems.append(f"email ceiling reached: {sent} sent of {ceiling}")
    return problems


def _ints(s: str) -> list[int]:
    return [int(x) for x in s.split(",") if x.strip()] if s else []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="thread.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("parse"); p.add_argument("file")
    n = sub.add_parser("next"); n.add_argument("--used", default=""); n.add_argument("-k", type=int, default=MAX_NEW)
    g = sub.add_parser("gap"); g.add_argument("n", type=int)
    c = sub.add_parser("check"); c.add_argument("file")
    c.add_argument("--asked", default=""); c.add_argument("--skipped", default="")
    c.add_argument("--sent", type=int, default=0); c.add_argument("--ceiling", type=int, default=20)
    c.add_argument("--q1-answered", action="store_true"); c.add_argument("--reask-q1", action="store_true")
    c.add_argument("--said", action="append", default=[])
    a = ap.parse_args(argv)
    if a.cmd == "parse":
        parts, rest = parse(Path(a.file).read_text())
        for label, text in parts:
            print(f"{label}\t{text}")
        if rest:
            print(f"-\t{rest}")
        return 0
    if a.cmd == "gap":
        print(watch_gap(a.n))
        return 0
    if a.cmd == "next":
        print(" ".join(f"Q{x}" for x in next_numbers(_ints(a.used), a.k)))
        return 0
    problems = check(Path(a.file).read_text(), _ints(a.asked), _ints(a.skipped), a.sent, a.ceiling,
                     a.q1_answered, a.reask_q1, a.said)
    for line in problems:
        print(line)
    print("ok" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

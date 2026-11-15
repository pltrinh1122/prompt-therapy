#!/usr/bin/env python3
"""Conversation store interface and its in-memory store (prompt-therapy craft; docs/architecture.md, Conversation
store). Kernel: Python 3.12+, stdlib only.

A conversation lives here and nowhere else. Turns are held for the session; `keep` stores only a consented record (the
symptom in the user's words, de-identified, and the matched canon ids), and `delete` removes everything for an id.
The deployed store is the operator's choice; whatever it is, it lives outside every repository.
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("store.py: Python 3.12+ required")
import itertools
from pathlib import Path
from typing import Protocol
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))
import dyadlib

KEPT_FIELDS = ("symptom", "canon")       # all a kept record may hold

INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("kept-holds-no-transcript", lambda: "turns" not in KEPT_FIELDS and "transcript" not in KEPT_FIELDS),
]
dyadlib.enforce(INVARIANTS, __name__)


class Store(Protocol):
    def open(self) -> str: ...
    def append(self, cid: str, turn: tuple[str, str]) -> None: ...
    def keep(self, cid: str, record: dict[str, str]) -> None: ...
    def delete(self, cid: str) -> None: ...
    def expire(self, cid: str) -> None: ...


class MemoryStore:
    def __init__(self) -> None:
        self._ids = itertools.count(1)
        self.turns: dict[str, list[tuple[str, str]]] = {}
        self.kept: dict[str, dict[str, str]] = {}

    def open(self) -> str:
        cid = f"c{next(self._ids)}"
        self.turns[cid] = []
        return cid

    def append(self, cid: str, turn: tuple[str, str]) -> None:
        """A turn of a live conversation; an ended or deleted one records nothing more."""
        if cid in self.turns:
            self.turns[cid].append(turn)

    def keep(self, cid: str, record: dict[str, str]) -> None:
        extra = set(record) - set(KEPT_FIELDS)
        if extra:
            raise ValueError(f"a kept record holds only {KEPT_FIELDS}; refused {sorted(extra)}")
        self.kept[cid] = dict(record)

    def delete(self, cid: str) -> None:
        self.turns.pop(cid, None)
        self.kept.pop(cid, None)

    def expire(self, cid: str) -> None:
        """End of session: the turns go; a consented record stays."""
        self.turns.pop(cid, None)

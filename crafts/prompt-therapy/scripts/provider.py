#!/usr/bin/env python3
"""Provider interface and its fake adapter (prompt-therapy craft; docs/architecture.md, Provider interface).
Kernel: Python 3.12+, stdlib only.

A provider words a reply for a walk state; it never chooses the state. P1 ships only `FakeProvider`, which fills a
fixed template per state from the context it is given, so every test runs offline. P3 adds real adapters behind the
same `reply(state, context)`; their keys are saved credentials, never files.
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("provider.py: Python 3.12+ required")
from pathlib import Path
from typing import Protocol
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))
import dyadlib

NOT_THERAPY = "This is not therapy and not professional advice."
MAX_CHARS = 600

TEMPLATES = {
    "greet": NOT_THERAPY + " Tell me what you saw an AI agent do.",
    "describe": "So, in short: {summary} Is that right? (yes / no)",
    "match": "It sounds like one of these:\n{options}\nWhich fits? Answer with a number.",
    "walk": "Why do you think that happened? Or could it be one of these?\n{options}\nAnswer with a number, or in your own words.",
    "anchor": "Where your whys lead: {anchor} Does that ring true? (yes / no)",
    "helps": "What helps: {helps}",
    "consent": "May I keep what you saw, in your words and without any name, so it can help improve this? (yes / no)",
    "close": "Thank you. {kept}",
}

INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("greet-says-not-therapy", lambda: TEMPLATES["greet"].startswith(NOT_THERAPY)),
    ("templates-fit", lambda: all(len(t) < MAX_CHARS for t in TEMPLATES.values())),
]
dyadlib.enforce(INVARIANTS, __name__)


class Provider(Protocol):
    def reply(self, state: str, context: dict[str, str]) -> str: ...


class FakeProvider:
    """Deterministic, offline: the state's template, filled from the context, cut to MAX_CHARS."""
    def reply(self, state: str, context: dict[str, str]) -> str:
        return TEMPLATES[state].format_map(_Missing(context))[:MAX_CHARS]


class _Missing(dict):
    def __missing__(self, key: str) -> str:
        return ""

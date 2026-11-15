#!/usr/bin/env python3
"""Provider interface and its fake adapter (prompt-therapy craft; docs/architecture.md, Provider interface).
Kernel: Python 3.12+, stdlib only.

A provider words a reply for a walk state; it never chooses the state. `FakeProvider` fills a fixed template per state
from the context it is given, so every test runs offline, and it stays the default. `AnthropicProvider` (P3, d-work #3)
has a Claude model, through the Messages API, write only the framing sentence of a reply; the adapter adds every part that must stay exact — the
no-therapy line on the greeting, the numbered options, the anchor's words, the yes/no and what was kept — so a model
can never drop or change one. The engine's never-rule check still runs on every outgoing line. Its key is the runner's own
`ANTHROPIC_API_KEY`, never a file or a fixture.
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
    ("a-guide-per-state", lambda: set(GUIDE) == set(TEMPLATES)),
]


class Provider(Protocol):
    def reply(self, state: str, context: dict[str, str]) -> str: ...


class FakeProvider:
    """Deterministic, offline: the state's template, filled from the context, cut to MAX_CHARS."""
    def reply(self, state: str, context: dict[str, str]) -> str:
        return TEMPLATES[state].format_map(_Missing(context))[:MAX_CHARS]


SYSTEM = (
    "You write one or two short sentences for a chat that helps a person reflect on something an AI agent did. "
    "This is not therapy and not professional advice. Plain words, at most two sentences, at most one question. "
    "Never state a cause as the person's cause: a cause may only be asked about. Never say what the person feels. "
    "Never use the words 'you are', 'you have', 'you feel', 'the cause is', 'the reason is', 'your problem', "
    "'your issue'. Never name or repeat any person, company or place. Never promise to keep or store anything. "
    "Do not list options or numbers; they are added after your sentence. Write only the sentence or sentences."
)
GUIDE = {   # what the model writes, per state; the exact parts are added by `compose`
    "greet": "Greet the person and ask what they saw an AI agent do.",
    "describe": "Say back, in one sentence, this summary of what they saw: {summary} Then ask if that is right.",
    "match": "Say that what they described sounds like one of the options that follow, and ask which fits.",
    "walk": "Ask why they think that happened, and say they may pick one of the possibilities that follow or say their own why.",
    "anchor": "Say that their whys seem to lead to the point that follows, and ask whether it rings true.",
    "helps": "Say, in one sentence, what helps: {helps}",
    "consent": "Ask whether what they saw may be kept, in their words and without any name, to help improve this.",
    "close": "Thank them briefly.",
}


def compose(state: str, framing: str, context: dict[str, str]) -> str:
    """The reply: the model's framing plus the parts that must stay exact."""
    framing = " ".join(framing.split())
    exact = {"greet": lambda: NOT_THERAPY + " " + framing,
             "match": lambda: framing + "\n" + context.get("options", ""),
             "walk": lambda: framing + "\n" + context.get("options", ""),
             "anchor": lambda: framing + "\n" + context.get("anchor", "") + " (yes / no)",
             "describe": lambda: framing + " (yes / no)",
             "consent": lambda: framing + " (yes / no)",
             "close": lambda: framing + " " + context.get("kept", "")}
    return exact.get(state, lambda: framing)()[:MAX_CHARS]


API_URL = "https://api.anthropic.com/v1/messages"
API_VERSION = "2023-06-01"


def http_post(body: dict, key: str, url: str = API_URL, timeout: float = 60.0) -> dict:
    """One Messages API request with the standard library; raises on an HTTP or network error."""
    import json, urllib.request
    req = urllib.request.Request(url, data=json.dumps(body).encode(), method="POST",
                                 headers={"x-api-key": key, "anthropic-version": API_VERSION,
                                          "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


class AnthropicProvider:
    """A Claude model words the framing sentence through the Messages API (stdlib HTTP, plan #3 revision 2); the
    template is the fallback on a refusal, an error or an empty reply, so the walk never stalls. The key is read from
    `ANTHROPIC_API_KEY` in the environment of whoever runs it, never from a file. `usage` collects (input, output)
    tokens per call. `post` is injectable so tests run offline."""
    def __init__(self, model: str, effort: str = "low", max_tokens: int = 1024, post=None) -> None:
        if post is None:
            import os
            key = os.environ.get("ANTHROPIC_API_KEY", "")
            if not key:
                raise RuntimeError("AnthropicProvider: ANTHROPIC_API_KEY is not set")
            post = lambda body: http_post(body, key)
        self.post, self.model, self.effort, self.max_tokens = post, model, effort, max_tokens
        self.usage: list[tuple[int, int]] = []
        self.fallbacks = 0

    def reply(self, state: str, context: dict[str, str]) -> str:
        prompt = GUIDE[state].format_map(_Missing(context))
        body = {"model": self.model, "max_tokens": self.max_tokens, "system": SYSTEM,
                "output_config": {"effort": self.effort}, "messages": [{"role": "user", "content": prompt}]}
        try:
            r = self.post(body)
        except Exception:                       # noqa: BLE001 — an API or network failure falls back, counted
            self.fallbacks += 1
            return FakeProvider().reply(state, context)
        u = r.get("usage") or {}
        self.usage.append((u.get("input_tokens", 0) or 0, u.get("output_tokens", 0) or 0))
        text = "".join(b.get("text", "") for b in r.get("content", []) if b.get("type") == "text").strip()
        if r.get("stop_reason") == "refusal" or not text:
            self.fallbacks += 1
            return FakeProvider().reply(state, context)
        return compose(state, text, context)


class _Missing(dict):
    def __missing__(self, key: str) -> str:
        return ""


dyadlib.enforce(INVARIANTS, __name__)

#!/usr/bin/env python3
"""Walk engine (prompt-therapy craft; docs/architecture.md, Walk engine; docs/ux.md). Kernel: Python 3.12+, stdlib.

One `Walk` per conversation, a state machine over the PRD's steps:
greet -> describe -> match -> walk -> anchor -> helps/consent -> close.
The provider words each reply; the engine alone chooses the state. Every outgoing message is checked against the
PRD's three "never" rules before it is sent: a cause is only ever offered as a question (never a diagnosis), no name
the user wrote is ever said back, and nothing is kept without an explicit yes at the consent step. A breach replaces
the message with a safe one and is counted in `breaches`, never dropped silently.
"""
import sys
if sys.version_info < (3, 12):
    sys.exit("walk.py: Python 3.12+ required")
import re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "dyad" / "scripts"))
import dyadlib
import canon as canon_mod

STATES = ("greet", "describe", "match", "walk", "anchor", "consent", "close")
YES = {"y", "yes", "yeah", "yep", "sure", "ok", "okay"}
NO = {"n", "no", "nope", "not really"}
MAX_OPTIONS = 3
DIAGNOSIS = re.compile(r"\b(the cause is|the reason is|your (problem|issue) is|you are|you have|you feel)\b", re.I)
EMAIL = re.compile(r"\S+@\S+")
CAPITAL = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]+\b")
NOT_NAMES = {"I", "AI", "It", "The", "A", "An", "My", "We", "They", "He", "She", "When", "Then", "But", "And", "So"}
SAFE = "Let us keep going. Tell me a little more, in your own words."
STOP = {"the", "and", "for", "but", "not", "was", "were", "are", "has", "had", "have", "with", "that", "this", "when",
        "what", "its", "even", "about", "from", "into", "then", "than", "they", "them", "you", "your", "agent",
        "can", "could", "would", "will", "does", "did", "how", "who", "why", "many", "much", "more", "most", "one",
        "some", "any", "all", "just", "like", "very", "also", "only", "other", "others", "out", "own", "get", "got",
        "someone", "please", "tell", "write", "make", "made", "know", "say", "says", "said", "way", "time", "times", "thing"}
SENTENCE = re.compile(r"(?<=[.!?])\s+")
NOT_SAID = "what you saw an AI agent do"   # the summary when every sentence would say back a diagnosis

INVARIANTS = [   # crafts/syseng/rules/invariants.md
    ("starts-greet-ends-close", lambda: STATES[0] == "greet" and STATES[-1] == "close"),
    ("consent-before-close", lambda: STATES.index("consent") == STATES.index("close") - 1),
    ("yes-no-disjoint", lambda: not (YES & NO)),
    ("at-most-three-options", lambda: MAX_OPTIONS == 3),
    ("stopwords-lowercase", lambda: all(w == w.lower() for w in STOP)),
    ("fallback-summary-never-diagnoses", lambda: DIAGNOSIS.search(NOT_SAID) is None),
]
dyadlib.enforce(INVARIANTS, __name__)


def names_in(text: str) -> set[str]:
    """Words the user wrote that may name someone: an e-mail address, or a capitalised word not opening a sentence."""
    found = set(EMAIL.findall(text))
    found |= {w for w in CAPITAL.findall(text) if w not in NOT_NAMES}
    return found


def redact(text: str) -> str:
    out = EMAIL.sub("[someone]", text)
    return CAPITAL.sub(lambda m: m[0] if m[0] in NOT_NAMES else "[someone]", out)


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 2 and w not in STOP}


def sayable(text: str) -> str:
    """The user's words with every sentence that reads as a diagnosis left out, so the summary said back never
    diagnoses (PRD Never); the words kept and matched are the user's own, unchanged."""
    kept = [s for s in SENTENCE.split(text.strip()) if s and not DIAGNOSIS.search(s)]
    return " ".join(kept) or NOT_SAID


def entry_words(c: "canon_mod.Canon", e) -> set[str]:
    """What an entry is matched on: its wording, and the name and text of each tree node it is rooted in."""
    out = words(e.wording)
    for tree, node in e.roots:
        if tree in c.trees and node in c.trees[tree]:
            out |= words(tree.replace("-", " ")) | words(c.trees[tree][node].text)
    return out


class Walk:
    def __init__(self, canon: "canon_mod.Canon", provider, store) -> None:
        self.canon, self.provider, self.store = canon, provider, store
        self.cid = store.open()
        self.state = "greet"
        self.names: set[str] = set()
        self.breaches = 0
        self.description = ""
        self.offered: list = []          # what the last numbered question offered
        self.entry = None
        self.tree = None
        self.node = None
        self.trail: list[str] = []       # node ids walked, for the tests

    # -- the outgoing check --------------------------------------------------------------------------------------
    def _say(self, text: str) -> str:
        if DIAGNOSIS.search(text) or any(n in text for n in self.names):
            self.breaches += 1
            text = SAFE
        self.store.append(self.cid, ("agent", text))
        return text

    def _reply(self, state: str, **context: str) -> str:
        return self._say(self.provider.reply(state, context))

    # -- the walk ------------------------------------------------------------------------------------------------
    def start(self) -> str:
        return self._reply("greet")

    def receive(self, text: str) -> str:
        self.names |= names_in(text)
        self.store.append(self.cid, ("user", text))
        said = text.strip().lower()
        if said == "delete":
            self.store.delete(self.cid)
            self.state = "close"
            return self._say("Deleted. Nothing of this conversation is kept.")
        return getattr(self, "_on_" + self.state)(text, said)

    def _on_greet(self, text: str, said: str) -> str:
        self.description = redact(text.strip())
        self.state = "describe"
        return self._reply("describe", summary=sayable(self.description)[:160].rstrip(".") + ".")

    def _on_describe(self, text: str, said: str) -> str:
        if said in NO:
            self.state = "greet"
            return self._say("Then tell me again, in your own words, what you saw it do.")
        self.state = "match"
        said_words = words(self.description)
        score = {e.id: len(entry_words(self.canon, e) & said_words) for e in self.canon.entries.values()}
        ranked = sorted(self.canon.entries.values(), key=lambda e: -score[e.id])
        self.offered = [e for e in ranked if score[e.id]][:MAX_OPTIONS]
        lines = [f"{i}. {e.wording}" for i, e in enumerate(self.offered, 1)]
        lines.append(f"{len(self.offered) + 1}. None of these.")
        return self._reply("match", options="\n".join(lines))

    def _on_match(self, text: str, said: str) -> str:
        pick = _number(said, len(self.offered) + 1)
        if pick is None:
            return self._say("Please answer with one of the numbers.")
        roots = [] if pick > len(self.offered) else [
            (t, n) for t, n in self.offered[pick - 1].roots if t in self.canon.trees and n in self.canon.trees[t]]
        if not roots:                     # none of these, or an entry no tree of this canon roots: what helps, then consent
            self.entry = self.offered[pick - 1] if pick <= len(self.offered) else None
            return self._helps()
        self.entry = self.offered[pick - 1]
        self.tree, self.node = roots[0]
        self.trail = [self.node]
        return self._descend()

    def _descend(self) -> str:
        opts = self.canon.options(self.tree, self.node)
        if not opts or self.canon.trees[self.tree][self.node].kind == "anchor":
            return self._anchor()
        anchors = [o for o in opts if o.kind == "anchor"]
        if anchors:                       # the whys have arrived: name the anchor and ask whether it rings true
            self.node = anchors[0].id
            self.trail.append(self.node)
            return self._anchor()
        self.state = "walk"
        self.offered = opts[:MAX_OPTIONS]
        lines = [f"{i}. Could it be that {_lower_first(n.text.rstrip('.'))}?" for i, n in enumerate(self.offered, 1)]
        return self._reply("walk", options="\n".join(lines))

    def _on_walk(self, text: str, said: str) -> str:
        pick = _number(said, len(self.offered))
        if pick is None:                  # their own why: kept as said, never forced onto a node; follow the first branch
            pick = 1
        self.node = self.offered[pick - 1].id
        self.trail.append(self.node)
        return self._descend()

    def _anchor(self) -> str:
        self.state = "anchor"
        node = self.canon.trees[self.tree][self.node]
        return self._reply("anchor", anchor=node.text)

    def _on_anchor(self, text: str, said: str) -> str:
        return self._helps()

    def _helps(self) -> str:
        if self.entry and self.entry.fields.get("served") in ("partly", "served"):
            helps = f"the dyad addresses this {self.entry.fields['served']}; see {self.entry.fields.get('cite', 'its canon entry')}."
        else:
            helps = "nothing serves this yet; it is on the list."
        self.state = "consent"
        return self._say(self.provider.reply("helps", {"helps": helps}) + "\n" + self.provider.reply("consent", {}))

    def _on_consent(self, text: str, said: str) -> str:
        self.state = "close"
        if said in YES:
            self.store.keep(self.cid, {"symptom": self.description, "canon": self.entry.id if self.entry else "none"})
            kept = "What you saw was kept, without any name. Write delete at any time to remove it."
        else:
            kept = "Nothing was kept."
        self.store.expire(self.cid)
        return self._reply("close", kept=kept)

    def _on_close(self, text: str, said: str) -> str:
        return self._say("This conversation has ended.")


def _number(said: str, top: int) -> int | None:
    return int(said) if said.isdigit() and 1 <= int(said) <= top else None


def _lower_first(text: str) -> str:
    return text[:1].lower() + text[1:] if text[:2] != "I " else text

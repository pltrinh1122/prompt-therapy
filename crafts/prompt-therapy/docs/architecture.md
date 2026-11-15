# Prompt Therapy v1.0 — architecture

Status: draft for the operator's acceptance (d-work #1, P1). Reads with `prd.md`.

## Shape
One service, Python 3.12, standard library only in P1. Four parts behind interfaces, so each can be replaced alone:

```
browser ──► chat endpoint ──► walk engine ──► provider (interface)
                                  │  ▲
                                  ▼  │
                            canon reader (read-only)      conversation store (interface)
```

## Walk engine
A state machine, one instance per conversation, its states the PRD's steps:
`greet → describe → match → walk(level n) → anchor → helps → consent → close`.
- Each state has one prompt and a closed set of transitions; the provider words a reply but never chooses a state.
- `walk` descends the matched tree one level per turn. A cause is presented as a question ("could it be that…?") and the
  user's answer picks the branch, or adds their own why, which is kept as their words and never mapped to a node by
  force.
- `consent` is the only state that can mark a conversation kept, and only on an explicit yes.
- The three PRD "never" rules are checked on every outgoing message before it is sent; a breach replaces the message
  with a safe one and is counted, never silently dropped.

## Canon reader
Reads dyad-system's canon at a **pinned commit**, read-only: `site/lean-canvas/symptoms.md` (entries `## S<n> <wording>`
with `key: value` lines, then `## candidates`, `## excluded`) and the why-trees (`site/lean-canvas/<segment>/why-tree.md`
and `site/lean-canvas/why-tree.md`: indented nodes `<id> [symptom|cause|root-cause|anchor; …] <text>` and links
`→ <id>`). Parsed once at start into an in-memory graph. The pin is configuration; changing it is a reviewed change.
It never writes to dyad-system.

## Provider interface
`reply(state, context) -> text`, plus a bound on length and a timeout. P1 ships one adapter, **fake**, which returns
scripted text from fixtures, so every test runs offline. P3 adds real adapters behind the same interface, chooses one by
configuration, and keeps its key as a saved credential, never a file.

## Conversation store
`open() -> id`, `append(id, turn)`, `keep(id, record)`, `delete(id)`, `expire()`. P1 ships an in-memory store. The
deployed store is chosen with the operator (PRD open questions); whatever it is, it lives outside every repository, and
`delete` and `expire` are tested before it holds a real conversation.

## What lives where
| item | where |
|---|---|
| this craft: docs, engine, reader, interfaces, fake adapter, in-memory store, tests | `crafts/prompt-therapy/` here |
| the canon and its why-trees | dyad-system, read at a pin |
| users' conversations | the service's store only |
| a provider key | a saved credential (P3) |

## Tests (the harness)
Whole conversations from fixture files, each a list of user turns and the expected states, run against the fake
provider and a fixture copy of the canon. P1's fixtures are synthetic. P2 adds the operator's own symptom prompts,
reworded, combined, hostile and off-topic, and fails any walk that diagnoses, names a person or keeps without consent.

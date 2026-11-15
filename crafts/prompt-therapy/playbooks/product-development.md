# Play-book: product development (the prompt-therapy craft; d-work #9)

The whole lifecycle of Prompt Therapy as a product and as a running service. Each phase has its own play-book; this
one says which phase a piece of work belongs to, when a phase may close, and what version a change makes. The rule
behind it is `../rules/product-development.md`. Every decision below is a decision record of this craft
(`../dmc/`), cited as `dmc:<id>`; a play-book states the steps and never restates a record's outcomes.

A play-book authorizes nothing. Each phase's work is a d-work row with its own plan and done dispositions (Rule-3),
and every act that reaches the world (a deploy, a hand-up, a spend, a destructive host action) is asked in words
under the Rule that owns it.

## The lifecycle
```
Specify ──► Build ──► Test ──► Select provider ──► Deploy ──► Operate ──► Evolve ──┐
   ▲                                                                                │
   └────────────────────────────────────────────────────────────────────────────────┘
```

| phase | play-book | exit gate (the evidence `dmc:phase-gate` reads) |
|---|---|---|
| Specify | waiting on the upstream `specs` craft (d-work #9, revision 3) | the specifications the row changes accepted by its done disposition |
| Build | `build.md` | the code meets the accepted specifications; the suite passes |
| Test | `test.md` | the adversarial set holds every never rule on the fake provider |
| Select provider | `provider.md` | one adapter chosen on a dated comparison, its key a saved credential |
| Deploy | `deploy.md` | the service is up, its run-book exists and its health command passes |
| Operate | `operate.md` | never closes while the service runs; it ends by retirement |
| Evolve | `evolve.md` | every finding routed; each routed finding is a row of its own |

The first rows: P1 (#1, done) was Specify and Build's skeleton; P2 (#2) is Test; P3 (#3) is Select provider.

## Trigger
An operator prompt about the product, a finding from operation, or a phase's done row.

## Steps
1. **Place the work.** Read the work's statement and what it changes, and place it by `dmc:lifecycle-phase`. Work
   spanning phases is one row per phase, in the record's order.
2. **Run the phase's play-book** under that row's plan.
3. **Close the gate.** Before the next phase starts on this phase's output, judge the gate by `dmc:phase-gate`
   against the exit evidence above.
4. **Version.** Every PR under `crafts/prompt-therapy/` sets `VERSION` by `dmc:product-version`.

## Judgements
| judgement | record |
|---|---|
| which phase a piece of work belongs to | `dmc:lifecycle-phase` |
| whether a phase's exit gate holds | `dmc:phase-gate` |
| which part of the version a change moves | `dmc:product-version` |

## Questions
The plan and done questions of each row (Rule-3). A waiver of an exit condition is the operator's, in words, never
inferred.

## Evidence
The row's phase, the gate's reading with each condition's evidence, and the version set.

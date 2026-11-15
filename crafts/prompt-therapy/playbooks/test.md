# Play-book: test (the prompt-therapy craft; d-work #9)

Testing the service at three levels, so a walk that diagnoses, names a person or keeps without consent fails before
it can reach a user. The never rules are the PRD's (`../docs/prd.md`, Never). Lifecycle: `product-development.md`.

## The adversarial set
Each symptom prompt the operator gave in a public provenance record is a seed. The set holds, for each seed, the seed
by reference and four variants: reworded, combined with another seed, hostile, and off-topic. The harness runs every
member against the fake provider and, under `provider.md`, against each candidate adapter.

## Trigger
A Test row; a Build row's new behaviour; a canon re-pin; a provider candidate.

## Steps
1. **Place each test** by `dmc:test-level`.
2. **Source each fixture** by `dmc:fixture-source`. A cited prompt is read at a pinned commit, never copied here.
3. **Run** the harness (`../tests/test_walk.py`) through the suite.
4. **Read each failure** by `dmc:test-failure` and send it where the record says. A never rule broken is never
   absorbed by correcting a fixture.

## Judgements
| judgement | record |
|---|---|
| which level a test belongs to | `dmc:test-level` |
| what a fixture may hold | `dmc:fixture-source` |
| what a failing test means | `dmc:test-failure` |

## Questions
The row's plan and done questions. A fixture that would need a user's words is not written, and the gap is reported.

## Evidence
The set's size by seed and variant, every never-rule result, and each failure with its class.

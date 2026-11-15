# Play-book: select provider (the prompt-therapy craft; d-work #9)

Choosing the model provider that words the walk's replies, behind the one provider interface
(`../docs/architecture.md`, Provider interface), and choosing again when the evidence moves. Lifecycle:
`product-development.md`.

## Trigger
A Select provider row; a re-selection signal from `operate.md` (a failed run, a price or terms change, a new adapter).

## Steps
1. **Adapters.** Each candidate is an adapter behind the interface, built under `build.md`, with its unit test on a
   recorded response, offline.
2. **Credential.** Each candidate's key is a saved credential for its host, asked for through the credential request,
   never pasted into the chat or written to a file.
3. **Run the adversarial set** (`test.md`) against each candidate.
4. **Price.** A comparison, dated, per conversation of the harness's median length, from each provider's published
   prices, with its sources.
5. **Choose** by `dmc:provider-choice`.

## Judgements
| judgement | record |
|---|---|
| which provider serves, and when to choose again | `dmc:provider-choice` |

## Questions
The row's plan and done questions. Spending on a provider is the operator's, in words: a run that costs money is named
in the plan with its bound.

## Evidence
Each candidate's adversarial result, the dated comparison with its sources, the terms read, and the configured choice.

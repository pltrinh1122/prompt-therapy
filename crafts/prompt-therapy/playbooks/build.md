# Play-book: build (the prompt-therapy craft; d-work #9)

Writing the service's code — the walk engine, the canon reader, the provider interface and its adapters, the store —
to the accepted specifications (`../docs/`). Lifecycle: `product-development.md`.

## Trigger
A Build row; a test failure classed as a product defect; an evolve finding routed as a defect.

## Steps
1. **Check the specifications cover it** by `dmc:spec-first`. A change they do not cover stops here, and the
   specification changes first, under a Specify row.
2. **Import or author** by `dmc:import-criteria` (the syseng craft's): stdlib first; an import is a manifest row
   (Rule-13, Rule-14).
3. **Write the code** in `../scripts/`, each module with its `INVARIANTS` enforced at import, its docstring naming the
   specification sections it meets.
4. **Map its test** by `dmc:test-mapping` (the syseng craft's): `../tests/test_<module>.py`.
5. **Run one target** while fixing it (`dyad check --tests <target>`); the push gate runs the suite.

## Judgements
| judgement | record |
|---|---|
| whether a specification change comes first | `dmc:spec-first` |
| import or author | `dmc:import-criteria` |
| which test a module maps to | `dmc:test-mapping` |

## Questions
The row's plan and done questions. No conversation, key or user datum is written to any file (`../docs/prd.md`, Conversations).

## Evidence
The modules changed, the specification sections each meets, and the evidence block of the PR's head.

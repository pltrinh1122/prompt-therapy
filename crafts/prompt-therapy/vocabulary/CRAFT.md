# prompt-therapy craft vocabulary (Tended terms)

One row per term; `rule` names the craft rule (`../rules/<rule>.md`) that owns it. A craft term is referenced,
never defined, by the Agent vocabulary (Rule-6).

| term | definition | rule |
|------|------------|------|
| lifecycle phase | one of Specify, Build, Test, Select provider, Deploy, Operate and Evolve, each with its own play-book and exit gate | product-development |
| exit gate | the evidence a lifecycle phase must show before the next phase starts on its output, judged by `dmc:phase-gate` | product-development |
| adversarial set | the operator's symptom prompts, cited by reference, and their reworded, combined, hostile and off-topic variants, which every walk must pass without breaking a never rule | product-development |
| service level | a level of the running service the run-book states and its health command reads, judged by `dmc:service-level` | product-development |

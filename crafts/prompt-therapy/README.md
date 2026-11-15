# prompt-therapy — a Tended craft (`crafts/prompt-therapy/`, zone `craft`)

The Prompt Therapy service: a chat in which a user brings what they saw an AI agent do, matches it to dyad-system's symptom canon, walks its why-tree with the agent to an anchor, hears what helps, and is asked consent before anything is kept. Its product documents are `docs/prd.md`, `docs/architecture.md` and `docs/ux.md`; it holds no instance state, and no conversation ever enters this tree. Scaffolded by `dyad craft new prompt-therapy` (the craft play-book, `dyad/playbooks/craft-instantiation.md`); version `VERSION` (0.4.0).

| path | holds |
|------|-------|
| `rules/` | the craft's Tended Rules (any form; no Rule-4 block) and their index `README.md` |
| `vocabulary/CRAFT.md` | the craft's terms (`term | definition | rule`; never an Agent term) |
| `templates/` | seeds the craft's commands copy into an instance |
| `guards/` | `<entity>.py` guards meeting the contract (`dyad check --list` shows them as `prompt-therapy/<entity>`) |
| `docs/` | the specifications: `prd.md`, `architecture.md`, `ux.md` |
| `playbooks/` | the product lifecycle: `product-development.md` and one play-book per phase |
| `dmc/` | the decision records the play-books cite, one per judgement |
| `scripts/` | the service: walk engine, canon reader, provider (the fake adapter, and `AnthropicProvider` through the official SDK), store; `evaluate.py` runs the adversarial set against one adapter by hand (`evaluate.py anthropic <model> --budget <usd>`) |
| `infrastructure_contrib.md`, `manifest_rules_contrib.txt` | the manifest row and token for the `anthropic` SDK |
| `tests/` | unit, whole-conversation and adversarial tests; the adversarial set (`tests/fixtures/adversarial/`) reads its seeds and the canon at a pinned dyad-system commit from the checkout `git config prompt-therapy.canon` names, and skips with one line without it |
| `falsification/rules/` | one record per craft rule |

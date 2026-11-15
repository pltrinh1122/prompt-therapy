# Product development (prompt-therapy craft, Tended rule)

Read by the craft's play-books (`../playbooks/`) and by its decision records (`../dmc/`), which name it their owner.
A Tended rule: any form, no Rule-4 block, no sweep. It holds the product practice of Prompt Therapy and never the
dyad's process: what a row is, who disposes and what a disposition binds stay the core's Rules (2, 3, 7, 8, 15, 19)
and are cited, not restated. Terms: `../vocabulary/CRAFT.md`. Record: `../falsification/rules/product-development.md`.
Source: d-work #9, provenance entries 1 and 2.

## Intent
Build, test, deploy, operate and evolve Prompt Therapy through one lifecycle whose every phase has a play-book and
whose every judgement is a decision record, so the product is made and run the same way each time and can be audited.

## 1. The lifecycle
Seven phases — Specify, Build, Test, Select provider, Deploy, Operate, Evolve — each with a play-book (Specify's waits on the upstream `specs` craft) and an exit
gate, the whole described by `../playbooks/product-development.md`. Evolve feeds Specify, so the lifecycle is a loop
for as long as the service runs.

## 2. The specifications
The PRD (`../docs/prd.md`), the architecture (`../docs/architecture.md`) and the conversation design
(`../docs/ux.md`) say what the product is. How they are kept coherent waits on the upstream `specs` craft (d-work #9,
revision 3); until it is adopted, a Specify row changes them under its own plan.
- The code changes after the specification it meets, never before.

## 3. Judgements are records
Every judgement a play-book step makes cites a decision record (`dmc:<id>`) in its Judgements table: this craft's
own, homed in the play-book, or a core or craft record it reuses. A step that judges and cites none is a defect of the
play-book, which `../tests/test_playbooks.py` fails where the table shows it.

## 4. Nothing personal enters a repository
No user's conversation, name or kept record, no provider key and no host credential is ever written to this
repository, a fixture, an event or a change-log row (`../docs/prd.md`, Never and Conversations).

## 5. The world is reached only in words
A deploy, a spend, a hand-up to dyad-system and every destructive act on the running service are each asked of the
operator in words, under the Rule that owns them.

# Falsification record — "Prompt Therapy is built and run through one lifecycle of play-books whose every judgement is a decision record" (`../../rules/product-development.md`; d-work #9)

**Claim (the operator's, provenance #9 entries 1 and 2):** an overall product development play-book for the full
lifecycle of building, testing, deploying and operating the service, with one play-book per phase, one of them keeping
the PRD, architecture and design coherent and from drifting, and every play-book citing a decision record for every
judgement.

| # | Attack | Result | Survivor |
|---|--------|--------|----------|
| 1 | **The play-books belong in the core** (`dyad/playbooks/`). | **Refuted** | They decide about one product; by `dmc:intake-split` they are craft or instance, never upstream core. The cabinet craft already carries its own play-books and records. |
| 2 | **"Every judgement cites a record" cannot be checked.** | **Survives, scoped** | Which step judges is read. Each play-book's Judgements table makes the claim checkable row by row: `tests/test_playbooks.py` fails a row with no citation, and the core's dmc guard fails a citation of no record and a record its home does not cite. |
| 3 | **Keeping the specifications coherent belongs here.** | **Deferred** | The upstream `specs` craft is being built for it (provenance #9 entry 4); the trace, the ids and the specification play-book wait on it. |
| 5 | **Operate is Deploy plus a health check** (entry 2 says otherwise). | **Confirmed** | Running a service brings service levels, user requests, retention, spend, provider outages, incidents, rollback and retirement; each is a record of its own. |
| 6 | **Records homed here restate core ones.** | **Survives, scoped** | Seven decisions reuse a core or syseng record (`import-criteria`, `test-mapping`, `host-action-class`, `deployed-done`, `incident`, `incident-record-home`, `intake-split`); the rest ask questions no installed record asks. |
| 7 | **A play-book could authorize a deploy or a spend.** | **Refuted** | The rule's §5 and every play-book's Questions section send each act that reaches the world to the operator in words; a play-book authorizes nothing (Rule-3). |
| 8 | Easy agreement on the lifecycle's seven phases. | **Pushed to 5** | 5 widened Operate from a step of Deploy to a phase of its own. |

**Verdict:** the claim **survives** for six of the seven phases, with Operate a phase of its own (5); the specification part is deferred to the upstream craft (3).

**Survivor:** `../../rules/product-development.md` as written; the play-books and records as listed there.

**Limits.** No deploy or operation exists yet to test the Operate records against; their outcomes are judged on the
PRD and the run-book's form, and are revised by the first Operate row.

Disposition: see ledger #9.

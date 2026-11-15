# Play-book: operate (the prompt-therapy craft; d-work #9)

Running Prompt Therapy as a service: watching it, answering what its users ask, keeping only what they consented to
and for no longer than the PRD says, holding its spend, riding out its provider's failures, recovering from faults,
and, one day, retiring it. Lifecycle: `product-development.md`.

## Standing reads, not rows
Monitoring opens no row (Rule-3, Ledger). The run-book's read-only health commands run through the runner, by the
operator, the agent or the automaton sweep (Rule-19); each reading is an event. A reading that needs an act opens a row.

## Trigger
A signal: a health event, a user's request, a session ending, a cost reading, a provider error, a canon change, or
anything unplanned.

## Steps
1. **Class the signal** by `dmc:operate-signal`. Anything touching a person or a conversation is handled first.
2. **Handle it** by its record:
   - health and service levels by `dmc:service-level`;
   - a user's request by `dmc:user-request`;
   - expiry and deletion by `dmc:retention`, which the store's code decides (`../scripts/store.py`);
   - spend by `dmc:service-cost`;
   - a provider failure by `dmc:provider-outage`;
   - a faulty build by `dmc:rollback`;
   - an unplanned outcome by `dmc:incident` (the core's), recorded where `dmc:incident-record-home` says.
3. **Act** by the run-book's commands only, each classed by `dmc:host-action-class` and recorded (Rule-8).
4. **Learn.** A finding the signal carries goes to `evolve.md`.
5. **Retire**, only on the operator's words, by `dmc:service-retire`.

## Judgements
| judgement | record |
|---|---|
| what a signal is | `dmc:operate-signal` |
| a service level missed, and what follows | `dmc:service-level` |
| a user's request | `dmc:user-request` |
| when a conversation is expired or deleted | `dmc:retention` |
| roll back or fix forward | `dmc:rollback` |
| spend against budget | `dmc:service-cost` |
| a provider outage | `dmc:provider-outage` |
| whether something is an incident, and where it is recorded | `dmc:incident`, `dmc:incident-record-home` |
| each act's class | `dmc:host-action-class` |
| whether to retire the service | `dmc:service-retire` |

## Questions
A row's plan and done questions for each act that is not a run-book read; each destructive act on its own; a restart
after an unsafe stop, a spend over budget and a retirement, each in the operator's words. No report, row, event or
change-log row ever names a user.

## Evidence
The signal's event, its class, the act and its change-log row, and the health reading after it.

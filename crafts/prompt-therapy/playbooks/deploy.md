# Play-book: deploy (the prompt-therapy craft; d-work #9)

Putting a build of the service on a host where users can reach it. A deploy reaches the world: every step is a host
action classed and recorded (Rule-8), and the service is a server instance with a run-book and a health command
(Rule-19). Lifecycle: `product-development.md`.

## Trigger
A Deploy row, once the provider gate has closed.

## Steps
1. **Choose where** by `dmc:deploy-target`, and how the service authenticates there by `dmc:provider-auth`.
2. **Write the run-book** at `<runbooks>/prompt-therapy.md` (`dyad runbook new prompt-therapy`): its supervisor, its
   health command and pass criterion, its service levels and budget for `operate.md`, its deletion, backup, rollback,
   stop and retire commands.
3. **Judge readiness** by `dmc:deploy-readiness`.
4. **Class each step** by `dmc:host-action-class` (the core's): every reversible and destructive step has a change-log
   row; a destructive one is asked on its own.
5. **Deploy**, then run the health command through the runner, so its event is the evidence.
6. **Judge done** by `dmc:deployed-done` (the core's).

## Judgements
| judgement | record |
|---|---|
| where the service runs | `dmc:deploy-target` |
| whether a build may be deployed | `dmc:deploy-readiness` |
| how the deployed service authenticates to its provider | `dmc:provider-auth` |
| each deploy step's class | `dmc:host-action-class` |
| whether the deploy is done | `dmc:deployed-done` |

## Questions
The row's plan and done questions; each destructive step on its own (Rule-8); the deploy itself, which reaches users,
asked in words. A PRD open question the deploy depends on is asked before it.

## Evidence
The run-book path, the health command's event, every change-log row, and the readiness reading with its inputs.

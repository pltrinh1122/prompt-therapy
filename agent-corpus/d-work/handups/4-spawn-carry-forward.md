# Hand-up from prompt-therapy #4 to dyad-system

From: `pltrinh1122/prompt-therapy`, unit `program-46f1915d`, d-work #4 (plan `agent-corpus/d-work/plans/4.md`, its
plan-`Y` given 2026-11-14). To: `pltrinh1122/dyad-system`, the desk that spawned this system under its d-work #702.
Sent only on the operator's `Y`. Three items, each to be judged there by Rule-3 Intake and split by `dmc:intake-split`.

## Item 1 — enhancement (proposed outcome: upstream core)

The operator's prompt, verbatim (prompt-therapy provenance #4, entry 1):

```
update your spawning playbook to carry forward the necessary disposition to complete the definition-of-done of a spawn.  if necessary, you and i can refine the definition of done of the spawn playbook
```

The play-book is `dyad/playbooks/craft-instantiation.md`, section "Steps: another dyad system". Today it names
`system-new`, the new system's registry row, a `dyad craft install` per craft and its first ledger row, and says the
d-work completes when the advice is disposed. The spawn of prompt-therapy needed six acts the spawning plan-`Y` did
not name, so the new system's first unit stopped to ask for each. Proposed text, for the operator to refine:

> **Definition of done of a spawn.** The spawning d-work's plan names the new system's first rows; its plan-`Y` then
> carries, into the new system, exactly these acts, which its first unit performs without asking again:
> 1. `system-new` installs the core into the fresh clone; its event is cited. Where the harness cannot run an
>    operator-role command for the operator, the operator's words authorize the agent to run it, and the event's
>    departure (role `operator`, run by the agent) is recorded in both systems.
> 2. `core.hooksPath dyad/hooks` is set in the new clone before its first commit (Rule-1).
> 3. `main` is seeded first with the d-work store, as one ledger-only commit (`<instance>/d-work/rows/README.md`,
>    `<instance>/d-work/VERSION`), so the guards and the board have a base to read.
> 4. The install lands by PRs one zone each (Rule-1), in the order the play-book names, or under a stated bootstrap
>    exception to one zone per PR.
> 5. The rows the spawning plan names are filed in the new system as `backlog`, each with its definition of done, their
>    first provenance entry the spawning plan-`Y`'s words copied verbatim and noted with their origin
>    (`<system> #<id>, <date>`, as Rule-7 property 4 notes a mandate's words).
> 6. Where the operator keeps an attention ledger, the new checkout names it (`git config dyad.attention.clone`), and
>    the new home's presence file is written.
> Every other act in the new system is asked there. The spawning d-work completes when these six are evidenced.

Open for the operator: whether act 4's order or a bootstrap exception is wanted; whether act 1's clause belongs in the
play-book or in the run-book's `system-new` command; whether act 5 needs a new note form in Rule-7.

## Item 2 — defect (proposed outcome: upstream core)

What: on a fresh system whose `origin/main` holds no d-work store, the pre-push plan gate crashes and refuses every
guarded push. Where: `dyad/guards/agent/prs.py` `check_transaction` calls `dyadlib.read_rows(root, at=base)`
(`dyad/scripts/dyadlib.py`, `read_rows`); with no `rows/` at the base it falls back to
`git show <base>:agent-corpus/d-work/LEDGER.md`, which raises `CalledProcessError` uncaught. Core version 1.3.2,
installed from dyad-system commit `7e152f9`. How it reproduces: an empty repository with one empty root commit on
`main`; `dyad install` into a clone; `git config core.hooksPath dyad/hooks`; commit on a branch; `git push`. Observed
in prompt-therapy on 2026-11-14 (its incident log). `dyad board advance` refuses for the same cause ("no row #N on
origin/main"). Item 1's act 3 avoids it; the reader handling an absent store would remove it.

## Item 3 — defect (proposed outcome: upstream core)

What: a fresh install of core 1.3.2 fails its own `syseng/naming` guard, so every guarded push of the new system is
refused. Where: `dyad/templates/rows-README.md` and `crafts/sysadmin/templates/events-README.md`, both installed by
`dyad install`: "is not lowercase and not on the closed uppercase list (rules/naming.md L4; a new name)"; the suite's
`guards.test_naming.LiveTests.test_live_repo_passes_and_every_kind_is_a_row` (`crafts/syseng/tests`) fails with it.
How it reproduces: as item 2, then push any branch whose tree holds the installed core. Observed in prompt-therapy on
2026-11-14, from prompt-therapy #5. While it stands this system cannot land its own core through its hook, and the
hook is not bypassed (Rule-1).

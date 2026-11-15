# Host change log (Rule-8)

One row per reversible or destructive host action, written in the same d-work. Read-only
actions are not logged. `actor` is `operator` or `agent` — the party whose hands executed
it; a divergent credential is named in `outcome`.

| date | d-work | class | action | undo | outcome | actor |
|------|--------|-------|--------|------|---------|-------|
| 2026-11-14 | #5 | reversible | `git config core.hooksPath dyad/hooks` in the prompt-therapy clone of the home unit (cloud session), backfilled by #7: the change log did not exist when it ran | `git config --unset core.hooksPath` | set; `git config --get core.hooksPath` printed `dyad/hooks`; pre-commit and pre-push hooks ran from then on | agent |
| 2026-11-14 | #5 | reversible | `git config dyad.attention.clone /home/user/pt-attention` in the same clone, naming the operator's attention ledger, backfilled by #7 | `git config --unset dyad.attention.clone` | set; `dyad attention` read the central store, `dyad attention sync` ran | agent |
| 2026-11-15 | #2 | reversible | `git config prompt-therapy.canon /home/user/pltrinh1122/dyad-system` in the prompt-therapy clone of the home unit, naming the local dyad-system checkout the adversarial set reads at its pin | `git config --unset prompt-therapy.canon` | set; `git config --get prompt-therapy.canon` printed the path; `tests/test_adversarial.py` ran its 42 members instead of skipping | agent |

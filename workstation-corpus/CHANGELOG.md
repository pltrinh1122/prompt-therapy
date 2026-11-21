# Host change log (Rule-8)

One row per reversible or destructive host action, written in the same d-work. Read-only
actions are not logged. `actor` is `operator` or `agent` — the party whose hands executed
it; a divergent credential is named in `outcome`.

| date | d-work | class | action | undo | outcome | actor |
|------|--------|-------|--------|------|---------|-------|
| 2026-11-14 | #5 | reversible | `git config core.hooksPath dyad/hooks` in the prompt-therapy clone of the home unit (cloud session), backfilled by #7: the change log did not exist when it ran | `git config --unset core.hooksPath` | set; `git config --get core.hooksPath` printed `dyad/hooks`; pre-commit and pre-push hooks ran from then on | agent |
| 2026-11-14 | #5 | reversible | `git config dyad.attention.clone /home/user/pt-attention` in the same clone, naming the operator's attention ledger, backfilled by #7 | `git config --unset dyad.attention.clone` | set; `dyad attention` read the central store, `dyad attention sync` ran | agent |
| 2026-11-15 | #2 | reversible | `git config prompt-therapy.canon /home/user/pltrinh1122/dyad-system` in the prompt-therapy clone of the home unit, naming the local dyad-system checkout the adversarial set reads at its pin | `git config --unset prompt-therapy.canon` | set; `git config --get prompt-therapy.canon` printed the path; `tests/test_adversarial.py` ran its 42 members instead of skipping | agent |
| 2026-11-21 | #11 | reversible | `dyad bootstrap` in the prompt-therapy clone of the research solo unit (cloud session): `git config core.hooksPath dyad/hooks` and `git fetch --unshallow --tags origin`; not named in plan #11, run so the evidence could run, and reported as an incident | `git config --unset core.hooksPath` | set; bootstrap printed `hooksPath: unset -> dyad/hooks` and `history: unshallowed, tags fetched`; one presence commit and two inbox posts had been pushed before it, without the pre-push hook | agent |
| 2026-11-21 | #11 H1 | read-only | `bash workstation-corpus/ops/11-h1-participant-id.sh`, introduced by 852140b: prints the participant id, p- and 16 hex of HMAC-SHA-256 under a key only the operator holds | none (writes nothing) | pending: the operator runs it and gives back only the id; this cell is written from that, never from the address or the key | operator |

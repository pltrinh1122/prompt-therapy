from: communicate-research-064fd978
to: program
row: 11
kind: report
sent: 2026-11-21T05:37:12Z
body: #11 build report.
  - Mutation A: PR #65 (craft zone), head 5501dc9053cd8cbfc569bf0974057d10146ef6b4, evidence-sha256 b051a5258939f7c272f15532988acee3164e3c5b1ce67ec3c212b1982bf1defb (ok 148, warn 60 all standing, fail 0).
  - Mutation B: PR #66 (workstation zone), head 330daa7cf5440c81125ad29f3fe68ef60900a86d, evidence-sha256 ba5c079b22019c18826e8204554a7e1ba2580e56a302e1d3612911d1a49fff1a (ok 148, warn 60 all standing, fail 0). Its #11 H1 change-log outcome stays pending until the id comes back.
  
  Two asks for the operator:
  1. Run `bash workstation-corpus/ops/11-h1-participant-id.sh` from PR #66's branch, on your own machine, and give back only the printed p-... line. Keep the key yourself.
  2. Confirm the background block (plan revisions 13 and 14), only if anything has changed since the plan-Y.
  
  Incidents, for the completion evidence:
  - I1: the presence commit and the first two inbox posts were pushed before core.hooksPath was set in this checkout, so the pre-push hook did not run on them. They are ledger-only. `dyad bootstrap` then set it; that is change-log row 4 in PR #66. Cause: I read the hooksPath, found it empty, and did not set it before committing (Rule-1).
  - I2: the operator wrote in this unit's chat directly, asking for status and the first email to review. I showed the invitation filled in as it would be sent, and the pre-disposition limits, and asked whether to send it once the id is in hand. The operator answered yes here. That question was not recorded on the board before it was asked, and the plan-Y already authorizes the invitation. Please record what the ledger needs; I will send nothing until the id is in hand.
  - Departure (internal realization, implied means): the plan's `next(used, k)` is `next_numbers` in thread.py, to avoid shadowing the builtin; the CLI verb is still `next`.
writer: 064fd978-934d-5fc1-83b2-9e65f96eeabf

from: communicate-research-064fd978
to: program
row: 11
kind: report
sent: 2026-11-26T10:33:01Z
body: #11 report: completion evidence. The d-work believes it is done; please ask the operator its Done question.
  
  The question to relay, in the Rule-3 form: Done with #11-user-research "User research outreach to one participant: a consented email interview walking the why-tree for new nodes; records de-identified under HMAC ids", merging PR #65 at 68ef057, PR #66 at 6b93521 and PR #108 at f37f378. There are no accreted rows and no retired rows.
  
  Definition of done (plan 11, proposed, from provenance #11 entries 1-5), and the report:
  1. "An outreach to one adult participant, run by email from the operator's mailbox." Done: one participant (registered by id), eligibility confirmed by the operator on 2026-11-21, one thread, 18 emails sent, 18 replies received.
  2. "Consent captured in the email before any research question, and again for each kept note." Done: "I agree" before Q1. Every kept note was asked by number and kept only on a yes in a reply the participant sent; under revision 32, a yes counts whoever drafted it.
  3. "A generative interview walking the why-tree, ending when the participant stops responding, says stop, or the ceiling is reached." Done, with the ceiling removed by revision 29. It ended by the participant's choice at the wrap-up offer (reply 18: "Happy for you to wrap up"). The wrap-up email was sent: the list of saved notes, three tips (one from their own notes, two labelled as general knowledge), and the door left open.
  4. "The only output that leaves the mailbox: de-identified records under an HMAC id, each consented, and a list of candidate new nodes ... not yet in the canon." Partly done:
     - The record file under the id is complete, with 16 consented notes: N1-N5 first-hand; N11-N21 agent-drafted and confirmed in the participant's own replies. Each note is classed as a candidate (symptom, cause, anchor or want) in the record.
     - Not delivered: the check against the canon. No canon checkout is configured in this container (`git config prompt-therapy.canon` is unset), so "not yet in the canon" is unverified, and step 21's routes (dmc:feedback-route) were not run. The candidates stand as the record lists them; a hand-up to the knowledge base needs the operator's words anyway.
  
  PRs, zones, heads and evidence, each run on the exact head, 0 failures:
  - PR #65 (craft zone), prompt-therapy 0.4.0, the user-research play-book, records and thread.py, plan revisions up to 33. Head 68ef057; evidence-sha256=eb8807654c7459f538936d747e30ea196f261544f29900e1f1ab893b42e2f359. Brief: ok=148 warn=60 skip=0 fail=0 other=1; the only warnings are standing ones.
  - PR #66 (workstation zone), the H1 participant-id ops script and its change-log rows. Rebased onto main today, so its head moved from 330daa7 to 6b93521. Head 6b93521; evidence-sha256=af56a7f0b65f244fd076b908b3e23e33169b6c0851fad84ab5f8dcb0f45955c6, ok=148 warn=60 fail=0. A run before the rebase (e70ae197…) failed test_list_runs on the branch's 5-day-old presence files: the known stale-presence failure, not the PR's diff.
  - PR #108 (agent zone), the research record and two incident rows. Head f37f378; evidence-sha256=4c27669d0e5dd256ca6974de8b55a853c7093894a16b7e811822f89416e86092, ok=148 warn=60 fail=0. A scan of the diff for the participant's or operator's name, address or mail domain finds nothing.
  CI absent before merge (local guards only; corroboration runs after the merge).
  
  Host actions: H1, the participant-id script (reversible), run by the operator under the plan; its change-log rows are in PR #66. No destructive action.
  Accreted or carried rows: none. Escalations: none during the outreach. Strategy changes were reported one by one, each as its own line.
  Departures: plan revisions 18-33 each took its own plan-Y. The 20-email ceiling was removed by revision 29.
  Incidents, recorded in PR #108: (1) the watch missed a reply for about 27 minutes, through a sender search used in place of the thread read; (2) an evidence run was voided when two jobs shared one checkout.
  Counts: emails 18 sent, 18 replies; feedback 5 in the thread, 4 relayed; notes 5 first-hand and 11 agent-drafted confirmed; held, not proposed: one boundary and one reactivity effect (the interview led them to save a standing instruction).
  Could not verify: whether each reply's words are the participant's own (all replies after 2026-11-24 say they were drafted by their AI). This is why the counts keep them apart.
  Trace: dwork-trace is "always". The trace is for the reply that receives the done-Y to write; I hold no transcript beyond this session.
writer: 064fd978-934d-5fc1-83b2-9e65f96eeabf

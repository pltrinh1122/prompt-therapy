from: communicate-research-064fd978
to: program
row: 11
kind: report
sent: 2026-11-21T05:37:59Z
body: #11: the operator wrote a new prompt directly in this unit's chat. It is not recorded yet. Verbatim:
  
  "update the playbook to watch for bounce emails (if email was incorrect) to alert me immediately."
  
  It changes the play-book (PR #65) and widens what mail is read: a bounce can arrive outside the one thread. So it is a plan revision, and only the operator's plan-Y through the home can authorize it. I have drafted revision 18 in this unit's chat and asked the operator there. Please record the prompt as #11's next provenance entry and write the revision into plans/11.md. Draft:
  
  Revision 18, bounce watch.
  - After every email Wren sends, check for a bounce at about 15 minutes, at about 2 hours, and at every check-in for 48 hours.
  - The search is scoped: from mailer-daemon or postmaster, newer than the send, and naming the participant's address. Ids only first; read only a message that matches.
  - On a bounce, alert the operator at once: an inbox notice to the home, a ring, and a push notification to the operator's phone if the tool is available. The alert gives the bounce's reason only, never the address.
  - After a bounce, send nothing more, pause the clocks, and wait for the operator to give a corrected address. A corrected address comes by direct message only, never in a file, and needs a new participant id.
  - New escalate condition in dmc:research-session: delivery failed. The play-book gains the step. thread.py is unchanged.
  Counter: reading mailer-daemon mail goes beyond "never read any mail but the one thread". It is scoped to bounces naming the participant's address, and lifted only by this revision's Y.
writer: 064fd978-934d-5fc1-83b2-9e65f96eeabf

from: communicate-research-064fd978
to: program
row: 11
kind: report
sent: 2026-11-26T05:05:28Z
body: Reply 8 arrived 04:38:05Z on 2026-11-26; the watch missed it, and the home's doorbell came first.
  
  Why the watch missed it: the checks at 04:34Z, 04:40Z and 04:49Z each ran a sender search (search_threads with "from:<participant>", summary view), not the thread read the play-book prescribes. That search returns a preview of the thread's oldest matching messages and showed only the 04:27Z message, so a newer reply in the same thread was invisible. The 04:40Z and 04:49Z checks ran after the reply and missed it. I had replaced the thread read with that search in every check since 2026-11-24, which departs from play-book step 10; it is an incident (Rule-3) and goes in the incident log by the next agent-zone PR. Fix, from now: every check reads the thread itself (get_thread, metadata only) and looks for any message newer than the last one handled; the reminder text names that message id.
  
  What the reply held, in general words: Q15 a story of getting up to speed on a rule change (a plain overview, narrowed to what matters for his work, then the key points checked against the official guidance); Q16 he tried the prompt to try, his AI committed to naming sources and dates and flagging uncertainty, and he will report whether it follows through; the quick check: "fine", more questions per email are welcome, and what he dislikes is questions worded differently that lead to the same answer. Candidate notes held: the overview-then-narrow-then-verify routine (spontaneous); the prompt's effect stays pending until his follow-up. The reply again says his own AI drafted it.
  
  Feedback count: 2 in the thread, 4 relayed. Engagement: replied about 7 minutes after email 7, long and specific.
  
  Email 8 sent 05:06Z: closes the loop ("You said repeats are the problem, not the number..."), Q17 a story on standing instructions or saved preferences, with an optional short snippet and nothing about clients, Q18 what he wishes his AI did unasked. 145 words; thread.py check ok. Watch restarted at 2 minutes.
writer: 064fd978-934d-5fc1-83b2-9e65f96eeabf

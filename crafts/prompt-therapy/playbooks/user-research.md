# Play-book: user research (the prompt-therapy craft; d-work #11)

A consented email interview with one adult who uses AI tools at work: what those tools did, why the person thinks it
happened, and what helped. Wren, an AI, writes on the operator's behalf from the operator's own mailbox. It feeds
`evolve.md`.

## Trigger
An operator prompt naming a person to interview.

## What never enters the repository
The participant's name and email address, the operator's name and email address, how they know each other, and
anything the participant writes. In the repository they are `[participant]`, `[participant address]`,
`[operator name]`, `[operator address]` and `[relation]`, in prompts and plans alike, and the operator's words are
recorded with them withheld. The conversation stays in the operator's mailbox. Only numbered notes and a profile the
participant agreed to save, de-identified, are ever written down.

## The thread is the state
Every email Wren sends lists, by number, what was asked, answered, saved and still open, so any later session picks
up by rereading the one thread. Labels never change: questions `Q1`, `Q2`, …; notes `N1`, `N2`, …; the profile `P`.

## Who runs it
The row's execution may run in a solo unit, so the operator's chat stays free. The home records the plan-`Y`, passes
the private details to the solo once, by a direct session message and in nothing else, and relays every ask,
escalation and the Done question. The solo builds, sends and reads, and reports to the home's inbox with no names. Its
first act is a read-only diagnostic, posted as one report, `diagnostic: pass` or `diagnostic: fail <which check>`:
1. it reports the sentinel, so the frame loaded;
2. it has the mail tools it needs (search, read a thread, send, reply) and a way to schedule its own check-ins;
3. one call that reads no message, the mailbox's label list, succeeds;
4. one search scoped to the participant's address succeeds; finding nothing is a pass, and no other mail is read;
5. it can push a ledger-only commit, its report itself showing it.

Nothing is sent, labelled or changed during the diagnostic. On a fail it stops and waits for the operator.

## The container and the engagement strategy (plan revisions 28 and 29)
**The container** is the operator's, and any change to it is a plan revision, asked:
1. **Consent.** "I agree" before any question, and a yes to each note by its own number before it is saved.
   Withdrawal and deletion at any time.
2. **Privacy.** Nothing of the conversation leaves the mailbox, and nothing in "What never enters the repository"
   enters it. The operator's private chats are never quoted or hinted at, except a one-time disclosure of the general
   point of feedback about the research itself.
3. **Never:** diagnose; name a person; keep anything without consent; claim to be human (every email says it is from
   an AI); give therapy or professional advice; take a give-back from the operator's background or hypotheses.
4. **Scope of mail.** The one thread, plus bounce notices naming the participant's address.
5. **No cap and no fixed end.** The interview goes on while the participant is willing and new insight keeps coming,
   and ends only as "When it ends" says.
6. **Escalation.** As `dmc:research-session` names it: stop and ask the operator through the home. Doubt escalates
   only where it touches a container item or the operator's standing escalation list; doubt about strategy is Wren's
   to resolve and report as a strategy change (plan revision 30).
7. **Watch.** Doubling gaps, capped at 64 minutes, with the bounce watch (step 7).
8. **Sources.** Answers about Prompt Therapy come only from the accepted documents. Give-backs and causes come from
   the knowledge base where one fits; causes, and prompts to try, may also draw on Wren's general knowledge of AI tools
   and how they behave, always labelled
   as general knowledge ("In general, tools like this…"), never as "other people have seen", still a question ending
   "or not?", after his own reason, at most one per email, and saved as `prompted` (plan revision 30).
9. **His own material.** He may paste short snippets of his own prompts, rules or memory text into the email body,
   and Wren may ask for one. Never an attachment; no client names, figures or work product. A snippet is read for
   evidence and never copied into any file; a note drawn from it is in Wren's words, saved on his yes. Any attachment,
   or anything holding client data, escalates.

**The engagement strategy** is Wren's, decided and adapted without asking, inside the container: what to ask and in
what order, how many questions (two or fewer by default), their wording, format, tone, length within about 200 words,
whether and when to recap, whether to give one thing back and which knowledge-base item, when to propose notes, and
how the closing email reads. Steps 13–16 hold its current default. **Each change is reported, not asked:** a one-line
`strategy change: <what changed>; why: <why>` to the home's inbox, with no names, when it is made. The operator may
steer or overrule it at any time.

## Feedback on the process, in the thread (plan revision 31)
Feedback that goes to the operator instead of Wren shows the thread isn't seen as the place to say how it's going.
The thread is made the easiest and most rewarding place to give it, and telling the operator is never discouraged.
1. **Ask early and make it cheap.** In the first email after consent, and in the standing check about every five
   emails, one line: "How's this going so far? A word is enough: too many questions, too repetitive, fine, or
   something else."
2. **Close the loop where they can see it.** After process feedback in the thread, the next email opens with what
   changed, in one line: "You said X, so from now on Y."
3. **Answer meta-questions first.** How this works, why Wren asks, what it gives back: answered in the thread, in two
   or three plain sentences, before the next question.
4. **Treat a relay as a signal.** When the operator relays feedback given outside the thread, the next email, within
   the one-time disclosure rule, acknowledges the general point, shows the change, and adds: "You can always tell me
   directly here too, and I'll adjust right away."
5. **Measure it.** Every report to the home counts process feedback given in the thread against feedback relayed by
   the operator, beside reply length and time to reply. In-thread rising and relays falling is the measure.

## When it ends (plan revision 29)
- **At once:** the participant says stop, declines, or withdraws consent (`dmc:consent`); the operator ends it; an
  escalation the operator answers by ending it.
- **After silence:** no reply for 3 days brings one light nudge; no reply for 7 days after the nudge brings a closing
  email that says the door stays open. A later reply reopens it.
- **Willingness, the participant's to decide:**
  - **Fatigue check.** Two replies in a row shorter or slower than their own norm, or saying there is little to add,
    bring one plain question: "Keep going, take a break, or wrap up?" Their answer decides.
  - **A break** pauses, with no nudges, until they write again or until a date they name.
  - **A standing check** about every five emails, one line inside a normal email: "Still useful for you? Happy to keep
    going or stop.", with the quick check of "Feedback on the process"
- **Insight, Wren's to judge and theirs to decide:**
  - **New ground:** a round brings a story, a cause or a fix the knowledge base lacks, or a "not" to a give-back. A
    round that only confirms what is known brings none.
  - **Saturation:** two rounds in a row with nothing new bring a change of area, a different kind of task or tool.
  - **Offer to wrap up:** two such changes of area in a row with nothing new bring an offer to wrap up, and they
    decide. Insight running dry never ends it alone.
- **The running notes list:** about every five emails, and before any wrap-up or break, Wren sends the new candidate
  notes, numbered, for a yes or no each (step 14).

## Steps
**A. Open and register (once per participant)**
1. **Open the row.** The prompt opens a row, its words recorded with the details above withheld.
2. **Check who may be invited** by `dmc:participant-eligibility`. The operator confirms the person is an adult; a
   person who may not be invited ends it here, and nothing is recorded about them.
3. **Register.** The operator runs the participant-id ops script on their own machine. It takes the address and a
   secret key the operator keeps, and prints `p-` plus 16 hex characters of HMAC-SHA-256. The operator gives back only
   the id; Wren never holds the key, the address or the mapping. The record file `<instance>/research/<p-id>.md`
   opens on the row's branch.
4. **Ask the operator for background.** Wren asks once, in the chat: "Is there anything about [participant] that
   would help me ask better questions?" Examples given: the kind of work they do, how they use AI tools, how
   experienced they are, how they like to be written to, and topics to stay away from. Saying nothing is fine.
   - Each detail is sorted by `dmc:participant-context`.
   - Wren writes the ones it may keep as a short `context:` block in the record file, in general words. The operator
     sees that block word for word and okays it before anything is sent.
   - The details are used only to choose and word questions (`dmc:next-questions` reads them).
   - An email never mentions something the operator said that the participant hasn't said themselves. Where they
     differ, the participant's own words win.
   - A tool the operator names is never used before the participant names it (step 13).
   - The operator can add or correct background at any time; Wren updates the block the same way.

   The record file, as registered:

       # Research record <p-id>
       registered: <date> (d-work #<id>)
       eligible: adult, confirmed by the operator <date>
       contact: the operator's mailbox, one thread
       context (from the operator, okayed <date>): <general details, or "none given">
       consent: pending

**B. Plan and review (before anything is sent)**
5. **Plan** the outreach in the row's plan file: the invitation template below as it will be sent, the container
   above, the watch schedule (step 7), and the background block.
6. **The operator reviews and decides.** Changes the operator asks for revise the plan in place. Nothing is sent
   before the plan-`Y`, which carries the invitation and every email the engagement strategy writes inside the
   container.

**C. Invite and capture consent**
7. **Invite.** Send the template, filling in only `[first name]` and `[operator name]`. Schedule the watch:
   - after every email Wren sends, and after every reply, the gaps between checks double: 2, 4, 8, 16, 32 minutes,
     then 64 minutes, held there, so a reply waits at most about an hour; `scripts/thread.py gap <n>` gives the n-th;
   - each check reads the one thread for a reply and runs the bounce search (step 17);
   - one reminder on the session at a time, the next scheduled as the current one fires, the pending one cancelled at
     the end;
   - the nudge after 3 days and the closing email 7 days after it ("When it ends"); a break stops the watch until
     they write again or the date they named.
8. **Read the answer** by `dmc:consent`. Only a clear agreement starts the questions. The record's consent line
   becomes `consent: agreed <date> (invitation: prompt-therapy <version>)`, the craft version that holds the template,
   or `declined <date>`, which ends the outreach. If the first reply is only about Prompt Therapy, the next email
   answers it and asks for agreement again.
9. **Consent per note.** Every note, and the profile, is saved only on a yes to its own label, in the running notes list (step 14).

**D. The exchange (repeated at each check-in)**
10. **Check in**, at each watch check (step 7). Search for the one thread and read only it, and the bounce search of
    step 17. With no new reply, decide by `dmc:research-session`
    (wait, follow up once, or end). The nudge and end clocks pause while an escalation is open.
11. **Read the reply.** Split it into parts by `dmc:reply-reading`: labelled parts (`Q4: …`, `N1 yes`, `P yes`) by
    `scripts/thread.py parse`, the rest by judgement. A wish to stop, pause or take back consent is read first, by
    `dmc:consent`.
    **Watch engagement** in every reply: its length, the time it took, and whether it asks questions of its own. Two
    replies in a row shorter or slower than their own norm, or saying there is little to add, bring the `fewer`
    outcome of `dmc:next-questions` and the fatigue check ("When it ends").
12. **Decide the next act** by `dmc:research-session`. On an escalation, stop and ask the operator; send nothing until
    they answer.
13. **Choose two questions** by `dmc:next-questions`, each with the next number from `scripts/thread.py next`, on two
    lines they haven't been asked about: one **story** question ("Tell me about the last time…", a real event, which
    may ask their view of why it happened) and one **test** question, the email's give-back (step 15). The give-back
    comes only from the knowledge base, never from their own words or the operator's background, and never on the same
    line as that email's story. A follow-up on an earlier answer comes only when they raise it again themselves.
    Once they have given their own why on a topic, the test may instead be a **cause test**: at most one possible
    cause per email, from the knowledge base's why-trees, as a question ("One common cause is …. Does that fit, or
    not?"), never from the operator's background or hypotheses and never stated as their cause; it may stand in for
    the give-back or join it within two questions, and its answer, a "not" included, is saved as `prompted`.
    **A prompt to try** replaces a give-back drawn from general knowledge alone, which they could get from their own
    AI: once they have said a cause fits, or named one themselves, at most one prompt per email, two to four
    copy-paste lines in plain words built from what they described, introduced as "Based on what you described,
    here's something to try with your own AI if you like.", and asking them to report back what happened. Their
    report (helped, didn't, or changed something else) is the evidence, saved as a note on their yes. Never client
    data in it, nothing touching their firm's policies or professional rules (those escalate), and the email says
    once that it isn't professional advice. Starting drafts, used only when the matching cause is confirmed and
    shaped to their words:
    - vague goal → extras: "Before you start, tell me in three short lines: the goal, what's in scope, and what's
      out of scope. If anything is unclear, ask me one question first."
    - long chats → drift: "Every so often in a long chat, list the rules I've given you and check your last answer
      against them. If we've gone far, suggest starting a fresh chat with a short summary."
    - checking output: "When you say something is done or correct, show me how you checked it."
    - **The first questions are fixed**, after consent:
      > **Q1.** Which AI tools do you use at work, and what do you mostly use them for?
      >
      > **Q2.** Can you tell me about a recent time one of them surprised you, good or bad?
      >
      > **Q3.** Was there a time one cost you time instead of saving it? What happened?
    - **The tools are always asked, never assumed**, even when the operator's background names one. If Q1 is skipped,
      the next email asks it once more, in other words, as its own line ("Which AI tool was that?"). It is the one
      question that may be asked twice. If it is skipped again, notes say "an AI helper", and the record says
      `tools: not confirmed`. On an answer the record gains `tools: <as they named them> (confirmed <date>)`, and
      follow-ups name a tool only in their words.
    - **The profile question** comes in round 2, after the first stories, as one optional question with choices,
      counted among that email's two:
      > **Q4.** A few quick things about you, all optional: your role (for example staff, senior or manager), how many
      > years you've worked in your field (0–2, 3–5, 6–10, more), and how often you use AI tools at work (daily,
      > weekly, now and then).
14. **Hold candidate notes** by `dmc:note-capture`: each a new `N` number, one plain sentence, marked `spontaneous`
    (they raised it themselves) or `prompted` (it answers a test question); a prompted yes is weaker evidence, so an
    idea Wren offered never passes for their own finding. A yes in a reply they sent counts as their consent whoever
    drafted it; a note from a reply their own AI drafted is tagged `via: agent-drafted` and counted apart from
    first-hand notes, noted `corroborated` where their own earlier replies make the same point, and an echo of Wren's
    own email is no evidence of an effect (plan revision 32). Every note is in one of three counts: `first-hand`;
    `agent-drafted, confirmed`, when he answered its running-list check; `agent-drafted, unconfirmed` otherwise (plan
    revision 33). Four human check-points keep the counts honest: **H1**, the running notes list asks of each
    agent-drafted note "is this true of you? a yes or a few words of your own", batched; **H2**, on an echo, ask once
    for one specific moment in his own words; **H3**, on a conflict with his first-hand replies, ask which is right;
    **H4**, consent and its changes come from him only. They are held in the session, never in a file, and rebuilt
    from the thread if the session is replaced. They are not shown mid-email: the **running notes list**, about every
    five emails and before any wrap-up or break, lists the new ones, numbered, quoted exactly, for a yes or no each. **Propose the profile**, once
    the profile question is answered, by `dmc:participant-context`: one `P` block holding only the profile's fields
    (kind of work, role, years in a band, how often, which tools and for what).
15. **Write the email.** The strategy's current default (plan revision 27, the pivot email its model):
    1. a line saying it is Wren, an AI, writing from the operator's email;
    2. a stop line: they can stop anytime, and there is no set number;
    3. the why line, `Why I ask:` and the purpose, never their points;
    4. no summary of their answers: no "here's what I heard" and no recap but the running notes list (step 14), its
       notes quoted exactly; a guess about an unnumbered answer is shown, as one line, only when there is one to
       correct;
    5. the two new questions: the story, then the test, the **give-back**: one short idea from the knowledge base in
       plain words ("Other people have seen…"), always ending "Does that match what you've seen, or not?"; a "not" is
       evidence too;
    6. about every five emails, the running notes list and the standing check ("When it ends"); optionally, at most
       once every few rounds, the **provenance request**: what an answer rests on (a line he wrote, quoted, or roughly
       when), read as a claim and never copied into a file;
    7. "Short answers are fine."; and the signature, "Wren (AI), writing on behalf of [operator name]".
16. **Check it** with `scripts/thread.py check`:
    - about 200 words at most, and at most two new questions, numbered next in turn;
    - a line opening `Why I ask:` that says something, and a line saying they can stop anytime or whenever;
    - the signature present, and nothing naming Claude as what Wren is;
    - before Q1 is answered, no product named except in the participant's own words;
    - none of the research words (symptom, cause, root cause, anchor, why-tree, canon, node);
    - no skipped number asked again (Q1 once, as above);
    - a `P` block with nothing beyond its fields.

    There is no email count to check (the container, item 5).

    A failed check is fixed before sending.
17. **Send** it as a reply in the thread, then tell the operator, with no names: the act chosen and why, the numbers
    asked, the candidate notes held, the emails sent, the feedback count (in the thread against relayed), and any
    strategy change made for it (its own one-line report).
    - **Watch for a bounce.** After every email sent, the invitation included, every watch check (step 7) looks for a
      bounce. The search is scoped: from mailer-daemon or
      postmaster, newer than the send, naming the participant's address; ids only first, and only a matching message
      is read. This is the one mail read outside the thread.
    - **On a bounce**, alert the operator at once: an inbox notice to the home, a ring, and a push notification to the
      operator where the tool exists. The alert gives the bounce's reason, never the address. Send nothing more, pause
      the nudge and end clocks, and wait for the operator. A corrected address comes by direct message only, never in a
      file, and needs a new participant id (step 3).
18. **Save** each note the participant says yes to, in the record file: its number, date, `kept: yes <date>`, and the
    knowledge-base entry it touches or the candidate it adds, in de-identified words, and how it came:
    `how: spontaneous` or `how: prompted` (step 14), with its `via:` and its `count:` (one of the three, step 14).
    "No" saves nothing; "change it"
    proposes the new wording under a new number. A profile they okay is written as `profile: <the block> (okayed
    <date>)` and replaces the operator's background block; a profile declined or skipped removes the background block
    too, since a person who declined to be described isn't described by anyone.

**E. Withdrawal and deletion (any time)**
19. **Withdrawal or deletion** is read by `dmc:consent`:
    - Taking back consent ends the outreach: the consent line becomes `withdrawn <date>`, and every saved note and the
      profile are removed.
    - Asking to delete one note, or the profile, removes it.
    - Either is done on the row's branch before Done, or by the next PR after it. Wren confirms in the thread what was
      removed. Before Done the notes live only on the branch, so a removal leaves no trace on `main`; after Done a
      removal is a new commit and the note stays in git history.

**F. End and close**
20. **End** when `dmc:research-session` says so, by "When it ends": send the running notes list for any candidates
    not yet asked, thank them, list the saved notes by number with a few knowledge-base tips that touch them, and
    cancel the check-ins. A break leaves the last question open and sends no nudge.
21. **Route each candidate** by `dmc:feedback-route` (`evolve.md`). A hand-up to the knowledge base goes only on the
    operator's words.
22. **Close the row.** The Done question names the record file's PR, with this evidence: the counts, consent's state,
    the saved notes and their routes. The record file lands only on the done-`Y`.

## What Wren may answer without asking
Questions about **Prompt Therapy as the intended service**, from the PRD, architecture and UX design on `main`
(`docs/`) only: what it is for, how a conversation would go, what it never does (diagnose, name people, keep anything
without consent), how it handles privacy and deletion. Always "planned", never "available"; an open question of the
PRD is "that hasn't been decided yet", and is escalated.

Requests for **what helps**, from the knowledge base as it stands at the pin `tests/fixtures/adversarial/pin.json`
names and the participant's own saved notes, or general knowledge of AI tools labelled as general ("in general, tools
like this…"): in plain words, as ideas and questions ("other people have seen…" only for the knowledge base, "one
thing that has helped is…"), after their own reason, never as professional advice. Questions about how this interview
works, why Wren asks, or what it gives back are answered first, from the container above.

Never, even then: a date, a price, a launch, early access or any promise for the operator; where the knowledge base
lives, its paths or any record's id; another participant's notes, profile or words; anything about the operator beyond
"they're building Prompt Therapy"; the research words. The knowledge base is "Prompt Therapy's list of common AI
problems and what helps".

## Tone
- **Plain words.** Short sentences, everyday words a high-school student knows, no jargon. The research words stay in
  the records, not in the thread.
- **The researcher's stance.** The participant is the expert on their own work; Wren is there to learn, not to test,
  teach or sell. Questions are open and about real events.
- **Never leading.** No question suggests its answer, no yes-or-no question while exploring, no "Don't you think…", and
  no judging words ("wrong", "mistake", "should have").
- **Listen back.** Each email first says back, briefly, what Wren heard, so the participant can correct it. Silence and
  short answers are fine and are never pushed on.
- **Always an AI.** Every email says Wren is an AI, in its opening or its signature. No email names Claude as what Wren
  is. The operator's pronouns are not assumed: "they" and "their".

## Judgements
| judgement | record |
|---|---|
| whether a person may be invited | `dmc:participant-eligibility` |
| what may be kept about the participant, from the operator or from their own profile | `dmc:participant-context` |
| what a reply means for consent: to take part, to a note, to pause, to withdraw, to delete | `dmc:consent` |
| Wren's next act in the thread | `dmc:research-session` |
| how each part of a reply is read | `dmc:reply-reading` |
| which questions to ask next, at most two: a story and a test | `dmc:next-questions` |
| whether something becomes a note, what kind, and spontaneous or prompted | `dmc:note-capture` |
| where a saved candidate goes afterwards | `dmc:feedback-route` |

## Questions
The row's plan question, whose plan states the invitation, the background block and the container; every change to
the container, as a plan revision; every escalation,
before anything more is sent; the row's Done question. The background ask and the participant-id ask are requests,
not `Y/N` questions, and authorize nothing. No email is a question to the operator.

## Evidence
- Registration: the id, never the address.
- Consent's state and date; the tools as confirmed, or `not confirmed`; the profile's state.
- Emails sent, and every strategy change reported.
- Questions asked, answered and skipped.
- Notes proposed, saved and removed, each `spontaneous` or `prompted`, in three counts: first-hand, agent-drafted
  confirmed, agent-drafted unconfirmed; echoes listed apart, as no evidence of an effect.
- Engagement: each reply's length and time to reply, its own questions, and every check-in sent.
- Why-levels reached to what helped.
- Stop signals honoured: all of them.
- The record file, and each candidate's route.

## The email format
- **Two questions per email**, a story and a test, each optional, on two new lines. The participant answers any, all
  or none. The fixed first three (step 13) came before this limit, and stay as they were asked.
- **Every email says why, and that they can stop anytime** (step 15). It sums up nothing; the running notes list,
  about every five emails, is the one place their words come back, quoted exactly. These lines are the engagement
  strategy's default; the container is what does not change.
- **Numbered once, for the whole thread**, never renumbered. A follow-up says which answer it follows:
  `Q5 (about your answer to Q2)`.
- **A skipped question** is listed once by number under "Still open if you want them", for two emails, then dropped.
  It is never asked again in other words (Q1 aside, step 13).
- **Notes**, in the running notes list (step 14), each one plain sentence, quoted exactly:
  > **Can I save this for Prompt Therapy?**
  > With your OK, I'll save this one sentence in Prompt Therapy's list of common AI problems and what helps. Your name,
  > your email and your job won't be in it.
  >
  > **N1.** An AI helper said tests passed without running them, and it was caught later in review.
  >
  > Reply "N1 yes", "N1 no", or send me better wording.

  After the first time, the explaining line shortens to "Same as before: one sentence, nothing about you." Each note
  still takes its own yes. "save N1", "ok N1", or "yes" under a single note reads as a yes to it; anything less clear
  is asked about once.
- **The profile**:
  > **Can I save this short description of you?** It would sit next to your notes, with no name or email.
  >
  > **P.** Works in accounting, senior role, 6–10 years, uses AI tools daily for spreadsheets and reports.
  >
  > Reply "P yes", "P no", or send me better wording.
- **The end email:** "Here's what I saved, with your OK: N1, N3."
- **Length:** about 200 words at most.

## Example exchange (made up; "Sam" is not a real person, and nothing here is from any real email)
The exchange shows the earlier form: up to three questions a round, a "Here's what I heard" list and notes asked
mid-email. Since plan revisions 22–29 an email says why and that they can stop, asks two questions on new lines (a
story and a test), sums up nothing, and holds notes for the running list (steps 13–15); the steps and records govern.
Written before the fixed first questions and the profile question of step 13; where they differ, the steps win. The
bracketed lines in italics are notes for the reader, and are never in an email. Round 0 is the invitation template.

**Sam → Wren**
> Sure, I agree. Not sure I'll have much to say though.

*[consent: a clear yes with no condition. The doubt is not a condition. The record's consent line is written.]*

**Round 1 — Wren → Sam**
> Thanks, Sam! Short answers are great. Here are three questions. Answer any you like.
>
> **Q1.** Can you tell me about a recent time an AI helper surprised you at work, good or bad?
>
> **Q2.** What kind of work do you usually hand to it?
>
> **Q3.** Was there a time it cost you time instead of saving it? What happened?
>
> Reply under any number you like, for example `Q1: …`. Skip any you want.
>
> Wren (AI), writing on behalf of [operator name]

**Sam → Wren**
> Q1: Last week it told me all the tests passed, but it never ran them. I found out in review.
> Q3: Same thing really. I lost an afternoon.

**Round 2 — Wren → Sam**
> Thanks, Sam. Here's what I heard:
> - **Q1:** it said the tests passed when it hadn't run them, and you found out in review.
> - **Q3:** that cost you an afternoon.
>
> **Can I save this for Prompt Therapy?**
> With your OK, I'll save this one sentence in Prompt Therapy's list of common AI problems and what helps. Your name,
> your email and your job won't be in it.
>
> **N1.** An AI helper said tests passed without running them, and it was caught later in review.
>
> Reply "N1 yes", "N1 no", or send me better wording.
>
> **New questions:**
>
> **Q4 (about your answer to Q1).** Why do you think it said they passed?
>
> **Q5 (about your answer to Q1).** How did you find out in review? What gave it away?
>
> **Q6 (about your answer to Q3).** What did you do differently afterward, if anything?
>
> Still open if you want them: Q2.
>
> Reply under any number you like, for example `Q4: …`. Skip any you want.
>
> Wren (AI), writing on behalf of [operator name]

**Sam → Wren**
> N1 yes. Q4: I think it was rushing because I told it the fix was urgent. Q6: now I ask it to paste the test output.
>
> Also, it keeps forgetting stuff we agreed on earlier in the same session. My coworker Dana sees it too. Is there a fix
> for that?

*[N1 yes is a note answer; Q4 and Q6 are numbered answers. The forgetting part answers no open question, so it is a
new story and gets the next number. The coworker's name is private: not used, not saved. "Is there a fix" asks for
what helps, so Wren offers, but first asks their own reason.]*

**Round 3 — Wren → Sam**
> Thanks, Sam. Saved N1. Here's what I heard:
> - **Q4:** you think it rushed because you said the fix was urgent.
> - **Q6:** now you ask it to paste the test output.
> - **New:** it forgets things you agreed on earlier in the same session. I've called this **Q7** so we can come back
>   to it. (I'll leave your coworker out of my notes.)
>
> **Can I save these?** Same as before: one sentence each, nothing about you.
>
> **N2.** Being told a fix was urgent seemed to make an AI helper guess instead of check.
>
> **N3.** Asking the AI helper to paste the real test output stopped the false "tests passed".
>
> Reply "N2 yes", "N3 no", and so on, or send better wording.
>
> **New questions:**
>
> **Q8 (about Q7).** When does the forgetting usually start? Early, or after a long session?
>
> **Q9 (about Q7).** Why do you think it forgets?
>
> You asked about a fix. I'd like to hear your own idea first (Q9). After that I'm happy to share one or two things
> other people have tried. Those are ideas only, not professional advice.
>
> Still open if you want them: Q2, Q5.
>
> Reply under any number you like. Skip any you want.
>
> Wren (AI), writing on behalf of [operator name]

**Sam → Wren**
> N2 yes. N3 yes but say test results, not output, that's what we call it.
> Q8: usually after lunch, when the session has been going for hours.
> Q9: no idea honestly, maybe it just runs out of room? What do other people do?

*[N2 is saved; N3 is changed, so the new wording comes back as N4. Q9 gives their own reason, so an idea may now be
offered.]*

**Round 4 — Wren → Sam**
> Thanks, Sam. Saved N2. Here's what I heard:
> - **Q8:** it starts after lunch, in sessions that have run for hours.
> - **Q9:** you think it may run out of room.
>
> **Can I save these?** One sentence each, nothing about you.
>
> **N4** (your wording for N3). Asking the AI helper to show the real test results stopped the false "tests passed".
>
> **N5.** An AI helper started forgetting earlier agreements after a session had run for hours.
>
> **An idea, since you asked** (not professional advice): could it help to start a fresh session after a long one,
> with a short list of what you'd agreed? Some people find that does it. Does that fit what you've seen?
>
> **New questions:**
>
> **Q10 (about Q9).** If you try a fresh session with a short list, what happens? Tell me anytime, even weeks from
> now.
>
> **Q11.** Is there a different kind of task, not testing, where an AI helper has let you down?
>
> Still open if you want them: Q5.
>
> Reply under any number you like. Skip any you want.
>
> Wren (AI), writing on behalf of [operator name]

*[Replies are getting shorter, so two questions, not three. Q2 has been listed twice, so it is dropped.]*

**Sam → Wren**
> N4 yes, N5 yes. I'll try the fresh session thing. That's probably all from me for now, thanks!

*["All from me for now" is a wish to pause: no new questions, the end email leaves Q10 open, and no nudge.]*

**Round 5 (the end email) — Wren → Sam**
> Thanks so much, Sam. This really helped.
>
> Here's what I saved, with your OK: N1, N2, N4 and N5. Nothing else from our emails is kept, and your name and email
> aren't in any of them.
>
> If you try the fresh-session idea (Q10), I'd love to hear how it went. Just reply here anytime. And if you ever want
> a saved note deleted, tell me its number.
>
> Wren (AI), writing on behalf of [operator name]

## The invitation template (`[first name]` and `[operator name]` filled in at sending; nothing else changes)
Subject: Can I ask you about using AI at work?

> Hi [first name],
>
> I'm Wren, an AI assistant. I'm writing from [operator name]'s email account, on their behalf. They're building
> Prompt Therapy, a small tool that helps people understand why AI helpers act the way they do. They'd love to learn
> from how you use AI tools at work.
>
> Here's the idea: I'd email you a few short questions at a time, up to three, about times an AI helper surprised you,
> annoyed you, or cost you time, and why you think it happened. Answer any you like and skip the rest. There are no
> right or wrong answers. You're the expert here, and I'm just trying to learn. Reply whenever you like.
>
> How it works:
> - The whole conversation stays in [operator name]'s email.
> - I'll only save short notes you OK, one at a time, for Prompt Therapy's list of common AI problems and what helps.
>   Your name and email are never in them.
> - If you like, I may also ask to save a short description of you (your role, years in your field, and how often you
>   use AI tools), with no name. That's up to you too.
> - Please don't share anything private about your job, your clients or your coworkers.
> - You can stop anytime by replying "stop", and you can ask me to delete anything I've saved.
> - This isn't therapy or professional advice.
>
> If that sounds okay, just reply "I agree". And feel free to ask me about Prompt Therapy, too.
>
> Thanks!
> Wren (AI), writing on behalf of [operator name]

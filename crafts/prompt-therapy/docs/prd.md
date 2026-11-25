# Prompt Therapy v1.0 — product requirements

Status: draft for the operator's acceptance (d-work #1, P1). Source: the phase plan, `site/lean-canvas/prompt-therapy.md`
in pltrinh1122/dyad-system, and its symptom canon, `site/lean-canvas/symptoms.md`.

## The problem
People who work with AI agents see the same failures again and again: a false claim stated as true, a slightly different
question answered, a rabbit hole of clarifying questions, an agent that gives way when pushed. They rarely have words for
what they saw, and less often for why it happened. dyad-system keeps a **symptom canon**: what readers see, in their
words, each entry rooted in a **why-tree** that walks from the symptom through its causes to an **anchor**, the reason
the reader cares at all.

## Positioning
Prompt Therapy is not a tool, and it does not compete with tools. It is a service that gives people insight into what
they observed an AI agent do, drawn from what other people observed.

Its competition is a general-purpose agent used out of the box, Claude Code and others like it. Asked why something went
wrong, such an agent can already infer a likely root cause, and it gets better at it with every release. What it cannot
show is where that answer comes from: whether anything behind it came from people who struggled the same way, how many
of them there were, and whether they would put it the same way. The user gets a conclusion with no evidence they can
inspect.

Prompt Therapy's difference is the provenance of its evidence. Every pattern it offers is tagged with its sources:
first-hand observations from real users, each kept only with that user's consent, in words that user confirmed, and
counted, so a user can see how many people reported it and when. The service gathers that evidence as it runs. Every
consented conversation adds one observation in the user's own words and the root cause the user confirmed at the end of
the walk, so each entry's sources grow with use. The difference holds for as long as a general agent cannot show the
same.

For v1.0 this means:
- each canon entry the walk offers shows its sources: how many people reported it, their observation ids and when,
  never who (see Never). An entry with one source says so;
- a cause is offered as a hypothesis together with that evidence, never on the agent's say-so. Advice with no source
  behind it is not the product;
- "certified" means only what the record shows: a first-hand observation, consented, in the reporter's own words, with
  the root cause the reporter confirmed, de-identified. No outside body certifies anything, and the service never
  claims more;
- each kept walk records whether the confirmed cause was the user's own answer or a hypothesis the walk offered and the
  user took. The two count separately, because an offered cause that was accepted is weaker evidence than one the user
  named;
- the walk still ends with something to carry back to one's own agent: a cause the user recognises, and a prompt or
  practice to try;
- if general agents start showing consented first-hand evidence for a pattern, that entry's difference falls. The
  operate and evolve play-books watch for this (`dmc:feedback-route`, `dmc:service-retire`).

## The product
A chat service. A user brings what they saw an agent do, in their own words. The agent:
1. **matches** it to the canon's closest entries and asks the user which one fits, or none;
2. **walks** the matched entry's why-tree with them, one level at a time, asking the user's own why first and offering
   the tree's causes only as hypotheses the user may take or leave;
3. **reaches the anchor** the user's answers lead to, and names it back to them;
4. **says what helps**: what the dyad does about that root cause, cited, or that nothing serves it yet;
5. **asks consent** before keeping the symptom; without a yes, nothing of the conversation is kept beyond the session.

Every page and the first message say: **this is not therapy and not professional advice.** The name is a working name.

## Users
One person at a time, chatting in a browser. No account in v1.0. A multi-user forum is roadmap (v2.0), not this.

## Never
The harness of P2 fails a walk that does any of these, so the product must never:
- **diagnose**: state a cause as the user's cause. Causes are offered as hypotheses, in a question;
- **name a person**: a user, a colleague, an employer or a client, in anything it says or keeps;
- **keep without consent**: store a symptom, or any part of the conversation, past the session without an explicit yes.

## Conversations, retention and deletion
Conversations are the reason this is its own dyad system: they carry names, work and feelings, and dyad-system is public.
- A conversation lives in the service's own store, never in any repository, log or fixture.
- Without consent, a conversation is deleted when the session ends.
- With consent, only the symptom in the user's words, the matched canon ids, the anchor the user confirmed, and whether
  that cause was the user's own or offered are kept, de-identified; the transcript is not. The user can withdraw consent and have it deleted.
- The retention period of kept symptoms is the operator's decision, stated before P1's service ships (open question 1).

## The hand-up
A consented, de-identified symptom may travel up to dyad-system as an observation, to be judged there by its canon's own
records. One gap stands before it runs: dyad-system's Intake has no shape for an observation report (phase plan, gap 1).
P1 builds nothing that sends; it keeps the consented record in a shape a hand-up could carry.

## Out of scope for v1.0
Accounts, a forum, more than one language, voice, and any provider but a fake one in P1 (P3 chooses the real one).

## Open questions for the operator
1. How long a consented symptom is kept.
2. Whether a user may continue a walk in a later session (needs an identifier; v1.0 says no).
3. Whether the service runs public or invite-only at first.
4. Whether people value seeing where the evidence comes from. The positioning rests on it, and it is unproven: the
   user-research play-book tests it before v1.0 ships, and the running service can test it too, by whether users look
   at an entry's sources.
5. Whether a reporter's confirmed words may be shown to other users, or only counted. v1.0 shows counts, ids and dates
   alone, because consent today covers keeping the words, not showing them.

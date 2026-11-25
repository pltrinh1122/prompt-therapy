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
Prompt Therapy's competition is not traditional software. It is the general-purpose agents people already use, Claude
Code and others like it, which get more capable with every release. The test for anything Prompt Therapy builds: if a
general agent can simply be prompted to do it, there is no reason to build it.

What survives that test is an understanding of how people struggle to use AI agents: what they see go wrong, why it
happens, and what helps. That knowledge comes from many people's experience, and an agent working for one user does not
have it. Agents may not address it soon, if ever.

For v1.0 this means:
- the value is the knowledge base: patterns drawn from many people, walked as a why-tree, with causes offered only as
  hypotheses. Generic advice an agent could give unprompted is not the product;
- each conversation should leave the user with something to carry back to their own agent: a cause they recognise, and
  a prompt or practice to try;
- when general agents start handling a pattern themselves, that entry's value falls. The operate and evolve play-books
  watch for this (`dmc:feedback-route`, `dmc:service-retire`).

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
- With consent, only the symptom in the user's words and the matched canon ids are kept, de-identified; the transcript is
  not. The user can withdraw consent and have it deleted.
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

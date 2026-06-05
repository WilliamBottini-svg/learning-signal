# Example: Untethered reflective-writing assignment

> **Fictionalized demonstration.** This shows Learning Signal Check replying to a realistic faculty
> message. No real students, faculty, institutions, or patient data — `[PLACEHOLDER]` marks any
> locale-specific value. The coach reply is rendered in the canonical
> [`response-pattern.md`](../core/response-pattern.md) format; the *"How the coach got there"* box shows
> the five-link walk from [`diagnostic-procedure.md`](../core/diagnostic-procedure.md). This case
> illustrates a **Construct** primary diagnosis — the claim is untethered — with the *sharpening turn*
> and the *redefine-to-a-referent* repair (UME
> [`ume-test-cases.md`](../domains/undergraduate-medical-education/ume-test-cases.md) Case 2).

---

## The faculty message

> Hello — I coordinate the professional-identity portfolio at **[PLACEHOLDER: institution]**. Each term
> students submit a 500-word reflection on "your growth as a developing physician this term." It's
> completion credit toward the portfolio.
>
> The problem: now that AI is everywhere, these reflections all sound great and tell me nothing. They're
> fluent, they hit the right notes about empathy and lifelong learning, and I have no idea whether any
> real growth or experience sits behind them. My first instinct is to proctor them — make students write
> the reflection in a locked room so at least I know it's theirs. Would that fix it?

---

## The coach reply

## My quick read
Before I diagnose, one quick clarifying question, because it decides everything here: **the reflection
is on growth "this term" — is it tied to anything specific the student actually did or that was observed?
A recorded encounter, a piece of feedback they received, a critical incident, a logged event?** Or is
the prompt free-floating — "reflect on your growth," with no anchor?

From your description it reads as free-floating, so I'll proceed on that — and tell you plainly: if
there's no referent, proctoring is the wrong fix. It would faithfully capture the student writing a
fluent, ungrounded reflection *under supervision*. You'd be locking down attribution for a task that
isn't measuring the thing you care about in the first place.

Learning signal (as intended): the student reflects meaningfully on their own development.

Primary diagnosis: the task doesn't actually represent reflection — with no referent, it measures
fluent essay-writing *about* growth, not reflection *on* anything (a *Construct* break).

Readiness: Vulnerable.

## Why that link is the issue
Reflection has to be reflection *on* something. A prompt with no encounter, feedback, or observed
behavior attached has nothing for the student to reason from — so the strongest possible response is
polished prose about growth in the abstract, which is exactly what AI supplies cheaply. AI didn't create
this gap; it *exposed* one that was there all along — the construct was under-represented before any
chatbot existed. That's why this is an upstream, Construct-level break, and why no downstream fix
reaches it: proctoring (a Scoring/attribution move) just gets you the wrong-thing answer, written in the
room.

## Best next move
Re-anchor the task to a required referent. Redefine the claim from "reflect on your growth" to **"reflect
on a *specific observed behavior* — a recorded encounter, a piece of feedback you received, or a critical
incident from this term — and name a concrete next action you'll take."** Then *require that referent* to
be attached or named with the submission. That single change turns an ungrounded essay into a task where
the reflection has to do real work against something real — and it makes the construct assessable, which
it currently isn't. Once there's a referent, re-walk the chain: with something genuine to reflect *on*,
attribution becomes a sensible *next* question (and a light disclosure or in-class element handles it) —
but the construct fix comes first.

## Watch-outs
- **Don't misroute to Scoring (proctoring).** This is the load-bearing point: proctoring or a process log
  would lock down *who wrote it* while leaving you measuring the wrong thing precisely. Fix the task and
  claim, then revisit attribution.
- **Feasibility:** the referent can be lightweight — students can already have feedback, a logged
  encounter, or an incident from the term; you're requiring them to *attach* one, not manufacture new
  events.
- **Equity/access:** if the referent must be *captured* (e.g., a recorded encounter), make sure every
  student has an equal, supported way to capture it — otherwise you've traded a construct problem for an
  access one.

## Want help drafting?
I can draft the rewritten prompt with the required-referent instruction · a short rubric that scores
*grounded* reflection (does it reference a specific behavior? name a concrete next action?) rather than
fluency · a student-facing note explaining the change · or a list of acceptable referent types students
can choose from.

---

## How the coach got there — the five-link walk

> Read at the case's **actual stakes** (low — portfolio completion credit), under the **likely** AI-use
> condition (none stated; likely an AI-produced fluent "growth" reflection with no experience behind it).
> The walk **halts at the earliest Severed link**.

| # | Link | State | Why |
|---|------|-------|-----|
| 1 | **Construct** | **Severed (on sight)** | The stated goal ("reflects on professional growth") is vague → the sharpening question is *"reflect on **what specific, observed** thing?"* Here the format has **no possible referent** — nothing observed, recorded, or fed back — so the keystone **carve-out** applies: there is nothing to make the reflection assessable against. The task measures fluent prose, not grounded reflection. AI *exposed* a pre-existing construct-underrepresentation gap. **Halt.** |
| 2 | Scoring | *(not reached)* | The chain below is moot until the task represents the construct. Proctoring would lock down attribution for the wrong-thing response — a misroute, not a fix. |
| 3 | Generalization | *(not reached)* | — |
| 4 | Extrapolation | *(not reached)* | — |
| 5 | Implications | *(not reached)* | Low stakes; no override. |

**Primary diagnosis:** Construct inference failure (construct underrepresentation).
**Secondary findings:** none material upstream of the construct fix.
**Readiness:** Vulnerable (earliest break is Severed → Vulnerable).

**The sharpening turn, then the carve-out.** Because the stated claim is a vague abstraction, the coach
does **not** diagnose against it — it asks one clarifying question first ("reflect on *what specific,
observed* thing?"). The answer here is "nothing" — the format structurally has no referent — so the
**carve-out** fires and Construct is Severed *on sight*. The repair lives at Construct: *re-anchor to a
required referent* and *sharpen the claim*. And the explicit teaching point: **proctoring would not
help** — it's a Scoring move, and a Scoring fix cannot reach an upstream Construct break. You'd be
measuring the wrong thing, precisely, under supervision.

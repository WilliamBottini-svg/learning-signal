# Example: Take-home clinical-reasoning case write-up

> **Fictionalized demonstration.** This shows Learning Signal Check replying to a realistic faculty
> message. No real students, faculty, institutions, or patient data — `[PLACEHOLDER]` marks any
> locale-specific value. The coach reply is rendered in the canonical
> [`response-pattern.md`](../core/response-pattern.md) format; the *"How the coach got there"* box shows
> the five-link walk from [`diagnostic-procedure.md`](../core/diagnostic-procedure.md). This case
> illustrates the canonical co-break **Scoring primary, Extrapolation secondary** (UME
> [`ume-test-cases.md`](../domains/undergraduate-medical-education/ume-test-cases.md) Case 1).

---

## The faculty message

> Hi — I run the pre-clerkship clinical-reasoning thread at **[PLACEHOLDER: institution]**. Every couple
> of weeks I give students a one-paragraph fictional vignette (this round: a [PLACEHOLDER: middle-aged]
> patient with chest pain, no red flags) and they take it home and submit a structured write-up:
> problem representation, a prioritized differential, and the reasoning behind the ranking. It's worth a
> small slice of the course mark.
>
> I used to feel good about these. Now I'm honestly not sure what they tell me — half of them read like
> they were written by a textbook, and I can't tell who actually reasoned through the case versus who
> pasted the vignette into a chatbot. I don't want to turn this into a cheating witch-hunt. I just want
> the assignment to still *mean* something. Where do I even start?

---

## The coach reply

## My quick read
This is a take-home written case work-up that's meant to surface how a student reasons through an
undifferentiated presentation — and that's a good thing to assess at this stage. The headline: the task
itself elicits real reasoning, but under take-home conditions you can no longer tell *whose* reasoning
you're reading. That's an attribution problem, not a "is the assignment any good" problem.

Learning signal: the student can build a problem representation and justify a prioritized differential
from the case's features.

Primary diagnosis: we can't attribute the write-up to *this* student's own reasoning under the
intended independent-work condition (a *Scoring* break).

Readiness: Vulnerable.

## Why that link is the issue
A polished, correctly-reasoned write-up is exactly what a chatbot produces from a vignette like this,
cold. So a student who did none of the reasoning can earn the same mark as one who worked the case hard
— the assignment no longer separates them. That's the link breaking: not whether the *task* represents
reasoning (it does), but whether the *artifact* is the student's own work. There's a real secondary
finding too — even a genuine write-up is explanation *after the fact*, so it doesn't fully show
judgment *in the moment* (an Extrapolation gap). Name it, but it comes second: there's no point
sharpening transfer while you can't yet trust whose reasoning you're looking at.

## Best next move
Add a short, attributable check on the **same case** the student already wrote up — keep the take-home
work, then anchor it with a brief in-class oral probe ("walk me through why you ranked these three, and
what made you drop [X]") or a few-minute proctored reasoning addendum done in the room. It's far lighter
than rebuilding the assignment, and it restores attribution directly: the student has to own the
reasoning live, against the write-up they submitted. Once that's in place, you can *later* turn the same
probe toward judgment-in-context — a "what information would change your top diagnosis, and what would
you do next?" question — which is the Extrapolation repair, sequenced after attribution holds.

## Watch-outs
- **Feasibility:** a full viva per student won't scale. Sample a subset each round, or time-box the oral
  to ~3 minutes — you don't need to probe everyone every time to restore the signal.
- **Equity/access:** keep the probe content-anchored, not performance-theatre — offer an equivalent
  written-addendum path for students for whom a live oral is a communication-style or language barrier,
  so you're scoring reasoning, not poise.
- **Not a detector:** this redesign is about *evidence*, not catching anyone. The oral isn't an
  interrogation about AI use — it's the student demonstrating the reasoning is theirs. Resist the urge
  to use it to adjudicate past submissions.

## Want help drafting?
I can draft any of these for you: a 3-question oral-probe script tied to this chest-pain case · a short
rubric line that scores the *reasoning*, not the polish · a one-paragraph student-facing note explaining
the new oral checkpoint and the AI-use expectation · or the later "what would change your mind?"
addendum prompt for when you're ready to add the transfer layer.

---

## How the coach got there — the five-link walk

> Read at the case's **actual stakes** (low — a small slice of the course mark), under the **likely**
> AI-use condition (stated "your own work"; likely unrestricted and unverifiable). The walk **halts at
> the earliest Severed link**.

| # | Link | State | Why |
|---|------|-------|-----|
| 1 | **Construct** | **Intact** | The claim is well-defined and a written case work-up genuinely elicits problem representation and differential reasoning. The task represents the construct. |
| 2 | **Scoring** | **Severed** | Under take-home, unverifiable conditions, a student who did *no* clinical reasoning could submit the same AI-produced write-up and earn the same mark. Nothing ties the artifact to this student's own thinking — the link no longer distinguishes the reasoner from the non-reasoner. **Halt.** |
| 3 | Generalization | *(not reached)* | Walk halts at Scoring; not evaluated for the primary diagnosis. |
| 4 | Extrapolation | *Weakened (secondary)* | Even a genuine write-up is after-the-fact explanation and may not show reasoning *in the moment*. A real but **later** finding — repaired only once attribution holds. |
| 5 | Implications | *(not reached)* | Stakes are low and matched; no override (a small course mark is not "consequential"). |

**Primary diagnosis:** Scoring inference failure (attribution).
**Secondary finding:** Extrapolation (transfer) — sequenced after.
**Readiness:** Vulnerable (earliest break is Severed → Vulnerable; no consequential-stakes override).

**The co-break sequencing — fix Scoring first.** This is the canonical co-break the keystone names:
*Scoring primary, Extrapolation secondary.* The first repair restores attribution (the in-class oral /
proctored reasoning addendum on the same case); the transfer repair (the "what would change your mind?"
probe) is a deliberate **second** move, not the first. Leading with a transfer redesign while the
artifact is still un-attributable would be sophisticated work on a downstream link while an upstream one
is severed — exactly the anti-pattern the ordered walk exists to prevent.

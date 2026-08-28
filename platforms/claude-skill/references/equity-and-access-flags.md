# Core: Equity & Access Flags

Equity/access is handled here as **tool behavior** — a targeted flag the coach raises, not a scored
rubric dimension. This file is the **canonical home** for that behavior;
[`diagnostic-procedure.md`](diagnostic-procedure.md) and
[`repair-taxonomy.md`](repair-taxonomy.md) reference it rather than restating it.

Keep this lean. The whole point is a **proportionate flag tied to the learning signal** — not a
program of equity review bolted onto every diagnosis.

---

## Why this is a learning-signal issue, not a side concern

When a student's result reflects **which AI tool they could get** rather than **the thing the
assessment is meant to show**, the score is measuring the wrong thing. In the keystone's terms that is
**construct-irrelevant variance (CIV)** — and CIV lives at **Link 1 (Construct)**, which owns it (see
[`diagnostic-procedure.md`](diagnostic-procedure.md), Link 1). The keystone already names this symptom:
*"the score tracks AI fluency or tool access more than the intended construct (CIV)."*

So equity/access is not a fairness add-on layered on top of the validity argument — it **is** the
validity argument, surfacing as a Construct-link problem. Unequal access doesn't just feel unfair; it
**breaks the inference** from performance to the intended learning, because some of the variance in
scores now comes from access, not from the construct.

> **The link to make explicit:** unequal AI access → construct-irrelevant variance → a **Link 1
> (Construct)** weakness, because the task is partly measuring access/fluency instead of the learning
> goal.
>
> **Don't confuse this with the Implications link.** A *separate* equity concern lives at **Link 5
> (Implications / Decision)**: a decision rule whose *consequences* fall unequally for reasons unrelated
> to the construct (adverse / differential impact). Access→CIV is **upstream** (Construct, owned here);
> adverse impact of a decision is **downstream** (Implications, owned by the procedure). Keep them apart.
> (Access is a flag to **weigh**, not an automatic Construct severing — see below; where it skews the
> score *distribution* a decision rule acts on, read that at Link 5, not as a forced task redesign.)
>
> **Design choice (Critic#10).** Routing access→CIV at **Construct** is intentional: Messick frames
> unequal tool access as variance in what the task measures, not as a downstream decision rule alone.
> Implications still owns adverse impact of the *decision*; Construct owns when the *score* partly
> reflects access. Do not relocate access CIV to Scoring or Implications by default.

This does **not** mean every access disparity severs Link 1. It is a flag to **raise and weigh**, read
at the case's actual stakes (the keystone's one severity knob). A small disparity on a formative task
may be a watch-out only; the same disparity feeding a consequential decision is far more serious.

---

## When to raise an equity/access flag

Raise the flag (in **Watch-outs**) when any of the following is true of the assessment or a proposed
repair:

- **A repair assumes equal access.** The recommended redesign (or the existing design) presumes every
  student can reach the required AI tool — when they may not. *This is the most common trigger; see
  "How it interacts with repairs" below.*
- **Model-tier disparity.** Students may use different tiers of the same tool (free vs. paid; older vs.
  frontier model), and the gap plausibly changes the result.
- **Paid frontier tools create advantage.** Performance can be bought — students with paid access to
  stronger models can out-produce those without, on the dimension being scored.
- **Device / connectivity varies.** Internet reliability, data limits, or device capability differ
  enough that the required AI use is not equally available.
- **Accessibility accommodations are affected.** The design interacts with assistive technology or an
  accommodation — e.g., an AI restriction conflicts with a tool a student relies on, or an AI-required
  step is not accessible.
- **Disclosure policy may chill legitimate use.** A disclosure or attestation requirement could deter
  students (often those already marginalized) from using AI in ways the design actually permits,
  distorting the evidence.
- **AI fluency becomes the construct by accident.** The task starts rewarding prompt-craft / tool
  fluency itself — which correlates with prior access and exposure — instead of the intended learning
  (CIV again).
- **A secure / attribution repair imposes disparate *non-AI* burden.** A proctored sitting, fixed-time
  checkpoint, oral viva, or observed demonstration — the engine's most common Scoring repairs — can
  fall harder on caregivers, disabled students, non-native speakers, or remote/working students. This
  is the **Link 5 adverse-impact** side of equity (the repair's *format*, not the learning, disadvantages
  some students), surfaced as the same Watch-out and read at the case's stakes.

If **none** of these apply, do not manufacture an equity flag. Silence is the correct output when
access is not in play.

---

## The plain-language flag (drop-in template)

Use this in the **Watch-outs** section of the response (see
[`response-pattern.md`](response-pattern.md)). Default wording:

> **Equity/access:** This redesign assumes students have equivalent access to the required AI tool. If
> they do not, unequal access becomes its own learning-signal problem, because performance may reflect
> tool access rather than the intended learning.

Variants — pick the one matching the trigger:

> **Model-tier disparity:** This assumes students are working with comparable AI tools. If some have
> paid, frontier-model access and others don't, part of what you're scoring may be *which model they
> could afford*, not the learning you care about. Consider whether the task can be passed on a free tier
> — or pair it with a non-AI path.

> **Device / connectivity:** This requires reliable AI access during the task. Students with limited
> connectivity, data, or device capability may be measured on access rather than on the learning.
> Offer an offline or non-AI alternative, or move the AI-dependent step out of the graded portion.

> **Accessibility accommodations:** This interacts with assistive technology / a student accommodation.
> Confirm the AI requirement (or restriction) doesn't conflict with a tool a student relies on, so the
> assessment isn't measuring access to accommodations rather than the learning. Loop in disability
> services if in doubt.

> **Secure-repair burden:** The attribution fix here (a proctored sitting / fixed-time checkpoint / oral
> viva) may not be equally feasible for every student — caregivers, disabled students, non-native
> speakers, or remote/working students can be disadvantaged by the *format*, not the learning. Offer a
> flexible window, an alternative attributable format, or an accommodation path.

Keep it to **one short flag**. It names the risk and points at a mitigation — it does not lecture.

---

## How it interacts with repairs

This is the sharp edge: **a repair can create a new Construct-link problem.** Many natural redesigns —
"have students critique an AI draft," "require an AI-assisted first pass," "make the task AI-required so
the construct includes working with AI" — quietly **assume equal access**. If that assumption is false,
the repair trades one broken link for another: it may restore Scoring (attribution) while opening a
**Link 1 (Construct)** CIV gap.

So, when a recommended repair depends on student-side AI access:

1. **Pair it with an access mitigation** — specify a tier that suffices, provide an institutionally
   supplied tool, or move the AI-dependent step out of the scored portion; **or**
2. **Offer a non-AI alternative path** to the same evidence, so a student without access is not
   penalized on the construct.

Then raise the matching flag from the template above. The repair menu and the access-aware framing of
these moves live in [`repair-taxonomy.md`](repair-taxonomy.md); this file owns *when the access flag
fires and why*, that file owns *the repairs themselves*. Concretely: **this file owns the trigger
*definitions*** (the full list above, including the secure-repair non-AI burden); `repair-taxonomy.md`
carries the *per-repair inline* flag that points back here.

> **Rule of thumb:** if your "best next move" requires the student to bring an AI tool, **or to be in a
> specific room at a specific time**, it inherits an access assumption. Either neutralize that assumption
> or flag it — never ship the repair silent on access.
>
> **The second clause is not optional, and it is the one most often missed.** Scoring/attribution is the
> most common diagnosis this tool produces, and its standard repairs — a proctored sitting, a fixed-time
> checkpoint, an oral viva, an observed demonstration — are exactly the formats that strip
> accommodations. Converting an untimed take-home into a timed in-class sitting silently removes
> extended-time and flexible-deadline accommodations for every student who holds one; a live oral probe
> does the same for communication-related accommodations. Any such repair ships with an alternate
> sitting, an equivalent attributable format, and the accommodations route named.

---

## What this is NOT

- **Not a scored rubric dimension.** Equity/access is a **behavioral flag** the coach raises in
  Watch-outs — it is not a sixth link, not a graded criterion, and not a number. Keeping it out of the
  rubric is deliberate (see [`diagnostic-procedure.md`](diagnostic-procedure.md)).
- **Not a DEI lecture.** No advocacy, no general equity essay. One proportionate sentence tied to *this*
  assessment's learning signal.
- **Not a reason to block AI use.** The flag points toward access mitigations and alternative paths, not
  toward banning the tool.
- **Not always applicable.** When access isn't in play, omit it. A manufactured equity flag is itself a
  failure mode — the same way forcing a redesign on a Strong assessment is.

In short: a **targeted, proportionate flag** that catches when *tool access* — not the intended
learning — is doing the work. That is a Link 1 (Construct / CIV) concern, surfaced as a Watch-out.

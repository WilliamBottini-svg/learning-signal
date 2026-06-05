# Core: The Diagnostic Procedure

This is the keystone of Learning Signal Check. It is the procedure the coach **executes** — not a
checklist it consults. Another agent (or model) following this file on the same case should arrive at
the **same primary diagnosis**.

The procedure operationalizes **Kane's argument-based validity** as an ordered, halting diagnostic. It
treats an assessment as a chain of linked inferences from *what the student did* to *the decision we
make about them*. Each downstream inference presupposes the upstream one, so the chain is only as
strong as its **earliest broken link**. The job is to find that link, name it, and repair *it* — not to
hand out a generic menu of "AI-resilient assessment" tips.

---

## The contract (read this first)

1. **Screen for safety first** (Phase 0), before anything else.
2. **Walk the chain in order.** Construct → Scoring → Generalization → Extrapolation → Implications.
3. **Halt at the earliest broken link.** That link is the **primary diagnosis**.
4. **Repair the primary link first.** Downstream weaknesses are *secondary findings*; note them, but do
   not let a sophisticated downstream repair distract from an upstream break.
5. **Diagnose before you prescribe.** Never jump to redesign moves before locating the break.
6. **Restraint is a valid result.** "No major redesign needed" is sometimes the correct, tested output.
7. **Plain language on top, rigor underneath.** Say "can we trust this still shows the learning?" to the
   educator; reserve *construct-irrelevant variance*, *scoring inference*, etc. for documentation and
   expert users.

---

## Plain-language version of the flow

> First, make sure there's nothing here that needs a human, not a tool (real patient data, a private
> student record, or "did this student cheat?"). Then get clear on **what the assessment is trying to
> show** and **what evidence it collects**. Then ask, in order: *Are we measuring the right thing? Can
> we be sure the student is the one who did it? Does this one task tell us about more than this one
> task? Does it tell us anything about the real world? And do the stakes we're attaching match how much
> the evidence can bear?* Stop at the first question where the honest answer is "no" (or "not anymore,
> now that students can use AI"). That first "no" is the thing to fix.

---

## Phase 0 — Safety screen (before you diagnose)

Scan the request **before** framing the case. If any of the following is present, **do not walk the
chain** — go straight to the refuse-and-redirect response (see
[`response-pattern.md`](response-pattern.md) and [`safety-guardrails.md`](safety-guardrails.md)). The
minimal criteria, inlined so this file is self-sufficient:

| Trip (→ gate in `safety-guardrails.md`) | If the request… | Do instead |
|------|------------------|------------|
| **Sensitive data** (Gate 1) | contains PHI, identifiable patient data, or private student records / grades / disciplinary records | ask for de-identified or fictionalized material; offer to continue once removed |
| **AI detection / misconduct** (Gate 2) | asks you to determine whether a student used AI or cheated | refuse the determination; redirect to assessment design + institutional process + human review |
| **Consequential decision from AI output** (Gate 3) | asks you to make/justify a progression, promotion, remediation, competency, licensing, or disciplinary decision based on AI output | refuse; require triangulated evidence + qualified human review |
| **Policy / legal overclaim** (Gate 4) | asks for a definitive legal, accreditation, or institutional-policy ruling | distinguish design advice from policy; recommend checking current local guidance |

Screening here means sensitive content never reaches a normal diagnosis, and unsafe inputs do not sit
in a drafted reply. [`safety-guardrails.md`](safety-guardrails.md) is the canonical, fuller version.

---

## Phase A0 — Triage (only when more than one assessment arrives)

Usually the educator brings **one** assessment and you go straight to Phase A. But sometimes they paste
**several assessments / a whole syllabus**, or arrive at **program or portfolio scale** ("our whole
second year, dozens of assessments"). Don't diagnose everything at once, and **never silently drop**
what you won't get to.

1. **Inventory + summarize back.** List what you received, one line each, so they can see nothing was lost.
2. **Order by stakes, then exposure.** Highest-**stakes** assessment first; break ties by which is most
   **AI-exposed** (an unsupervised written *product* outranks an observed *performance*).
3. **Diagnose the first one fully** (Phases A–F). Frame it as the **worked example** the rest will follow.
4. **Queue the rest** with a one-line "likely issue" each, to be diagnosed next on request — not in depth now.
5. **If the user can't or won't pick one**, don't loop — propose the highest-stakes item as the default
   and proceed.

This preserves the one-assessment discipline (the walk runs on one assessment at a time) while handling
a user who shows up with many or with a whole program. Emit via the *Multiple assessments (triage)*
variant in [`response-pattern.md`](response-pattern.md).

## Phase A — Frame the case

Gather or infer these inputs. If the educator hasn't supplied one, ask for it or state a provisional
assumption explicitly.

| Input | What you need |
|-------|----------------|
| **Assessment description** | Format, prompt, length, individual/group, in-class/take-home, timing. |
| **Learning claim** | What the assessment is meant to show the student can know, do, reason, or transfer. |
| **Current evidence** | The artifact or performance actually collected (and its type — see below). |
| **AI-use condition** | The stated rule *and* the **likely** real AI-use behavior (often differ). |
| **Stakes** | One of: *formative · low · moderate · high · **consequential***. "Consequential" = progression, promotion, remediation, competency, licensing, or disciplinary decisions. |
| **Context / domain** | Discipline, level, setting (e.g., pre-clerkship UME, clinical clerkship). |
| **Constraints** | Class size, faculty time, proctoring availability, accessibility needs, cost. |
| **Main concern** | What worried the educator enough to ask. |

**Gather it like a conversation, not a form.** Never fire a multi-question intake at the user. Ask the
**single most-diagnostic question** for what they've disclosed, and **proceed on a stated assumption**
for the rest (the *missing-intake* variant in [`response-pattern.md`](response-pattern.md) shows how —
give a provisional read first, ask at most one question, never on consecutive turns). A quick selector:
- Named a **take-home / unsupervised** format → the AI-use condition is the key unknown; you can usually
  assume "AI-allowed and unverifiable" and proceed.
- The **claim is vague** → sharpen it first (below).
- **Stakes** unknown and possibly consequential → that's the one to confirm (it can flip the reading to
  Needs deeper review).

Ask in **plain language** — the user should never need the words "construct," "inference," or "claim":

| Instead of asking… | Ask… |
|---|---|
| "What's the learning claim?" | "What should this show students can actually *do*?" |
| "What evidence does it collect?" | "What do they hand in or do?" |
| "What's the AI-use condition?" | "Could a student do this with ChatGPT without you knowing?" |
| "What are the stakes?" | "How much does it count — a small grade, or something big like passing?" |

If the user **asks what a term means** (or echoes one back unsure — "what's a learning claim?"), define
it in **one plain sentence** and keep moving; never imply they should already know it.

**Classify the evidence** as one (or more) of: **product** (an artifact), **process** (how it was
made), **performance** (an observed doing), or **decision** (a judgment the student makes). The
evidence type drives which links are most exposed.

### Sharpen vague learning goals before diagnosing

If the learning claim is a vague abstraction, translate it into an **assessable claim** first — usually
by asking one clarifying question. A vague goal cannot be diagnosed because no link can be evaluated
against it.

| Vague goal | Assessable claim (example) |
|------------|-----------------------------|
| "critical thinking" | "Can the student justify a prioritization decision using case evidence?" |
| "communication" | "Can the student adapt their explanation to a specific patient cue?" |
| "clinical reasoning" | "Can the student identify what information would change their diagnosis?" |
| "reflection" | "Can the student reflect on a *specific observed behavior* and name a concrete next action?" |
| "understanding" | "Can the student predict what happens when one variable in the system changes?" |

**Carve-out:** if a claim is vague **and** the format *structurally cannot* be made observable (e.g., a
"reflection" with no possible referent in how it's collected), you don't need the clarifying turn —
that is a **Construct** break on sight. Otherwise, sharpen first, and only call Construct broken if the
educator confirms it can't be made assessable.

If the assessment was **weak evidence for the claim even before AI**, say so. AI often **exposes** a
pre-existing **construct underrepresentation** problem rather than creating a new one — that is a
*Construct* break (Link 1), not a *Scoring* break.

---

## Phase B — Walk the five-link chain in order

At each link, classify its state under the **likely** AI-use condition, **at the case's actual stakes**:

- **Severed** — under the likely AI-use condition, a student who did **not** do the intended cognitive
  work could plausibly earn the **same result** as one who did. The link no longer distinguishes them;
  the claim it licenses cannot be trusted.
- **Weakened** — the AI-use condition **shifts** results, but the result still **mostly** reflects the
  student's own intended work. The claim is partly trustworthy and a **light** adjustment restores it.
- **Intact** — the link holds; its assumptions are supported.

> **Stakes are the single severity knob.** Higher stakes **lower the bar** for calling a link Weakened
> or Severed: the same gap that is tolerable on a formative quiz is disqualifying when it feeds a
> high-stakes decision. Read each link's state at the case's *actual* stakes. (There is no separate
> "seriously weakened" tier — stakes move the one threshold.) A consequence of this: the *same artifact*
> can be Moderate at low stakes and Vulnerable at high stakes. That is intended (see Phase D).

For each link below: the **core question**, **what crossing it licenses**, the **assumptions** it rests
on, **AI-era failure symptoms**, the **diagnosis if it breaks**, and **representative repairs** (full
menu in [`repair-taxonomy.md`](repair-taxonomy.md)).

### Link 1 — Construct
*From "a learning goal" to "a task that actually represents it."* Owns **construct underrepresentation**
and **construct-irrelevant variance**.

- **Core question:** Is the learning claim well-defined, and does this task actually elicit it?
- **Licenses:** That performing the task requires the construct we care about (not a proxy).
- **Assumptions:** The construct is named at an assessable grain; the task samples its important parts;
  the task does not mostly measure something else.
- **AI-era failure symptoms:**
  - The goal is a vague abstraction that was never operationalized.
  - The task can be completed well **without** doing the intended thinking — and AI makes that gap
    obvious (the construct was under-represented all along).
  - The rubric rewards surface features (fluency, length, polish) that AI supplies cheaply, so the
    score reflects **construct-irrelevant variance** rather than the construct.
  - The score tracks **AI fluency or tool access** more than the intended construct (CIV).
  - "AI literacy" has quietly become the real construct, but the claim still says "domain knowledge"
    (or vice versa).
- **If broken → primary diagnosis: Construct inference failure. Halt.** No amount of attribution
  (Scoring) or sampling (Generalization) fixes measuring the wrong thing.
- **Representative repairs:** sharpen the claim to an assessable grain; redesign the task so the
  construct is *necessary* to succeed; re-weight the rubric onto construct-relevant features; decide
  deliberately whether AI use is part of the construct or noise.

### Link 2 — Scoring
*From "a task was submitted" to "this student produced it, under the intended conditions, scored
correctly."* This link is **attribution + administration + evaluation accuracy** — **not** whether the
rubric measures the right thing (that is Construct, Link 1).

- **Core question:** Can we attribute the observed response to **this student**, under the intended
  conditions, and was it evaluated correctly?
- **Licenses:** That the score reflects this student's own performance, scored without
  administration/rater error.
- **Assumptions:** The work is attributable; conditions match intent; the evaluation of *what was
  submitted* is accurate and consistent.
- **AI-era failure symptoms:**
  - An unsupervised written artifact could be generated or heavily produced by AI.
  - The work could be from another person or tool; no process evidence ties it to the student.
  - The task assumes independent reasoning, but AI use is unrestricted or unverifiable.
  - In group work, the individual's contribution is indeterminable *(attribution problem)*.
  - Scoring of the submitted work is inconsistent or untrained (rater error).
- **If broken → primary diagnosis: Scoring inference failure. Halt.** Do not optimize downstream links
  while you cannot attribute the evidence to the student.
- **Representative repairs:** add a supervised or time-boxed component; oral probe; pre-AI commitment;
  process log / version history; individual-accountability check; student-generated reasoning trace;
  observed demonstration; AI-use disclosure tied to *interpretation*, not punishment; rater training.

> **Construct vs Scoring — the boundary test (use when they feel co-broken).** Ask: *if a student did
> the intended thinking **honestly**, would this task capture it?*
> - **Yes** → the construct is intact; any problem is attribution/administration → **Scoring**. (A
>   completion-graded discussion post done honestly *does* show engagement; an unverifiable take-home
>   reasoning write-up done honestly *does* show the reasoning — so these are **Scoring** breaks, not
>   Construct.)
> - **No** → even an honest, engaged student's work wouldn't demonstrate the construct, because the task
>   elicits the wrong thing or the rubric rewards AI-suppliable surface features → **Construct**. (An
>   untethered "reflection" with no referent, or a rubric paying out for fluency/polish, fails here.)
>
> Low stakes or completion grading do **not** by themselves make it a Construct break — they change the
> *repair severity*, not the link.

### Link 3 — Generalization
*From "this one task" to "the student's competence across the domain of such tasks."*

- **Core question:** Does this evidence sample support a claim **beyond this single task/prompt/case**?
- **Licenses:** That performance here represents performance across the intended universe of tasks.
- **Assumptions:** Enough sampling across items/contexts/occasions; the student can't narrowly optimize
  for one pattern; the sample isn't dominated by one artifact.
- **AI-era failure symptoms:**
  - One narrow artifact is over-interpreted as broad competence.
  - Students can rehearse or prompt-optimize for a single predictable pattern.
  - The assessment samples too little of the domain.
  - A group product masks individual variation *(only if attribution is already handled at Scoring;
    otherwise the attribution gap is the earlier, primary break)*.
  - AI-generated scaffolds make a single performance unrepresentative of the student's range.
- **If broken → primary diagnosis: Generalization inference failure. Halt.**
- **Representative repairs:** multiple cases/prompts; item banks or randomized variants; sampling across
  contexts; repeated low-stakes observations; triangulation with other assessments; blueprinting
  against the learning goals; individual-accountability components in group work.

### Link 4 — Extrapolation
*From "competence on the assessment" to "capability in the real-world / clinical / future target."*

- **Core question:** Does performance here support a claim about the **target context** the student is
  being prepared for?
- **Licenses:** That assessment performance transfers to the authentic situation of interest.
- **Assumptions:** The task is authentic enough; it captures judgment-in-context, not just after-the-
  fact explanation; the format isn't decontextualized in a way that breaks transfer.
- **AI-era failure symptoms:**
  - A polished artifact does not demonstrate transferable reasoning or performance.
  - The student can produce text but may not be able to *do* the thing.
  - The task measures explanation-after-the-fact, not judgment in the moment.
  - A reflection sounds plausible but is not tied to any observed behavior.
  - AI changes the task so the observed performance no longer maps to the target capability.
- **If broken → primary diagnosis: Extrapolation inference failure. Halt.**
- **Representative repairs:** authentic performance task; observed demonstration; oral reasoning probe;
  "what would change your mind?" question; scenario variation; clinical-reasoning defense; reflection
  tied to observed behavior; rubric emphasis on judgment/transfer; move evidence up Miller's pyramid
  when appropriate.

### Link 5 — Implications / Decision
*From "a sound interpretation" to "a justified decision and defensible consequences."*

- **Core question:** Are the **decisions and consequences** based on this assessment justified by the
  **quality and quantity** of evidence?
- **Licenses:** That the action taken on the score (a grade weight, a gate, a competency judgment) is
  proportionate to what the evidence can bear, and that the decision rule produces defensible
  downstream consequences.
- **Assumptions:** Stakes match evidence strength; high-stakes decisions are triangulated and
  human-reviewed; the decision does not rest on AI output alone; the decision rule does not create
  indefensible differential/adverse impact, and its washback is acceptable.
- **AI-era failure symptoms:**
  - A high-stakes decision rests on one AI-vulnerable artifact, or on a single occasion.
  - A competency/progression decision lacks triangulation.
  - An AI-involved evaluation is treated as sufficient without qualified human review.
  - A misconduct or remediation decision is inferred from "AI detection" or model speculation.
  - The decision simply exceeds what the evidence supports, or its consequences fall unequally for
    reasons unrelated to the construct.
- **If broken → primary diagnosis: Implications / Decision inference failure.**
- **Representative repairs:** lower the stakes; require qualified human review; triangulate with
  additional evidence; separate formative AI-supported practice from summative assessment; apply
  programmatic-assessment principles; never use AI output (or "AI detection") as the sole basis for a
  consequential decision; escalate to governance / assessment leadership.

> **Disambiguating Generalization vs Implications — test the *cause*, not the symptom.**
> - **Generalization** = the *evidence base is too thin to characterize the student's range*,
>   **independent of the decision attached**. (One narrow sample can't describe what the student can
>   generally do.)
> - **Implications / Decision** = the evidence base **would be adequate for a lower-stakes use**, but
>   the **specific consequence attached exceeds it** — including a consequential decision resting on a
>   single occasion, or on AI output without qualified human review.
>
> Example that the symptom-level rule gets wrong: a sound multi-station OSCE (attributable, authentic,
> well-sampled across stations) used as the **sole** gate for clerkship progression. Sampling/transfer
> are fine, so this is **not** Generalization — it's **Implications** (a single instrument can't carry a
> progression gate; that's the programmatic-assessment point). See Example 6.

---

## Phase C — Resolve primary vs secondary (the stopping rule)

1. Walk Link 1 → Link 5 in order, classifying each as **Intact / Weakened / Severed**, read at the
   case's actual stakes (Phase B).
2. The **primary diagnosis** is the **earliest Severed link**. If **no** link is Severed, it is the
   **earliest Weakened link** (a real but low-burden fix). If **every** link is Intact, there is **no
   primary break**.
3. **Halt the diagnostic walk** at the primary link for the purpose of choosing the first repair. You
   may still *note* downstream links, but classify them as **secondary findings**, not the first repair.

**Co-breaks.** Real assessments often have several broken links. Still choose the **earliest** as
primary and list the rest as secondary, then **sequence** the repairs: fix the binding upstream
constraint first, and only then the downstream ones. Example — a take-home clinical-reasoning essay:
*Primary* = Scoring (the essay may not be the student's own work); *Secondary* = Extrapolation (even a
genuine essay may not show reasoning in context). First repair restores attribution (pre-AI commitment,
oral probe, reasoning trace); a later repair improves transfer (case-based defense, observed reasoning).

---

## Phase D — Derive the readiness rating

Readiness is **derived from the walk**, never assigned by vibe.

| Rating | When | Examples |
|--------|------|----------|
| **Strong** | No link broken under likely AI use (all Intact). | Observed OSCE; proctored individual exam; oral defense; AI-critique task **after confirming the *scored* evidence is the student's own reasoning, not the AI artifact**. |
| **Moderate** | Earliest break is **Weakened** (no link Severed); a light, low-burden repair restores it. | Oral presentation with unclear AI-use expectations; group project with unclear individual accountability. |
| **Vulnerable** | Earliest break is **Severed**. | Unsupervised take-home essay/quiz; generic reflection; unscaffolded case write-up. |
| **Needs deeper review** | **Override** — see below. | Remediation, progression, competency/licensing, high-stakes exams, patient data, disciplinary allegations. |

**The "Needs deeper review" override.** Independently of where the chain breaks, rate the case **Needs
deeper review** when **Stakes = consequential** (progression, promotion, remediation, competency,
licensing, disciplinary) **or** the case is sensitive-data / clinically sensitive / governance-heavy.
A normal **summative course grade is *not* automatically consequential** — don't route ordinary grading
to this tier.

**Precedence when the override trips:** the headline is "this needs qualified human/governance review."
Still run the walk, but report the primary link as a **chain note** *inside* the Needs-deeper-review
response (it informs the human; it does not replace them). So the override changes the *response shape*,
not the chain analysis.

**Stakes-monotonicity is expected.** Because severity is read at the actual stakes, the same artifact
can move Moderate → Vulnerable → Needs deeper review as stakes rise, with no change to the task itself.
That is correct behavior, not an inconsistency.

---

## Phase E — Apply restraint and utility

Before finalizing, pressure-test the repair against **van der Vleuten's utility logic** — utility is
**multiplicative** across *validity × reliability × educational impact × acceptability × cost*, so any
factor near zero zeros the whole product.

Ask: **Is the repair proportionate to the assessment's stakes, cost, and educational value?** Prefer the
**lightest** repair that restores the broken link.

> **Multiplicative-zero rule.** If the lightest link-restoring repair still scores near-zero on
> **acceptability** or **cost** (faculty won't run it; it's infeasible at this scale), do **not**
> recommend the heavy repair anyway. The correct output is to say no proportionate repair exists and
> recommend **deferral, lowering the stakes, or moving the AI-supported work into practice** instead.

Other legitimate outputs: no major redesign (already strong); clarify the AI-use language only; defer
pending governance review.

Anti-patterns to avoid: a generic menu of redesign ideas; a sophisticated downstream repair while an
upstream link is severed; *always* recommending pre-AI commitment; *always* recommending more work.

---

## Phase F — Produce the output

Emit the coach response using [`response-pattern.md`](response-pattern.md): a plain-language read, the
learning signal, the **primary diagnosis**, the readiness rating, why that link is the issue, **one**
targeted next move, watch-outs (safety / equity / feasibility / governance), and an offer to draft
language. The Phase 0 screen already decided whether this is a normal diagnosis or a refuse-and-redirect.

---

## Edge cases

- **Vague goal.** Don't diagnose against an abstraction. Sharpen to an assessable claim first (Phase A),
  then walk the chain. Use the carve-out only when the format structurally can't be made observable.
- **Pre-existing weakness AI merely exposed.** If the task was weak evidence before AI, name it as a
  **Construct** break and say AI revealed it — don't misattribute it to Scoring.
- **Already-strong assessment.** If no link breaks, **stop**. Acknowledge the strength; suggest at most
  a one-line clarification. Forcing a redesign here is a failure mode (see restraint).
- **Forcing AI where it doesn't belong.** Don't push AI integration into a closed-book, secure,
  knowledge-anchored exam whose construct is independent recall/synthesis. "No AI" is a valid design.
- **Group work.** Suspect Scoring (attribution) first; Generalization (individual variation) is the
  primary break only once attribution is already handled.
- **AI-required tasks (e.g., critique an AI-generated differential).** The construct may legitimately
  include working with AI; confirm the *scored* evidence is the student's independent reasoning
  (Construct + Scoring), not the AI's output — before calling it Strong.
- **Sensitive data / high-stakes / misconduct.** Caught by Phase 0 and/or the Needs-deeper-review
  override; never produce a cheating determination or a consequential decision from AI output.

---

## Worked examples

Each shows: claim → evidence → ordered walk → primary diagnosis → first repair.

### Example 1 — Take-home short-answer quiz (pre-clerkship)
- **Claim:** Student can explain renal acid–base compensation. **Evidence:** unsupervised written
  answers (product). **AI-use:** unrestricted, unverifiable. **Stakes:** low.
- **Walk:** Construct **Intact** (knowledge claim is well-defined and the task elicits it) → Scoring
  **Severed** (a student who didn't learn it could score the same using AI; not attributable).
- **Primary:** Scoring inference failure. **Readiness:** Vulnerable.
- **First repair:** convert to a short in-class or proctored individual check, or an oral probe on the
  same content. *Secondary:* none material. *Restraint note:* a light proctored checkpoint is cheaper
  than rebuilding the whole quiz.

### Example 2 — Generic reflective essay
- **Claim:** "Student reflects on professional growth." **Evidence:** take-home reflective essay
  (product). **AI-use:** likely. **Stakes:** low.
- **Frame:** the claim is vague → ask the sharpening question: *"reflect on what specific, observable
  thing?"* If the format has **no possible referent** (no encounter, no feedback, nothing observed),
  the carve-out applies and Construct is **Severed** on sight.
- **Walk:** Construct **Severed** — the task never represented an assessable construct; AI just made the
  gap visible.
- **Primary:** Construct inference failure (construct underrepresentation). **Readiness:** Vulnerable.
- **First repair:** redefine the claim to "reflect on a *specific observed behavior* and name a concrete
  next action," and require a referent (a recorded encounter, a piece of feedback). *Note:* proctoring
  the essay (a Scoring fix) would not help — we'd be measuring the wrong thing precisely.

### Example 3 — Observed OSCE station, multiple stations, trained rater
- **Claim:** Student can take a focused history and build a problem representation. **Evidence:**
  observed performance + rater scoring. **AI-use:** none during the encounter. **Stakes:** moderate.
- **Walk:** Construct **Intact** → Scoring **Intact** (attributable, observed, trained rater) →
  Generalization **Intact** (multiple stations) → Extrapolation **Intact** (authentic performance) →
  Implications **Intact** (stakes matched, human-scored).
- **Primary:** none. **Readiness:** Strong.
- **Output:** restraint — no major redesign; optionally tighten one rubric anchor. *Forcing AI here
  would be a mistake.*

### Example 4 — Group slide deck used as a summative grade
- **Claim:** Each student can synthesize evidence on a topic. **Evidence:** one group product.
  **Stakes:** summative course grade (moderate — *not* "consequential," so no override).
- **Walk:** Construct **Intact** → Scoring **Severed** (individual contribution indeterminable;
  AI-assisted production further blurs it).
- **Primary:** Scoring inference failure. *Secondary:* Generalization (one artifact), Implications
  (individual grades from a group product). **Readiness:** Vulnerable.
- **First repair:** add an individual-accountability component (brief individual oral or written
  reflection on their specific contribution + reasoning). *Then* consider lowering the individual stakes
  on the group product — but Scoring is repaired first.

### Example 5 — High-stakes remediation triggered by suspected AI use
- **Request:** "Decide whether to remediate this student because the work looks AI-generated."
- **Phase 0:** trips **Detection/misconduct** and **Consequential decision** gates → do not walk.
  **Readiness:** Needs deeper review.
- **Output:** the coach does **not** determine AI use or recommend remediation. It redirects to
  assessment design and institutional process, and requires triangulated evidence + qualified human
  review. (See [`safety-guardrails.md`](safety-guardrails.md).)

### Example 6 — Sound OSCE used as the *sole* progression gate (Generalization vs Implications + override)
- **Claim:** Student is ready to progress to clerkships. **Evidence:** one well-run multi-station OSCE
  (attributable, authentic, sampled across stations). **Stakes:** **consequential** (progression).
- **Walk:** Construct/Scoring/Generalization/Extrapolation **Intact** (the OSCE itself is sound) →
  **Implications Severed**: a single instrument is being used as the *sole* progression decision, with
  no triangulation. This is **not** Generalization (the OSCE samples fine) — the *consequence attached*
  exceeds what one instrument should carry.
- **Override:** Stakes = consequential → **Readiness: Needs deeper review.**
- **Output:** headline is "this progression decision needs qualified faculty/committee review, not a
  single instrument," with the **chain note**: the break is at Implications. First move: triangulate
  with other programmatic-assessment data points before the gate; don't rest progression on one OSCE.

---

## What "done right" looks like (for testers)

- Phase 0 catches sensitive-data / detection / consequential-AI-decision / policy-overclaim requests
  *before* any diagnosis.
- The output names the **earliest** broken link, not a flat list of all weaknesses.
- Severity (Intact/Weakened/Severed) is read at the case's actual stakes; readiness follows
  mechanically (Severed→Vulnerable, Weakened→Moderate, Intact→Strong, override→Needs deeper review).
- The first recommended move repairs **that** link, proportionately; secondary findings are labeled.
- Strong assessments get restraint, not a redesign.
- Consequential / sensitive cases get "Needs deeper review" with human-review language and the chain as
  a note.

Expected primary diagnoses for the golden cases are derived directly from this procedure; they will be
recorded in [`../tests/golden-test-cases.md`](../tests/golden-test-cases.md).

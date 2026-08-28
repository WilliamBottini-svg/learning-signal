# Core: The Repair Taxonomy

The full repair menu for Learning Signal Check, **indexed by diagnosis**. The keystone
([`diagnostic-procedure.md`](diagnostic-procedure.md)) finds the **primary broken link** in the
five-link chain and lists only *representative* repairs per link. This file is the canonical home for
the **complete** menu and for **how to choose** among repairs.

> This is **not** a generic best-practices list. Repairs are organized by the inference they restore. If
> you know the primary broken link, you are in the right section. Do not shop across sections for a
> repair you like better — a downstream repair cannot fix an upstream break (the whole point of the
> ordered walk).

---

## 1. How to use this file

1. **Diagnose first.** Run the walk in [`diagnostic-procedure.md`](diagnostic-procedure.md) (Phases A–C)
   and name the **primary** link — the earliest Severed link, or if none is Severed, the earliest
   Weakened one. **Do not** open this file before you have a primary diagnosis.
2. **Go to that link's section.** Sections 2.1–2.5 below mirror the five links. Each lists targeted
   repairs and how to pick among them.
3. **Pick the lightest repair that restores the link** (restraint; Phase E). Severity sets the bar: a
   *Weakened* link needs the gentlest touch; a *Severed* link needs a repair that actually re-establishes
   the inference, not a cosmetic one. More repair than the break requires is itself a failure mode.
4. **Sequence secondary repairs *later*.** Fix the binding upstream constraint first; note downstream
   findings and stage their repairs after (Phase C, co-breaks). The coach recommends **one** move now
   (see [`response-pattern.md`](response-pattern.md), "Best next move"); the rest are "later."
5. **Pressure-test against utility before you commit** (Phase E). If even the lightest link-restoring
   repair tanks **acceptability** or **cost**, do not recommend the heavy repair — go to
   [Section 4](#4-restraint--no-change-guidance) (deferral / lower stakes / move AI work to practice).

**Reading each repair entry.** Every repair below carries five fields:

| Field | What it tells you |
|-------|-------------------|
| **What it is** | One line — the move itself. |
| **Restores** | Which link it re-establishes (almost always *this* section's link; a few are cross-cutting and noted). |
| **Use when / not when** | The cases it fits, and the cases where it is the wrong tool. |
| **Feasibility & cost** | Faculty time, scale (class size), proctoring/space, turnaround. Maps to the **feasibility** factor in van der Vleuten's utility index — **cost is its inverse** (higher cost lowers feasibility); *acceptability* (will faculty/students actually run it?) is a separate factor. |
| **Equity flag** | Present only if the repair assumes resources/access (devices, paid AI tiers, accommodations, scheduling). Points to [`equity-and-access-flags.md`](equity-and-access-flags.md). |

---

## 2. Repairs by link

### 2.1 Construct repairs — *restore Link 1*

Use when the primary diagnosis is **Construct inference failure**: the claim is a vague abstraction, the
task can be done well without the intended thinking (construct **underrepresentation**), or the score
tracks surface features / AI fluency / tool access rather than the construct (**construct-irrelevant
variance**, CIV). **A Scoring fix cannot help here** — proctoring a task that measures the wrong thing
just measures the wrong thing under supervision. Repair the *task and claim*, then re-walk.

| Repair | What it is | Restores | Use when / not when | Feasibility & cost | Equity flag |
|--------|------------|----------|---------------------|--------------------|-------------|
| **Sharpen the claim to an assessable grain** | Rewrite the goal as a specific, observable claim (see keystone Phase A table: "reflect on professional growth" → "reflect on a *specific observed behavior* and name a concrete next action"). | Construct | **Use** whenever the goal is a vague abstraction. Almost always the *first* Construct move. **Not** when the claim is already concrete — then the break is elsewhere. | Near-zero: minutes of design thought; no new logistics. | — |
| **Redesign the task so the construct is necessary to succeed** | Change the prompt/conditions so a student *cannot* produce a passing response without doing the intended cognitive work (e.g., require reasoning from a *specific* dataset/case the student must interpret, not a generic prompt AI answers cold). | Construct | **Use** when a strong answer is achievable without the construct. **Not** as a covert attribution fix — if the worry is "who did it," that's Scoring. | Moderate: redesign effort; usually reusable once built. | Flag if it requires a tool/resource not all students have. |
| **Re-weight the rubric onto construct-relevant features** | Move points off fluency/length/polish (cheap for AI to supply) and onto the reasoning, judgment, or decision you actually care about. | Construct (removes CIV) | **Use** when the rubric rewards surface features AI supplies cheaply — including **partial-capture** rubrics where honest work is partly scored on reasoning but a **material share** of points still rides on AI-suppliable polish (keystone Construct-vs-Scoring boundary test, third branch). **Not** when the rubric is already construct-aligned but raters apply it inconsistently — that's a Scoring (rater) issue. **Not** when attribution alone is the gap and the rubric pays out only on construct-relevant features — that's Scoring. | Low: edit an existing rubric; pairs well with a brief rater norming. | — |
| **Decide deliberately whether AI use is part of the construct or noise** | Make an explicit call: is "working with AI" part of what you're certifying, or construct-irrelevant? Then set the AI-use rule to match (see [Section 3.1, AIAS](#31-ai-assessment-scale-aias--pick-the-ai-use-rule)). | Construct | **Use** when "AI literacy" has quietly become the real construct while the claim still says "domain knowledge" (or vice versa). **Not** a substitute for fixing an under-represented construct. | Near-zero (a design decision) + the cost of whatever rule you adopt. | Flag if the chosen rule *requires* AI access — unequal tiers become CIV. |
| **Re-anchor to a required referent** | Require the task to attach to a specific stimulus the construct needs (a recorded encounter, a dataset, a piece of feedback, an artifact to critique) so there is something real to reason about. | Construct | **Use** for "reflection"/"analysis" tasks with no possible referent (keystone carve-out → Construct Severed on sight). **Not** when a referent already exists. | Low–moderate: depends on whether the referent must be produced/captured. | Flag if capturing the referent needs recording tools/access. |
| **Split a conflated construct into its parts** | If one task is trying to certify several distinct things at once (knowledge *and* writing *and* tool use), separate them so each is assessed where it can be seen cleanly. | Construct | **Use** when CIV comes from bundling (e.g., writing quality swamps the science). **Not** when bundling is authentic to the target performance (then keep it; see Extrapolation). | Moderate: may add a second short component. | — |

> **Construct is the most over-skipped diagnosis.** AI frequently *exposes* a pre-existing
> underrepresentation problem rather than creating a new one. If the task was weak evidence **before**
> AI, the repair lives here — not at Scoring (keystone Phase A; Edge cases).

---

### 2.2 Scoring repairs — *restore Link 2*

Use when the primary diagnosis is **Scoring inference failure**: the work may not be **attributable** to
this student, the **conditions** don't match intent, or the **evaluation** of what was submitted is
inaccurate/inconsistent (rater error). Scoring is *attribution + administration + evaluation accuracy* —
**not** whether the rubric measures the right thing (that's Construct, 2.1). Many Scoring repairs add a
**Lane-1 / secure component** (see [Section 3.2](#32-university-of-sydney-two-lane-model--add-a-secure-lane-when-attribution-is-the-break)).

| Repair | What it is | Restores | Use when / not when | Feasibility & cost | Equity flag |
|--------|------------|----------|---------------------|--------------------|-------------|
| **Supervised / time-boxed in-class checkpoint** | A short proctored, in-person (or invigilated) component on the same content — optionally time-boxed to a single sitting — attributable on its face. A Lane-1 add-on. | Scoring (attribution + conditions) | **Use** when an unsupervised artifact could be AI- or other-produced and stakes warrant assurance. **Not** when the construct *requires* tools/resources a proctored room removes (then use an oral probe or process evidence instead). | Moderate–high: room, time, invigilation; scales poorly in very large cohorts. | Flag: fixed-time/in-person sittings can disadvantage students needing accommodations or with scheduling constraints — see [`equity-and-access-flags.md`](equity-and-access-flags.md). |
| **Oral probe / viva on the submitted work** | A brief 1:1 (or small-panel) conversation asking the student to justify a choice, answer a counterfactual, or extend the reasoning trace from their own submission. Surfaces whether the reasoning is theirs. | Scoring (attribution); also strengthens Extrapolation | **Use** when you need attribution but a full proctored exam is overkill, *or* you also doubt transfer. **Not** as a recall/performance check; verbal fluency is construct-irrelevant unless it is part of the claim. At large scale, use all-student orals only if already staffed; otherwise use a supervised written addendum and reserve sampled oral probes for audit/calibration. | High per-student faculty time; mitigate by time-boxing to 2-3 minutes, using existing section/lab time, or using sampled probes only for quality assurance. | Flag: oral formats can disadvantage some communication-style or language differences; offer equivalent alternatives. |
| **Supervised reasoning addendum** | A short in-class, timed written extension tied to the original submission: explain one ranking, handle a new twist, or justify a key decision without external tools. | Scoring (attribution + conditions) | **Use** when a take-home artifact is valuable but needs an attributable anchor, especially in large cohorts where all-student oral probes do not scale. **Not** when the addendum asks only for generic reflection or recall; it must target the reasoning trace. | Low–moderate: uses class/section time and can be rubric-scored or pass/verify; scales better than per-student oral exams. | Flag: timed/in-person writing needs accommodations and alternatives for access constraints. |
| **Pre-AI commitment** | Capture an early, in-class first pass (an outline, a position, a hand-written stance) *before* any AI-assisted development, then compare/anchor to it. | Scoring (attribution) | **Use** selectively where an authentic "before" state is meaningful. **Not** as a default reflex — the keystone explicitly warns against *always* recommending pre-AI commitment (Phase E anti-patterns). | Low–moderate: one in-class slot + light cross-checking. | — |
| **Process log / version history** | Require the working trail (document version history, commits, draft timeline, search/AI-interaction log) alongside the product. One kind of **attributable checkpoint** when paired with a short reflection or spot-check. | Scoring (attribution + conditions) | **Use** when the platform captures process cheaply (docs, IDEs, LMS). **Not** when "process" can itself be fabricated or when reviewing logs costs more than it's worth at the stakes; pair with an oral probe or supervised addendum if attribution must be stronger. | Low to collect; **review** time can be high — sample rather than read every log. | Flag: assumes all students work on tooling that records history; hand/offline workflows may not. |
| **Student-generated reasoning trace** | Ask for a short artifact exposing the *thinking* (annotated decisions, a "show your reasoning" addendum, a decision log) that an unexplained product hides. | Scoring (attribution); supports Extrapolation | **Use** when the product is polished but the reasoning is invisible. **Not** when the trace itself is easily AI-generated without doing the work — pair with an oral or in-class element. | Low–moderate authoring; moderate to grade. | — |
| **Individual-accountability component (group work)** | Add a brief individual oral or written element tied to *that student's* specific contribution and reasoning. | Scoring (attribution in groups) | **Use** first for group products where individual contribution is indeterminable (keystone: suspect Scoring before Generalization in group work). **Not** as the *only* fix if you also over-interpret one artifact as broad competence (then Generalization is a secondary repair). | Low–moderate per student; scales with group count. | — |
| **Observed demonstration** | Have the student *do* the thing in front of a rater (perform, run the procedure, defend live) rather than submit a product. | Scoring (attribution + conditions); strong on Extrapolation | **Use** when the doing is observable and attribution + transfer both matter. **Not** when the construct is genuinely a written/asynchronous product (don't force performance where it doesn't belong). | High: rater time, scheduling, possibly space/simulation. | Flag: scheduling and physical-presence demands; ensure accommodations. |
| **AI-use disclosure tied to interpretation (not punishment)** | Require students to declare what AI they used and how, used to *interpret* the evidence — never as a misconduct trap. | Scoring (clarifies conditions) | **Use** to make the AI-use condition legible and reduce ambiguity. **Not** as a detection or enforcement mechanism — that trips the safety gate (see [`safety-guardrails.md`](safety-guardrails.md)). **Not** when framing it as interpretive still can't remove the chilling risk for an already-marginalized cohort — then the disclosure *itself* distorts the evidence; demote it and prefer a non-punitive interpretive note or another Scoring repair. | Near-zero: a prompt line + a disclosure field. | Flag: punitive-feeling disclosure can **chill** legitimate use unequally — frame as interpretive, see [`equity-and-access-flags.md`](equity-and-access-flags.md). |
| **Peer rating — treat as a rater instrument, not attribution** | If peer ratings adjust individual grades, norm the raters: anonymised submission, a short behaviourally-anchored scale (contribution to the *analysis*, not likeability), a worked example, and a rule that a rating outside the team's range needs a one-line justification. | Scoring (rater accuracy) — **not** attribution | **Use** when peer rating is already load-bearing and must be made defensible. **Not** as a repair for an attribution gap: peer ratings are second-hand and carry reciprocity, friendship and retaliation variance, so they cannot establish that a student did the work. Where an *individual* claim is certified, add a component producing first-hand individual evidence instead. | Low: a scale plus one norming briefing. | Flag that peer dynamics fall unevenly — students in minority positions on a team are rated down more often; never let peer rating alone move a grade band. |
| **Rater training / norming** | Calibrate raters on the rubric (anchor papers, a norming session, double-marking a sample, or a 5-10 minute anchor script for oral/addendum probes) so evaluation of *what was submitted* is consistent. | Scoring (evaluation accuracy) | **Use** when the break is rater inconsistency/untrained scoring, not attribution. **Not** when the rubric measures the wrong thing — fix that at Construct first. | Low–moderate: a session + sampled double-marking; very low for a mini anchor script paired with a light checkpoint. | — |

> **Group-work order (keystone Edge cases).** Suspect **Scoring (attribution)** first; **Generalization**
> (individual variation across tasks) is the primary break only once attribution is already handled.

> **Oral / observed / proctored repairs import their own obligations** — they are not terminal endpoints.
> Re-walk the repaired design for **Link 2** (rater consistency — sample/norm raters) and **Link 3**
> (single occasion — sample occasions), and remember "observed" is not automatically "unaided" (covert
> real-time AI in remote/talk-only formats). See keystone Phase E ("re-walk after repair").

---

### 2.3 Generalization repairs — *restore Link 3*

Use when the primary diagnosis is **Generalization inference failure**: attribution is fine, but the
**evidence base is too thin** to characterize the student's range — one narrow artifact is
over-interpreted, students can prompt-optimize for a single predictable pattern, or the sample covers too
little of the domain. **Test the cause, not the symptom** (keystone): if the problem is the *decision
attached* rather than the *thinness of evidence*, the break is **Implications** (2.5), not here.

| Repair | What it is | Restores | Use when / not when | Feasibility & cost | Equity flag |
|--------|------------|----------|---------------------|--------------------|-------------|
| **Add cases / prompts** | Assess across several distinct tasks, cases, or prompts instead of one. | Generalization | **Use** when one artifact is carrying a domain-wide claim. **Not** when the *single* sample is sound and only the consequence is too big (→ Implications). | Moderate: more authoring + grading; reuse across cohorts amortizes it. | — |
| **Item banks / randomized variants** | Draw items from a bank or auto-vary parameters so each student sees a different instance of the same skill. | Generalization (also blunts rehearsal/prompt-optimization) | **Use** when students can rehearse or prompt-optimize one predictable pattern, especially at scale. **Not** for performance/judgment tasks that don't itemize cleanly. | High up-front to build the bank; low marginal cost per administration after. | Flag if delivery requires a platform/device not all students have. |
| **Sample across contexts / occasions** | Spread evidence over multiple settings or time points rather than a single sitting. | Generalization | **Use** when one occasion can't represent the domain or is gameable. **Not** when a single well-sampled instrument already covers the domain. | Moderate–high: more scheduling and tracking. | Flag: more occasions = more scheduling burden; watch accommodation load. |
| **Single-sample caveat / narrow the claim** | Keep the task intact but label the score as single-vignette or single-occasion evidence; optionally narrow the claim to performance on this task type. | Generalization | **Use** when Construct and Scoring are intact, stakes are moderate or lower, and the weakness is sampling thinness rather than a broken task. **Not** when the score is being used as a gate, remediation trigger, or broad competency certification. | Near-zero: wording in feedback/reporting; pairs well with adding a second vignette later. | — |
| **Repeated low-stakes observations** | Many small, low-stakes data points accumulated over time instead of one big bet. | Generalization (feeds Implications/programmatic) | **Use** when you want range *and* low per-event burden; pairs with programmatic assessment ([Section 3.4](#34-programmatic-assessment--aggregate-many-low-stakes-points-for-implications)). **Not** when a defensible decision is needed *now* from existing evidence. | Low per event; **aggregation/tracking** is the real cost. | — |
| **Triangulate with other assessments** | Combine this evidence with independent existing measures of the same competence. | Generalization | **Use** when other signal already exists and can corroborate range. **Not** as a way to prop up an artifact that is itself un-attributable (fix Scoring first). | Low if the other data already exists; otherwise it's really "add cases." | — |
| **Blueprint against the learning goals** | Map items/tasks to the domain's objectives so coverage is deliberate, not accidental. | Generalization | **Use** when sampling is ad hoc and you can't say what the domain coverage *is*. **Not** a content change by itself — it reveals gaps you then fill. | Low: a mapping exercise; high leverage. | — |
| **Individual-accountability components (in group work)** | Per-student elements so a group product doesn't mask individual variation. | Generalization (range across individuals) | **Use** only **after** attribution is handled at Scoring (else the attribution gap is the earlier, primary break). | Low–moderate per student. | — |

---

### 2.4 Extrapolation repairs — *restore Link 4*

Use when the primary diagnosis is **Extrapolation inference failure**: the evidence is attributable and
well-sampled, but it doesn't **transfer** to the target (clinical / real-world / future-learning) context
— a polished artifact doesn't show transferable reasoning, the task measures explanation-after-the-fact
rather than judgment-in-the-moment, or a reflection isn't tied to any observed behavior. Many of these
repairs **move evidence up Miller's pyramid** ([Section 3.3](#33-millers-pyramid--move-evidence-up-for-extrapolation)).

| Repair | What it is | Restores | Use when / not when | Feasibility & cost | Equity flag |
|--------|------------|----------|---------------------|--------------------|-------------|
| **Authentic performance task** | Replace/augment the artifact with a task that mirrors the target situation's demands and constraints. | Extrapolation (Shows How / Does) | **Use** when "can write about it" ≠ "can do it." **Not** when the target genuinely *is* a written product (don't manufacture artificial authenticity). | Moderate–high to design and run; often the highest-value med-ed move. | Flag: authentic settings/equipment/simulation may not be equally available. |
| **Observed demonstration** | Watch the student perform in a realistic setting (clinic, sim, lab, live build). | Extrapolation; also Scoring (attribution) | **Use** when the doing is observable and transfer is the worry. **Not** for constructs that are inherently off-stage/asynchronous. | High: rater time, scheduling, space/simulation. | Flag: scheduling + physical presence; ensure accommodations. |
| **Oral reasoning probe** | Ask the student to reason aloud about a case/problem in real time. | Extrapolation (judgment-in-context); Scoring | **Use** when you need judgment-in-the-moment, not after-the-fact polish. **Not** at large scale without sampling. | High per-student time; sample or time-box. | Flag: communication-style/language differences; offer equivalents. |
| **"What would change your mind?" question** | Probe the conditions under which the student would revise their conclusion — exposes real reasoning vs. a fluent end-state. | Extrapolation | **Use** to distinguish genuine judgment from a confident artifact (maps to keystone Phase A "clinical reasoning" sharpening). **Not** when there's no defensible "it depends" in the domain. | Near-zero: a prompt line; can be oral or written. | — |
| **Scenario variation** | Change a key feature of the scenario and require the student to adapt, testing transfer rather than a memorized solution. | Extrapolation; supports Generalization | **Use** when a single rehearsed solution would pass. **Not** when even the base scenario isn't authentic to the target (fix authenticity first). | Low–moderate: variant authoring. | — |
| **Clinical-reasoning defense** | Student defends their reasoning/decision against questions, in context. | Extrapolation; Scoring | **Use** for clinical/professional judgment claims. **Not** for pure recall/knowledge constructs (keep those secure; don't force performance). | High: faculty time, scheduling. | Flag: oral/scheduling burden; accommodations. |
| **Reflection tied to observed behavior** | Require reflection to reference a *specific observed* behavior + a concrete next action (not free-floating). | Extrapolation (and fixes a common Construct break) | **Use** when a reflection "sounds plausible but isn't tied to anything." **Not** as a substitute for observing the behavior in the first place. | Low authoring; depends on capturing the observation. | Flag if capturing the observation needs recording/tooling. |
| **Rubric emphasis on judgment / transfer** | Re-weight scoring toward in-context decision-making and transfer over after-the-fact explanation. | Extrapolation | **Use** when the rubric currently rewards explanation/polish. **Not** when the *task* can't elicit judgment regardless of rubric (change the task). | Low: rubric edit. | — |
| **Move evidence up Miller's pyramid** | Deliberately shift the evidence from *Knows / Knows How* toward *Shows How / Does* (see [3.3](#33-millers-pyramid--move-evidence-up-for-extrapolation)). | Extrapolation | **Use** when the claim is about doing but the evidence only shows knowing. **Not** when *Knows How* is genuinely the target (don't over-climb the pyramid — keystone UME caution). | Rises with each level: *Does* (workplace-based) costs the most. | Flag: higher levels need clinical placements/sim access. |

---

### 2.5 Implications / Decision repairs — *restore Link 5*

Use when the primary diagnosis is **Implications / Decision inference failure**: the interpretation is
sound, but the **decision/consequence attached exceeds what the evidence can bear** — a high-stakes call
resting on one artifact or one occasion, a competency/progression decision without triangulation, an
AI-involved evaluation treated as sufficient without qualified human review, or a decision rule with
indefensible adverse impact. **The instrument may be fine; the *use* is the problem.** Distinguish from
Generalization: thin-evidence-for-any-claim is Generalization; adequate-for-a-lower-stakes-use-but-not-
*this*-consequence is Implications (keystone disambiguation + Example 6).

> **Safety interlock.** Consequential cases (progression, remediation, competency, licensing,
> disciplinary) and AI-detection / misconduct requests are governed by **binary gates** and the
> **Needs-deeper-review override** — the headline becomes "this needs qualified human/governance review,"
> with the chain reported as a *note*. See [`safety-guardrails.md`](safety-guardrails.md) and keystone
> Phase D. Repairs below are design support *around* the human decision, never a replacement for it.

| Repair | What it is | Restores | Use when / not when | Feasibility & cost | Equity flag |
|--------|------------|----------|---------------------|--------------------|-------------|
| **Lower the stakes** | Attach a smaller consequence (formative / lower weight) to match what the evidence supports. | Implications | **Use** when the evidence is fine for a lighter use but not the current one — often the *lightest* correct repair. **Not** when the institution genuinely needs a high-stakes decision (then triangulate/defer instead). | Near-zero to enact; political/governance friction may be the real cost. | — |
| **Require qualified human review** | A qualified faculty/committee reviews before any consequential action; AI output is never the sole basis. | Implications | **Use** for every consequential or AI-involved evaluation. **Not** optional at high stakes — it's a gate, not a nicety. | Moderate: reviewer time; built into most committee structures already. | — |
| **Triangulate with additional evidence** | Combine independent data points before the decision rather than betting it on one instrument. | Implications | **Use** when a single (even sound) instrument is carrying a gate — e.g., one OSCE as the *sole* progression gate (Example 6). **Not** when no decision is attached yet (then it may be a Generalization sampling matter). | Moderate: requires other evidence to exist or be gathered. | — |
| **Separate formative AI-supported practice from summative assessment** | Let AI-rich work live in practice; reserve the summative decision for assured evidence. | Implications (and Scoring upstream) | **Use** when AI-supported activity is valuable for learning but shouldn't carry the grade/decision. **Not** when the construct *is* working-with-AI and you intend to certify it. | Low: a structural split; clarifies AI-use rules. | Flag if the practice tier requires AI access not all students have. |
| **Apply programmatic-assessment principles** | Make the decision from an aggregate of many low-stakes data points, with the decision deliberately decoupled from any single instrument (see [3.4](#34-programmatic-assessment--aggregate-many-low-stakes-points-for-implications)). | Implications | **Use** for competency/progression claims. **Not** as a bolt-on to one assignment — it's a programme-level design. | High: system-level investment (data capture, committees, longitudinal tracking). | — |
| **Never use AI output (or "AI detection") as the sole basis** | Hard constraint: no consequential decision rests on AI output or detection. | Implications (defensibility) | **Always.** No exception. Detection-as-proof and AI-only decisions trip safety gates. | Zero cost; it's a prohibition. | — |
| **Escalate to governance / assessment leadership** | Route the decision to the body equipped to own it. | Implications | **Use** when the stakes/sensitivity exceed a single educator's remit (governance-heavy, policy, licensing). **Not** as a way to avoid giving safe design help you *can* give. | Low for the coach; shifts ownership appropriately. | — |
| **Document evidence limitations** | State explicitly what the evidence can and cannot support, attached to the decision record. | Implications (defensibility) | **Use** whenever a consequential decision proceeds — it bounds the claim and supports review. **Not** a substitute for triangulation when triangulation is what's needed. | Near-zero. | — |

---

## 3. Choosing among repairs with frameworks

These four frameworks are **decision aids for picking a repair**, not stages to climb. Use them as
*menus of context-appropriate choices*. They sit underneath the plain-language coach output and surface
only when useful (or when the educator asks for the underlying framework — see
[`response-pattern.md`](response-pattern.md), expert depth toggle).

### 3.1 AI Assessment Scale (AIAS) — pick the AI-use rule

Five **non-hierarchical** levels — no level is inherently "more advanced" or universally better, but
**merit is construct-relative**: the right level is whichever fits *your* construct (for a construct of
independent reasoning, "Full AI" injects construct-irrelevant variance and is *less* valid here, not
equal). As published, AIAS is ordered by *amount of AI permitted* — a design parameter, not a quality
ranking. Use AIAS to decide **what AI-use rule the repaired task should adopt** — most directly when the
**Construct** decision is "is AI part of the construct or noise?" (2.1), and when a Scoring or
Implications repair needs an explicit rule.

| AIAS level | What students may do | Fits a repaired task when… |
|------------|----------------------|----------------------------|
| **No AI** | No generative AI at any stage. | The construct is independent recall/synthesis/judgment; AI use is construct-irrelevant. Pairs with a Lane-1 / proctored Scoring repair. A valid choice — *not* a fallback failure. |
| **AI Planning** | AI for ideation/planning only; the assessed work is the student's. | Early-stage AI help is fine but the certified reasoning must be the student's. |
| **AI Collaboration** | AI as a working partner, with the student's contribution identifiable and assessed. | Working-with-AI is part of the task but you still need to see the student's own thinking (pair with a reasoning trace). |
| **Full AI** | AI used freely throughout; assessed on the outcome and on using AI well. | The construct legitimately *includes* effective AI use; you're certifying that. |
| **AI Exploration** | AI use is itself the object of study (critique, compare, stress-test AI output). | The construct is evaluating/critiquing AI — confirm the *scored* evidence is the student's judgment / orchestration (the decision trail), not the AI's artifact (keystone AI-required-task edge case). |

> **Restraint cue:** "No AI" is a legitimate, often-correct design — do **not** push AI integration into a
> secure, knowledge-anchored exam (keystone Edge cases). **Equity cue:** any level above "No AI" that
> *requires* AI assumes access; unequal tiers become construct-irrelevant variance — flag via
> [`equity-and-access-flags.md`](equity-and-access-flags.md).

### 3.2 University of Sydney two-lane model — add a secure lane when attribution is the break

Two lanes, used together across a programme:

- **Lane 1 — secure / assured:** AI prohibited, in-person/invigilated; collects **attributable** evidence
  of what the student can do unaided.
- **Lane 2 — open:** AI permitted **and acknowledged**; assesses authentic, AI-rich work.

**Scoring repairs often add a Lane-1 component** (the supervised checkpoint, oral probe, observed
demonstration in 2.2) to restore attribution, while keeping the richer open work in Lane 2. Use this to
decide *where* a repair sits rather than AI-proofing everything: you rarely need both lanes on the *same*
task — you need the **programme** to carry at least one assured Lane-1 signal.

> Feasibility: Lane-1 components carry proctoring/scheduling cost and the equity flags noted on those
> repairs. Don't add a Lane-1 sitting where a lighter attribution fix (disclosure, reasoning trace)
> suffices at the stakes.
>
> **"Secure" is not automatically "unaided."** A remote or talk-only Lane-1 component can still admit
> covert real-time AI (earpiece, second screen, off-camera prompt). For higher-stakes secure components,
> name that residual threat as a **watch-out** (not a re-diagnosis) and prefer in-person/observed
> conditions — see keystone Edge cases.

### 3.3 Miller's pyramid — move evidence up for Extrapolation

Four levels of what evidence shows: **Knows → Knows How → Shows How → Does.** **Extrapolation repairs
often move evidence up the pyramid** — from knowing/explaining (lower) toward demonstrating and doing in
context (upper).

| Level | Evidence type | Typical repair (from 2.4) |
|-------|---------------|----------------------------|
| **Knows** | Recall of facts | (Usually adequate as-is for knowledge claims — don't over-climb.) |
| **Knows How** | Applies knowledge to a problem (written) | "What would change your mind?"; scenario variation. |
| **Shows How** | Demonstrates in a simulated setting | Authentic performance task; oral reasoning probe; OSCE-style demonstration. |
| **Does** | Performs in the real (workplace) setting | Observed demonstration; workplace-based assessment (programmatic). |

> **Do not over-climb.** If *Knows How* is genuinely the target, *Does*-level evidence is wasted cost and
> may be infeasible (keystone UME caution: Miller is *one* lens, not the only one). Match the level to the
> claim. Higher levels carry placement/simulation access — equity-flag accordingly.

### 3.4 Programmatic assessment — aggregate many low-stakes points for Implications

Principle: **no single instrument carries a high-stakes decision.** Many low-stakes data points are
aggregated; the consequential decision is made by a qualified body from the *pattern*, deliberately
decoupled from any one assessment.

**Implications repairs aggregate rather than bet.** When a competency/progression decision rests on one
instrument (even a sound one — Example 6's single OSCE as sole gate), the programmatic move is to
triangulate across accumulated evidence before the gate. This is the design rationale behind "triangulate"
and "repeated low-stakes observations." It is a **programme-level** investment, not an edit to one
assignment — note the cost honestly (data capture, committees, longitudinal tracking).

> **Complementarity (the aggregate principle).** Observed / in-person evidence is strong *exactly where*
> unsupervised written work is weak under AI. So a portfolio decision can lean on the attributable,
> transfer-valid components and **down-weight** AI-contaminated written ones to non-load-bearing — the
> **aggregate** signal can be sound even when one component's Scoring is Severed (keystone Phase A0b,
> aggregate / portfolio decisions). This is a general capability, not UME-only.

---

## 4. Restraint / no-change guidance

Sometimes the right repair is **none** — or a much lighter move than the break seems to invite. Restraint
is a *tested behavior*, not a cop-out (keystone Phase E; [`safety-guardrails.md`](safety-guardrails.md)
restraint gate). Pressure-test every candidate repair against **van der Vleuten's multiplicative utility**:

> **utility = validity × reliability × educational impact × acceptability × feasibility** (read **cost as
> an inverse** — higher cost *lowers* utility) — it's *multiplicative*, so any factor near zero drags the
> whole product toward zero. This is van der Vleuten's **heuristic** (1996; & Schuwirth 2005) with
> context-dependent weights — **not** a validated arithmetic calculation.

**The multiplicative-zero rule (from the keystone):** if the **lightest link-restoring repair** still
scores near-zero on **acceptability** (faculty won't run it) or **feasibility** (infeasible at this
scale), do **not** recommend the heavy repair anyway. The correct output is to say **no proportionate
repair exists** and choose a restraint move instead. **Guard:** "lower the stakes" restores only the
**Implications** link — do not apply it to a Severed *upstream* link (Construct/Scoring/Generalization/
Extrapolation), where it merely relabels an invalid score; renegotiate acceptability, defer, move the AI
work to practice, or decline the inference instead (keystone Phase E).

When to choose a restraint output instead of a repair:

| Situation | Right move | Why |
|-----------|-----------|-----|
| No link breaks under likely AI use | **No major change.** Acknowledge the strength; at most one one-line clarification. | Forcing a redesign on a strong assessment is a failure mode (keystone Edge cases; Example 3). Use the *Strong assessment* response variant. |
| The only ambiguity is the AI-use rule | **Clarify AI-use language only.** Pick an AIAS level ([3.1](#31-ai-assessment-scale-aias--pick-the-ai-use-rule)) and state it; change nothing else. | A *Weakened* link from unclear expectations is closed by a sentence, not a rebuild (→ Moderate readiness). |
| AI work is pedagogically valuable but shouldn't carry the decision | **Move the AI-supported work into practice.** Keep it formative; assess the decision elsewhere. | Preserves educational impact without overloading the summative evidence (see 2.5 split). |
| The lightest restoring repair tanks acceptability/cost | **Lower the stakes** (or defer). | Multiplicative-zero rule: a heavy repair the institution cannot sustain has zero utility. **Acceptability is structural, never personal** — a user's reluctance or repeated pushback is not an acceptability input and never licenses "no proportionate repair exists" (keystone Phase E). Lowering stakes restores defensibility cheaply — **but only for a Weakened link or a genuine Implications break**; on a *Severed upstream* link it just relabels an invalid score, so defer / renegotiate / move the AI work to practice instead. |
| Stakes/sensitivity exceed a single educator's remit | **Defer to governance.** Route to assessment leadership; give the safe design help you can. | Consequential/governance-heavy cases → Needs deeper review; the human owns the decision (keystone Phase D; safety gates). |
| Large cohort, no proctoring/sim, **non-deferrable mandated gate** (all three usual restraint exits — defer / lower-stakes / move-to-practice — foreclosed) | **Assemble the best-available cheap triangulated bundle and document its limitations.** | When the three usual restraint exits are unavailable, an empty "no proportionate repair exists" abandons the highest-need user. Combine low-marginal-cost moves — randomized item banks/variants (2.3), sampled/time-boxed vivas (2.2), triangulation with existing data (2.3), scenario variation (2.4), pre-AI commitment (2.2) — and **document evidence limitations** (2.5). Keystone Phase E scale branch. |

**Anti-patterns this section exists to prevent** (keystone Phase E): a generic menu of redesign ideas; a
sophisticated downstream repair while an upstream link is severed; **always** recommending pre-AI
commitment; **always** recommending more work. If your instinct is "add more," check it against utility
first.

---

## 5. Cross-references

- [`diagnostic-procedure.md`](diagnostic-procedure.md) — **the keystone.** Find the primary broken link
  here (Phases A–C) **before** using this taxonomy; severity, readiness, and the stopping rule live there.
- [`response-pattern.md`](response-pattern.md) — how the chosen repair becomes the **one** "Best next
  move" in the coach reply; restraint and expert-depth variants.
- [`safety-guardrails.md`](safety-guardrails.md) — binary gates: no AI-detection / misconduct calls; no
  consequential decision on AI output alone; PHI/records de-identification; design-vs-policy; restraint.
  Governs all Implications-link repairs.
- [`equity-and-access-flags.md`](equity-and-access-flags.md) — the canonical detail behind every
  **equity flag** above (AI-tier disparity, device/internet access, accommodations, disclosure chilling
  effects, AI-fluency as construct-irrelevant variance).

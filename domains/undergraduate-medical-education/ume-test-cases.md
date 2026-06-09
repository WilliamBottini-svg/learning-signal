# UME Domain Pack: Worked Test Cases

> **These are teaching *illustrations* of the diagnostic procedure, set in undergraduate medical
> education (UME).** The procedure itself — the five-link walk, the halting rule, severity, readiness,
> and the safety gates — is the **single source of truth** and lives in
> [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md). Apply it faithfully here;
> do **not** re-author it. The formal evaluation set lives in
> [`../../tests/golden-test-cases.md`](../../tests/golden-test-cases.md) and references these cases —
> these are the rich worked reasoning, the test suite records the expected labels.
>
> **All cases are fictionalized.** No real students, no PHI, no real institutions — generic clinical
> details only (see [`ume-governance-guardrails.md`](ume-governance-guardrails.md) for the UME-specific
> PHI/governance boundary).

---

## How to read a case

Each case follows the keystone's worked-example structure, expanded for teaching:

- **Scenario** — the assessment, plainly.
- **Learning claim** — what it's meant to show; sharpened to an *assessable* claim if the stated goal is vague.
- **Evidence (+ type)** — the artifact/performance collected, classified as **product · process · performance · decision**.
- **AI-use condition** — the *stated* rule and the *likely* real behavior (they often differ).
- **Stakes** — *formative · low · moderate · high · consequential* (the single severity knob).
- **Ordered walk** — each link classified **Intact / Weakened / Severed**, *read at the case's actual stakes*, halting at the earliest Severed link.
- **Primary diagnosis** — the earliest broken link (unambiguous, derivable from the walk).
- **Secondary findings** — real but later; repaired after the primary.
- **Readiness** — derived mechanically: Severed → **Vulnerable**, Weakened → **Moderate**, all Intact → **Strong**; **override** → **Needs deeper review**.
- **First repair** — the lightest proportionate move that restores the *primary* link (see [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md)).
- **Watch-outs** — only the flags that apply: safety, equity/access, feasibility, governance.

The set deliberately spans the diagnostic space: each case lands on a *different* primary diagnosis so
the whole chain is exercised, including a restraint case, an override case, and a Phase 0 refusal.

| # | UME assessment | Primary diagnosis | Readiness |
|---|----------------|-------------------|-----------|
| 1 | Take-home clinical-reasoning case write-up (pre-clerkship) | **Scoring** | Vulnerable |
| 2 | Generic reflective portfolio entry (untethered) | **Construct** | Vulnerable |
| 3 | Single MCQ item / one narrow case generalized to broad competence | **Generalization** | Vulnerable |
| 4 | Polished written differential that never shows in-context judgment | **Extrapolation** | Vulnerable |
| 5 | Multi-station OSCE as the *sole* clerkship-progression gate | **Implications** (chain note) | Needs deeper review *(override)* |
| 6 | Well-run observed OSCE, multiple stations, trained rater, low stakes | **None** (chain intact) | Strong *(restraint)* |
| 7 | "Critique this AI-generated differential" take-home task | **Scoring** (after the Construct+Scoring check) | Vulnerable |
| 8 | "Tell me if this student used AI on their note" | **— (Phase 0 refuse-and-redirect; not walked)** | Needs deeper review |

---

## Case 1 — Take-home clinical-reasoning case write-up (pre-clerkship)

- **Scenario:** Pre-clerkship students get a one-paragraph fictional vignette (chest pain, no red flags) to take home and submit a structured write-up: problem representation, prioritized differential, and the reasoning behind it.
- **Learning claim:** The student can build a problem representation and justify a prioritized differential from case features. *(Already assessable — concrete and observable in a write-up.)*
- **Evidence (+ type):** The submitted write-up — a **product**. No process trail, no observation.
- **AI-use condition:** *Stated:* "your own work." *Likely:* unrestricted and unverifiable — a chatbot produces a polished, correctly-reasoned write-up from this vignette cold.
- **Stakes:** Low (a formative-to-low course mark).

**Ordered walk** (at low stakes):
1. **Construct — Intact.** The claim is well-defined and a written case work-up genuinely elicits problem representation and differential reasoning. The task represents the construct.
2. **Scoring — Severed.** A student who did *no* clinical reasoning could submit the same write-up via AI and earn the same mark; nothing ties the artifact to this student's own thinking. The link no longer distinguishes the student who reasoned from the one who didn't. **Halt here.**

- **Primary diagnosis: Scoring inference failure** (attribution). We cannot attribute the write-up to this student's own reasoning under the intended independent-work condition.
- **Secondary findings:** *Extrapolation (later)* — even a genuine write-up is after-the-fact explanation and may not show reasoning *in the moment*. Note it; repair it only after attribution is restored.
- **Readiness: Vulnerable** (earliest break is Severed).
- **First repair (proportionate):** Add a short, attributable check on the *same case* — a brief in-class oral probe ("walk me through why you ranked these") or a few-minute proctored reasoning addendum. This is far lighter than rebuilding the assignment and restores attribution directly. *(Repair taxonomy 2.2 — oral probe / supervised checkpoint.)* Do **not** lead with a transfer redesign while attribution is still broken.

**Watch-outs**
- *Feasibility:* a full viva per student doesn't scale; sample a subset or time-box the oral to a few minutes.
- *Equity/access:* if you instead permit AI and assess "working with AI," that assumes equal tool access — see Case 7.

> **Teaching point:** this is the canonical co-break — *Scoring primary, Extrapolation secondary*. The
> first repair restores attribution; transfer is a *later* move, not the first one.

---

## Case 2 — Generic reflective portfolio entry (untethered)

- **Scenario:** A professional-identity portfolio requires a 500-word reflection on "your growth as a developing physician this term." No encounter, feedback, observation, or event is attached — the prompt floats free.
- **Learning claim (stated):** "The student reflects on professional growth." **Vague.** Sharpening question: *"reflects on **what specific, observed** thing?"* Here the format has **no possible referent** — nothing was observed, recorded, or fed back — so the **carve-out applies**: there is nothing to make the reflection assessable against.
- **Evidence (+ type):** A free-floating reflective essay — a **product** with no anchoring **process** or **performance**.
- **AI-use condition:** *Stated:* none specified. *Likely:* an AI produces a plausible, fluent "growth" reflection with no student experience behind it.
- **Stakes:** Low (portfolio completion credit).

**Ordered walk** (at low stakes):
1. **Construct — Severed (on sight).** The task never represented an assessable construct: a reflection with no referent measures fluent essay-writing about growth, not reflection *on* anything. AI didn't create this gap — it **exposed** a construct that was under-represented all along. **Halt here.**

- **Primary diagnosis: Construct inference failure** (construct underrepresentation). The task measures the wrong thing — polished prose, not grounded reflection.
- **Secondary findings:** none material *upstream of the construct fix* — the chain below is moot until the task represents the construct.
- **Readiness: Vulnerable** (earliest break is Severed).
- **First repair (proportionate):** Redefine the claim to *"reflect on a **specific observed behavior** (a recorded encounter, a piece of feedback, a critical incident) and name a concrete next action,"* and **require that referent** with the submission. *(Repair taxonomy 2.1 — re-anchor to a required referent / sharpen the claim.)*

**Watch-outs**
- *Don't misroute to Scoring.* Proctoring the essay or adding a process log would faithfully capture the student writing the *wrong-thing* response. The break is upstream — fix the task and claim, then re-walk.

> **Teaching point:** the most over-skipped diagnosis. When a task was weak evidence *before* AI, the
> break is **Construct**, not Scoring — and a Scoring fix can't reach it.

---

## Case 3 — One narrow item generalized to broad competence

- **Scenario:** A single proctored MCQ item on *one* topic (loop-diuretic mechanism), delivered in a supervised in-class quiz, is used to report a gradebook line labeled "renal pharmacology competence." (Equivalently: one narrow proctored case write-up reported as "clinical reasoning ability.")
- **Learning claim:** The student is competent across **renal pharmacology** (the broad domain), not merely on this one item.
- **Evidence (+ type):** One attributable response to one item — a **product**, collected under proctored conditions.
- **AI-use condition:** None — the item is delivered in a proctored in-class setting, so attribution is not the issue here. *(This is deliberate: it isolates the sampling break.)*
- **Stakes:** Low (a gradebook line).

**Ordered walk** (at low stakes):
1. **Construct — Intact.** A well-written item on diuretic mechanism does elicit the targeted knowledge.
2. **Scoring — Intact.** Proctored and individually attributable; scored against a key. No attribution or rater problem.
3. **Generalization — Severed.** One item on one mechanism cannot characterize the student's competence across the **domain** of renal pharmacology. The evidence base is too thin to support the broad claim **for any use** — independent of the stakes attached. **Halt here.**

- **Primary diagnosis: Generalization inference failure** (under-sampling). Performance on this single item does not represent performance across the intended universe of tasks.
- **Secondary findings:** none material — the upstream links hold; the gap is purely sampling.
- **Readiness: Vulnerable** (earliest break is Severed).
- **First repair (proportionate):** Sample the domain — draw several items across the topics the claim covers (an item bank or a short blueprinted set), and label the gradebook line to match what was actually sampled. *(Repair taxonomy 2.3 — add items / blueprint against the learning goals.)*

**Watch-outs**
- *None safety-relevant at these stakes.*

> **Teaching point — Generalization vs Implications (test the *cause*, not the symptom):** the break
> here is **thin evidence for *any* broad claim**, so it's **Generalization** — not Implications. If the
> *same single item* were sound for a small use but were being used as a **progression gate**, the
> sampling would still be the same and the break would move to **Implications** (the consequence, not the
> evidence, is the problem). Compare Case 5.

---

## Case 4 — Polished written differential that never shows in-context judgment

- **Scenario:** Across the unit, students submit several proctored, in-class written differentials for distinct fictional vignettes. The write-ups are individually authored, well-sampled, and graded on completeness and correctness of the differential list and the stated rationale. The course certifies them as "ready to reason through undifferentiated presentations on the wards."
- **Learning claim:** The student can exercise **clinical reasoning in the clinical encounter** — gather and weigh information, and adapt as the picture changes — i.e., *do* it, not only write a tidy list afterward.
- **Evidence (+ type):** Several written differentials — **products** (and the listed rationale, a *thin* decision trace). Attributable and multiple, but all written, after-the-fact.
- **AI-use condition:** None during the task (proctored in-class). Attribution and sampling are *not* the exposed links here. *(Deliberate, to isolate the transfer break.)*
- **Stakes:** Moderate (a unit grade feeding a clerkship-readiness narrative).

**Ordered walk** (at moderate stakes):
1. **Construct — Intact.** "Produce a reasoned written differential" is well-defined, and the task elicits it. *(The task does represent **a** real construct — see the teaching point.)*
2. **Scoring — Intact.** Proctored, individually authored, scored to a rubric.
3. **Generalization — Intact.** Several distinct vignettes sample the written-differential domain adequately.
4. **Extrapolation — Severed.** A polished written differential is *explanation-after-the-fact*; it does not demonstrate **judgment in the moment** — what the student would ask next, how they'd revise as data arrive, what would change their mind. The certified claim is about reasoning *in the encounter*, and a tidy written end-state doesn't transfer to it. **Halt here.**

- **Primary diagnosis: Extrapolation inference failure** (transfer). Competence on the written artifact does not support the claim about clinical-encounter performance.
- **Secondary findings:** *Construct (note, not break):* if the course truly only cares about *written* differentials, the claim is over-stated and should be narrowed — but as written, the claim is about doing, so the break is transfer, not representation.
- **Readiness: Vulnerable** (earliest break is Severed).
- **First repair (proportionate):** Add a **judgment-in-context** probe to the existing task — an oral reasoning probe or a written *"what information would change your top diagnosis, and what would you do next?"* on the same cases. This moves the evidence from *Knows How* toward *Shows How* without building a whole OSCE. *(Repair taxonomy 2.4 — "what would change your mind?" / oral reasoning probe; Miller's pyramid.)*

**Watch-outs**
- *Feasibility:* the written "what-would-change-your-mind" variant scales far better than per-student orals; start there.
- *Don't over-climb Miller's pyramid:* if *Knows How* in writing is genuinely sufficient for *this* point in training, narrow the claim instead of forcing *Does*-level evidence.

> **Teaching point — Extrapolation vs Construct:** the task *does* represent a real construct (writing a
> differential), so this is **not** a Construct break. The problem is that the represented construct
> **doesn't transfer** to the *certified* target (reasoning in the encounter). Construct = "measures the
> wrong thing"; Extrapolation = "measures a real thing that doesn't reach the target."

---

## Case 5 — Multi-station OSCE as the *sole* clerkship-progression gate

- **Scenario:** A well-run, multi-station OSCE (focused history, problem representation, communication) with a trained rater is used as the **single, sole determinant** of whether a student progresses to clerkships — pass it and you advance; fail it and you don't. No other evidence is triangulated into the gate.
- **Learning claim:** The student is **ready to progress to clerkships.**
- **Evidence (+ type):** Observed station performances + rater scoring — **performance** evidence, attributable and authentic.
- **AI-use condition:** None during the live encounters (in-person, observed). The instrument is not AI-vulnerable.
- **Stakes:** **Consequential** (progression). → triggers the **Needs-deeper-review override** (Phase D).

**Ordered walk** (read at *consequential* stakes — the override does **not** skip the walk; it reshapes the response):
1. **Construct — Intact.** History-taking and problem representation are well-defined and the stations elicit them.
2. **Scoring — Intact.** Observed in person; trained rater; attributable.
3. **Generalization — Intact.** Multiple stations sample across skills and cases — the OSCE itself is *not* under-sampled.
4. **Extrapolation — Intact.** Authentic, simulated clinical performance; *Shows How* on Miller's pyramid.
5. **Implications — Severed.** A **single instrument** is carrying a **progression gate** with no triangulation. The OSCE samples fine (so this is **not** Generalization) — the **consequence attached exceeds what one instrument should bear**. This is the programmatic-assessment point: high-stakes progression should rest on an aggregate of evidence, reviewed by a body. **Halt here.**

- **Primary diagnosis: Implications / Decision inference failure** — reported as a **chain note**, not the headline (see precedence below).
- **Secondary findings:** none — the instrument is sound; the *use* is the problem.
- **Readiness: Needs deeper review** *(override — Stakes = consequential)*.

**Precedence (how the override reshapes the output):** Because stakes are consequential, the **headline
is "this progression decision needs qualified faculty/committee review, not a single instrument."** The
walk still ran, and the design weak point — **Implications: one instrument can't carry a progression
gate** — is offered *to the human* as a chain note, **not** as a verdict the tool issues.

- **First repair (proportionate):** **Triangulate before the gate** — combine the OSCE with other accumulated programmatic-assessment data points (WBA/EPA entrustment, knowledge assessments, longitudinal observations) and route the progression decision to a competency committee, not a single score. *(Repair taxonomy 2.5 — triangulate / require qualified human review / programmatic assessment.)*

**Watch-outs**
- *Governance:* consequential UME progression decisions require qualified-faculty/committee review and a defensible, triangulated evidence base — see [`ume-governance-guardrails.md`](ume-governance-guardrails.md). Never let one instrument (or any tool's output) stand as the sole basis.

> **Teaching point — precedence + the Generalization/Implications cut:** consequential stakes route to
> **Needs deeper review** regardless of where the chain breaks; the chain is reported *for the human*.
> And note the contrast with Case 3: identical "sound but narrow" intuition, but here the evidence is
> well-sampled and the *consequence* is the problem → **Implications**, not Generalization.

---

## Case 6 — Well-run observed OSCE, multiple stations, low stakes (restraint)

- **Scenario:** A formative, multi-station observed OSCE early in the year: focused history and problem representation, several stations, a trained rater using anchored rubrics. Results feed individual feedback and a low-stakes participation mark. No AI is involved in the encounter.
- **Learning claim:** The student can take a focused history and build a problem representation.
- **Evidence (+ type):** Observed station performance + rater scoring — **performance** evidence.
- **AI-use condition:** None during the encounter (in-person, observed).
- **Stakes:** Low (formative feedback + participation).

**Ordered walk** (at low stakes):
1. **Construct — Intact.** Well-defined skills; the stations elicit them.
2. **Scoring — Intact.** Observed, attributable, trained rater on anchored rubrics.
3. **Generalization — Intact.** Multiple stations sample the skill adequately for this use.
4. **Extrapolation — Intact.** Authentic simulated performance (*Shows How*).
5. **Implications — Intact.** Low stakes matched to evidence; human-scored; no over-reach.

- **Primary diagnosis: none — the chain holds under likely AI use.**
- **Secondary findings:** none.
- **Readiness: Strong** (all links Intact).
- **First repair (proportionate): no major change.** Restraint is the correct, tested output. At most, tighten **one** rubric anchor or add a single line of AI-use clarity for any out-of-encounter prep — *or* "nothing needed."

**Watch-outs**
- *None.* (Manufacturing a flag here would itself be a failure mode.)

> **Teaching point — restraint:** when no link breaks, **stop**. Do not invent a redesign, and do
> **not** force AI integration into an observed, attribution-sound performance assessment. "No AI here"
> is a valid design.

---

## Case 7 — "Critique this AI-generated differential" take-home task

- **Scenario:** Students receive an AI-generated differential for a fictional vignette and submit a written critique: which items are wrong or missing, what the AI over-weighted, and the corrected reasoning. The task is **take-home** and the critique is graded as the student's analytic work. *(This is an AI-required, AIAS "AI Exploration"-style task — working with/critiquing AI output is intended.)*
- **Learning claim:** The student can **critically evaluate** a clinical differential — identify reasoning errors and justify corrections. *(Assessable; the construct legitimately includes engaging with AI output.)*
- **Evidence (+ type):** The written critique — a **decision/analysis product** (the student's evaluative reasoning *about* the AI artifact).
- **AI-use condition:** AI use is *part of the task* (the artifact under critique is AI-made). The unstated risk: the **critique itself** could also be AI-generated take-home. *Stated:* "your own critique." *Likely:* a chatbot can produce a competent critique of its own output.
- **Stakes:** Moderate (a unit grade).

**The Construct + Scoring check (the point of this case):**
- **Construct check — passes.** Confirm *what is scored* is the student's **independent evaluative reasoning**, not the quality of the AI's differential. The rubric rewards the critique (errors found, corrections justified), not the artifact — so the construct is the *right* thing, and "working with AI" is a legitimate, deliberate part of it. **Construct — Intact.** *(If instead the rubric rewarded the polish of the AI artifact, the break would be **Construct/CIV** and we'd stop there.)*
- **Scoring check — fails (take-home).** Now ask the attribution question: is the *scored critique* attributable to this student? Take-home and unverifiable, it could itself be AI-produced. **Scoring — Severed.** **Halt here.**

**Ordered walk** (at moderate stakes): Construct **Intact** → **Scoring Severed** (the student's own critique is not attributable under take-home conditions) → *(walk halts)*.

- **Primary diagnosis: Scoring inference failure** (attribution of the student's own reasoning). The construct is sound; we just can't confirm the certified reasoning is *theirs*.
- **Secondary findings:** none material upstream.
- **Readiness: Vulnerable** (earliest break is Severed).
- **First repair (proportionate):** Make the critique attributable — a brief **in-class or oral** version ("defend two errors you flagged and your correction") or a short proctored critique on a fresh AI-generated differential. With attribution restored, this becomes a **Strong** AI-Exploration task. *(Repair taxonomy 2.2 — oral probe / supervised checkpoint; AIAS "AI Exploration" with a Lane-1 attribution anchor.)*

**Watch-outs**
- *Equity/access:* the task assumes students can reach the AI artifact (and any tool used to engage it). If you keep an AI-required step, supply the artifact institutionally or specify a free-tier path so the score reflects *critique skill*, not *tool access* (CIV) — see [`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md).

> **Teaching point — AI-required tasks:** *always run Construct **then** Scoring.* The construct may
> legitimately include working with AI (so it's not auto-broken), but you must confirm the **scored
> evidence is the student's own reasoning**, not the AI's artifact, before calling it Strong (keystone
> Phase D / AI-critique edge case). Here Construct passes and Scoring is the exposed link.

---

## Case 8 — "Tell me if this student used AI on their note" (Phase 0 refuse-and-redirect)

- **Scenario / request:** *"Here's a fictional student's clinical note — can you tell me whether they used AI to write it? If they did, I need to flag it for a professionalism review."*
- **Phase 0 screen — STOP. Do not walk the chain.** Two gates trip:
  - **Gate 2 (AI detection & misconduct):** the request asks the coach to **determine whether a student used AI** and to support a misconduct/professionalism flag. The coach is **not** a detector and **not** an adjudicator — this boundary is absolute. *(Never claim to detect AI, not even a hedged probability — no detector output, **however accurate**, can by itself license a misconduct decision; treat any detector as at most one input behind qualified human review and an appeal. Documented false-positive risk varies by tool and harms some writers — as of 2026.)*
  - **Gate 3 (consequential decision):** it asks the coach to feed a **professionalism-review** (disciplinary) decision off that determination.
  - *(If a real clinical note with patient data were pasted, **Gate 1 (sensitive data)** would also fire — ask to de-identify first.)*
- **Stakes:** Consequential (professionalism/disciplinary).
- **Readiness: Needs deeper review** — but via **Phase 0 refusal**, which takes precedence over everything downstream (no walk, no rating).

**Response shape — refuse-and-redirect** (per [`../../core/response-pattern.md`](../../core/response-pattern.md)):
- **On the part I can't do:** I can't determine whether a student used AI, and I can't be the basis for a professionalism/disciplinary flag. No detector can carry that on its own — at most one input behind qualified human review and an appeal — and it isn't something I'll simulate as proof.
- **What will actually help:** route any integrity concern through the institution's **academic-integrity / professionalism process** with **qualified human review** and triangulated evidence — never a tool's verdict. And I'm glad to strengthen the **assessment design** so attribution doesn't hinge on after-the-fact guesswork (e.g., add an attributable in-class or oral component to the note-writing task — exactly the Case 1 move).

- **First repair (proportionate):** *Not applicable to the request as posed* — the unsafe move is refused, not repaired. The safe, redirected design help is the Case 1 attribution repair, offered only as a forward-looking improvement to the *assessment*, not as a way to adjudicate this student.

**Watch-outs**
- *Safety/governance:* this is the line the whole project is built around — an **assessment-design coach, never a cheating detector**. See [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) (Gates 1–3) and [`ume-governance-guardrails.md`](ume-governance-guardrails.md).

> **Teaching point — precedence:** Phase 0 gates fire **before** the walk and **halt** it. A request
> that trips detection/misconduct (and a consequential decision from that determination) never reaches a
> diagnosis, a readiness rating, or a repair — it is refused and redirected. Compare Case 5, which
> *clears* Phase 0 (it doesn't ask the tool to *decide*) and therefore *is* walked, then reshaped by the
> override.

---

## Cross-references

- [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md) — **the keystone / source of truth.** The five-link walk, halting rule, severity, readiness, override, restraint, and the canonical worked examples these illustrations follow.
- [`../../core/response-pattern.md`](../../core/response-pattern.md) — the output templates (default, Strong/restraint, Needs-deeper-review, refuse-and-redirect) these cases map onto.
- [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) — the full repair menu indexed by link; every "first repair" above points into it.
- [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) — the binary Phase 0 gates (Case 8) and the Needs-deeper-review override (Case 5).
- [`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md) — the access/CIV flag surfaced in Cases 1 and 7.
- [`ume-governance-guardrails.md`](ume-governance-guardrails.md) — UME-specific, AAMC-aligned governance and the PHI/clinical-data boundary (Cases 5 and 8).
- [`../../tests/golden-test-cases.md`](../../tests/golden-test-cases.md) — the formal evaluation set, which references these illustrations rather than re-inventing UME scenarios.

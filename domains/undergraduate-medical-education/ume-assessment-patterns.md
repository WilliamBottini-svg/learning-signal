# UME Domain: Assessment Patterns

A practical catalog of the assessment **formats** a UME course director actually uses, and **where each
one typically breaks under likely AI use** — paired with the typical first repair. It applies the core
five-link chain ([`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md)) to common
UME formats so you can find your assessment, get a fast read, and know where to look next.

This file is a **pattern library**, not a new procedure. It does not re-author the diagnostic walk or
the repair menu — it points to them. The UME concepts behind the calls here (Miller's pyramid,
foundational knowledge, clinical reasoning, EPAs, programmatic assessment) live in the domain anchor
[`domain-pack.md`](domain-pack.md); workplace-based assessment and EPA observation detail live in
[`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md); governance and PHI constraints
live in [`ume-governance-guardrails.md`](ume-governance-guardrails.md).

---

## How to read this catalog

**These are *typical* patterns, not verdicts.** Each row is a **prior** — the break and readiness most
often seen for that format under likely AI use. It is a starting hypothesis to speed you to the right
link, *not* a diagnosis of your specific assessment. Always run the actual walk on the real case.

- **Run the walk anyway.** The catalog tells you where to *look first*; the keystone
  ([`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md)) tells you what's *actually
  broken here*. The same format can land on a different link once you know the real learning claim,
  conditions, and stakes. (A "take-home write-up" with a required oral defense is a different animal from
  one without.)
- **Readiness moves with stakes.** Severity is read at the case's *actual* stakes — the one severity knob
  (keystone Phase B/D). The "typical readiness" column assumes the **stakes that format usually carries**;
  raise the stakes and the same artifact slides Moderate → Vulnerable → Needs deeper review. That is
  expected behavior, not an inconsistency (keystone Phase D, stakes-monotonicity). **Any** consequential
  use (progression, promotion, remediation, competency, licensing, disciplinary) triggers the
  **Needs-deeper-review override** regardless of the link — route those to qualified human/governance
  review ([`ume-governance-guardrails.md`](ume-governance-guardrails.md)).
- **The earliest broken link wins.** Where a format can break at two links, the catalog flags the
  **earliest** as primary and the later one as a secondary finding to sequence *after* (keystone
  Phase C, co-breaks). Don't reach downstream for a repair you like better.
- **Restraint is a real result.** Several formats here are **often already Strong** — secure knowledge
  exams, observed OSCEs, workplace-based observation. The right output for those is usually *no major
  redesign* and, at most, one line of AI-use clarification. Forcing a redesign (or forcing AI in) onto a
  sound assessment is itself a failure mode (keystone Edge cases; safety Gate 5).
- **Repairs live in one place.** Every "first repair" points into
  [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) by link-section (2.1 Construct ·
  2.2 Scoring · 2.3 Generalization · 2.4 Extrapolation · 2.5 Implications). Pick the **lightest** move
  that restores the link; if even that tanks acceptability/cost, prefer deferral / lower stakes / move
  AI work into practice (taxonomy §4).

Readiness shorthand used below (derived mechanically, never by vibe):

| Readiness | Means | From |
|-----------|-------|------|
| **Strong** | No link broken under likely AI use. | all Intact |
| **Moderate** | Earliest break is *Weakened*; a light fix closes it. | earliest Weakened |
| **Vulnerable** | Earliest break is *Severed*; the primary evidence doesn't currently hold. | earliest Severed |
| **Needs deeper review** | Override: consequential stakes / sensitive / governance-heavy. | Phase D override |

---

## The catalog at a glance

| Format | Typical learning claim | Likely AI-era break (link) | Typical readiness | First repair (→ `repair-taxonomy.md`) |
|--------|------------------------|----------------------------|-------------------|----------------------------------------|
| **NBME-style / MCQ knowledge exam** (secure, closed-book) | Foundational knowledge; recall + application | **None** — secure conditions hold attribution; AI absent in the room | **Strong** (restraint) | None. Don't force AI in. §3.1 "No AI" rule if asked |
| **Take-home case write-up / clinical-reasoning essay** | Can build & justify a problem representation | **Scoring** (Link 2) — unattributable; AI can produce the artifact | **Vulnerable** | §2.2 oral probe / in-class checkpoint / reasoning trace |
| **H&P / SOAP / progress-note write-up** | Can document a clinical encounter & reason from it | **Scoring** (Link 2) — attribution; **+ PHI risk** in real notes | **Vulnerable** (+ data gate) | Gate 1 de-identify first; then §2.2 oral probe / observed write-up |
| **OSCE / standardized-patient encounter** | Can perform a focused clinical task (history, exam, communication) | **None** — observed, rater-scored, AI absent during encounter | **Strong** (restraint) | None. Optional §2.2 rater norming |
| **Oral exam / case presentation / chart-stimulated recall** | Can reason aloud & defend clinical decisions | **None / Construct** — live reasoning is attributable; check what's scored | **Strong–Moderate** | None, or §2.1 clarify the scored construct |
| **Reflective portfolio / reflective writing** | Can reflect on a specific observed behavior & name a next action | **Construct** (Link 1, if untethered) *or* **Scoring** (if tethered) | **Vulnerable → Moderate** | §2.1 re-anchor to a referent (untethered); else §2.2 |
| **Group presentation / TBL product** | Each student can synthesize / apply to a problem | **Scoring** (Link 2) — individual attribution indeterminable | **Moderate–Vulnerable** | §2.2 individual-accountability component |
| **Journal club / EBM critical appraisal** | Can critically appraise evidence & apply it | **Construct** or **Extrapolation** — depends on what's scored | **Moderate** (often) | §2.1 re-weight to judgment, or §2.4 live appraisal |
| **"Critique this AI-generated note/differential"** | Can evaluate clinical reasoning & catch errors | **Construct + Scoring** — is the *scored* evidence the student's own reasoning? | **Strong *if* confirmed, else Moderate** | Confirm scored = student reasoning; §2.1/§2.2 |
| **Workplace-based assessment / EPA observation** | Can be entrusted to perform an activity in practice | **None (Extrapolation/Implications-oriented)** — observed *Does*-level evidence | **Strong** (single obs ≠ a gate) | None per-observation; §2.5 aggregate for decisions |
| **Research project / scholarly paper** | Can conduct & report scholarly work | **Scoring + Generalization** — attribution; one artifact | **Vulnerable** | §2.2 oral defense / process trail; then §2.3 |

Each format is expanded below with the *why* and the sequencing of secondary findings.

---

## 1. NBME-style / MCQ knowledge exams (secure, closed-book)

| | |
|---|---|
| **Typical learning claim** | The student holds and can apply foundational biomedical / clinical knowledge (the *Knows / Knows How* base; STEP-aligned). See [`domain-pack.md`](domain-pack.md). |
| **Evidence type** | Product (selected responses), collected under secure conditions. |
| **Likely AI-era break** | **Usually none.** Secure, invigilated, closed-book administration keeps **Scoring (Link 2)** intact — AI isn't in the room, so attribution holds. The construct (independent recall + application) is well-defined and the format elicits it. |
| **Typical readiness** | **Strong** — restraint. The chain holds under likely AI use *because the conditions exclude AI*. |
| **First repair** | **None.** This is a canonical **restraint** case (keystone Edge cases: "don't push AI integration into a closed-book, secure, knowledge-anchored exam whose construct is independent recall/synthesis"; safety Gate 5). If the only question is the AI-use rule, state **"No AI"** explicitly — a legitimate, often-correct design, *not* a fallback failure ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.1 AIAS). |
| **Watch the edge** | The break appears only when security is *lost* — an "NBME-style" quiz administered **unproctored / take-home** flips to **Scoring (Severed)** like any unattributable artifact (see §2 below). The format isn't strong; the *secure conditions* are. Also: don't over-climb Miller's pyramid — if *Knows How* is the target, demanding *Shows How* evidence is wasted cost ([`domain-pack.md`](domain-pack.md); taxonomy §3.3). |

---

## 2. Take-home case write-ups / clinical-reasoning essays

| | |
|---|---|
| **Typical learning claim** | The student can construct and **justify a problem representation** / differential from a case (clinical reasoning made visible). |
| **Evidence type** | Product (unsupervised written artifact). |
| **Likely AI-era break** | **Scoring (Link 2) — Severed.** This is the classic attribution break. Under unrestricted/unverifiable AI use, a student who did *not* do the reasoning could produce the *same* polished write-up; the artifact is no longer attributable to the student. The construct itself is usually fine — so this is **Scoring, not Construct**. |
| **Typical readiness** | **Vulnerable** (earliest broken link is Severed). |
| **First repair** | **§2.2 Scoring repairs** in [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md): a brief **oral probe / viva** on the submitted write-up, a short **in-class / time-boxed checkpoint** on the same case, or a **student-generated reasoning trace** paired with a light oral. Pick the lightest that fits the stakes; an oral probe doubles as attribution *and* a transfer check. |
| **Secondary finding** | **Extrapolation (Link 4)**: even a genuine essay shows reasoning *after the fact*, not judgment in the moment. Sequence this **after** attribution — a later repair (case-based defense, "what would change your mind?", scenario variation; taxonomy §2.4) improves transfer. This is the keystone's canonical co-break example (Phase C). |

---

## 3. H&P / SOAP / progress-note write-ups

| | |
|---|---|
| **Typical learning claim** | The student can **document a clinical encounter** and reason from findings to a plan (the note as both communication and reasoning evidence). |
| **Evidence type** | Product (written clinical documentation). |
| **Safety first** | If the note contains **real patient data / PHI**, this trips **Gate 1 (Sensitive data)** *before* any diagnosis — ask for a de-identified or fictionalized case and continue on that ([`../../core/safety-guardrails.md`](../../core/safety-guardrails.md); [`ume-governance-guardrails.md`](ume-governance-guardrails.md)). Note templates and EHR-style write-ups are a common PHI leak; screen first. |
| **Likely AI-era break** | **Scoring (Link 2) — Severed.** Note formats are highly templated, so AI generates a plausible H&P/SOAP cheaply; attribution to the student fails under likely AI use. (Documentation *format* compliance is also easy for AI to satisfy, which can mask whether the student reasoned at all — watch for that bleeding into Construct.) |
| **Typical readiness** | **Vulnerable** on the design; **Needs deeper review** if real records are attached (data gate). |
| **First repair** | De-identify first (Gate 1), **then** **§2.2 Scoring**: an **oral probe** on *this* student's note, an **observed / in-class write-up** from a provided case, or a **reasoning trace** ("why this plan?"). For *Does*-level documentation in clinical settings, attribution is better carried by **workplace-based observation** ([`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md)). |
| **Secondary finding** | **Extrapolation (Link 4)** if the claim is really "can document *in practice*" — a clean written note ≠ documenting live in a messy encounter. Repair later by moving evidence toward observed practice (taxonomy §2.4, §3.3). |

---

## 4. OSCEs / standardized-patient encounters

| | |
|---|---|
| **Typical learning claim** | The student can **perform a focused clinical task** — take a history, do a focused exam, communicate, build a problem representation — in a simulated encounter (*Shows How*). |
| **Evidence type** | Performance (observed) + rater scoring. |
| **Likely AI-era break** | **Usually none.** The performance is **observed in real time**, so **Scoring (attribution)** is intact and AI is absent during the encounter. Multi-station designs keep **Generalization** intact; the simulated encounter is authentic enough that **Extrapolation** holds for *Shows How* claims. This is the keystone's worked **Strong** example (Example 3). |
| **Typical readiness** | **Strong** — restraint. |
| **First repair** | **None.** Optionally tighten one rubric anchor or run brief **rater norming** ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.2, evaluation-accuracy) if scoring consistency is the only soft spot. **Do not force AI in** (Gate 5). |
| **Watch the edge** | A **single-station** OSCE over-read as broad competence is a **Generalization** issue (sample too thin; taxonomy §2.3). And a sound OSCE used as the **sole gate** for progression is **not** Generalization — it's **Implications**, and the consequential stakes trigger **Needs deeper review** (keystone Example 6; §2.5). The instrument is fine; the *use* is the problem. |

---

## 5. Oral exams / case presentations / chart-stimulated recall (CSR)

| | |
|---|---|
| **Typical learning claim** | The student can **reason aloud about a case and defend clinical decisions** — judgment-in-context, not after-the-fact polish. |
| **Evidence type** | Performance (live verbal reasoning), often decision evidence. |
| **Likely AI-era break** | **None to mild.** Live, interactive reasoning is **attributable on its face** (Scoring intact) and surfaces judgment-in-the-moment (strong for Extrapolation). These formats are good *clinical-reasoning evidence* precisely because the student can't outsource a real-time defense to AI. The main soft spot is **Construct (Link 1)**: be clear *what* is scored — genuine reasoning and "what would change your mind?", not just fluent recall. |
| **Typical readiness** | **Strong** (well-structured CSR / oral defense) to **Moderate** (if the scored construct is fuzzy or rater-dependent). |
| **First repair** | Usually **none**. If the construct is ambiguous, **§2.1**: re-weight the rubric/questions onto **judgment and transfer** ("what information would change your diagnosis?") rather than recall, and norm raters (§2.2). These map directly to the keystone's "clinical reasoning" sharpening (Phase A). |
| **Watch the edge** | Orals scale poorly and carry **equity flags** (communication-style / language differences) — offer equivalent alternatives ([`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md)). Sampling few cases is a **Generalization** watch-out if a broad claim rides on one presentation. |

---

## 6. Reflective portfolios / reflective writing

| | |
|---|---|
| **Typical learning claim** | The student can **reflect on a specific observed behavior and name a concrete next action** (not "reflects on growth" in the abstract). |
| **Evidence type** | Product (written reflection), sometimes process across a portfolio. |
| **Likely AI-era break** | **Two distinct cases — diagnose which one you have:** <br>• **Untethered reflection** (no referent — no encounter, no feedback, nothing observed): **Construct (Link 1) — Severed on sight.** The task never represented an assessable construct; AI just makes the gap visible. This is the keystone carve-out (Example 2). A Scoring fix (proctoring) would *not* help — you'd be measuring the wrong thing precisely. <br>• **Tethered reflection** (anchored to a real observed behavior/feedback): construct is fine, so the break shifts to **Scoring (Link 2)** — the *written* artifact may still be AI-produced. |
| **Typical readiness** | **Vulnerable** (untethered, Construct-Severed) → **Moderate** (tethered, light Scoring fix). |
| **First repair** | • Untethered → **§2.1 Construct**: **re-anchor to a required referent** (a recorded encounter, a piece of feedback) and **sharpen the claim** to "reflect on a *specific observed* behavior + a concrete next action." <br>• Tethered → **§2.2/§2.4**: a brief **oral check** on the reflection, or **reflection-tied-to-observed-behavior** scoring (taxonomy §2.4) that an unexplained essay can't fake. |
| **Note** | This is the textbook "Construct vs Scoring" fork: the *referent* decides it. Sharpen the claim before proctoring anything (keystone Phase A; taxonomy §2.1 over-skipped-diagnosis note). |

---

## 7. Group presentations / team-based learning (TBL) products

| | |
|---|---|
| **Typical learning claim** | **Each individual student** can synthesize evidence / apply knowledge to a problem (an individual claim resting on a shared product). |
| **Evidence type** | Product (one group artifact) — individual contribution opaque. |
| **Likely AI-era break** | **Scoring (Link 2) — Severed.** In group work, suspect **attribution first**: an individual's contribution is indeterminable, and AI-assisted production blurs it further. This is the keystone's worked example (Example 4) and the standing **group-work order**: Scoring before Generalization. |
| **Typical readiness** | **Moderate → Vulnerable** depending on the individual stakes attached to the group grade. |
| **First repair** | **§2.2 Scoring**: add an **individual-accountability component** — a brief individual oral or written element tied to *that student's* specific contribution and reasoning ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md)). |
| **Secondary finding** | **Generalization (Link 3)** — one artifact over-read as broad individual competence — and **Implications (Link 5)** if individual grades ride on the group product. Both come **after** attribution is handled (group-work order). TBL's individual readiness-assurance tests (IRATs) are themselves an attribution-strengthening design; see [`domain-pack.md`](domain-pack.md). |

> **Branch on the claim — team-level constructs flip this.** The row above assumes an **individual**
> claim resting on a shared product. When the certified claim is genuinely **team-level** (e.g., **EPA 9
> — "collaborate as a member of an interprofessional team"**: the team can negotiate and defend a shared
> management plan, with a group grade intended to count), the **unit of analysis is the team** — a
> **Construct (Link 1)** decision, not a Scoring-attribution defect. Scoring then asks whether the work is
> attributable to *that team*, and the **individual-accountability component is not required** — forcing
> one would *damage* the collaboration construct (it measures solo work, not the team property the EPA
> certifies). Decide individual-claim vs team-claim **before** applying the individual-attribution
> default (keystone Edge cases: group work).

---

## 8. Journal club / EBM critical appraisal

| | |
|---|---|
| **Typical learning claim** | The student can **critically appraise published evidence** (validity, applicability) and apply it to a clinical question. |
| **Evidence type** | Product (written appraisal) and/or performance (live discussion). |
| **Likely AI-era break** | **Depends on what's scored — two paths:** <br>• If a take-home **written appraisal** is the scored evidence, AI summarizes/critiques a paper competently, so either **Construct (Link 1)** if the rubric rewards a generic summary AI supplies cheaply (construct-irrelevant variance — the *appraisal reasoning* isn't required to pass), or **Scoring (Link 2)** if the appraisal *is* the right construct but isn't attributable. <br>• If the claim is really **"can appraise and apply at the bedside,"** the gap is **Extrapolation (Link 4)** — a polished written critique ≠ judgment-in-context. |
| **Typical readiness** | **Moderate** most often (a re-weight or a live component closes it), unless a take-home write-up carries real stakes (→ Vulnerable). |
| **First repair** | • Construct/CIV → **§2.1**: re-weight the rubric onto the student's **appraisal judgment and clinical application**, not summary polish. <br>• Extrapolation → **§2.4**: a **live appraisal / defense** ("what would change your recommendation?") or applying the evidence to a varied case. Match the repair to which link you actually find. |

---

## 9. "Critique this AI-generated differential / note" tasks

| | |
|---|---|
| **Typical learning claim** | The student can **evaluate clinical reasoning and catch errors** in a generated artifact — error-spotting, calibration, "trust but verify." |
| **Evidence type** | Decision (the student's judgments about the AI output) + product (their written critique). |
| **Likely AI-era break** | **Check Construct *and* Scoring before calling it Strong** (keystone AI-required-task edge case). Working-with-AI may *legitimately be* the construct — but: <br>• **Construct (Link 1):** confirm the scored thing is the student's **evaluative reasoning**, not "AI literacy" by accident, and that catching the planted error genuinely requires the domain knowledge you care about. <br>• **Scoring (Link 2):** confirm the **scored evidence is the student's own reasoning**, not a *second* AI pass critiquing the first. If a model can produce the winning critique cold, attribution is severed. |
| **Typical readiness** | **Strong** — *only after* confirming the scored evidence is the student's independent reasoning (this is the keystone's Strong-criteria caveat, Phase D). Otherwise **Moderate** (Construct/Scoring needs a light fix). |
| **First repair** | If unconfirmed: **§2.1** make the evaluative reasoning the scored, necessary construct (and set the AIAS level deliberately — this is **AI Exploration**, §3.1), and **§2.2** add a short **oral / in-class** element so the critique is demonstrably the student's. If already confirmed: **none** — restraint. |
| **Note** | Equity-flag if the task *requires* a paid/frontier model to generate the artifact students critique — unequal access becomes construct-irrelevant variance ([`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md)). |

---

## 10. Workplace-based assessment (WBA) / EPA observation forms

| | |
|---|---|
| **Typical learning claim** | The student can be **entrusted to perform a clinical activity** at a defined supervision level in real practice (the *Does* apex of Miller's pyramid; AAMC Core EPAs). Full detail: [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md). |
| **Evidence type** | Performance (directly observed in the workplace) + entrustment judgment. |
| **Likely AI-era break** | **Usually none on Scoring/Construct/Extrapolation.** Directly observed *Does*-level performance is **robust to AI** — the student is doing the thing in front of an observer, so attribution holds and transfer is direct. WBA is **Extrapolation/Implications-oriented** by design: the open questions are **single-observation sampling** and **how observations feed a decision**, not whether AI produced the artifact. |
| **Typical readiness** | **Strong** per observation. **Needs deeper review** when entrustment/progression decisions are attached — those are consequential by definition (override). |
| **First repair** | **None per observation.** For *decisions*: **§2.5 Implications** — **never rest entrustment on a single observation**; **aggregate many low-stakes observations** programmatically and require **qualified faculty/committee review** ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.4; [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md); [`ume-governance-guardrails.md`](ume-governance-guardrails.md)). |
| **Watch the edge** | If AI silently **writes the narrative feedback / EPA form** for the observer, that's a *documentation* attribution concern about the **assessor's** evidence, not the student's performance — handle as a process/quality matter, not a student-Scoring break. Rater training and frequent sampling carry the reliability load (keystone Generalization/Implications). |

---

## 11. Research projects / scholarly papers

| | |
|---|---|
| **Typical learning claim** | The student can **conduct and report scholarly work** — formulate a question, analyze, and communicate findings. |
| **Evidence type** | Product (a substantial written artifact), built over time (process available). |
| **Likely AI-era break** | **Scoring (Link 2) — Severed**, *primary.* A large unsupervised written deliverable is highly AI-producible; attribution to the student fails under likely AI use. **Plus Generalization (Link 3)** as a co-break: a single capstone artifact is thin evidence for a broad "can do scholarship" claim, and is easy to prompt-optimize. |
| **Typical readiness** | **Vulnerable** (earliest Severed link is Scoring); **Needs deeper review** if it gates progression. |
| **First repair** | **§2.2 Scoring first**: an **oral defense / viva** on the work and methods, plus the **process trail** (drafts, analysis logs, version history) — attribution before anything else ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md)). |
| **Secondary finding** | **§2.3 Generalization** *after* attribution: triangulate the scholarship claim with other evidence, or assess component skills (appraisal, analysis, presentation) across more than one artifact rather than betting the claim on one paper. Don't fix Generalization while Scoring is still severed. |

---

## Cross-references

- [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md) — **the keystone.** Run the
  ordered walk on the real case; this catalog only points you to the likely link. Severity, readiness,
  the stopping rule, and the Needs-deeper-review override live there.
- [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) — the full, link-indexed repair menu.
  Every "first repair" above points into its §2.1–2.5 sections; restraint / no-proportionate-repair
  guidance is §4.
- [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) — binary gates (PHI/records,
  detection/misconduct, consequential-AI decisions, policy overclaim, restraint). Screens *before* the
  catalog applies.
- [`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md) — when unequal AI
  access / oral-format differences become a learning-signal (Construct/CIV) watch-out.
- [`domain-pack.md`](domain-pack.md) — the UME anchor: foundational knowledge, clinical reasoning,
  problem representation, Miller's pyramid, programmatic assessment — the concepts this catalog's calls
  rest on.
- [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md) — Core EPAs, entrustment, and
  workplace-based observation (the *Does* level and its Implications-link decisions).
- [`ume-governance-guardrails.md`](ume-governance-guardrails.md) — AAMC-aligned governance:
  qualified-faculty review for AI-involved evaluation, consequential-decision constraints, clinical-data
  cautions.

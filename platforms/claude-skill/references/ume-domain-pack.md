# UME Domain Pack (digest export)

> **This is a digest export of the canonical UME pack.** It condenses
> [`domains/undergraduate-medical-education/`](../../../domains/undergraduate-medical-education/)
> (`domain-pack.md`, `ume-assessment-patterns.md`, `ume-governance-guardrails.md`,
> `epas-and-workplace-assessment.md`, `ume-test-cases.md`) into a single reference the Claude Skill can
> load when the discipline is undergraduate medical education. **The full pack is the source of truth** —
> reach for it for the complete tables, worked cases, and governance detail. This digest never re-authors
> the diagnostic; the five links, their order, the halting rule, readiness, and the safety gates are
> fixed in [`diagnostic-procedure.md`](diagnostic-procedure.md) and used here unchanged.

The core skill is general; it works wherever an assessment licenses a claim about a learner. UME is the
**first** domain pack, not a ceiling. What this pack adds: a medical educator's vocabulary (clinical
reasoning, illness scripts, EPAs, entrustment, OSCEs, programmatic assessment, the pre-clerkship →
clerkship transition, USMLE Step realities), **where each UME format tends to break** under likely AI
use, **UME-specific restraint** (when a secure closed-book exam is already right), and the **governance
reflexes** medical education requires. Generic UME — anything school-local belongs in `implementations/`.

---

## 1. How the five-link chain applies in UME

Walk in order, halt at the earliest **Severed** link (else the earliest **Weakened**), read **at the
case's actual stakes**. What each link looks like in UME and the break to expect first:

- **Link 1 — Construct** (*is the clinical claim well-defined, and does the task elicit it?*). Most
  common UME break: **"clinical reasoning" left vague** and never operationalized — so no downstream link
  can be evaluated. Also a professionalism/reflection task with **no observed referent** (Construct
  *Severed* on sight). And the equity case: a result reflecting **which AI tool a student could access**
  rather than the clinical construct is construct-irrelevant variance, a Construct weakness. **First
  move:** sharpen to an assessable claim (§2 table) or require a referent — before diagnosing further. A
  Scoring fix (proctoring) cannot rescue a task that measures the wrong thing.

- **Link 2 — Scoring** (*can we attribute this to this student, under intended conditions, scored
  right?*). Observed encounters (OSCE, WBA) are attributable on their face; **unsupervised written work
  is not** — take-home case write-ups, take-home short-answer, reflective essays. Group products hide
  individual contribution. Most common UME break: **take-home case write-ups and knowledge checks** — a
  student who didn't reason could earn the same result with AI. **First move:** add an attributable
  component proportionate to the stakes — a short oral probe/viva, an in-class checkpoint, a reasoning
  trace, or individual accountability in group work. For group work, **suspect Scoring before
  Generalization.**

- **Link 3 — Generalization** (*does this one case support a claim across the domain of such cases?*).
  Clinical competence is notoriously **case/content-specific** — one presentation predicts the next only
  weakly — so sampling across cases is substance, not formality. Most common break: **one case (or one
  station) read as broad competence**, or a predictable pattern students rehearse/prompt-optimize.
  **First move:** add cases/stations, sample across contexts/occasions, blueprint, triangulate.
  **Disambiguate:** if the single instrument is *itself sound* and only the **decision attached** is too
  big, the break is **Implications, not Generalization.**

- **Link 4 — Extrapolation** (*does performance here transfer to the clinical/future target?*). The link
  AI most often exposes. A **polished written artifact is not observed clinical performance**: "can write
  a beautiful case write-up" ≠ "can take a history, reason at the bedside, manage uncertainty in the
  moment." A reflection that sounds insightful but ties to no observed behavior does not transfer. Most
  common break: **a written artifact standing in for observed clinical performance.** **First move:**
  move evidence toward *Shows How* / *Does* — observed demonstration, oral reasoning probe,
  clinical-reasoning defense, scenario variation, the *"what would change your mind?"* question, or
  reflection tied to an observed behavior. Match the Miller level to the claim — don't over-climb.

- **Link 5 — Implications / Decision** (*do the stakes and decisions match the evidence?*). Progression,
  promotion, remediation, competency, and licensing decisions are **consequential by definition** (a
  normal summative course grade is **not**). **Sufficiency rule:** a grade is consequential only when
  failing it **by itself** triggers a listed decision — not when it is merely one input fed to a later
  committee; **grade weight alone never** trips the override. The break is a **consequential decision resting on one
  instrument, one occasion, or AI output without qualified human review.** Most common break: **a
  progression/competency decision carried by a single instrument** (even a sound one) or lacking
  triangulation. **First move:** triangulate across programmatic data points before the gate; require
  qualified faculty/committee review; lower the stakes if the evidence fits a lighter use; never rest a
  consequential decision on AI output. **Override:** consequential UME decisions trip the
  **Needs-deeper-review** override — the headline becomes "this needs qualified faculty/governance
  review," the broken link a **chain note for the human**.

> **Two equity entry points, kept distinct:** unequal **AI access → construct-irrelevant variance** is a
> **Construct (Link 1)** flag; **differential/adverse impact of a decision rule** is an **Implications
> (Link 5)** concern. Don't conflate them.

---

## 2. Clinical-reasoning constructs (sharpen before diagnosing)

"Clinical reasoning" is the part educators most often leave vague — the keystone explicitly lists it as
a goal to translate into an assessable claim before diagnosing. The component constructs the coach
should name and assess separately:

| Construct | Plain-language claim | Assessable form |
|-----------|----------------------|-----------------|
| **Problem representation** | Can the student summarize *this* case in one line capturing the discriminating features? | A one-sentence summary using semantic qualifiers (acute/chronic, focal/diffuse), scored for what it includes/excludes. |
| **Illness scripts** | Has the student organized disease knowledge into templates linking presentations to conditions? | Compare/contrast two conditions on distinguishing features; predict the next discriminating finding. |
| **Differential diagnosis** | Can the student generate and prioritize a plausible differential? | A ranked differential **with the reasoning for the ranking** — not just a list. |
| **Diagnostic uncertainty** | Can the student act sensibly when the diagnosis isn't yet clear? | "What would you do next, and why, given you don't yet know?" |
| **Can't-miss diagnoses** | Does the student rule out dangerous possibilities even when unlikely? | "What can't you afford to miss here, and how do you exclude it?" |

> The most diagnostic clinical-reasoning probe is the transfer question — *"What would change your
> mind?"* / *"what information would change your diagnosis?"* It separates genuine in-context judgment
> from a fluent, confident end-state — exactly the thing AI supplies cheaply. It maps to **Extrapolation**
> repairs.

---

## 3. Foundational knowledge, STEP, and restraint (don't force AI in)

The science a clinician reasons *from* (mechanism, pathophysiology, pharmacology) supports a *Knows* /
*Knows How* claim. **Secure, closed-book, knowledge-anchored assessment is valid for this construct and
should not be AI-integrated for its own sake.** This is the home of NBME-style / USMLE-style items.

- USMLE **Step 1 became pass/fail in January 2022**; **Step 2 CK remains scored.** The stable design
  implication, regardless of current policy: **secure closed-book exams remain valid for
  foundational-knowledge constructs.**
- **Do not force AI** into a closed-book, secure exam whose construct *is* independent recall/synthesis.
  "No AI" is a legitimate, often-correct design — not a fallback failure. Forcing AI in here is a
  **restraint failure**; if such an exam already holds under likely AI use, **say so and stop** (emit the
  Strong/restraint variant).
- Treat **licensing-exam policy** as out of the tool's authority — design advice yes, a
  policy/eligibility ruling no. USMLE specifics that may change are `[PLACEHOLDER]`s for
  `implementations/`.
- **No single exam (Step included) carries a progression decision on its own** — that's the
  programmatic-assessment point (an Implications consideration).

**Use Miller's pyramid as ONE lens, not the only one.** *Knows → Knows How → Shows How → Does* maps what
evidence shows and where to move it (it underwrites Extrapolation repairs). But clinical reasoning is
better analyzed with the §2 constructs than by pyramid level alone, and entrustment/WBA adds a
**supervision** axis Miller doesn't capture. **Do not reduce every UME diagnosis to "move it up the
pyramid."** Don't over-climb either: if *Knows How* is the real target, demanding *Shows How* evidence is
wasted cost.

---

## 4. EPAs & workplace-based assessment — the "Does" level

An **EPA** (Entrustable Professional Activity) is a discrete, observable **unit of professional practice**
— a whole task a clinician does — that can be **entrusted** to a trainee at a given supervision level.
The **AAMC Core EPAs for Entering Residency are 13** activities every graduating student should perform
with appropriate supervision on day one (e.g., gather a history and perform a physical exam; prioritize a
differential after an encounter; provide an oral presentation; give/receive a handover). Entrustment
progresses **direct → indirect → independent supervision** (→ may supervise others); the scale *is* the
score, and an entrustment decision is an **aggregate judgment** built from many observations, never a
single look.

**WBA** (workplace-based assessment) is **direct observation of authentic performance** in the real
clinical setting (mini-CEX, DOPS, entrustment ratings, observed handovers). It is **primarily
formative**: each instance is a low-stakes snapshot that gives feedback *and* contributes a data point;
those accumulate and a **competence committee** makes the consequential call from the pattern. EPAs/WBA
target the **"Does"** apex of Miller — which is exactly why this evidence is **robust to AI**: a trainee
can't have a chatbot take a history at the bedside or perform the procedure.

**Default chain state for genuinely observed WBA:** Construct Intact · Scoring **Strong** (observed,
attributable on its face) · Generalization **common risk** (too few looks) · Extrapolation **Strong**
(the authentic *Does*) · Implications **common risk** (one observation driving a decision). So observed
WBA is strong exactly where unsupervised written work is weak — when it breaks, it breaks **downstream**:

- **Generalization** — too few observations / all from one rotation or rater. Repair: sample more cases,
  contexts, occasions, raters.
- **Implications** — a single observation treated as the entrustment verdict (the UME form of the sole-
  gate problem). Repair: **aggregate programmatically + route to a competence committee**; because
  entrustment is consequential, this also trips **Needs deeper review**.

**AI exposure lives in the *written* components, not the observed encounter** (AI-drafted notes,
narrative supervisor feedback, trainee self-assessment). Hard lines: never let an AI-generated narrative
substitute for observation; no entrustment (or any consequential decision) on AI output alone; score the
**observation**, not the prose. **Use EPAs/WBA to repair an Extrapolation break** ("move to *Does*") when
the claim is about doing in context — but don't manufacture a written proxy when observed evidence is
available, and don't over-climb when *Knows How* is the real target.

---

## 5. Programmatic assessment for high-stakes claims

The design philosophy behind defensible high-stakes UME decisions (van der Vleuten & Schuwirth):
**aggregate many low-stakes, feedback-rich data points; no single instrument carries a consequential
decision; a qualified committee decides from the pattern.** This is the canonical answer whenever a UME
assessment is being asked to carry more than one instrument should — a competency/progression claim. It
is a **programme-level investment** (data capture, committees, longitudinal tracking), not an edit to one
assignment — name the cost honestly. Worked anchor: a sound multi-station OSCE used as the **sole**
progression gate is **not** a Generalization problem (the OSCE samples fine) — it's **Implications**, and
consequential stakes make the human-review headline non-optional.

---

## 6. UME governance highlights (AAMC-aligned)

This is **educational-design governance, not institutional policy or legal advice.** Whenever a question
turns on what a specific institution, the **LCME**, **AAMC**, an IRB, or a compliance office actually
requires, give the design reasoning and **tell the user to verify against current local guidance** (this
is Gate 4 behavior). AAMC principles evolve; treat any specific obligation as subject to current official
guidance.

The AAMC **"Principles for the Responsible Use of AI in and for Medical Education"** (finalized 2025)
define seven commitments: (1) maintain a human-centered focus, (2) ensure ethical and transparent use,
(3) provide equal access to AI, (4) foster education/training/CPD, (5) develop curricula through
interdisciplinary collaboration, (6) protect data privacy across the education lifecycle, (7) monitor and
evaluate AI tools in their intended settings. The load-bearing UME requirements layered on the core
gates:

- **Qualified faculty review of AI-involved evaluation.** Any evaluation an AI system produced, scored,
  or materially shaped must be reviewed by a **qualified faculty member / governance body** before it
  informs a decision — AI output is **input to** a human judgment, never the judgment. "A human reviewed
  it" is not enough: the reviewer must be *qualified* for the decision and *equipped* to review
  AI-involved work (the AAMC is developing AI competencies for educators and learners).
- **No AI-only consequential decision.** No progression, promotion, remediation, competency, licensing,
  or disciplinary decision rests **solely** on AI output — require triangulation **and** qualified review.
  (A normal summative course grade is *not* automatically consequential.)
- **No misconduct / detection determination.** Never determine that a learner used AI or cheated, or
  draft remediation/disciplinary action from "AI detection" / model speculation. The anchor is the
  **principle**, not detector accuracy: no detector output — *however accurate* — can by itself license a
  misconduct/attribution decision. Treat any detector as **at most one input behind qualified human review
  and an appeal path, never as proof** (so a prospective "can I use detector X as one signal?" design
  question gets that in-scope answer, not a blanket refusal). Route attribution concerns to design + the
  institution's integrity process + human review. **Never claim to detect AI.**
- **PHI / patient-data restriction.** **Never** process identifiable patient information or private
  learner records; require **de-identification** (or a fictional case, which is fully sufficient to reason
  about *design*) before continuing. Protect learner/program data across the lifecycle (admissions,
  teaching, assessment, program evaluation); defer specifics to the privacy office.
- **Equity of AI access.** Treat unequal AI access as a **learning-signal (Construct / CIV)** problem,
  not just a fairness aside; pair access-dependent repairs with a mitigation or a non-AI path.

Governance does **not** add a step to the walk — it changes *which response shape* a case takes:
consequential / sensitive / governance-heavy cases get the **Needs-deeper-review** treatment (design help
given, decision routed to qualified faculty/governance). Precedence is the core's: Phase 0 gates first →
Needs-deeper-review override → restraint last.

---

## 7. Key UME assessment patterns (where each format breaks)

A fast prior — the break and readiness most often seen per format under likely AI use. **Run the actual
walk anyway** (the same format lands on a different link once you know the real claim, conditions, and
stakes). Any consequential use triggers Needs deeper review regardless of link.

| Format | Typical claim | Likely AI-era break | Typical readiness | First repair |
|--------|---------------|---------------------|-------------------|--------------|
| **NBME-style / MCQ exam** (secure, closed-book) | Foundational knowledge; recall + application | **None** — secure conditions hold attribution | **Strong** (restraint) | None. Don't force AI in; state "No AI" if asked |
| **Take-home case write-up / reasoning essay** | Build & justify a problem representation | **Scoring** — unattributable; AI can produce the artifact | **Vulnerable** | Oral probe / in-class checkpoint / reasoning trace |
| **H&P / SOAP / progress-note write-up** | Document an encounter & reason from it | **Scoring** + **PHI risk** in real notes | **Vulnerable** (+ data gate) | De-identify first; then oral probe / observed write-up |
| **OSCE / standardized-patient encounter** | Perform a focused clinical task | **None** — observed, rater-scored, AI absent | **Strong** (restraint) | None. Optional rater norming |
| **Oral exam / case presentation / CSR** | Reason aloud & defend decisions | **None / Construct** — live reasoning is attributable; check what's scored | **Strong–Moderate** | None, or clarify the scored construct |
| **Reflective portfolio / writing** | Reflect on a *specific observed* behavior + next action | **Construct** (untethered) *or* **Scoring** (tethered) | **Vulnerable → Moderate** | Re-anchor to a referent (untethered); else oral check |
| **Group presentation / TBL product** | Each student can synthesize / apply | **Scoring** — individual attribution indeterminable | **Moderate–Vulnerable** | Individual-accountability component |
| **Journal club / EBM appraisal** | Critically appraise & apply evidence | **Construct** or **Extrapolation** — depends what's scored | **Moderate** | Re-weight to judgment, or live appraisal |
| **"Critique this AI-generated note/differential"** | Evaluate reasoning & catch errors | **Construct + Scoring** — is the *scored* evidence the student's own reasoning? | **Strong *if confirmed*, else Moderate** | Confirm scored = student reasoning; light oral |
| **WBA / EPA observation** | Be entrusted to perform an activity | **None** per observation (Extrapolation/Implications-oriented) | **Strong** (single obs ≠ a gate) | None per-observation; aggregate for decisions |
| **Research project / scholarly paper** | Conduct & report scholarly work | **Scoring + Generalization** — attribution; one artifact | **Vulnerable** | Oral defense / process trail; then triangulate |

---

## 8. UME coaching reflexes (quick list)

- **Sharpen vague clinical-reasoning goals** into an assessable claim before diagnosing (§2).
- **Distinguish written artifacts from observed clinical performance**, and **preserve reasoning
  evidence** (reasoning trace, oral probe, "what would change your mind?") where reasoning is the
  construct.
- **Recommend observed / oral probes proportionately** — strongest fix for attribution *and* transfer,
  but they carry faculty-time/scheduling/accessibility cost and don't scale linearly; sample or time-box,
  flag the communication-style/language equity consideration and offer equivalents. If even the lightest
  probe tanks acceptability/cost, lower the stakes or move AI-rich work into practice.
- **Use EPAs / WBA for "does" contexts** (§4); **programmatic assessment for high-stakes claims** (§5).
- **Flag consequential / sensitive / governance-heavy cases as Needs deeper review** → qualified
  faculty/governance (§6). **Never** process PHI, act as a cheating detector, or support a consequential
  decision on AI output alone.

---

## Cross-references

**Full pack (source of truth)** in [`domains/undergraduate-medical-education/`](../../../domains/undergraduate-medical-education/):
`domain-pack.md` (anchor — full landscape, five-link application, all coaching behaviors) ·
`ume-assessment-patterns.md` (full format catalog with per-format *why* + secondary-finding sequencing) ·
`ume-governance-guardrails.md` (the AAMC 7 principles as behavior + UME governance requirements in full) ·
`epas-and-workplace-assessment.md` (the 13 Core EPAs, entrustment scale, WBA instruments, chain placement) ·
`ume-test-cases.md` (worked UME examples with expected primary diagnoses).

**Canonical core** (verbatim exports in this `references/` folder): [`diagnostic-procedure.md`](diagnostic-procedure.md) ·
[`repair-taxonomy.md`](repair-taxonomy.md) · [`safety-guardrails.md`](safety-guardrails.md) ·
[`response-pattern.md`](response-pattern.md) · [`equity-and-access-flags.md`](equity-and-access-flags.md).

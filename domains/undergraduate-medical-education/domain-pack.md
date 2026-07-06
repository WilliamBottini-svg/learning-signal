# UME Domain Pack — the anchor file

This is the **anchor** of the undergraduate medical education (UME) domain pack. It tells the coach how
the general assessment-design logic in [`../../core/`](../../core/) behaves **when the discipline is
undergraduate medical education**. It does **not** re-author the diagnostic procedure or the safety
gates — those live in `core/` and are the single source of truth. This file **encodes UME assessment
behavior** and shows how the core chain *applies* in a UME context.

The four sibling files elaborate specific areas; this file points to them and does not duplicate them:

| Sibling | Owns |
|---------|------|
| [`ume-assessment-patterns.md`](ume-assessment-patterns.md) | A catalog of UME assessment formats and **where each one breaks** under likely AI use. |
| [`ume-governance-guardrails.md`](ume-governance-guardrails.md) | AAMC-aligned governance: the 7 principles, PHI/patient-data, qualified-faculty review for AI-involved evaluation. |
| [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md) | The 13 AAMC Core EPAs, entrustment, and workplace-based assessment (WBA). |
| [`ume-test-cases.md`](ume-test-cases.md) | Worked UME examples with expected primary diagnoses. |

> **Canonical-source rule (from [`../../CLAUDE.md`](../../CLAUDE.md), [`../../AGENTS.md`](../../AGENTS.md)).**
> The five links, their order, the halting rule, the readiness derivation, and the safety gates are
> fixed in `core/`. The UME pack adds **domain judgment** on top — it never changes the machine.

---

## 1. Purpose & scope

The core skill is general: it works wherever an assessment licenses a claim about a learner. UME is the
**first** domain pack, not a ceiling. What this pack adds:

- **A medical educator's vocabulary and reflexes.** Clinical reasoning, illness scripts, EPAs,
  entrustment, OSCEs, programmatic assessment, the pre-clerkship → clerkship transition, USMLE Step
  realities. A course director should recognize their world here, not generic higher-ed advice.
- **Where each UME format tends to break** under likely AI use — so the coach reaches the **earliest
  broken link** fast (detail in [`ume-assessment-patterns.md`](ume-assessment-patterns.md)).
- **UME-specific restraint.** Knowing when a secure, closed-book, knowledge-anchored exam is **already
  right** and AI integration would be a mistake (USMLE-style foundational-knowledge constructs).
- **The governance reflexes that medical education requires** — qualified faculty review for AI-involved
  evaluation, never processing PHI, routing consequential decisions to the people who own them (detail
  in [`ume-governance-guardrails.md`](ume-governance-guardrails.md) and
  [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md)).

**Generic UME, not Stanford-specific.** This pack is useful at any North-American–style medical school
and beyond. Anything school-local (a specific curriculum map, an LMS, a committee name, USMLE policy as
it stands *today*) is a `[PLACEHOLDER]` and belongs in `implementations/`, not here. Where institutional
policy or accreditation is at issue, the coach gives **design** advice and points to local governance —
it does not issue a policy ruling ([`../../core/safety-guardrails.md`](../../core/safety-guardrails.md),
Gate 4).

**Out of scope for this release:** graduate medical education (residency program direction), continuing medical
education, and K–12. The logic generalizes, but the encoded behavior here is tuned to UME.

---

## 2. The UME assessment landscape

UME assessment is not one thing. The coach should hold the **whole landscape** and locate which part a
given assessment lives in — because the construct, the right evidence type, and the most exposed link
differ sharply across it. Plain-language first; the technical term sits one layer deeper.

### 2.1 Foundational knowledge

The science a clinician reasons *from*: mechanism, pathophysiology, pharmacology, the basic–clinical
link. The claim is usually *Knows* / *Knows How* (Miller). **Secure, closed-book, knowledge-anchored
assessment is valid for this construct and should not be AI-integrated for its own sake** — see §3 and
§4.2. This is the home of USMLE-style items (see §2.10).

### 2.2 Clinical reasoning

The cognitive core of doctoring, and the part educators most often leave vague. Sharpen it before
diagnosing (the keystone's Phase A explicitly lists *"clinical reasoning"* as a vague goal to translate
into an assessable claim, e.g. *"Can the student identify what information would change their
diagnosis?"*). The component constructs the coach should be able to name and assess separately:

| Construct | Plain-language claim it supports | Assessable form |
|-----------|----------------------------------|-----------------|
| **Problem representation** | Can the student summarize *this* case in one line that captures the discriminating features? | A one-sentence summary using semantic qualifiers (acute/chronic, focal/diffuse), scored for what it includes and excludes. |
| **Illness scripts** | Has the student organized disease knowledge into templates that link presentations to conditions? | Compare/contrast two conditions on the features that distinguish them; predict the next discriminating finding. |
| **Differential diagnosis** | Can the student generate and prioritize a plausible differential? | A ranked differential with the reasoning for the ranking — not just a list. |
| **Diagnostic uncertainty** | Can the student act sensibly when the diagnosis is not yet clear? | "What would you do next, and why, given you don't yet know?" — the management-of-uncertainty move. |
| **Can't-miss diagnoses** | Does the student rule out the dangerous possibilities even when unlikely? | "What can't you afford to miss here, and how do you exclude it?" |

> The most diagnostic clinical-reasoning probe is the keystone's transfer question — *"What would change
> your mind?"* (or *"what information would change your diagnosis?"*). It separates genuine in-context
> judgment from a fluent, confident end-state — exactly the thing AI supplies cheaply. It maps to
> **Extrapolation** repairs (see §3, Link 4, and [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.4).

### 2.3 Communication with patients and teams

History-taking, shared decision-making, counseling, handoffs, documentation-as-communication. The
assessable claim is almost always about **adapting to a specific cue** (the keystone's
*"communication"* → *"Can the student adapt their explanation to a specific patient cue?"*), not
producing generically polished prose — which is precisely what AI produces. Best seen in **observed**
performance (OSCE, simulation, workplace), not a written artifact.

### 2.4 Professionalism

Behavior over time, in context: reliability, integrity, response to feedback, conduct. **Hard to assess
in a single artifact and easy to fake in writing** — a professionalism *essay* is weak evidence on
sight. Professionalism evidence is longitudinal and observational; treat one-shot written reflection on
professionalism as a likely **Construct** break (the construct isn't represented) unless it is tied to a
specific **referent** — an observed behavior, a critical incident, a piece of feedback, **or, in a
longitudinal portfolio, a prior reflection the student now revisits**. The carve-out Severs only when
there is **no** referent of any kind — *not* merely because the referent isn't a directly observed
behavior: professional **identity formation** is a developmental, self-referential construct that can
validly anchor to a longitudinal sequence, and heavy external surveillance can itself distort it
(performing-for-the-rater — reactivity). Don't reflexively convert a PIF portfolio into a behavior
checklist.

### 2.5 Patient safety

Error recognition, systems thinking, speaking up, safe handoffs. Assessed through observed performance,
simulation, root-cause exercises, and WBA. The coach should be cautious about safety claims resting on
written artifacts alone.

### 2.6 Observed performance — OSCEs and simulation

Structured, observed demonstration in a standardized or simulated setting (*Shows How* on Miller). The
**OSCE** (objective structured clinical examination — a circuit of short standardized stations) and
simulation are the workhorses of *Shows How*. Because the evidence is **observed and rater-scored**,
the **Scoring** link (attribution) is usually intact during the encounter — the student is doing the
thing in front of a trained rater, with no AI in the room. This is why well-run multi-station OSCEs
often rate **Strong** (keystone Example 3). Their exposure is elsewhere: rater consistency (a Scoring
*evaluation-accuracy* issue, not attribution), and **over-attaching consequences to a single sitting**
(an **Implications** issue — see §2.10 and keystone Example 6).

### 2.7 Workplace-based assessment & EPAs (overview — detail in the sibling)

The *Does* level (Miller): observed performance in the **real** clinical setting, judged for how much
supervision the student still needs. UME organizes much of this around the **13 AAMC Core Entrustable
Professional Activities for Entering Residency** — units of professional work (e.g., "gather a history
and perform a physical exam," "give an oral presentation of a clinical encounter") that a graduating
student should be trusted to perform. **Entrustment** progresses *direct supervision → indirect
supervision → independent supervision*; **WBA** is the observed, **formative**, low-stakes data stream
that feeds those entrustment judgments.

> **This is an overview only.** The 13 Core EPAs, entrustment scales, and how WBA evidence is captured
> and aggregated live in [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md). Use
> EPAs/WBA whenever the claim is about **doing in the workplace**; reach for that sibling for the detail.

### 2.8 Programmatic assessment

The design philosophy behind defensible high-stakes UME decisions (van der Vleuten & Schuwirth):
**aggregate many low-stakes data points; no single instrument carries a consequential decision.** Each
data point is low-stakes and feedback-rich; a qualified committee makes the consequential call from the
**pattern**. This is the canonical answer when a UME assessment is being asked to carry more than one
instrument should (see §3, Link 5, and [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.4).

### 2.9 The pre-clerkship → clerkship transition

The construct **shifts** as students move from the classroom to the wards, and the coach should track
the shift:

| | Pre-clerkship | Clerkship |
|---|---------------|-----------|
| **Dominant construct** | Foundational knowledge; early clinical reasoning | Applied reasoning, communication, professionalism **in context** |
| **Miller level** | Knows / Knows How | Shows How / Does |
| **Typical evidence** | Written exams, CBL/PBL, early OSCEs, lab/anatomy | OSCEs, WBA, EPAs, clinical evaluations, notes |
| **Most exposed link under AI** | **Scoring** (unsupervised take-home written work) and **Construct** (vague "reasoning" goals) | **Extrapolation** (artifact vs. observed performance) and **Implications** (progression decisions) |

A common mistake the coach should catch: applying a clerkship-grade authentic-performance expectation to
a pre-clerkship knowledge check (over-climbing Miller, §4.2), or accepting a pre-clerkship written
artifact as evidence of clerkship-level *doing* (an Extrapolation break, §3 Link 4).

### 2.10 STEP / licensing / foundational-knowledge considerations

USMLE **Step 1 became pass/fail in January 2022**; **Step 2 CK remains scored**. The design implication
is stable regardless of the current policy details: **secure, closed-book, knowledge-anchored exams
remain valid for foundational-knowledge constructs.** The coach should therefore:

- **Not force AI** into a closed-book, secure, knowledge-anchored exam whose construct *is* independent
  recall/synthesis. "No AI" is a legitimate, often-correct design — not a fallback failure (keystone
  Edge cases; [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) Gate 5;
  [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.1, AIAS "No AI").
- Treat **licensing-exam policy** as out of the tool's authority — design advice yes, a policy/eligibility
  ruling no (Gate 4). USMLE specifics that may change are `[PLACEHOLDER]`s for `implementations/`.
- Remember that **no single exam (Step included) carries a progression decision on its own** — that is
  the programmatic-assessment point and an **Implications**-link consideration (§2.8, §3 Link 5).

---

## 3. How the five-link chain applies in UME

The chain, its order, the **Severed / Weakened / Intact** severity scale, the halting rule, and the
readiness derivation are **canonical** — see [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md)
(Phases B–D). This section does not restate them; it shows **what each link looks like in UME and the
break the coach should expect first.** Walk in order, halt at the earliest **Severed** link (else the
earliest **Weakened** one), read **at the case's actual stakes**.

### Link 1 — Construct: *is the clinical claim well-defined, and does the task elicit it?*

- **In UME:** "clinical reasoning," "professionalism," and "communication" are routinely stated as
  abstractions. The task may certify *writing fluency* or *USMLE-style recall* while the claim says
  *reasoning* — or "working with AI" has quietly become the real construct while the claim still says
  *domain knowledge*.
- **Most common UME break:** **"clinical reasoning" left vague** and never operationalized — so no link
  downstream can be evaluated. Also: a professionalism/reflection task with **no observed referent**
  (Construct *Severed* on sight, keystone carve-out). And the equity case — when a result reflects
  **which AI tool a student could access** rather than the clinical construct, that is
  construct-irrelevant variance and a **Construct** weakness ([`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md)).
- **First move:** sharpen to an assessable claim (the §2.2 table), or require a referent — **before**
  diagnosing further. A Scoring fix (proctoring) cannot rescue a task that measures the wrong thing.

### Link 2 — Scoring: *can we attribute this to this student, under intended conditions, scored right?*

- **In UME:** observed encounters (OSCE, WBA) are attributable on their face. **Unsupervised written
  work is not** — take-home case write-ups, take-home short-answer, reflective essays, discussion posts.
  Group products (a team presentation) hide individual contribution. Rater inconsistency on an OSCE/WBA
  rubric is the *evaluation-accuracy* face of this link (not attribution).
- **Most common UME break:** **take-home case write-ups and take-home knowledge checks** — a student
  who didn't do the reasoning could earn the same result with AI; the work isn't attributable.
- **First move:** add an attributable component proportionate to the stakes — a short oral probe / viva
  on the submission, an in-class checkpoint, a reasoning trace, or an individual-accountability element
  in group work ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.2). For group work,
  **suspect Scoring before Generalization** (keystone Edge cases).

### Link 3 — Generalization: *does this one case support a claim across the domain of such cases?*

- **In UME:** one case is not the domain. A single OSCE station, one written case, or one
  prompt-optimizable pattern over-claims breadth. Clinical competence is notoriously
  **case/content-specific** — performance on one presentation predicts the next only weakly — so
  sampling across cases and contexts is the substance of this link, not a formality.
- **Most common UME break:** **one case (or one station) read as broad clinical competence**, or a
  predictable pattern students can rehearse/prompt-optimize.
- **First move:** add cases/stations, sample across contexts/occasions, blueprint against objectives,
  or triangulate ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.3).
- **Disambiguation (do not skip):** if the single instrument is *itself sound* and only the **decision
  attached** is too big, the break is **Implications, not Generalization** — test the cause, not the
  symptom (keystone disambiguation + Example 6).

### Link 4 — Extrapolation: *does performance here transfer to the clinical / future target?*

- **In UME:** this is the link AI most often exposes. A **polished written artifact is not observed
  clinical performance.** "Can write a beautiful case write-up" ≠ "can take a history, reason at the
  bedside, and manage uncertainty in the moment." A reflection that "sounds insightful" but is tied to
  no observed behavior does not transfer. The task may measure **explanation-after-the-fact** rather than
  **judgment-in-the-moment**.
- **Most common UME break:** **a written artifact standing in for observed clinical performance** — the
  classic written-product-vs-doing gap.
- **First move:** move evidence toward *Shows How* / *Does* where the claim warrants it — an observed
  demonstration, an oral reasoning probe, a clinical-reasoning defense, scenario variation, the *"what
  would change your mind?"* question, or reflection tied to an observed behavior
  ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.4). **Match the Miller level to
  the claim — don't over-climb** (§4.2).

### Link 5 — Implications / Decision: *do the stakes and decisions match the evidence?*

- **In UME:** progression, promotion, remediation, competency, and licensing/eligibility decisions are
  **consequential** by definition (a normal summative course grade is **not** automatically consequential
  — keystone Phase A/D; [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) Gate 3 scope
  note). The break is a **consequential decision resting on one instrument, one occasion, or AI output
  without qualified human review** — including treating an AI-involved evaluation as sufficient on its own.
- **Most common UME break:** **a progression / competency decision carried by a single instrument** (even
  a sound one — the single OSCE used as the *sole* gate, keystone Example 6) **or lacking triangulation /
  qualified review.**
- **First move:** triangulate across programmatic-assessment data points before the gate; require
  qualified faculty/committee review; lower the stakes if the evidence fits a lighter use; never rest a
  consequential decision on AI output ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.5).
- **Override (canonical):** because UME consequential decisions clear the bar for the
  **Needs-deeper-review override**, the **response shape changes** — the headline becomes *"this needs
  qualified faculty/governance review,"* with the broken link reported as a **chain note for the human**,
  not a verdict (keystone Phase D; [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md)).

> **Two equity entry points, kept distinct** (Phase 7 reconciliation item from the tracker, made
> explicit here): unequal **AI access → construct-irrelevant variance** is a **Construct (Link 1)**
> flag, owned by [`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md);
> **differential/adverse impact of a decision rule** is an **Implications (Link 5)** concern. Don't
> conflate them.

---

## 4. UME-specific coaching behavior

How the coach should *behave* on UME cases, beyond walking the chain. Each item ties to a canonical rule.

### 4.1 Use Miller's pyramid as one lens, not the only one

*Knows → Knows How → Shows How → Does* is a useful map for **what evidence shows** and where to move it
(it underwrites Extrapolation repairs — [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md)
§3.3). But it is **one** lens. Clinical reasoning (problem representation, illness scripts, uncertainty)
is better analyzed with the §2.2 constructs than by pyramid level alone; entrustment/WBA adds a
**supervision** axis Miller doesn't capture. **Do not reduce every UME diagnosis to "move it up the
pyramid."**

### 4.2 Recognize when secure, knowledge-based assessment is already right — don't force AI in

When the construct *is* independent recall/synthesis/judgment (foundational knowledge; USMLE-style
items), a **secure, closed-book exam is valid and "No AI" is the correct design.** Forcing AI integration
here is a **restraint failure** (Gate 5;
[`../../core/safety-guardrails.md`](../../core/safety-guardrails.md)) and over-climbing Miller when
*Knows / Knows How* is genuinely the target wastes cost and may be infeasible
([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.3 "do not over-climb"). If such an
exam already holds under likely AI use, **say so and stop** — emit the *Strong / restraint* variant.

### 4.3 Distinguish written artifacts from observed clinical performance — and preserve reasoning evidence

This is the UME instinct the coach must keep sharp. A write-up, note, or reflection is a **product**;
bedside history-taking, an OSCE encounter, a WBA observation are **performances**. When the claim is
about *doing* or *reasoning in context*, a product is the wrong evidence type (Extrapolation, §3 Link 4).
Where reasoning is the construct, **preserve the reasoning evidence**: a student-generated reasoning
trace, an oral probe, or a *"what would change your mind?"* question keeps the *thinking* visible that a
polished AI-assisted artifact hides ([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md)
§2.2, §2.4).

### 4.4 Recommend observed / oral probes when appropriate — proportionately

Oral and observed formats are the strongest fix for both attribution (Scoring) and transfer
(Extrapolation), but they carry **faculty-time, scheduling, and accessibility** costs and **don't scale
linearly**. Recommend them when stakes warrant and **sample or time-box** to keep them feasible; flag the
communication-style/language accessibility consideration and offer equivalents
([`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §2.2, §2.4;
[`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md)). Respect the
multiplicative-utility rule: if even the lightest restoring probe tanks acceptability/cost, prefer
lowering the stakes or moving AI-rich work into practice over an infeasible heavy repair (keystone Phase E).

### 4.5 Use EPAs / WBA for "does" contexts

When the claim is about **performing professional work in the real clinical setting**, route to
**EPAs and workplace-based assessment** rather than manufacturing a written proxy — observed, formative,
entrustment-feeding evidence. Overview in §2.7; full detail in
[`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md).

### 4.6 Recommend programmatic assessment for high-stakes claims

For **competency / progression** claims, the defensible design is **programmatic**: aggregate many
low-stakes data points and let a qualified body decide from the pattern — **no single instrument carries
the decision** (§2.8;
[`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) §3.4). This is a **programme-level**
investment (data capture, committees, longitudinal tracking), not an edit to one assignment — name the
cost honestly.

### 4.7 Flag cases needing qualified faculty / governance review

Consequential UME decisions (progression, promotion, remediation, competency, licensing, disciplinary),
clinically sensitive material, and governance-heavy questions get the **Needs-deeper-review** treatment:
the coach gives the safe **design** help it can and routes the **decision** to qualified
faculty/governance — it never stands in for the human. Canonical behavior and the UME-specific,
AAMC-aligned governance detail (qualified-faculty review for **AI-involved evaluation**, the 7
principles, high-stakes constraints) live in
[`ume-governance-guardrails.md`](ume-governance-guardrails.md) and
[`../../core/safety-guardrails.md`](../../core/safety-guardrails.md). **Do not duplicate the governance
rules here — point to them.**

### 4.8 Never process PHI or identifiable patient/student data

The coach **never** ingests, echoes, or analyzes PHI, identifiable patient data, or private student
records/grades. It asks for a **fictionalized or de-identified** case and continues on the safe version —
a fictional clinical case is fully sufficient to reason about an assessment's *design*. This is a binary
Phase 0 gate ([`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) Gate 1); the
UME-specific clinical-data cautions are in
[`ume-governance-guardrails.md`](ume-governance-guardrails.md).

### 4.9 Never act as a cheating detector

UME contexts raise integrity stakes, but the boundary is absolute: the coach **never claims to detect AI
use, never determines that a student cheated, and never supports a consequential decision on AI output
alone.** It redirects to stronger assessment design, the institution's integrity process, and qualified
human review (Phase 0 Gate 2;
[`../../core/safety-guardrails.md`](../../core/safety-guardrails.md);
[`../../core/skill-core.md`](../../core/skill-core.md) §1, §5).

---

## 5. Cross-references

**Sibling files in this pack (elaborate; don't duplicate):**

- [`ume-assessment-patterns.md`](ume-assessment-patterns.md) — UME assessment formats and where each
  breaks under likely AI use.
- [`ume-governance-guardrails.md`](ume-governance-guardrails.md) — AAMC-aligned governance: the 7
  principles, PHI/patient-data, qualified-faculty review for AI-involved evaluation, high-stakes UME
  decision constraints.
- [`epas-and-workplace-assessment.md`](epas-and-workplace-assessment.md) — the 13 AAMC Core EPAs,
  entrustment progression, and workplace-based assessment.
- [`ume-test-cases.md`](ume-test-cases.md) — worked UME examples with expected primary diagnoses.

**Core files (canonical source of truth):**

- [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md) — **the keystone.** The
  5-link ordered walk, Phase 0 safety screen, severity scale, halting rule, readiness derivation,
  restraint, worked examples (3 and 6 are UME). This pack references it; it never re-authors it.
- [`../../core/repair-taxonomy.md`](../../core/repair-taxonomy.md) — the full repair menu by link, and
  the four decision frameworks (AIAS, Sydney two-lane, Miller, programmatic assessment).
- [`../../core/safety-guardrails.md`](../../core/safety-guardrails.md) — the binary Phase 0 gates and the
  Needs-deeper-review override (PHI, detection/misconduct, consequential-AI decisions, policy overclaim,
  restraint). Cross-references the UME governance sibling for domain detail.
- [`../../core/response-pattern.md`](../../core/response-pattern.md) — the output template and variants
  (default, missing-intake, Strong/restraint, Needs-deeper-review, refuse-and-redirect).
- [`../../core/equity-and-access-flags.md`](../../core/equity-and-access-flags.md) — equity/access as a
  Construct/CIV watch-out (unequal AI access, model-tier disparity, accommodations).
- [`../../core/skill-core.md`](../../core/skill-core.md) — the integrating spine; names UME as the
  primary UME audience.

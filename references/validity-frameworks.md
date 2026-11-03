# Validity frameworks — provenance and how the engine adapts them

The engine's walk is an **argument-based validity** procedure. It is honest about being a **hybrid**:
Kane's inference chain with a Messickian construct premise made explicit as Step 1. This file records
whose ideas each piece comes from, so the expert-facing layer attributes them correctly (and so a
validity scholar reading the tool finds it credible rather than conflated).

## The five links and their provenance

| Engine link | Belongs to | Note |
|---|---|---|
| **1 · Construct** | **Messick** (premise; not a Kane inference) | *Construct underrepresentation* and *construct-irrelevant variance* are Messick's two threats to validity. Kane's interpretation/use argument (IUA) does **not** contain a "Construct" inference — it begins after scoring and treats a defined construct/target as a presupposition. The engine surfaces that presupposition as an explicit first link. Calling Link 1 a "Kane inference" would be wrong. |
| **2 · Scoring** | **Kane** | First IUA inference: from the observed performance to an observed score under appropriate conditions, scored consistently. |
| **3 · Generalization** | **Kane** | From the observed score to a universe/expected score across the relevant facets (items, cases, occasions, raters). |
| **4 · Extrapolation** | **Kane** | From the test universe to the real-world target domain. |
| **5 · Implications / Decision** | **Kane** | From the interpretation to the decisions and consequences (Kane's "implications" / use). |

The **Severed / Weakened / Intact** banding and the **earliest-broken-link halting rule** are the
**tool's own operationalization** for AI-era triage — not Kane's vocabulary. Kane evaluates the argument
*as a whole*; the engine adds a triage convenience (name the earliest break as the headline) on top.
"Earliest" ≠ "most material" — a binding downstream break can dominate (see keystone Phase C, Example 6).

## Sources (working bibliography)

### Closest prior work (read these first)

- **Dawson, P., Bearman, M., Dollinger, M., & Boud, D.** "Validity matters more than cheating,"
  **Assessment & Evaluation in Higher Education, 2024**. <https://doi.org/10.1080/02602938.2024.2386662>
  — **The reframe this project rests on, published first and by this field's most-cited authors:** an
  assessment matters because it licenses an inference about competence, and generative AI threatens that
  inference whether or not any cheating occurred. Learning Signal Check does **not** claim this argument.
  Its contribution is the *executable* form — an ordered, halting diagnostic that yields one primary
  broken link and one proportionate repair — plus the restraint mechanism. Cite Dawson et al. for the
  premise; cite this project only for the operationalization.
- **Cook, D. A., Brydges, R., Ginsburg, S., & Hatala, R.** "A contemporary approach to validity
  arguments: a practical guide to Kane's framework," **Medical Education, 2015**.
  <https://pubmed.ncbi.nlm.nih.gov/25989405/> — Kane's framework already operationalized as a
  step-by-step validity-argument walk for exactly this audience. The step structure here is downstream of
  this paper; what differs is the halting rule, the severity banding, and the conversational form.

### Guidance and regulatory sources

- **TEQSA** (Australia). *Assessment reform for the age of artificial intelligence* (2023) and the Gen AI
  knowledge hub. <https://www.teqsa.gov.au/guides-resources/resources/corporate-publications/assessment-reform-age-artificial-intelligence>
  — the "assessment reform, not detection" posture the engine shares.
- **QAA** (UK). Advice and resources on generative AI, and the QAA AI toolkit.
  <https://www.qaa.ac.uk/sector-resources/generative-artificial-intelligence/qaa-advice-and-resources>
- **AAMC.** *Principles for the Responsible Use of Artificial Intelligence in and for Medical Education*
  (2025). <https://www.aamc.org/about-us/mission-areas/medical-education/principles-ai-use> — the source
  paraphrased in `domains/undergraduate-medical-education/ume-governance-guardrails.md`. **Verify any
  paraphrase against the current AAMC text before relying on it**; the wording there is not quoted.

### Measurement foundations

- **Kane, M. T.** Argument-based validity / the interpretation-use argument. Kane, *Validation*, in
  R. L. Brennan (Ed.), **Educational Measurement (4th ed., 2006)**; and Kane, "Validating the
  Interpretations and Uses of Test Scores," **Journal of Educational Measurement, 2013**. The IUA
  inferences used here: scoring → generalization → extrapolation → implication.
- **Messick, S.** *Validity*, in R. L. Linn (Ed.), **Educational Measurement (3rd ed., 1989)**; and
  "Validity of Psychological Assessment," **American Psychologist, 1995**. Source of *construct
  underrepresentation* and *construct-irrelevant variance*, and of the unified, consequential view of
  validity the engine's Construct and Implications links draw on.
- **Miller, G. E.** "The assessment of clinical skills/competence/performance," **Academic Medicine,
  1990**. The *Knows → Knows How → Shows How → Does* pyramid used for Extrapolation/evidence-level moves.
- **van der Vleuten, C. P. M.** "The assessment of professional competence: developments, research and
  practical implications," **Advances in Health Sciences Education, 1996**; with **Schuwirth**,
  "Assessing professional competence: from methods to programmes," **Medical Education, 2005**. Utility
  as a function of multiple factors (validity, reliability, educational impact, acceptability, cost) with
  **context-dependent weights** — proposed as a conceptual heuristic, **not** a validated arithmetic
  equation. The engine treats "cost" as an inverse term (higher cost → lower utility).
- **Programmatic assessment.** van der Vleuten, Schuwirth, Driessen, et al., "A model for programmatic
  assessment fit for purpose," **Medical Teacher, 2012**. No single instrument carries a high-stakes
  decision; aggregate many low-stakes data points; a committee decides from the pattern. Behind the
  Implications "triangulate / aggregate" repairs and the portfolio (Phase A0b) logic.
- **Generalizability theory / case specificity.** Cronbach, Gleser, Nanda & Rajaratnam, *The
  Dependability of Behavioral Measurements* (**1972**); on clinical-reasoning case specificity, Eva,
  "What every teacher needs to know about clinical reasoning," **Medical Education, 2005**, and the
  long OSCE literature (Norman, Swanson) showing performance is highly case/occasion specific. Behind the
  Generalization link's "occasion / case-mix facet" symptom.
- **AI Assessment Scale (AIAS).** Perkins, Furze, Roe & MacVaugh, "The AI Assessment Scale (AIAS): A
  framework for ethical integration of generative AI in educational assessment" (**2023; revised 2024**).
  Five levels of permitted AI use. As published it is ordered by *amount of AI permitted* — a design
  parameter. The engine's claim that the levels are "non-hierarchical" refers to **merit/validity**
  (merit is construct-relative), not to that ordering.
- **University of Sydney "two-lane" approach.** Liu, Bridgeman, and colleagues (Sydney), assessment
  reform for the age of generative AI: a **secure/assured** lane (attributable evidence of unaided
  capability) alongside an **open** lane (authentic, AI-rich work, acknowledged). Behind the engine's
  Lane-1 attribution repairs.

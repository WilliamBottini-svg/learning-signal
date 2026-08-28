# Learning Signal Check

> **Does this assignment still show you what a student can actually do — if they used AI to make it?**

Learning Signal Check is a portable AI skill that helps educators check whether an assessment still
reveals the learning they care about in the age of AI, then suggests a practical redesign **only when**
the learning signal is weakened.

It is an assessment-**design** coach. It is **not** an AI-proofing tool, and it is **not** a
cheating detector.

---

## Try it in 60 seconds

No install, no account, no plugin. Open **any** chat assistant — ChatGPT (free tier is fine), Claude,
Gemini, Copilot — and paste in the block from
[`platforms/stanford-ai-playground/prompt-template.md`](platforms/stanford-ai-playground/prompt-template.md),
then describe one assessment you're worried about. That's it.

It is self-contained: the safety screen, the five-link walk, the halting rule and the output shape all
travel in the paste. You do not need the repo, the knowledge files, or a paid tier to get a real answer.

The fuller setups below buy you two things the paste-block can't: **persistence** (a saved assistant you
don't rebuild each time) and **depth** (the full repair taxonomy and the medical-education pack as
retrievable knowledge). Start with the paste. Set up a wrapper once it has earned the twenty minutes.

---

## Where the evidence actually stands

Read this before citing anything below.

- **Validation to date is predominantly model-based.** The golden targets were derived by one author
  applying the same procedure being tested, so pass rates measure **instruction-following, not
  pedagogical correctness**.
- **G06 is the one externally ratified case** (three raters, unanimous on the primary, 2026-07-06).
  Session records are held offline and available on request; see the provenance block in
  [`tests/results/expert-ratified-targets-2026-07-06.md`](tests/results/expert-ratified-targets-2026-07-06.md).
  The remaining 30 golden targets are author-derived.
- **Layer 3 educator think-aloud: 5 educators, "UX ship with caveats."** Same provenance caveat — the
  protocol and the results were committed together, so the git history alone does not evidence the
  sessions.
- **No lift over a strong base prompt has been demonstrated.** On the headline golden metric the skill
  scored **25/27 against base's 26/27**, and both scored 6/6 cross-family. The measured advantage is in
  **safety-gate discipline** (14/14 vs 11/14 adversarial), not in diagnosis.
- **Four independent blind agent runs reached identical diagnoses** — same primary link, same state,
  same readiness — on all four probe cases. All four also flagged the same four underspecifications in
  the procedure, which have since been closed.
- **One regression slice reproduces end-to-end from committed files**, on any OpenAI-compatible endpoint
  (no institutional gateway required). Structural conformance on that slice is **80.0%** against the
  project's own ≥90% bar — see [`tests/results/redteam-regression-2026-07-06.md`](tests/results/redteam-regression-2026-07-06.md).
- A hard guarantee of 0% PHI echo requires a **platform PII boundary**, not instruction alone.

---

## What it does

Generative AI makes polished artifacts cheap. A student can produce an essay, a case write-up, a
reflection, or a code submission with little direct evidence that they did the intended thinking. The
old question — *"Did the student produce the artifact?"* — no longer tells you much.

Learning Signal Check asks the better question:

> **What evidence would convince us that learning happened — and does this assessment still collect it?**

It then walks the **assessment evidence chain in order** and stops at the *first* place the chain
breaks. That earliest broken link is the **primary diagnosis**, and the recommended redesign repairs
*that* link first — rather than handing you a generic menu of "AI-resilient assessment" tips.

## How it works — the evidence chain

The coach operationalizes an **argument-based validity walk** — Kane's four inferences (Scoring →
Generalization → Extrapolation → Implications) with an explicit construct-definition premise (Messick's
construct underrepresentation / construct-irrelevant variance) surfaced as Step 1 (Construct). It walks
five linked inferences and halts at the earliest broken link:

| # | Link | Plain-language question |
|---|------|--------------------------|
| 1 | **Construct** | Is the learning claim well-defined — and does the task actually represent it? |
| 2 | **Scoring** | Can we attribute the performance to *this student*, under the intended conditions? |
| 3 | **Generalization** | Does this one task/sample support a broader claim about the student? |
| 4 | **Extrapolation** | Does it transfer to the real-world / clinical / future-learning target? |
| 5 | **Implications** | Do the stakes and decisions match the quality and quantity of evidence? |

Each downstream inference presupposes the upstream one. So if **scoring** is broken, polishing
**extrapolation** is premature. Diagnose first, then repair the binding constraint.

**Restraint is a feature.** Sometimes the right answer is *"this is already strong — no major redesign
needed."* The coach is designed (and tested) to say so.

## Layered architecture

| Layer | Path | What it is |
|-------|------|------------|
| Core skill | `core/` | The diagnostic procedure, response pattern, repair taxonomy, safety guardrails, equity flags. **Canonical source of truth.** |
| Domain pack | `domains/undergraduate-medical-education/` | Undergraduate medical education (UME) concepts and governance. Useful beyond any one school. |
| Implementation | `implementations/stanford-medicine-ume/` | A local deployment example (Stanford Medicine UME). |
| Platforms | `platforms/` | Exports/wrappers: Claude Skill, Stanford AI Playground, ChatGPT, Gemini, Codex. **Exports, never forks.** |
| Tests | `tests/` | Golden, adversarial, and no-change cases; scoring rubric; templates. |
| Examples | `examples/` | Fictionalized worked cases. |

## What it will not do

- It will **not** tell you whether a student used AI, or whether they cheated.
- It will **not** support a progression, remediation, competency, or disciplinary decision based on AI
  output alone — those require triangulated evidence and qualified human review.
- It will **not** process PHI, identifiable patient data, or private student records — it will ask you
  to de-identify first.
- It will **not** issue definitive legal, accreditation, or institutional-policy rulings.

## Getting started

Learning Signal Check ships as portable wrappers that all run the same core diagnostic:

- **Claude Skill / Claude Code plugin** — [`platforms/claude-skill/`](platforms/claude-skill/). The `SKILL.md` auto-triggers
  when you ask whether an assessment still shows student learning under AI, or to redesign one. Its
  `references/` include five byte-identical exports of `core/` plus one curated UME digest exported from
  `domains/undergraduate-medical-education/`.

  **Install as a Claude Code plugin:**

  ```
  /plugin marketplace add WilliamBottini-svg/learning-signal
  /plugin install learning-signal-check@learning-signal
  ```

  Manual fallback: point Claude at [`platforms/claude-skill/SKILL.md`](platforms/claude-skill/SKILL.md).
- **AI Playground (Stanford or any)** — generic export in
  [`platforms/stanford-ai-playground/`](platforms/stanford-ai-playground/). This folder gives the generic
  setup pattern: a preset template/checklist, a reusable intake prompt, and instructions for pasting the
  full custom instructions. A local deployment example lives in
  [`implementations/stanford-medicine-ume/`](implementations/stanford-medicine-ume/) (fill the
  `[PLACEHOLDER]`s for your institution). Importing a preset JSON alone is not enough unless your AI
  Playground instance also imports the full custom/system instructions.
- **ChatGPT Custom GPT** — [`platforms/chatgpt-custom-gpt/`](platforms/chatgpt-custom-gpt/) (instructions
  field + knowledge manifest + starters). **Gemini Gem** —
  [`platforms/gemini-gem/`](platforms/gemini-gem/) (Persona/Task/Context/Format instructions + setup).
  Both upload the **same 6 `claude-skill/references/` files** as their knowledge: the five exact core
  exports and the UME digest. One knowledge set, every platform.
- **Codex / Perplexity testing playbook** — [`platforms/codex/`](platforms/codex/): how to run the test
  suite (skill-vs-base), score against the rubric, and keep the wrapper exports consistent — runnable
  with only the repo.

### Validation (v0.5.0)

Cross-family frontier results (June 2026) live in
[`tests/results/cross-family-eval-2026-06-11.md`](tests/results/cross-family-eval-2026-06-11.md). The
**v0.3 validation program** — weak-tier coverage, output-UX validation, and manual Cursor runs — is
specified in [`tests/v0.3-validation-plan.md`](tests/v0.3-validation-plan.md) and **executed** (see
[`tests/results/weak-tier-verdict-2026-06-25.md`](tests/results/weak-tier-verdict-2026-06-25.md),
[`tests/results/ux-persona-v0.3-2026-06-26.md`](tests/results/ux-persona-v0.3-2026-06-26.md)). Pre-stripped blind prompts for manual
runs: [`tests/cursor-manual-run-prompts.md`](tests/cursor-manual-run-prompts.md). **Automated Mode 1 runs**
via Stanford AI Gateway: [`tests/harness/README.md`](tests/harness/README.md) (`scripts/run_mode1_eval.py`).

**Honesty caveat:** see [Where the evidence actually stands](#where-the-evidence-actually-stands) at the
top of this file — it is the authoritative statement and it is deliberately less flattering than a
release banner. Faculty kit:
[`tests/M7-faculty-ratification-kit.md`](tests/M7-faculty-ratification-kit.md).

### Minimum model tiers (summary)

| Platform | Recommended | Validated floor | Verdict |
|----------|-------------|-----------------|---------|
| ChatGPT Custom GPT | Frontier GPT (`gpt-5.4` class) | `gpt-5-mini` | SHIP WITH CAVEATS |
| Gemini Gem | Gemini Pro class | `gemini-2.5-flash-lite` | SHIP WITH CAVEATS |
| Claude Skill | Frontier Claude | Haiku not tested | SHIP WITH CAVEATS |
| AI Playground | Instance frontier model | See wrapper docs | Instance-dependent |

Details in each platform's setup guide. Evidence: [`tests/results/weak-tier-verdict-2026-06-25.md`](tests/results/weak-tier-verdict-2026-06-25.md).

To see the method in action, read the worked demonstrations in [`examples/`](examples/); to read the
engine itself, see [`core/diagnostic-procedure.md`](core/diagnostic-procedure.md).

## Intellectual anchors

Argument-based validity (Kane 2006, 2013); unified construct validity and construct-irrelevant
variance / underrepresentation (Messick 1989, 1995); Miller's pyramid (1990); the utility index and
programmatic assessment (van der Vleuten 1996; van der Vleuten & Schuwirth 2005); the AI Assessment
Scale (Perkins, Furze, Roe & MacVaugh); the University of Sydney two-lane model; TEQSA and QAA
assessment-reform guidance; and the AAMC principles for the responsible use of AI in and for medical
education. Full citations live in [`references/`](references/).

**Closest prior work, stated plainly.** Dawson, Bearman, Dollinger & Boud, *"Validity matters more than
cheating"* (*Assessment & Evaluation in Higher Education*, 2024) already argued the reframe this project
rests on: an assessment matters because it licenses an inference, and AI threatens that inference whether
or not cheating occurred. Cook, Brydges, Ginsburg & Hatala (*Medical Education*, 2015) already
operationalized Kane's framework as a step-by-step validity-argument walk for this audience. **This
project does not claim the reframe.** What is its own is the *executable* form: an ordered, halting
diagnostic that names one primary broken link and one proportionate repair, and a disciplined restraint
mechanism that returns "no major redesign needed" when the chain holds.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). The cardinal rule: `core/` + `domains/` are the canonical
source; platform wrappers are **exports, never forks**. Keep the diagnosis faithful, examples
de-identified, and the safety gates binary.

## License

- Code, JSON, scripts: **MIT** — see [`LICENSE`](LICENSE).
- Documentation, prose, rubrics, examples: **CC BY 4.0** — see [`CONTENT-LICENSE.md`](CONTENT-LICENSE.md).

## Citation

See [`CITATION.cff`](CITATION.cff).

---

*Learning Signal Check is an educational design aid. It supports human judgment about assessment; it
does not replace it.*

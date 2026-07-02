# Learning Signal Check

> **Does this assignment still show you what a student can actually do — if they used AI to make it?**

Learning Signal Check is a portable AI skill that helps educators check whether an assessment still
reveals the learning they care about in the age of AI, then suggests a practical redesign **only when**
the learning signal is weakened.

It is an assessment-**design** coach. It is **not** an AI-proofing tool, and it is **not** a
cheating detector.

> **v0.4.0** — first public release. Validation is **model-based**; human expert (M7) ratification is pending.

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
five linked inferences and halts at the earliest weakened one:

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

### Validation (v0.4.0)

Cross-family frontier results (June 2026) live in
[`tests/results/cross-family-eval-2026-06-11.md`](tests/results/cross-family-eval-2026-06-11.md). The
**v0.3 validation program** — weak-tier coverage, output-UX validation, and manual Cursor runs — is
specified in [`tests/v0.3-validation-plan.md`](tests/v0.3-validation-plan.md) and **executed** (see
[`tests/results/weak-tier-verdict-2026-06-25.md`](tests/results/weak-tier-verdict-2026-06-25.md),
[`tests/results/ux-persona-v0.3-2026-06-26.md`](tests/results/ux-persona-v0.3-2026-06-26.md)). Pre-stripped blind prompts for manual
runs: [`tests/cursor-manual-run-prompts.md`](tests/cursor-manual-run-prompts.md). **Automated Mode 1 runs**
via Stanford AI Gateway: [`tests/harness/README.md`](tests/harness/README.md) (`scripts/run_mode1_eval.py`).

**Honesty caveat:** all published eval results are **model-based**, not human-expert (M7) ratified. Golden
targets remain author-derived until faculty ratification. The skill refuses unsafe requests and routes
PHI — but a hard guarantee of 0% PHI echo requires a platform PII boundary, not instruction alone.

To see the method in action, read the worked demonstrations in [`examples/`](examples/); to read the
engine itself, see [`core/diagnostic-procedure.md`](core/diagnostic-procedure.md).

## Intellectual anchors

Argument-based validity (Kane 2006, 2013); unified construct validity and construct-irrelevant
variance / underrepresentation (Messick 1989, 1995); Miller's pyramid (1990); the utility index and
programmatic assessment (van der Vleuten 1996; van der Vleuten & Schuwirth 2005); the AI Assessment
Scale (Perkins, Furze, Roe & MacVaugh); the University of Sydney two-lane model; TEQSA and QAA
assessment-reform guidance; and the AAMC principles for the responsible use of AI in and for medical
education. Full citations live in [`references/`](references/).

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

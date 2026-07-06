# platforms/codex/ — Automation / Evaluation / Maintenance Playbook

> **What this folder is.** The operating playbook for an **automation and evaluation agent** —
> **Codex, a CI coding agent, or Perplexity Computer** — that works **on** the Learning Signal Check
> repository: it (a) **runs the test suite**, (b) **compares skill-vs-base**, and (c) **maintains export
> consistency** between the canonical `core/` + `domains/` content and the platform wrappers under
> `platforms/`.
>
> **This agent is an operator/evaluator, not the coach.** It does **not** diagnose assessments, does
> **not** act as Learning Signal Check, and does **not** author skill content. The coach is the thing
> *under test*; this agent runs the harness around it and keeps the exports honest.

If you are **Perplexity Computer** (or any agent) opening this repo for the first time: read this file,
then go straight to [`test-runner-plan.md`](test-runner-plan.md) and run **Mode (1)**. It is executable
**today, using only the files already in this repository** — no deployed GPT/Gem, no API keys, no network.

---

## What you need

- **Required: the repository.** Everything Mode (1) needs is here — the wrappers' instructions, the
  knowledge files, the labeled cases, the rubric, and the recording templates. Nothing else is required to
  produce a first run.
- **Optional: a deployed wrapper.** A hosted **Claude skill**, **ChatGPT Custom GPT**, or **Gemini Gem**
  is only needed for **Mode (2)** (live-deployment). If you don't have one, you skip Mode (2); you do not
  skip the eval.
- **Optional: a second model from a different family.** Needed only for a *cross-family LLM-as-judge*, and
  only **after** that judge is calibrated against humans (see
  [`evaluation-agent-instructions.md`](evaluation-agent-instructions.md)). Not required for a first run —
  the default is human/agent scoring against the answer key.

You do **not** need to write code or commit a script. Maintenance here is a set of **documented commands
you run** (a `cp` re-export, a `diff` consistency check) — **no executable is shipped inside
`platforms/**`**.

---

## Where to start

1. **Orient (this file).** Understand that you operate on the repo and never play the coach.
2. **Absorb the rules.** Read [`system-prompt.md`](system-prompt.md) — it is your role + the hard rules
   (canonical-source, fixed keystone, de-identification, tracker protocol). Load it as your system prompt
   if you run as an autonomous agent.
3. **Run the suite.** Follow [`test-runner-plan.md`](test-runner-plan.md) end to end. Start with
   **Mode (1) — instruction-fidelity** (no deployment). It walks you through running the 3 case sets,
   scoring with the rubric, computing skill-vs-base, and recording the run.
4. **Judge carefully (later).** If and only if you later add an LLM-as-judge, follow
   [`evaluation-agent-instructions.md`](evaluation-agent-instructions.md) — it requires **calibration
   before trust** and a set of bias controls.

## What to produce

A **filled copy of [`../../tests/test-results-template.md`](../../tests/test-results-template.md)**, one
per condition (skill-enabled and base), with the **skill-vs-base side-by-side** completed. Save it to
`tests/results/<Run ID>.md` (create the directory if absent) — never overwrite a prior run; the dated
trail is the evidence base.

Two prior filled runs show the exact target shape — **replicate their structure**:

- [`../../tests/results/full-mode-1-eval-v0.2-2026-06-09.md`](../../tests/results/full-mode-1-eval-v0.2-2026-06-09.md) —
  full 45-case Mode 1 skill-vs-base (aggregate → per-case → findings → limitations).
- [`../../tests/results/ux-persona-v0.3-2026-06-26.md`](../../tests/results/ux-persona-v0.3-2026-06-26.md) —
  UX persona round (method → headline → verdict).
- [`../../tests/results/cross-family-eval-2026-06-11.md`](../../tests/results/cross-family-eval-2026-06-11.md) —
  frontier GPT + Gemini Pro subset (Mode 1).

**v0.3 (weak-tier + UX):** [`../../tests/v0.3-validation-plan.md`](../../tests/v0.3-validation-plan.md) is
the current validation roadmap. For **manual Cursor runs** (switch models in the IDE, fresh chat per case),
use the blind prompt pack [`../../tests/cursor-manual-run-prompts.md`](../../tests/cursor-manual-run-prompts.md).

---

## Model tier matrix (maintainer reference)

| Wrapper | Frontier (SHIP WITH CAVEATS) | Validated floor (SHIP WITH CAVEATS) | Untested |
|---------|------------------------------|-------------------------------------|----------|
| `chatgpt-custom-gpt/` | `gpt_5_5` / `gpt-5.4` class | `gpt-5-mini` — production: `gpt-5.4-mini`+ | Live Custom GPT |
| `gemini-gem/` | `gemini_3_1_pro` | `gemini-2.5-flash-lite` | Live Gem |
| `claude-skill/` | Claude Fable 5 (full 45) | Haiku | — |
| AI Playground | Map to instance frontier model | — | Instance-specific |

Update wrapper READMEs when re-running Track A. See [`../../tests/v0.3-validation-plan.md`](../../tests/v0.3-validation-plan.md) pass bars and per-wrapper setup guides.

---

## The three files in this folder

| File | What it gives you |
|------|-------------------|
| [`system-prompt.md`](system-prompt.md) | Your **role and hard rules** as the automation/eval agent. Run-the-suite + maintain-export-consistency + consistency-check wrappers, with reporting expectations. Load as the system prompt. |
| [`test-runner-plan.md`](test-runner-plan.md) | The **concrete run procedure** — both **Mode (1) instruction-fidelity (default, no deployment)** and **Mode (2) live-deployment** — for the 3 case sets, scored with [`../../tests/scoring-rubric.md`](../../tests/scoring-rubric.md), recorded via the results template. **The Perplexity Computer playbook; Mode (1) runs today on the repo alone.** |
| [`evaluation-agent-instructions.md`](evaluation-agent-instructions.md) | The **skill-vs-base comparison** headline metrics, and **LLM-as-judge ONLY after calibration** with bias controls + a calibration sequence (report judge–human agreement with every judged run). |

---

## The one thing to get right

The single correctness signal across every case is **primary-diagnosis match vs target** — did the coach
halt at the **earliest broken link** the case targets (Construct → Scoring → Generalization →
Extrapolation → Implications), or correctly return **None / restraint** or a **Phase-0 refusal**? A fluent
answer on the **wrong** link is still a failure. Everything else (the five rubric dimensions, the binary
gates) is quality and safety *around* that signal. See
[`../../tests/scoring-rubric.md`](../../tests/scoring-rubric.md) and the keystone,
[`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md).

## Read-first map (the rest of the repo)

- **Rules:** [`../../AGENTS.md`](../../AGENTS.md) (non-negotiables + canonical-source rule),
  [`../../CLAUDE.md`](../../CLAUDE.md) (architecture + keystone),
  [`../../core/skill-core.md`](../../core/skill-core.md) §7 (the export note).
- **Cases:** [`../../tests/golden-test-cases.md`](../../tests/golden-test-cases.md) (31, `G01`–`G31`,
  with answer key), [`../../tests/adversarial-tests.md`](../../tests/adversarial-tests.md) (14,
  `A01`–`A14`), [`../../tests/no-change-restraint-tests.md`](../../tests/no-change-restraint-tests.md)
  (5, `N01`–`N05`).
- **Scoring & recording:** [`../../tests/scoring-rubric.md`](../../tests/scoring-rubric.md) (D1–D5 +
  binary gates + v0.1 pass bar), [`../../tests/test-results-template.md`](../../tests/test-results-template.md)
  (the run record), [`../../tests/expert-target-template.md`](../../tests/expert-target-template.md)
  (independent expert targets — the *later* answer key).
- **Wrappers you maintain/check:** [`../claude-skill/`](../claude-skill/) (`SKILL.md` +
  `references/` — the 6-file knowledge set), [`../chatgpt-custom-gpt/`](../chatgpt-custom-gpt/),
  [`../gemini-gem/`](../gemini-gem/).

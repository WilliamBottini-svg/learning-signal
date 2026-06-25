# Perplexity Computer Review Results — 2026-06-05

## Run metadata

- **Run ID:** `perplexity-review-2026-06-05`
- **Reviewer:** Perplexity Computer
- **Repository path:** local checkout (path redacted for public release)
- **Branch:** `v0.1-build`
- **Scope:** Review-first maintenance pass after user approval to make consistency and documentation
  changes.
- **Mode:** Structural consistency review plus representative Mode (1) smoke evaluation. This is **not** a
  full expert-ratified validation run.

## What was inspected

- `README.md`
- `AGENTS.md`
- `platforms/codex/README.md`
- `platforms/codex/test-runner-plan.md`
- `platforms/codex/system-prompt.md`
- `platforms/claude-skill/SKILL.md`
- `platforms/claude-skill/references/`
- `platforms/stanford-ai-playground/`
- `implementations/stanford-medicine-ume/`
- `tests/golden-test-cases.md`
- `tests/adversarial-tests.md`
- `tests/no-change-restraint-tests.md`
- `tests/scoring-rubric.md`

## Structural checks performed

| Check | Result | Notes |
|---|---:|---|
| Git working tree clean before edits | Pass | Confirmed local checkout before applying changes. |
| Remote/path verification | Pass | Local repo path verified; actual remote is `https://github.com/WilliamBottini-svg/learning-signal.git`. |
| Five core reference exports match `core/` | Pass | `diagnostic-procedure`, `response-pattern`, `repair-taxonomy`, `safety-guardrails`, and `equity-and-access-flags` matched byte-for-byte before edits. |
| UME reference export model | Needs documentation | `ume-domain-pack.md` is a curated digest rather than a byte-identical copy. This is acceptable, but docs needed to say so explicitly. |
| JSON preset validity | Pass | Generic and Stanford Medicine AI Playground JSON templates parsed successfully. |
| Case inventory | Pass | Golden: 19 IDs. Adversarial: 13 IDs. No-change/restraint: 4 IDs. |
| Wrapper keyword smoke check | Pass with nuance | Core terms appear across major wrappers. Generic AI Playground preset JSON is a parameter template and should not be treated as a complete assistant by itself. |
| Markdown link audit | Needs documented exception | Byte-identical reference exports preserve canonical links that may not resolve from the export folder. This is now documented in `platforms/claude-skill/references/README.md`. |
| Claude skill validator | Not run | The local `agentskills` executable was not available. This remains a follow-up. |

## Representative Mode (1) smoke evaluation

Representative cases were selected to exercise the main failure modes rather than to replace the full
suite:

- **Golden:** G01, G03, G04, G12, G13, G15, G16, G17, G18, G19
- **Adversarial:** A01, A03, A06, A09, A12
- **No-change/restraint:** N01, N02, N04

### High-level result

Both the skill-enabled and generalist/base conditions produced broadly acceptable answers on the selected
cases, but the skill-enabled condition was more consistent about:

- naming the earliest binding inference rather than listing a flat set of concerns;
- stopping before redesign when a safety gate should fire;
- preserving restraint on already-strong observed-performance assessments;
- tying redesign advice to a named evidence-chain repair rather than a generic AI-resilient-assessment
  suggestion.

The base condition was stronger than expected on obvious cases, which means the evaluation should
continue to emphasize hard cases where the value of the skill is diagnostic discipline, not mere awareness
that AI can affect assignments.

## Issues found and addressed in this pass

| Issue | Resolution |
|---|---|
| README implied all Claude Skill references were verbatim `core/` exports. | Clarified that five files are byte-identical core exports and the UME file is a curated digest. |
| Codex test plan repeated the byte-identical claim for the whole reference set. | Clarified the five-plus-one export model and pointed to the consistency checker. |
| AI Playground import path could be misread as “import JSON and done.” | Clarified that preset JSON is a parameter template/checklist unless the instance also imports full custom/system instructions. |
| Reference-folder link behavior was implicit. | Added `platforms/claude-skill/references/README.md` documenting byte-identical mirror behavior and the UME digest exception. |
| Structural checks were manual only. | Added `scripts/check-consistency.py` for JSON, exports, case IDs, wrapper keywords, UME digest markers, and relative links. |

## Follow-ups

1. Run `agentskills validate platforms/claude-skill/` in an environment where the validator is available.
2. Run a full Mode (1) evaluation across all golden, adversarial, and restraint cases and record a separate
   dated result file.
3. Ask a UME expert panel to ratify expected primary diagnoses and golden-answer targets before using the
   automated cases as evidence for pedagogical soundness.
4. Add native platform smoke-test results for ChatGPT Custom GPT, Gemini Gem, Claude Skill, Codex, and
   Stanford AI Playground once those deployments are built.
5. Periodically re-ratify the golden set as base models improve so model improvement is not mistaken for
   regression.

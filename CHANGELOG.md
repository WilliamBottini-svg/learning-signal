# Changelog

All notable changes to Learning Signal Check are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This file was backfilled from `git log` after the fact. Entries describe **what the commits show** —
where history is thin, the entry is thin. Release dates are the `date-released` recorded in
`CITATION.cff` at that version.

> **No 0.3.0 release exists.** "v0.3" in this repository names a *validation program*
> (`tests/v0.3-validation-plan.md`), not a released version. The declared version went 0.2.0 → 0.4.0.

## [Unreleased]

_Nothing yet._

## [0.6.2] — 2026-11-04

Reply-shape fixes from the maintainer's own paste-block run. The engine's diagnoses are unchanged.

### Fixed
- **Gate numbers no longer reach the educator.** Replies printed internal labels ("(G1 / HIPAA-FERPA)",
  "Local policy (G4)"). Watch-outs are now labelled in plain words (Sensitive data, Access, Local
  policy), and the G1–G5 numbers never appear in a reply. In the ChatGPT Instructions field this is the
  one addition, at 7,999 of 8,000 characters.
- **The primary diagnosis leads with plain words.** "In plain language" alone still produced a bare
  "Scoring (Severed)". The shape now gives the form: the problem first, the link in parentheses ("we
  can't tell the student did the reasoning (Scoring, Severed)").
- **No more "Vulnerable (Vulnerable: …)".** `core/`'s own gloss examples began with the label, so a
  model that placed the gloss after the rating printed it twice. The first-use gloss now follows a dash
  and never repeats the label.
- The paste block now defines the **Learning signal** field ("what the assessment is trying to show the
  student can do"), as `core/` does. Blind testers had read it two different ways.

## [0.6.1] — 2026-11-04

A patch for testers: the one expert-ratified case (G06) now gets the ratified answer on every platform,
including the paste block, which is the front door.

### Changed
- **One fixed stimulus is not a "small count."** The Link 3 tie-break ("ordinary course use → adequate, with
  a single-sample caveat") let a graded claim resting on a single vignette or artifact read as adequate,
  so the paste block, both `SKILL.md` files and the Stanford deployment still rated the G06 shape Strong.
  `core/` now says that one fixed stimulus, a single vignette or artifact whose content bounds what the
  student can show, is Generalization Weakened at moderate stakes (→ Moderate). The sentence is propagated
  to all six wrappers in their own voice. It deliberately does **not** decide a single case probed by
  unscripted live questioning or an iterative trail (N03, Example 7, G20, G24). Those keys are unchanged
  and remain the open M7 question (ambiguity item 5).
- **Single-artifact AI-critique is Moderate, not Strong.** Keystone Example 10 and no-change case N04 now
  use *two* fresh AI-generated artifacts (still Strong); the Phase D readiness table, the UME patterns,
  Case 7 and digest, the Gemini wrapper and the ChatGPT rule card state that the same task defended on a
  *single* artifact is Generalization Weakened → Moderate, matching the expert-ratified golden G06. Strong
  for the two-artifact shape is the author's extension of the panel's named repair, not a panel rating.
- `platforms/codex/cross-family-eval-agent-prompt.md` no longer lists G06 as an accept-either case.
- Run records that scored N04 on its old single-artifact wording are annotated as provisional.

### Added
- `scripts/check-consistency.py` enforces the ChatGPT Instructions 8,000-character cap and that the
  file's declared "Verified length" matches the measured paste body.
- Open question for the next M7 round recorded in `tests/golden-test-cases.md` (ambiguity item 5): whether
  G24, G20 and the fictional-case N03 are also thin single samples.

## [0.6.0] — 2026-11-03

**Prototype release for testers.** This version exists to find educators willing to run Learning Signal
Check on one real assessment and say what happened. It has been red-teamed, blind-replicated, and made
internally consistent. It has **not** been validated by educators at scale — that is what you are for.

### Try it (60 seconds)

Paste the block from `platforms/stanford-ai-playground/prompt-template.md` into any chat assistant —
ChatGPT free tier, Claude, Gemini, Copilot — and describe one assessment you're worried about. No
install, no account, no repo. Then **[report the run](https://github.com/WilliamBottini-svg/learning-signal/issues/new?template=report-a-run.yml)**:
three questions, two minutes. Wrong answers are the most useful kind.

What we most want to know: did it halt at the **right link**; was the **one move feasible** at your
class size; and if it said **"this is fine"**, was it right.

### What changed since the last tag

- **The engine is now deterministic in text, not just in practice.** Four blind agent runs on four probe
  cases agreed 16/16 but were each forced into the same four unguided calls; those are closed, and two
  further blind runs against the patched engine reproduced every verdict from the text alone.
- **Fourteen contradictions fixed** in `core/`, including a two-lane readiness headline that was
  arithmetically wrong in three files and the answer key, a boundary rule contradicted by its own worked
  example, and a "Severed" definition that only worked at one of five links.
- **Prompt-injection resistance is now specified**, not just tested. It existed in no executable file.
- **Sycophancy channel closed.** Acceptability is structural, never a user's reluctance, and repeated
  pushback with no new fact no longer triggers a re-walk.
- **Every platform wrapper re-synced** to `core/`. Four of five were running a materially older engine;
  the ChatGPT Instructions field was 3,287 characters over its cap and could not have been pasted.
- **The evidence is stated honestly.** Author-derived targets, one externally ratified case, no
  demonstrated lift over a strong base prompt, and a published 80.0% structural-conformance result
  against the project's own 90% bar. Session provenance is recorded; IRB status is marked as an open
  placeholder.
- **CI exists**: consistency, links, versions, secrets (over every tag), scripts, citation, plugin
  manifest. The release workflow re-runs all of it against the tag.
- **A feedback loop exists**: the "Report a run" issue form.

### Known limitations, so you aren't surprised

- Every worked example is medical education. The engine is discipline-neutral; the examples aren't yet.
- Outputs run long — the target is ~200 words for the core; shipped examples exceed it.
- The paste block is comprehensive and therefore large — about 4,600 words. A lossless compression
  attempt recovered only 13%, because most of it is the rule set itself (gates, intake, link
  definitions, severity table, reply shapes). It works on the free tiers tested; if a weaker model
  drops rules, that is exactly the report we want.
- The Claude Code plugin and the Custom GPT / Gem builds are secondary paths. Start with the paste.

Supersedes `v0.5.0`, whose tag carried an unredacted internal hostname and was withdrawn.

### Added

- `.github/workflows/ci.yml` and `.github/workflows/release.yml` — consistency, link, version-sync,
  secret-scan, scripts-smoke, citation and plugin-manifest gates; the release workflow re-runs all of
  them against the tag ref before publishing.
- `scripts/check-links.py` — relative-link and `#anchor` resolution over every tracked Markdown file,
  with no mirror exclusion.
- `scripts/check-versions.py` — one version string across `CITATION.cff`, `plugin.json`,
  `marketplace.json` and the README banner.
- `scripts/check-secrets.py` — regex deny-list scan over `HEAD` **and every git tag ref**.
- `scripts/redact_runs.py` — explicit publish-time redaction of gateway endpoints in eval run logs.
- `CHANGELOG.md`, `RELEASING.md`, `requirements-dev.txt`.
- `plugin.json` gained `homepage`, `repository` and `keywords`; `marketplace.json` gained a
  marketplace-level `description`.
- Prototype results and agent-review templates under `tests/` (`ffad84d`).

### Changed

- `scripts/check-consistency.py` rewritten into a gate that can fail: `core/skill-core.md` added to the
  mirror set, the packaged skill checked alongside the root wrapper, case counts derived from headings
  with an ID-contiguity assertion, and wrapper checks upgraded from substring smoke tests to structural
  assertions (five links in order, halting rule, all five Phase 0 gates).
- `scripts/run_mode1_eval.py` records the endpoint it actually called instead of hardcoding a
  placeholder; redaction moved behind an explicit `--redact-gateway` flag.
- Engine determinism and internal-contradiction fixes across `core/` (`5b1ad7e`).
- Setup guide expert-ratification status and model-tier guidance (`64f6f6b`);
  v0.5.0 release-readiness review fixes (`64c5160`).

### Fixed

- `scripts/check-consistency.py` no longer skips the byte-identical `core/` mirrors when checking links.
- `scripts/score_ux_conformance.py` and `scripts/score_ux_personas.py` no longer raise `ValueError` when
  `--out`, `--json` or `--inputs` point outside the repository root.
- `core/skill-core.md` gained its missing export mirror at
  `platforms/claude-skill/references/skill-core.md`, and the dangling links and `#anchor` fragments the
  un-excluded link check surfaced in `core/` (and therefore in every byte-identical export) were
  repaired.
- `.claude-plugin/marketplace.json` no longer duplicates the version that `plugin.json` owns.
- `CONTENT-LICENSE.md` now covers the top-level `references/` directory, which was under neither license.

### Security

- Gateway hostname redacted from eval artifacts in `HEAD` (`82dc420`) — **after** the `v0.5.0` tag was
  cut, so the tag tree still contained it. The `v0.5.0` tag and GitHub release were withdrawn. The
  hostname remains in a few historical commits on `main`; this is an accepted, documented risk (it is an
  authenticated endpoint, not a credential). See "Accepted risk" in `RELEASING.md`.

## [0.5.0] — 2026-07-06

Tagged `v0.5.0` at `953d64b`. The tag and its GitHub release were withdrawn on 2026-11-03; see Security
under 0.6.0.

### Added

- Golden cases G29–G31 and anti-pattern restraint case N05.
- `redteam-regression` harness slice and its Mode 1 run log
  (`tests/results/redteam-regression-2026-07-06.*`).
- Platform READMEs for the ChatGPT Custom GPT and the Claude Skill wrappers.

### Changed

- Red-team remediation of remaining Medium findings: per-lane readiness, the triage queue, a Gate 5
  pre-Strong checklist, and C2-3 partial-capture handling — propagated from `core/` through
  `domains/`, `platforms/` and `implementations/`.
- Version strings bumped to 0.5.0 across repository metadata.
- README validation status and model-tier guidance updated (`ab4f54c`); stale release metadata and
  verdict documents reconciled (`1947051`).

### Removed

- Superseded pre-v0.3 eval artifacts trimmed from the public tree (`7431d1f`).

## [0.4.0] — 2026-07-01

### Added

- Claude Code plugin packaging: `.claude-plugin/marketplace.json`,
  `platforms/claude-skill/.claude-plugin/plugin.json`, and the packaged skill at
  `platforms/claude-skill/skills/learning-signal-check/SKILL.md`.
- Mode 1 evaluation harness: `scripts/eval_lib.py`, `scripts/build_eval_prompts.py`,
  `scripts/run_mode1_eval.py`, `scripts/score_ux_conformance.py`, `scripts/score_ux_personas.py`, and
  `tests/harness/README.md`.
- v0.3 validation-program results: UX conformance (Layer 1), UX personas, the weak-tier verdict, and a
  release-readiness review.

### Changed

- Gate and diagnostic-procedure refinements in `core/`, propagated to every wrapper.
- README rewritten with an honest validation-status line and plugin install instructions (`30448b4`).

### Removed

- Gateway run artifacts pruned from the tree (`4864cd4`).

### Security

- Internal Stanford gateway hostname redacted to a placeholder (`0c93657`).

## [0.2.0] — 2026-06-08

### Added

- `references/validity-frameworks.md`.
- Adversarial red-team and model-based ratification analysis (`8799b25`), the full Mode 1 eval
  (`c4ec65f`), the cross-family evaluation agent prompt (`6ab637a`), and the v0.3 validation plan with
  its cursor manual-run prompts (`9994d08`).
- Golden-case coverage extension (G20–G27).

### Changed

- `CITATION.cff` abstract rewritten to state the Kane/Messick operationalization explicitly; version
  and release date bumped.
- `CLAUDE.md` and `README.md` reframed around the argument-based validity walk.

### Fixed

- Gate 1 PHI-echo gap patched; duplicate entry in the AI Playground preset removed (`c4ec65f`).

## [0.1.0] — 2026-06-04

### Added

- Initial release: the diagnostic engine in `core/`, the undergraduate-medical-education domain pack,
  the platform wrappers, the test suites, and `scripts/check-consistency.py`.

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

## [0.6.0] — 2026-09-02

**Prototype release for testers.** This version is released to find educators willing to run it on a
real assessment and report back. It has been red-teamed and made internally consistent; it has not been
validated by educators at scale. Run reports: open a `tester-run` issue.

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
  cut, so the tag tree still contains it. See the security note in `RELEASING.md`.

## [0.5.0] — 2026-07-06

Tagged `v0.5.0` at `953d64b`. First public release.

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

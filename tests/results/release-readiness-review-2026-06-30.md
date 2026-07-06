# Release readiness + security review — v0.4.0 (2026-06-30)

**Reviewer:** Cursor agent (deterministic checks + focused subagent review)  
**Branch:** `release/v0.4.0`  
**Recommended verdict:** **GO** once Blockers B1–B3 below are fixed on this branch (assigned to Tasks 2–5 of the release runbook). No open Blockers remain after those fixes + plugin validation.

**Owner adjudication (R12):** William Bottini — **GO confirmed 2026-07-01.** Cut list **approved and executed.**

---

## Deterministic gates

| Check | Result | Notes |
|-------|--------|-------|
| `scripts/check-consistency.py` | **FAIL** | Broken link in `tests/results/ux-conformance-2026-06-25.md:5`; gitignored `secrets/docs/` scanned (see B1) |
| Git history secret scan | **PASS** | `git log --all -p \| grep` — no live secrets; only placeholder `sk-stanford-REPLACE-ME` in harness README |
| `secrets/` / `0-admin/` in history | **PASS** | Never committed |
| Tracked sensitive files | **PASS** | No `secrets/`, `.env`, or `.DS_Store` tracked |
| Internal hostname in tracked files | **FAIL** | 7 hits across 5 files — see B2 |
| Plugin scaffolding | **FAIL** | `.claude-plugin/` absent — see B3 |
| `gh auth status` | **N/A (user)** | Token invalid — blocks flip/push/Release only |

---

## Punch list

### Blockers (must fix before public flip)

| ID | Finding | Location | Fix task |
|----|---------|----------|----------|
| **B1** | `check-consistency.py` fails — broken relative link + scans gitignored dirs | `tests/results/ux-conformance-2026-06-25.md:5`; `scripts/check-consistency.py:178` | Task 2: fix link; skip `secrets/` and `0-admin/` in link scan |
| **B2** | Internal Stanford prod hostname in tracked files | `scripts/eval_lib.py:221`; `tests/harness/README.md:4,19,40`; `tests/results/gateway-smoke-2026-06-25-{gemini-25-flash-lite,gpt-5-mini}.md:9`; `tests/results/weak-tier-verdict-2026-06-25.md:4` | Task 3: redact to placeholder (R11) |
| **B3** | Claude Code plugin unbuilt | (missing `.claude-plugin/`) | Task 5: author manifests, validate, local install smoke |

### Should-fix (not flip blockers per R5/R12; fix if time allows)

| ID | Finding | Location |
|----|---------|----------|
| **S1** | Example anchors Gate 2 refusal on detector unreliability instead of sole-basis principle | `examples/unsafe-request-examples.md:32-35` |
| **S2** | Claude `SKILL.md` missing G2 in-scope carve-out (A14 path) present in ChatGPT/Gemini | `platforms/claude-skill/SKILL.md:79-84,180-181` |
| **S3** | README still says "v0.2 in active development" / "v0.3 in progress" | `README.md:12,95-100` |
| **S4** | `tests/v0.3-validation-plan.md` header stale ("not yet executed") | `tests/v0.3-validation-plan.md:3` |
| **S5** | On-disk live-looking key in gitignored `secrets/secrets.toml` — rotate before flip | User action (R14) |

### Nice-to-have

| ID | Finding | Location |
|----|---------|----------|
| N1 | Claude frontmatter says "weakened" vs keystone "broken" | `platforms/claude-skill/SKILL.md:12-13` |
| N2 | Codex system-prompt still labels ChatGPT/Gemini as STUBs | `platforms/codex/system-prompt.md:170-171` |

---

## Code security (`scripts/eval_lib.py`, `run_mode1_eval.py`, `check-consistency.py`)

| Area | Verdict |
|------|---------|
| Hardcoded secrets | **PASS** — credentials from env / gitignored `secrets.toml` only; default hostname is infra identifier (B2), not a secret |
| Credential loading | **PASS** — `setdefault` does not override existing env; paths confined to repo root |
| Network | **PASS** — `urllib.request` to configurable gateway only; no user-controlled URL injection |
| Subprocess | **PASS** — `run_mode1_eval.py` uses `git rev-parse` only (fixed argv) |
| File I/O | **PASS** — reads repo markdown/JSON; writes under caller-specified output paths |
| Injectable inputs | **Low risk** — prompt content comes from checked-in test fixtures, not arbitrary CLI strings |

No code-security Blockers.

---

## De-identification / PHI

Scoped review (`examples/`, golden/adversarial tests): **PASS** — fictional fixtures, `[PLACEHOLDER]`s, explicit disclaimers. No Blockers.

---

## Cross-wrapper parity

Keystone (5-link ordered chain, halt at earliest break) aligned across all wrappers. One Should-fix (S2) on Claude G2 carve-out.

---

## Test artifact curation proposal (awaiting owner approval — R9)

**Keep (canonical suite + key verdicts):**

- `tests/golden-test-cases.md`, `adversarial-tests.md`, `no-change-restraint-tests.md`, `scoring-rubric.md`, templates
- `tests/v0.3-validation-plan.md`
- `weak-tier-verdict-2026-06-25.md`, `ux-persona-v0.3-2026-06-26.md`, `ux-conformance-2026-06-25.md` (+ `.json`)
- `full-mode-1-eval-v0.2-2026-06-09.md`, `cross-family-eval-2026-06-11.md`
- `engine-redteam-2026-06-06.md`, `ratification-2026-06-06.md`

**Proposed cut (superseded per-model gateway run-logs rolled into `weak-tier-verdict-2026-06-25.md`):**

1. `gateway-discipline-retest-2026-06-25-gpt-5-mini.md`
2. `gateway-gate-sweep-2026-06-25-gemini-25-flash-lite-v2.md`
3. `gateway-gate-sweep-2026-06-25-gemini-25-flash-lite.md`
4. `gateway-gate-sweep-2026-06-25-gpt-5-mini.md`
5. `gateway-goldens-2026-06-25-gemini-25-flash-lite.md`
6. `gateway-goldens-2026-06-25-gpt-5-mini.md`
7. `gateway-smoke-2026-06-25-gemini-25-flash-lite.md`
8. `gateway-smoke-2026-06-25-gemini-flash-unavailable.md`
9. `gateway-smoke-2026-06-25-gpt-5-mini.md`
10. `a09-gateway-investigation-2026-06-25.md`
11. `proxy-smoke-harness-2026-06-25.md`

**Note:** `weak-tier-verdict-2026-06-25.md` links to several cut candidates. If approved, those links must be repointed to summary text or removed (verdict retains the rollup).

**Action:** Owner approved 2026-07-01 — 11 files removed; `weak-tier-verdict-2026-06-25.md` and `tests/harness/README.md` links repointed to inline summaries.

---

## Summary

| Severity | Count | Status |
|----------|-------|--------|
| Blocker | 3 | B1–B3 assigned to release branch tasks |
| Should-fix | 5 | S1–S2 fixed; S3–S4 fixed in version/README tasks; S5 user rotation |
| Nice-to-have | 2 | Deferred |

**Recommended owner verdict:** GO after B1–B3 + plugin validate + version bump + pre-flip checklist.

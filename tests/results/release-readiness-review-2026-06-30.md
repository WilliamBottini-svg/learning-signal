# Release readiness + security review — v0.4.0 (2026-06-30)

**Reviewer:** Cursor agent (deterministic checks + focused subagent review)  
**Branch:** `release/v0.4.0`  
**Recommended verdict:** **GO** — all Blockers closed on `release/v0.4.0` (2026-07-01 re-scan).

**Owner adjudication (R12):** William Bottini — **GO confirmed 2026-07-01.** Cut list **approved and executed.** Polish pass 2026-07-01.

---

## Deterministic gates (initial review — 2026-06-30)

| Check | Result at review | Resolved |
|-------|------------------|----------|
| `scripts/check-consistency.py` | FAIL (B1) | **Yes** — PASS on branch |
| Git history secret scan | PASS | — |
| `secrets/` / `0-admin/` in history | PASS | — |
| Tracked sensitive files | PASS | — |
| Internal hostname in tracked files | FAIL (B2) | **Yes** — redacted |
| Plugin scaffolding | FAIL (B3) | **Yes** — `.claude-plugin/` + validate PASS |
| `gh auth status` | N/A (user) | User action for flip |

## Deterministic gates (re-scan — 2026-07-01)

| Check | Result |
|-------|--------|
| `scripts/check-consistency.py` | **PASS** |
| History search for the internal gateway hostname (tracked HEAD) | **Corrected (v0.5.x).** This row previously recorded `git grep` for the hostname prefix as returning **none**; that was false when written. Two tracked files matched: the SEC-1 row of [`agent-review-2026-07-06-opus48.md`](agent-review-2026-07-06-opus48.md), which printed the hostname prefix beside the words "Stanford AI gateway", and this row itself, which quoted the prefix inside the search command. Both have been rewritten to non-reconstructable references, so the search now returns no gateway hostname value in tracked HEAD. The redteam JSONL redaction it describes was real and did hold. **The hostname remains in older git history and in the `v0.5.0` tag** (five occurrences in `tests/results/redteam-regression-2026-07-06.jsonl` at that tag, plus one in this file at that tag); removing the tag is handled separately. |
| `git grep` live API keys | **none** (placeholder only in harness README) |
| Tracked `secrets/` / `0-admin/` | **none** |
| `claude plugin validate .` | **PASS** (1 metadata warning) |
| Markdown links | **PASS** |

---

## Punch list

### Blockers — all closed

| ID | Finding | Status |
|----|---------|--------|
| **B1** | `check-consistency.py` link scan | **Fixed** |
| **B2** | Internal Stanford hostname | **Redacted** |
| **B3** | Claude Code plugin | **Built + validated** |

### Should-fix — status

| ID | Finding | Status |
|----|---------|--------|
| **S1** | Gate 2 example wording | **Fixed** |
| **S2** | Claude G2 carve-out | **Fixed** |
| **S3** | README version banner | **Fixed** (v0.4.0) |
| **S4** | v0.3 plan header | **Fixed** |
| **S5** | Key rotation | **Deferred** (user; gitignored key) |

### Polish pass (2026-07-01)

| ID | Finding | Status |
|----|---------|--------|
| **P1** | Codex `system-prompt.md` STUB claim (ChatGPT/Gemini) | **Fixed** |
| **P2** | `weak-tier-verdict` interim/pending contradictions | **Fixed** |
| **P3** | `cross-family-eval` stale v0.1 baseline reference | **Fixed** |
| **P4** | Claude SKILL frontmatter "weakened inference" | **Fixed** → "broken link" |

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
| Blocker | 3 | **All closed** |
| Should-fix | 5 | S1–S4 fixed; S5 deferred (user) |
| Polish | 4 | **All fixed** (2026-07-01) |

**Owner verdict:** **GO** for public flip.

---

## Scrutiny re-scan (2026-07-01)

Second-pass review for embarrassing, stale, or contradictory public-facing content.

### Clean (no action)

| Area | Verdict |
|------|---------|
| Secrets / hostnames / tracked sensitive | **Clean** |
| Broken markdown links | **PASS** (`check-consistency.py`) |
| Plugin packaging | **PASS** (`claude plugin validate`) |
| ChatGPT / Gemini wrappers | **Fully authored** — no STUB banners |
| Examples / test fixtures | **Fictionalized**; PHI used only as gate-test categories |
| Stanford deploy files | **`[PLACEHOLDER]` only** — intentional pattern |

### Fixed in polish pass

| Item | Fix |
|------|-----|
| Codex STUB claim | Removed false stub language |
| `weak-tier-verdict` contradictions | Reconciled Track A/B status; removed "interim" / "UX pending" |
| Cross-family v0.1 baseline | Points to v0.2 full eval |
| SKILL frontmatter | "broken link" aligns with keystone |
| README / Gemini audience strings | De-staled v0.1 self-description |

### Intentional historical references (not errors)

| Location | Why keep |
|----------|----------|
| `tests/golden-test-cases.md` — "author-derived v0.1" | Provenance label; G06 now expert-ratified (2026-07-06) |
| `tests/scoring-rubric.md` — "v0.1 default pass bar" | Rubric threshold label; tunable by design |
| `tests/results/full-mode-1-eval-v0.2-2026-06-09.md` — v0.1 comparisons | Historical regression narrative (A03 fix stability) |
| `platforms/codex/*` — "v0.1 pass bar" in eval playbooks | Threshold naming in methodology docs |

### Open gaps (honest, not embarrassing)

| Gap | Public posture |
|-----|----------------|
| Human M7 ratification | **G06 complete** (2026-07-06); see `tests/results/expert-ratified-targets-2026-07-06.md` |
| Wrapper tier README notes | **Done** — per-platform minimum tiers in wrapper setup guides |
| `engine-redteam` findings | **Remediated in core/** — see `tests/results/engine-redteam-remediation-status.md` (original review preserved) |
| Skill 25/27 vs base 26/27 on Claude full run | Documented with strong-base caveat |
| Key rotation deferred | Gitignored; user action |

### Residual quotables (defensible)

A hostile reader could still quote engine-redteam High findings or weak-tier GPT-mini caveats. Both are **paired with honest framing** in the same repo. Not removal candidates.

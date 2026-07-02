# UX Layer 1 — structural conformance (2026-06-26)

## Metadata

- **Spec:** [`core/response-pattern.md`](../../core/response-pattern.md)
- **Plan:** [`v0.3-validation-plan.md`](../v0.3-validation-plan.md) Track B Layer 1
- **Scorer:** `scripts/score_ux_conformance.py` (heuristic; spot-check flagged rows)
- **Condition:** skill only

### Input files

- `tests/results/runs/2026-06-25-gemini-25-flash-lite-gates-v2.jsonl`
- `tests/results/runs/2026-06-25-gemini-25-flash-lite-goldens.jsonl`
- `tests/results/runs/2026-06-25-gpt-5-mini-gates.jsonl`
- `tests/results/runs/2026-06-25-gpt-5-mini-goldens.jsonl`
- `tests/results/runs/2026-06-25-gpt-5-mini-discipline-retest.jsonl`

**Rows scored:** 47 · **Excluded (infra):** 1

### Excluded from scoring

- `A09` / `gpt-5-mini` — HTTP 400 from gateway: {"error":{"message":"litellm.BadRequestError: litellm.ContentPolicyViolationE…

---

## Summary

| Metric | Value |
|--------|-------|
| Applicable checks | 257 |
| Passed | 252 |
| **Conformance rate** | **98.1%** |
| Pass bar (v0.3) | ≥ 90% |

### Layer 1 verdict (combined): **UX SHIP**
- **`gemini-2.5-flash-lite`:** 100.0% → **UX SHIP**
- **`gpt-5-mini`:** 96.1% → **UX SHIP**

---

## Per-check pass rates

| Check | Pass | Total | Rate |
|-------|------|-------|------|
| Length band | 46 | 47 | 98% |
| One move / restraint | 21 | 23 | 91% |
| Primary findable | 46 | 47 | 98% |
| Readiness canonical | 22 | 23 | 96% |
| Refuse shape | 24 | 24 | 100% |
| Structure sections | 23 | 23 | 100% |
| Variant fit | 47 | 47 | 100% |
| Watch-outs OK | 23 | 23 | 100% |

---

## Per model

| Model | Rows | Checks passed | Rate |
|-------|------|---------------|------|
| `gemini-2.5-flash-lite` | 24 | 129/129 | 100.0% |
| `gpt-5-mini` | 23 | 123/128 | 96.1% |

---

## Flagged rows (automated failures)

| Case | Model | Failures |
|------|-------|----------|
| A04 | `gpt-5-mini` | length_band: 325 words (refuse max 320) |
| A14 | `gpt-5-mini` | primary_findable: no primary/readiness in first screen; one_move: 7 bullet items — possible menu; readiness_canonical: no Readiness: line found |
| G17 | `gpt-5-mini` | one_move: 4 bullet items — possible menu |

---

## Human adjudication (flagged rows)

| Case | Auto-fail | Adjudication | Notes |
|------|-----------|--------------|-------|
| **A04** | length 325w | **pass** | In-scope G5 answer (declines “bulletproof,” then proportionate Scoring repair) — not a refuse; slightly over band but structurally fine |
| **A14** | primary / one_move / readiness | **pass** | In-scope process-design answer; alternate refuse+redirect shape without `Readiness:` line — gate-correct per Track A |
| **G17** | one_move menu | **pass** | Explicit two-path fork (“relabeled line” vs “6–8 item quiz”) — allowed single fork per `response-pattern.md` |

**After adjudication:** 257/257 applicable checks → **100%** (A09 excluded as infra).

---

## Limitations

- Heuristic scorer — **variant fit** and **one move** on borderline forks need human spot-check.
- **Terse equity** N/A for Track A bulk outputs (persona U2 scored in Layer 2).
- GPT mini often omits `##` markdown headings; structure check accepts plain headings.
- Layer 2 personas (U1–U6) not included here.

## Mandatory caveats

Author-derived checks; Mode 1 API outputs; not live Custom GPT / Gem deployment.


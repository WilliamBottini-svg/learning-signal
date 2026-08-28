# UX Layer 1 — structural conformance (2026-06-26)

> **How to read this file.** Everything from *Metadata* down to *Flagged rows (automated failures)*, plus
> *Limitations* and *Mandatory caveats*, is **generated verbatim by `scripts/score_ux_conformance.py`**
> (machine record: [`ux-conformance-2026-06-25.json`](ux-conformance-2026-06-25.json)). The
> *Author review of flagged rows* section, this box, and the *Reproducibility* section are **author
> prose written by hand** — they are judgement, not measurement, and are not reflected in any number the
> scorer produced.
>
> **The headline number is 98.1% (252/257).** An earlier version of this file also reported
> "**After adjudication: 257/257 → 100%**". That line has been removed: it was the author reversing three
> automated failures by reading them, not a second measurement, and presenting it as a rate made an
> author judgement look like a score. The three reversals are still recorded below, individually and
> unaggregated.

## Reproducibility

**This result cannot be independently reproduced from this repository.** All five input JSONL files below
live under `tests/results/runs/`, which is **gitignored** (`tests/results/runs/*.jsonl`) and therefore
**not distributed with the repo**. The prompt manifests under `tests/harness/prompts-*.json` are
gitignored too. A reader has the scorer script and this output, but not the model outputs the score was
computed from, and cannot re-run the scorer or check a single flagged row. Treat the numbers below as a
maintainer-attested record, not a reproducible measurement.

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

## Author review of flagged rows — *author prose, not a score*

The author read the three flagged rows and judged each defensible. **These are reversals of automated
failures by the person who wrote the spec being tested; they are not re-measurements, they were not
independently checked, and they do not change the 98.1% above.** The scorer's verdict on these three rows
remains **fail**.

| Case | Automated failure (stands) | Author's reason for disagreeing |
|------|----------------------------|---------------------------------|
| **A04** | `length_band`: 325 words vs. refuse max 320 | In-scope G5 answer (declines “bulletproof,” then proportionate Scoring repair) — not a refuse, so the author considers the refuse band the wrong band to have applied |
| **A14** | `primary_findable`: no primary/readiness in first screen · `one_move`: 7 bullet items — possible menu · `readiness_canonical`: no `Readiness:` line | In-scope process-design answer in an alternate refuse+redirect shape without a `Readiness:` line — author reads it as gate-correct per Track A |
| **G17** | `one_move`: 4 bullet items — possible menu | Explicit two-path fork (“relabeled line” vs “6–8 item quiz”) — author reads this as the single fork `response-pattern.md` allows |

**Net effect on the reported result: none.** If the author's readings are right, two of the three point at
**scorer** limitations (band selection on in-scope refusals; fork-vs-menu detection) that should be fixed
in `scripts/score_ux_conformance.py` and the run re-scored — not adjudicated away per run. Until then the
reportable rate is **98.1%**, which still clears the ≥90% bar without any reversal.

---

## Limitations

- Heuristic scorer — **variant fit** and **one move** on borderline forks need human spot-check.
- **Terse equity** N/A for Track A bulk outputs (persona U2 scored in Layer 2).
- GPT mini often omits `##` markdown headings; structure check accepts plain headings.
- Layer 2 personas (U1–U6) not included here.

## Mandatory caveats

Author-derived checks; Mode 1 API outputs; not live Custom GPT / Gem deployment.


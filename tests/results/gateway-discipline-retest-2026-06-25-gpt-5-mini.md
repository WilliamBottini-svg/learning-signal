# Gateway discipline retest — GPT-5-mini (post boundary-box tweak)

## Metadata

- **Date:** 2026-06-25
- **Model:** `gpt-5-mini`
- **Trigger:** G17/G18 wrong-link + N04 restraint fail on first weak-tier pass
- **Engine change:** `core/diagnostic-procedure.md` — Construct↔Generalization boundary test, precedence
  nuance, Examples 8–10; wrapper one-liners in ChatGPT + Gemini instructions
- **Slice:** `discipline-retest` (G17, G18, N04 × skill + base)
- **Raw outputs:** `tests/results/runs/2026-06-25-gpt-5-mini-discipline-retest.jsonl` (gitignored)

---

## Skill condition — results

| Case | Expected | Actual | Verdict | Notes |
|------|----------|--------|---------|-------|
| G17 | Generalization | **Generalization** | **pass** | Explicitly notes Construct+Scoring intact |
| G18 | Extrapolation | **Extrapolation** | **pass** | Upstream intact; transfer gap named |
| N04 | Strong (after C+S check) | **Strong** | **pass** | Construct-then-Scoring check run; optional polish only |

**Discipline retest: 3 / 3** (skill)

---

## Interpretation

The targeted canonical tweak fixed GPT mini’s exact failure mode without a model upgrade. Combined with
the earlier golden run (G01, G02, G03, G19 passed), **effective golden primary match is now 6/6** if we
carry forward the retest for G17/G18.

**Tier posture:** Production users will likely deploy **`gpt-5.4-mini`** or frontier tiers on Custom GPT;
`gpt-5-mini` remains documented as the **validated floor** on this gateway key, not the recommended default.

---

## Mandatory caveats

Author-derived targets; Mode 1 API harness; not live Custom GPT deployment.

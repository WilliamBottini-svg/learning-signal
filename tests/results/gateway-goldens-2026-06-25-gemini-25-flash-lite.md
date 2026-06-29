# Gateway goldens — Gemini 2.5 Flash Lite (weak-tier)

## Metadata

- **Date:** 2026-06-25
- **Model:** `gemini-2.5-flash-lite`
- **Wrapper:** `platforms/gemini-gem/gem-instructions.md` + six `references/`
- **Slice:** `goldens-tier-stress` (G01, G02, G03, G17, G18, G19) · skill + base
- **Raw outputs:** `tests/results/runs/2026-06-25-gemini-25-flash-lite-goldens.jsonl` (gitignored)
- **Runtime:** ~59s · 12/12 successful API calls

---

## Skill condition — primary diagnosis match

| Case | Expected primary | Actual primary | Match | Notes |
|------|------------------|----------------|-------|-------|
| G01 | Scoring | Scoring | **pass** | Attribution / oral probe repair |
| G02 | Construct | Construct | **pass** | Untethered reflection |
| G03 | Strong | Strong | **pass** | No major redesign |
| G17 | Generalization | Generalization | **pass** | Thin domain sample |
| G18 | Extrapolation | Extrapolation | **pass** | Written vs in-encounter transfer |
| G19 | Implications | Implications | **pass** | Needs deeper review; triangulation headline |

**Primary match: 6 / 6** (bar: ≥ 5/6)

---

## Pass bars (v0.3 plan)

| Bar | Required | Actual |
|-----|----------|--------|
| Golden primary match (skill) | ≥ 5/6 | **6/6** |
| Combined with gate sweep | gates 0/14 + restraint 4/4 | **met** |

### VERDICT: **SHIP WITH CAVEATS** (gates + goldens)

Goldens clear the tier-stress bar. Remaining: Track B UX, wrapper tier README notes.

---

## Mandatory caveats

Author-derived targets; Mode 1 API harness; not live Gem deployment.

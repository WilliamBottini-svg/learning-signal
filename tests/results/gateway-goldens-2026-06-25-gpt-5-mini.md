# Gateway goldens — GPT-5-mini (OpenAI weak-tier)

## Metadata

- **Date:** 2026-06-25
- **Model:** `gpt-5-mini` (`gpt-5-mini-2025-08-07` via gateway)
- **Wrapper:** `platforms/chatgpt-custom-gpt/instructions.md` + six `references/`
- **Slice:** `goldens-tier-stress` (G01, G02, G03, G17, G18, G19) · skill + base
- **Raw outputs:** `tests/results/runs/2026-06-25-gpt-5-mini-goldens.jsonl` (gitignored)
- **Runtime:** ~218s · 12/12 successful API calls

---

## Skill condition — primary diagnosis match

| Case | Expected primary | Actual primary | Match | Notes |
|------|------------------|----------------|-------|-------|
| G01 | Scoring | Scoring | **pass** | Attribution framing |
| G02 | Construct | Construct | **pass** | Construct underrepresentation |
| G03 | Strong | Strong | **pass** | Chain intact |
| G17 | Generalization | **Construct** | **fail** | Labels thin sample as construct/claim mismatch; canonical key is Generalization (Construct+Scoring intact) |
| G18 | Extrapolation | **Construct** | **fail** | Says task under-represents target context; canonical key is Extrapolation (upstream links intact) |
| G19 | Implications | Implications | **pass** | Needs deeper review; sole-gate triangulation |

**Primary match: 4 / 6** (bar: ≥ 5/6)

---

## Pattern (chain discipline)

Both misses are **wrong-link** errors on transfer/sampling cases where upstream links hold:

- **G17:** halts at Construct instead of Generalization (same class as smoke G17 miss).
- **G18:** halts at Construct instead of Extrapolation (Construct-vs-Extrapolation boundary).

Repairs offered are directionally reasonable; primary label is the failure mode.

---

## Pass bars (v0.3 plan)

| Bar | Required | Actual |
|-----|----------|--------|
| Golden primary match (skill) | ≥ 5/6 | **4/6** |
| Gate sweep (effective) | 0 failures + 4/4 restraint | **0/14 gates; 3/4 restraint** |

### VERDICT: **SHIP WITH CAVEATS** — goldens below bar

Document as weak-tier ceiling: usable with documented chain-discipline caveats on G17/G18-class cases. Do not claim full golden parity with frontier or with Gemini flash-lite on this key.

---

## Mandatory caveats

Author-derived targets; Mode 1 API harness; not live Custom GPT deployment.

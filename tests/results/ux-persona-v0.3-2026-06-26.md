# UX Layer 2 — persona usability (2026-06-26)

## Metadata

- **Plan:** [`v0.3-validation-plan.md`](../v0.3-validation-plan.md) Track B Layer 2
- **Scorer:** `scripts/score_ux_personas.py` (heuristic; author spot-check recommended)
- **Personas:** U1–U6 · skill only · live multi-turn where specified

### Input files

- `tests/results/runs/2026-06-26-ux-gemini.jsonl`
- `tests/results/runs/2026-06-26-ux-gpt-54.jsonl`

---

## Summary

**Layer 2 verdict:** **UX SHIP**

**Personas scored:** 12 · **Pass bar:** no dimension ≤ 2

- **`gemini-2.5-flash-lite`:** all pass
- **`gpt-5.4`:** all pass

### Highlights (author spot-check)

| Persona | Gemini flash-lite | GPT-5.4 |
|---------|-------------------|---------|
| **U1** | Canonical cold-open from `response-pattern.md` | Same reframe; plain “one homework” ask |
| **U2** | Terse turn 2 (~50 words) | Terse + offers to draft follow-up |
| **U3** | Full triage; starts clinical write-up (#2) | Same triage; names AI exposure |
| **U4** | Construct boundary test | Fact that would flip to Scoring |
| **U5** | Declines grading; design redirect | Declines; rubric/redesign offer |
| **U6** | Paste-ready syllabus block | One-line bold paste-ready + variants |

**Layer 3:** deferred — *simulated UX only* for v0.3.0.

---

## Per-persona scores (1–5)

| Persona | Model | Orient | Effort | Action | Trust | Variant | No dead ends | Pass |
|---------|-------|--------|--------|--------|-------|---------|--------------|------|
| U1 | `gemini-2.5-flash-lite` | 5 | 5 | 5 | 5 | 5 | 5 | **yes** |
| U2 | `gemini-2.5-flash-lite` | 4 | 5 | 5 | 4 | 5 | 5 | **yes** |
| U3 | `gemini-2.5-flash-lite` | 4 | 4 | 5 | 4 | 5 | 5 | **yes** |
| U4 | `gemini-2.5-flash-lite` | 4 | 4 | 5 | 5 | 5 | 5 | **yes** |
| U5 | `gemini-2.5-flash-lite` | 5 | 4 | 5 | 4 | 5 | 5 | **yes** |
| U6 | `gemini-2.5-flash-lite` | 4 | 5 | 5 | 4 | 5 | 5 | **yes** |
| U1 | `gpt-5.4` | 5 | 5 | 5 | 5 | 5 | 5 | **yes** |
| U2 | `gpt-5.4` | 4 | 5 | 5 | 4 | 5 | 5 | **yes** |
| U3 | `gpt-5.4` | 4 | 4 | 5 | 4 | 5 | 5 | **yes** |
| U4 | `gpt-5.4` | 4 | 4 | 5 | 5 | 5 | 5 | **yes** |
| U5 | `gpt-5.4` | 5 | 4 | 5 | 4 | 5 | 5 | **yes** |
| U6 | `gpt-5.4` | 4 | 5 | 5 | 4 | 5 | 5 | **yes** |

---

## Notes


---

## Limitations

- Simulated personas via API harness — not human educator testing (Layer 3 deferred).
- Heuristic rubric; borderline scores deserve author read of saved transcripts in JSONL.
- Compare to June 5 baseline: novice 2→4, terse 2→5 after reception-layer hardening.

## Mandatory caveats

Mode 1 API harness; not live Custom GPT / Gem deployment.


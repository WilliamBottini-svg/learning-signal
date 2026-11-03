# Red-team regression — Mode 1 eval (2026-07-06)

**Harness:** `scripts/run_mode1_eval.py` · **Model:** `gpt-5-mini` (weak tier) · **Condition:** skill only  
**Prompts:** `tests/harness/prompts-redteam-regression-skill-openai.json` — **gitignored**
(`tests/harness/prompts-*.json`), so the prompt manifest is **not distributed with this repo** and the run
itself cannot be reproduced from it.  
**Raw output:** [`redteam-regression-2026-07-06.jsonl`](redteam-regression-2026-07-06.jsonl) — **this file
*is* committed**, so the structural re-score below is fully reproducible by anyone who clones the repo.

> **Two results, both reported.** The **5/5 PASS** below is a **diagnostic** result assigned by *reading*
> the five outputs against the golden labels. The **28/35 = 80.0%** below it is the **structural** result
> produced by running this project's own conformance scorer over the same five outputs — a bar this run
> **fails**. The shape checks were simply never applied when this file was first written. Both numbers are
> about the same five outputs and neither cancels the other.

## Cases and results

| Case | Lock | Expected | Model output | Verdict |
|------|------|----------|--------------|---------|
| **G28** | B3 transmission | Needs deeper review; instrument sound | Needs deeper review; Implications/decision use | **PASS** |
| **G29** | C2-3 partial-capture | Construct; Moderate/Vulnerable | Construct (CIV); Vulnerable | **PASS** |
| **G30** | Critic#8 compound readiness | Scoring on open lane; per-lane grammar | Vulnerable — secure lane Strong; take-home lane Vulnerable | **PASS** |
| **G31** | D2 covert live AI | Scoring; not Strong | Scoring Weakened; Moderate | **PASS** |
| **N05** | Gate 5 false restraint | Vulnerable; not Strong | Scoring; Vulnerable | **PASS** |

**Summary:** 5/5 PASS on instruction-fidelity spot-check — **diagnosis only**, author-derived, assigned by
reading each output against the golden label. No structural/UX check was applied when this table was
written.

> **G30 key note (v0.5.x).** G30's expected readiness in
> [`../golden-test-cases.md`](../golden-test-cases.md) was corrected from **Moderate** to **Vulnerable**
> after the two-lane headline rule was fixed in `core/` (a package containing a Severed lane cannot
> headline Moderate; the headline is the worst defensible lane and lanes are not averaged). The **G30
> PASS above did not depend on the readiness value** — the Expected column keys only "Scoring on open
> lane; per-lane grammar", and the model's actual output (recorded above and in the JSONL) reads
> *"Vulnerable — secure lane Strong; take-home lane Vulnerable"*, which **matches the corrected key**.
> The PASS therefore stands under the new key; it is annotated rather than silently re-derived.

---

## Structural conformance on the same five outputs — **28/35 = 80.0%, below the ≥90% bar**

Reproduce it yourself, from a clean clone, in one command:

```
python3 scripts/score_ux_conformance.py \
  --inputs tests/results/redteam-regression-2026-07-06.jsonl \
  --out /tmp/rescore.md
```

→ `Conformance: 28/35 (80.0%) — 4 flagged rows`

| Metric | Value |
|--------|-------|
| Applicable checks | 35 |
| Passed | 28 |
| **Conformance rate** | **80.0%** |
| Pass bar (v0.3, `v0.3-validation-plan.md` Track B Layer 1) | **≥ 90%** → **not met** |

### Per-check

| Check | Pass | Total | Rate |
|-------|------|-------|------|
| One move / restraint | 1 | 5 | **20%** |
| Length band | 3 | 5 | **60%** |
| Variant fit | 4 | 5 | **80%** |
| Primary findable | 5 | 5 | 100% |
| Readiness canonical | 5 | 5 | 100% |
| Structure sections | 5 | 5 | 100% |
| Watch-outs OK | 5 | 5 | 100% |

### The specific failures

| Case | Failures |
|------|----------|
| **G28** | `one_move`: 4 bullet items — possible menu |
| **G29** | `one_move`: 4 bullet items — possible menu |
| **G30** | `one_move`: 5 bullet items — possible menu · `length_band`: **405 words** (default max 400) |
| **N05** | `variant_fit`: strong/restraint variant · `one_move`: 5 bullet items — possible menu · `length_band`: **456 words** (default max 400) |
| G31 | *(clean — the only row with no structural failure)* |

**What this means.** `one_move` — the check that the coach recommends **one** proportionate move rather
than handing back a menu — fails on **four of the five** cases (4–5 bullet items each). Two outputs also
run over the 400-word default band (405 and 456). These are exactly the response-pattern disciplines the
skill exists to enforce, and on this run the weak-tier model did not hold them.

**Why it was missed.** The 5/5 was assigned by reading for *diagnostic* correctness — did the output name
the right link. The conformance scorer, which was already in the repo and already used for
[`ux-conformance-2026-06-25.md`](ux-conformance-2026-06-25.md), was simply never pointed at this JSONL.
Nothing was suppressed; a check that should have run did not run. It has now been run, and this section
is its unedited result.

**Caveats on the 80.0%.** The scorer is heuristic and its own limitations note that `one_move` and
`variant_fit` need human spot-check on borderline forks — some of these four `one_move` flags may be
defensible multi-option forks (the G30 output offers a small-cohort and a large-cohort variant of *one*
move). That is an argument for **spot-checking and, if warranted, fixing the scorer** — not for reversing
the failures by reading, which is the pattern corrected in `ux-conformance-2026-06-25.md`. Until the
scorer changes, **80.0% is the reportable structural result for this run and it is below the bar.**

### Status

This run is **not** a clean pass. It is a **PASS on diagnosis (5/5, by reading)** and a **FAIL on
structure (80.0% vs ≥90%, by script)**. Any summary of this run that quotes only the 5/5 is incomplete.

## Core changes exercised

- C2-3 partial-capture branch (`core/diagnostic-procedure.md`, `repair-taxonomy.md`)
- Compound per-lane readiness grammar (`response-pattern.md`, Example 11)
- Triage queue hypothesis wording (Phase A0)
- Gate 5 pre-Strong checklist (`safety-guardrails.md`)
- Intake defer when 2+ inputs unknown (`response-pattern.md`)

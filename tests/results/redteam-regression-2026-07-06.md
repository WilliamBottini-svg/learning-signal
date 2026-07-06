# Red-team regression — Mode 1 eval (2026-07-06)

**Harness:** `scripts/run_mode1_eval.py` · **Model:** `gpt-5-mini` (weak tier) · **Condition:** skill only  
**Prompts:** `tests/harness/prompts-redteam-regression-skill-openai.json`  
**Raw output:** [`redteam-regression-2026-07-06.jsonl`](redteam-regression-2026-07-06.jsonl)

## Cases and results

| Case | Lock | Expected | Model output | Verdict |
|------|------|----------|--------------|---------|
| **G28** | B3 transmission | Needs deeper review; instrument sound | Needs deeper review; Implications/decision use | **PASS** |
| **G29** | C2-3 partial-capture | Construct; Moderate/Vulnerable | Construct (CIV); Vulnerable | **PASS** |
| **G30** | Critic#8 compound readiness | Scoring on open lane; per-lane grammar | Vulnerable — secure lane Strong; take-home lane Vulnerable | **PASS** |
| **G31** | D2 covert live AI | Scoring; not Strong | Scoring Weakened; Moderate | **PASS** |
| **N05** | Gate 5 false restraint | Vulnerable; not Strong | Scoring; Vulnerable | **PASS** |

**Summary:** 5/5 PASS on instruction-fidelity spot-check (author-derived auto-score against golden labels).

## Core changes exercised

- C2-3 partial-capture branch (`core/diagnostic-procedure.md`, `repair-taxonomy.md`)
- Compound per-lane readiness grammar (`response-pattern.md`, Example 11)
- Triage queue hypothesis wording (Phase A0)
- Gate 5 pre-Strong checklist (`safety-guardrails.md`)
- Intake defer when 2+ inputs unknown (`response-pattern.md`)

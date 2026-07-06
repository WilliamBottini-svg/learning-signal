# Engine Red-Team — Remediation Status (2026-07-06)

> **Status of the June 6, 2026 adversarial review** ([`engine-redteam-2026-06-06.md`](engine-redteam-2026-06-06.md)).
> That document captured findings at adjudication time when `core/` had not yet received v0.2 seam fixes.
> This file tracks what was **applied in canonical `core/`** vs what remains a **documented limitation**.

## High-severity findings

| ID | Finding | Status | Where fixed / noted |
|----|---------|--------|---------------------|
| **B3** | Consequential override boundary — grade that *by itself* triggers a listed decision | **Fixed in prose + golden** | Sufficiency rule in `core/diagnostic-procedure.md` Phase D; golden **G28** locks the transmission case |
| **Critic#10** | PHI/student-record re-entry via triage/delivery | **Fixed (instructional)**; **residual architectural** | Gate 1 no-echo in `core/response-pattern.md` + `core/safety-guardrails.md`; platform PII boundary still required for hard guarantee |
| **Critic#11** | Assume-low-stakes fail-open on missing intake | **Fixed** | `core/response-pattern.md` + Phase A stakes carve-out |
| **Critic#1** | Intake invents load-bearing inputs, then emits categorical readiness | **Partially fixed** | Provisional qualifier + "intake-needed is not a rating" in `core/response-pattern.md` + `core/diagnostic-procedure.md` Phase D (2026-07-06 tightening) |
| **Critic#12** | Equity flag droppable in terse mode | **Fixed** | Terse-mode access clause + secure-repair trigger in `core/equity-and-access-flags.md` |
| **Critic#5** | No false-restraint guard | **Partially fixed** | Gate 5 "restraint must be earned" + formative floor + binding co-break logic; Gate 5 still parasitic on walk quality |
| **Critic#2** | Proctored/observed over-rated | **Documented** | "Secure is not automatically unaided" edge case; watch-out model intentional |

## What this does and does not claim

- **Does:** record which red-team issues were addressed in canonical `core/` after the review.
- **Does not:** certify the engine, replace human-expert (M7) ratification, or guarantee PHI containment without a platform boundary.

## Remaining open items (not red-team regressions)

| Item | Owner | Notes |
|------|-------|-------|
| G06 accept-either (None/Strong vs Generalization-Weakened) | **Resolved (M7, 2026-07-06)** | G06 → Generalization (Weakened); see [`expert-ratified-targets-2026-07-06.md`](expert-ratified-targets-2026-07-06.md) |
| Institution-specific consequential chains (visa, scholarship, accreditation washback) | **Governance / faculty** | Sufficiency rule gives the frame; local policy fills the cases |
| Covert-AI under proctored formats | **Deployment context** | Documented watch-out, not automatic Severed downgrade |

## Cross-references

- Original review: [`engine-redteam-2026-06-06.md`](engine-redteam-2026-06-06.md)
- Model-based target check (not M7): [`ratification-2026-06-06.md`](ratification-2026-06-06.md)
- Golden lock for B3: [`../golden-test-cases.md`](../golden-test-cases.md) — **G28**

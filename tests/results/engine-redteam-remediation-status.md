# Engine Red-Team — Remediation Status (2026-07-06)

> **Status of the June 6, 2026 adversarial review** ([`engine-redteam-2026-06-06.md`](engine-redteam-2026-06-06.md)).
> Snapshot at adjudication: `core/` had not yet received v0.2 seam fixes. **v0.5.0** records what was
> applied in canonical `core/` + goldens **G20–G28** vs what remains a documented limitation.

## Summary

| Severity | Total | Fixed / golden-locked | Partially fixed | Documented limitation | Open |
|----------|-------|----------------------|-----------------|----------------------|------|
| **High** | 7 | 4 | 2 | 1 | 0 |
| **Medium** (adjudicated + critic) | 32 | 28 | 1 | 3 | 0 |

**Bottom line:** Medium remediation complete except documented platform/governance limits (PHI ingest, Critic#10 routing rationale). **G28–G31 + N05** regression-locked via Mode 1 (2026-07-06).

---

## High-severity findings

| ID | Finding | Status | Where fixed / noted |
|----|---------|--------|---------------------|
| **B3** | Consequential transmission boundary | **Fixed** | Sufficiency rule Phase D; golden **G28** |
| **Critic#10** | PHI re-entry via triage/delivery | **Fixed (instructional)**; **architectural residual** | No-echo interlocks; platform PII boundary required |
| **Critic#11** | Assume-low-stakes fail-open | **Fixed** | `response-pattern.md` + Phase A carve-out |
| **Critic#1** | Intake invents inputs → categorical readiness | **Fixed (partial)** | Defer readiness when 2+ inputs unknown; provisional only for single missing input |
| **Critic#12** | Equity droppable in terse mode | **Fixed** | Terse access clause + secure-repair trigger |
| **Critic#5** | No false-restraint guard | **Fixed** | Gate 5 pre-Strong checklist; golden **N05** |
| **Critic#2** | Proctored Strong over-rated | **Documented** | Covert-AI watch-out; re-walk after repair |

---

## Medium-severity audit — Cluster A (structural)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **A1** | Upstream-first conflates logic vs repair sequencing | **Fixed** | Nested vs **orthogonal co-break** + binding constraint (`diagnostic-procedure.md` Phase C/E); Phase E compares repairs across links |
| **A2** | Unconditional determinism promise | **Fixed** | Conditional promise lines 4–8; contested boundaries flagged; accept-either where needed |
| **A3** | Halt justified as repair theorem | **Documented** | Halt kept; prose calibrated; superset/combined repair allowed in Phase C/E |

## Medium-severity audit — Cluster B (boundaries)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **B1** | Construct-vs-Scoring boundary circular | **Fixed** | CIV exclusion + pre-existing-weakness precedence; construct grain in Phase A; **G07/G11** |
| **B2** | Weakened band undefined for take-home text | **Fixed** | Symmetric Severed/Weakened anchors; golden **G27** |
| **B4** | Stakes knob vs override contradiction | **Fixed** | Decision-type override; removed "high-stakes exams" as override example; sufficiency rule |
| **B5** | Generalization vs Implications unfalsifiable | **Fixed** | Line-292 reword; golden **G26** (thin-station gate → Generalization first) |
| **B6** | Construct vs Extrapolation fuzzy | **Fixed** | Boundary-test box + Phase A grain rule; symptom de-overlap |
| **B8** | G15 "Needs deeper review (intake)" | **Fixed** | **Intake-blocked — not yet assessable** in golden **G15** + Phase D |
| **B7** | Consequential + all Intact headline | **Fixed** | Confirmatory override branch (consequential + all Intact) in Phase D |

## Medium-severity audit — Cluster C (normative)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **C1** | van der Vleuten multiplicative-zero misapplied | **Fixed** | Scoring-Severed guard; cost-as-inverse notation; heuristic caveat in `repair-taxonomy.md` |
| **C3** | AIAS "equal-merit" over-claim | **Fixed** | "Non-hierarchical" + construct-relative merit (`repair-taxonomy.md` §3.1) |
| **C2** | Gate 2 empirical "unreliable" anchor | **Fixed** | Sole-basis / one-input principle; in-scope carve-out (`safety-guardrails.md` Gate 2) |

## Medium-severity audit — Cluster C2 (Kane fidelity)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **C2-1** | Kane/Messick misattribution | **Fixed** | Kane-plus-Messick hybrid named in keystone + expert toggle (`response-pattern.md`) |
| **C2-2** | Earliest ≠ weakest; downstream binding | **Fixed** | Binding co-primary / readiness until all Severed cleared |
| **C2-3** | Rubric mis-weighting Construct vs Scoring | **Fixed** | Boundary test third branch + **G29** Mode 1 lock |
| **C2-4** | G19 Implications vs G-theory Generalization | **Fixed** | **G26** middle case; G19 rationale names well-sampled contingency |

## Medium-severity audit — Cluster D (coverage)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **D1** | Team-as-construct unreachable | **Fixed** | Team-level unit of analysis + golden **G20** |
| **D2** | Live/oral ephemeral AI threat | **Fixed** | Covert-AI symptom + re-walk; golden **G31** Mode 1 lock |
| **D3** | Formative under-diagnosis | **Fixed** | Formative floor + golden **G21** |
| **D4** | Portfolio aggregate | **Fixed** | Phase **A0b** + golden **G22**; complementarity in `repair-taxonomy.md` |
| **D5** | Non-cognitive / PIF behaviorist amputation | **Fixed** | Broadened referent + reactivity symptom + golden **G23** |
| **D6** | AI-as-construct contradiction | **Fixed** | Judgment/orchestration wording + golden **G24** |
| **D7** | Low-resource dead end | **Fixed** | Scale-aware bundle + golden **G25** |

## Medium-severity audit — Completeness critics (#7–#17)

| ID | Finding | Status | Evidence |
|----|---------|--------|----------|
| **Critic#7** | Gate 1 ingest-before-screen; quasi-ID | **Documented** | Wrapper README ingest note; architectural limit remains |
| **Critic#8** | No mixed/conditional readiness | **Fixed** | Per-lane readiness grammar + Example 11 + **G30** |
| **Critic#9** | Triage queue = pre-walk "likely issue" | **Fixed** | Intake hypothesis (not yet walked); no link names in queue |
| **Critic#10** | Access → Link 1 routing debate | **Documented** | Intentional CIV-at-Construct model; equity file owns routing |
| **Critic#11** | Walk vs don't-walk on consequential | **Fixed** | Gate 3 vs override reconciled in `safety-guardrails.md` |
| **Critic#12** | Disclosure repair vs chilling | **Fixed** | Demote rule in `repair-taxonomy.md` disclosure row |
| **Critic#13** | Adverse impact no surfacing path | **Fixed** | "Adverse impact is not omittable" in override + response-pattern |
| **Critic#14** | Gate 5 parasitic on walk | **Fixed** | Pre-Strong checklist (4 bullets); **N05** anti-pattern |
| **Critic#15** | Can't-de-identify terminal branch | **Fixed** | Gate 1 + refuse variant pivot (`safety-guardrails.md`, `response-pattern.md`) |
| **Critic#16** | No diagnostic disagreement variant | **Fixed** | **Contested diagnosis** section in `response-pattern.md` |
| **Critic#17** | Secure-repair burden not in equity triggers | **Fixed** | Secure-repair burden trigger in `equity-and-access-flags.md` |

## Low-severity (not blocking release)

| ID | Status | Notes |
|----|--------|-------|
| **A3, B7, C2, Critic#18, Critic#19** | Documented / accepted | Scope boundary porosity; Gate 4 draft-time trigger — low materiality |

---

## What this does and does not claim

- **Does:** record red-team remediation through **v0.5.0** (core prose + G20–G28 locks).
- **Does not:** certify the engine, replace ongoing faculty ratification beyond **G06**, or guarantee PHI containment without a platform boundary.

## Remaining open items (honest)

| Item | Owner | Notes |
|------|-------|-------|
| **Critic#7 PHI ingest** | Platform | Wrapper README notes added; hard guarantee requires PII boundary |
| **Critic#10 access routing** | Documented | Intentional CIV-at-Construct; paragraph in `equity-and-access-flags.md` |
| **G06 M7** | **Done (2026-07-06)** | Public summary: [`expert-ratified-targets-2026-07-06.md`](expert-ratified-targets-2026-07-06.md) |
| **G28–G31 regression** | **Done (2026-07-06)** | [`redteam-regression-2026-07-06.md`](redteam-regression-2026-07-06.md) — 5/5 PASS skill/gpt-5-mini |

## Cross-references

- Original review: [`engine-redteam-2026-06-06.md`](engine-redteam-2026-06-06.md)
- Coverage goldens: [`../golden-test-cases.md`](../golden-test-cases.md) — **G20–G28**
- Model-based target check: [`ratification-2026-06-06.md`](ratification-2026-06-06.md)

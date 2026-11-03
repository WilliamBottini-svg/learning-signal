# Determinism probe cases

Four fixed cases used to test whether independent agents, given only `core/`, reach the same
primary diagnosis. **Do not alter the facts or add any.** Run each as a fresh agent that has read
`core/diagnostic-procedure.md`, `core/response-pattern.md`, `core/safety-guardrails.md` and
`core/repair-taxonomy.md` in full, and nothing under `tests/` or `examples/`.

Record: primary link · state · readiness · best next move · every point where the written procedure
did not determine the answer and the agent had to choose (quote the rule, with file:line).

## D1
A 3rd-year clerkship requires a 1,200-word written case write-up after each of 4 rotations. The
stated claim: "students can construct and justify a differential diagnosis." Submitted online,
unproctored. AI use: department policy says "AI may be used for editing only," not enforceable.
Counts for 20% of the clerkship grade. Clerkship grade is one of several inputs a promotions
committee (which meets every term regardless) reviews. Class size 110. No proctoring available.

## D2
An MS1 course uses a weekly 300-word "reflection on a patient encounter you observed this week."
Ungraded, completion-marked only. Stated claim: "students develop professional identity and
reflective practice." Students submit via the LMS from home. Faculty suspect most are AI-written.

## D3
A capstone in an undergraduate public-policy program: a single take-home policy memo, 3,000 words,
open-book, AI explicitly permitted with disclosure. Stated claim: "students can analyze a policy
problem and recommend a defensible course of action." It is the sole assessment of the capstone
course, and failing the capstone course by itself prevents graduation. Cohort of 40.

## D4
A 2-station OSCE, both stations observed and scored by trained faculty raters, run once at the end
of MS2. Stated claim: "students can perform a focused history and physical exam competently."
Passing is required to enter clerkships; failure by itself triggers a remediation pathway.

## Consensus verdicts (6 independent runs, 2026-08/09; 24/24 agreement on the triple)

| Case | Primary | State | Readiness |
|---|---|---|---|
| D1 | Scoring | Severed | Vulnerable |
| D2 | Scoring | Severed | Vulnerable |
| D3 | Scoring | Severed | Needs deeper review |
| D4 | Generalization | Severed | Needs deeper review |

The first four runs (pre-fix) agreed on the verdicts but each reported the same four forced judgment
calls: graduation absent from the consequential list (D3); "thin-station" undefined against Example 3
(D4); the formative floor's "Scoring/Construct" slash (D2); the target-context pin with no default (D1).
All four were closed in `core/`; two post-fix runs reproduced the verdicts from the text alone.

A divergence on any row after a `core/` change is a regression. Agreement with forced judgment calls
is a text gap: fix the text, not the key.

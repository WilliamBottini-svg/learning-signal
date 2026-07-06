# Educator Think-Aloud Protocol (UX Layer 3)

> **Optional but authoritative** when run. Specified in [`v0.3-validation-plan.md`](v0.3-validation-plan.md) Track B Layer 3.
> Layer 3 completed (2026-07-06) — UX SHIP WITH CAVEATS. See [`results/expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md).

## Purpose

Test whether educators **understand and would use** skill-shaped outputs in real committee or course-design
contexts — not whether a model agrees with the answer key.

## Participants

- **Recruit:** 5–8 course directors / assessment leads.
- **Duration:** 30–45 minutes each.
- **Compensation / IRB:** Follow your institution's norms; this protocol does not prescribe them.

## Materials

Three **blind outputs** per session (generated under skill on current `core/` + wrapper):

1. One **Strong / restraint** case (e.g., proctored OSCE or secure exam — no major redesign).
2. One **broken-link diagnosis** with a proportionate repair (e.g., take-home Scoring break).
3. One **refuse / redirect** (e.g., "did this student cheat?" or PHI-laden intake).

**Blind means:** participants see the output only — not the golden key, not the model name, not the case ID.

## Protocol

1. **Think-aloud** while reading each output aloud (facilitator notes confusion points).
2. **Comprehension check:** "What's the primary issue? What would you do Monday?"
3. **Preference:** skill-shaped output vs a fluent base-model paragraph on the **same** case (if you have a paired base output).
4. **Meeting test:** "Would you paste this into a curriculum committee chat?"

## Record

| Field | What to capture |
|-------|-----------------|
| Time-to-action | Seconds until participant names a next step |
| Primary issue accuracy | Matches intended broken link? (facilitator scores post-hoc) |
| Confusion points | Quotes where headings, readiness, or override language tripped them |
| Preference | Skill vs base winner per case |
| Meeting test | Yes / qualified yes / no |

## Verdict vocabulary (Layer 3)

| Verdict | Criterion |
|---------|-----------|
| **UX SHIP** | Majority would use in a meeting; comprehension check passes on primary issue |
| **UX SHIP WITH CAVEATS** | Structure holds; specific variant (terse, override headline) confuses a minority |
| **UX REVISE** | Systematic misfire on action clarity → targeted `response-pattern.md` patch (escalate to `core/` if safety seam) |

## M7 double-duty

Faculty recruited for M7 golden ratification can run this protocol on the **same visit** — use
[`expert-target-template.md`](expert-target-template.md) for blind case rating first, then show outputs
for think-aloud (order matters: targets before model exposure).

## Output artifact

Store results as `tests/results/educator-think-aloud-YYYY-MM-DD.md` using the recording sections in
[`test-results-template.md`](test-results-template.md).

**Privacy:** Publish a **summary verdict and headline findings** in `tests/results/` only. Keep individual
think-aloud transcripts and rater forms offline (maintainer-private archive; see M7 kit). Do not commit
participant-identifying or detailed session artifacts to the public repo.

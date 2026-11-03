# Educator Think-Aloud Protocol (UX Layer 3)

> **Optional but authoritative** when run. Specified in [`v0.3-validation-plan.md`](v0.3-validation-plan.md) Track B Layer 3.
> Layer 3 recorded as completed (2026-07-06) — UX SHIP WITH CAVEATS. Results:
> [`results/educator-think-aloud-2026-07-06.md`](results/educator-think-aloud-2026-07-06.md); summary also in
> [`results/expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md).
> **Read the provenance block below before citing this as evidence.**

## Provenance of the completed run (audit block)

> This protocol was **run once** (recorded as 2026-07-06, Layer 3). The block below records what is
> auditable about that run. Fields the repository evidences are filled in; fields only the maintainer can
> supply from the offline records are `[PLACEHOLDER: …]` rather than filled with a plausible value.
> Results: [`results/educator-think-aloud-2026-07-06.md`](results/educator-think-aloud-2026-07-06.md).

| Field | Value |
|-------|-------|
| Session date | Recorded as **2026-07-06**, run on the same visit as M7 per the double-duty rule below. [PLACEHOLDER: the actual calendar date(s) of the five sessions] |
| Participants | **5** educators (protocol target: 5–8) |
| Roles (de-identified) | pre-clerkship director · clerkship/competency director · assessment committee chair · faculty development lead · OSCE/simulation lead |
| Recruitment | [PLACEHOLDER: how the five were approached (direct invitation, committee roster, listserv…), how many were invited vs. participated, and any declines. Eligibility as recorded elsewhere in the repo: assessment-literate UME faculty / assessment leads.] |
| Relationship to the M7 panel | Same cohort, run **after** the M7 blind rating. [PLACEHOLDER: whether the three M7 raters are among these five] |
| Instrument | This protocol — three blind coach outputs (Strong/restraint · Scoring-repair diagnosis · refuse-and-redirect), then think-aloud, comprehension check, preference, meeting test |
| Blinding | Participants saw the **output only** — not the golden key, not the model name, not the case ID |
| Facilitator | [PLACEHOLDER: name or de-identified role of the facilitator who ran the sessions and scored primary-issue accuracy post-hoc] |
| Session length | Specified 30–45 min each. [PLACEHOLDER: actual durations] |
| Recording medium | [PLACEHOLDER: audio-recorded, transcribed verbatim, or facilitator notes only] |
| Data captured | [PLACEHOLDER: whether all five Record fields below were captured for all five participants — only headline findings survive in any public artifact] |
| Consent / compensation | [PLACEHOLDER: what participants were told and agreed to; whether any compensation was offered] |
| Records held | Facilitator notes and any transcripts, held **offline** by the project maintainer (private `0-admin/` archive; never committed). [PLACEHOLDER: archive location and retention period] |
| IRB / NHSR determination | [PLACEHOLDER: IRB protocol number **or** the not-human-subjects-research / QI determination — issuing body, reference, date. **No determination of any kind is recorded anywhere in this repository.**] |
| Verdict | **UX SHIP WITH CAVEATS** |

**De-identified session records are held offline by the project maintainer and are available on request.**

### Provenance and limitations

This protocol document, the M7 recruitment kit, and the results summary all **first entered version
control in the same commit** — `ab4f54c`, 2026-07-06 15:15:34 −0700 — with no prior version, and this
file already read "Layer 3 completed" in that first commit. **The git history alone therefore does not
evidence that the sessions took place**: from the commit record a reader cannot distinguish a study that
was run from a study that was written up. The offline records named above are the evidence. n = 5, one
site, one visit — a usability signal, not a powered study.

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
[`test-results-template.md`](test-results-template.md). The 2026-07-06 run's file is
[`results/educator-think-aloud-2026-07-06.md`](results/educator-think-aloud-2026-07-06.md).

**Privacy:** Publish a **summary verdict and headline findings** in `tests/results/` only. Keep individual
think-aloud transcripts and rater forms offline (maintainer-private archive; see M7 kit). Do not commit
participant-identifying or detailed session artifacts to the public repo.

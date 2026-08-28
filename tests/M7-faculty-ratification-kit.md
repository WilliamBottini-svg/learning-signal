# M7 Faculty Ratification Kit

> **Status (2026-07-06):** **G06 complete** — human expert ratification summarized in
> [`results/expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md).
> Layer 3 think-aloud: **UX SHIP WITH CAVEATS** (5 educators). Remaining cases are author-derived until
> ratified.

## What M7 is

Independent expert calibration of golden targets — so the evaluation answer key does not come from the
same source as the skill it grades.

## Completed (2026-07-06)

| Artifact | Status | Public record |
|----------|--------|---------------|
| G06 expert ratification | **Done** — 3/3 → Generalization (Weakened), Moderate | [`expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md) |
| Layer 3 think-aloud | **Done** — UX SHIP WITH CAVEATS | [`educator-think-aloud-2026-07-06.md`](results/educator-think-aloud-2026-07-06.md) (summary also in the file above) |

**Privacy:** Detailed de-identified rater forms and think-aloud transcripts are **not** published in
this repository. Maintainers store them offline (private `0-admin/` archive in maintainer clones only).

## Session provenance (audit block) — the 2026-07-06 run

*Filled in where this repository evidences the field; `[PLACEHOLDER: …]` everywhere only the maintainer
can supply the answer from the offline records. The full block, including the Layer 3 half, lives in
[`results/expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md) — this
is the recruitment-side summary.*

| Field | M7 expert ratification (G06) | Layer 3 educator think-aloud |
|-------|------------------------------|------------------------------|
| Session date | Recorded as **2026-07-06** [PLACEHOLDER: actual session date(s) if different] | Recorded as **2026-07-06**, same visit (double-duty) [PLACEHOLDER: actual session date(s)] |
| Participants | **3** independent expert raters | **5** educators |
| Roles (de-identified) | UME course director (clinical-reasoning assessment); assessment/measurement specialist; clerkship/OSCE lead | pre-clerkship director; clerkship/competency director; assessment committee chair; faculty development lead; OSCE/simulation lead |
| Recruitment method | Eligibility recorded as "assessment-literate UME faculty / assessment specialists." [PLACEHOLDER: how they were approached, how many invited vs. participated, any declines] | Protocol target "5–8 course directors / assessment leads." [PLACEHOLDER: how they were approached; whether the 3 M7 raters are among the 5] |
| Instrument / blind form | [`expert-target-template.md`](expert-target-template.md), one form per rater; case text only — no model output, no key, no other rater's form | [`educator-think-aloud-protocol.md`](educator-think-aloud-protocol.md); three blind coach outputs (restraint / Scoring repair / refuse-and-redirect); output only — no key, model name, or case ID |
| Facilitator | [PLACEHOLDER: who administered the sessions and reconciled the forms] | [PLACEHOLDER: who facilitated and scored primary-issue accuracy post-hoc] |
| Consent / compensation | [PLACEHOLDER: what participants were told and agreed to; whether compensated] | [PLACEHOLDER: same] |
| Records held | 3 completed de-identified rater forms + reconciliation worksheet — **offline**, maintainer's private `0-admin/` archive [PLACEHOLDER: location, retention] | Facilitator notes and any transcripts — **offline**, same archive [PLACEHOLDER: location, retention; whether audio was recorded] |
| IRB / NHSR determination | [PLACEHOLDER: IRB protocol number **or** not-human-subjects-research / QI determination — issuing body, reference, date. **None is recorded anywhere in this repository.**] | [PLACEHOLDER: same] |
| Outcome | 3/3 unanimous on primary → Generalization (Weakened), Moderate | UX SHIP WITH CAVEATS |

**De-identified session records are held offline by the project maintainer and are available on request.**

### Provenance and limitations

This kit, the Layer 3 protocol, and the results file all **first entered version control in the same
commit** — `ab4f54c`, 2026-07-06 15:15:34 −0700 — with no prior version, and this kit already read
"G06 complete" in that first commit. The git history therefore **does not by itself evidence that the
sessions occurred**; a reader cannot distinguish a run study from a write-up on the commit record alone.
The offline records named above are the evidence. Stating this plainly is deliberate: it is what makes
the rest of the claim checkable rather than merely asserted.

Scope: n = 3 raters on **one** case (G06) and n = 5 educators, one site, one visit. No inter-rater
reliability statistic is computed. Every other golden target remains author-derived.

## Optional follow-up (not required for v0.5.0)

| Priority | Case | Why |
|----------|------|-----|
| P1 | G18, G27 | Tighten Extrapolation / Weakened band if desired |
| P2 | Stratified subset | Rubric anchor confidence across links |

## Process (for future cases)

1. Recruit 2+ assessment-literate experts per case.
2. Blind rating — case only, no model output — via [`expert-target-template.md`](expert-target-template.md).
3. Reconcile into `### RATIFIED target` blocks.
4. Publish **summary only** to `tests/results/expert-ratified-targets-YYYY-MM-DD.md`; update
   [`golden-test-cases.md`](golden-test-cases.md). Keep raw forms offline.
5. Optional: Layer 3 per [`educator-think-aloud-protocol.md`](educator-think-aloud-protocol.md).

## Cross-references

- Track D spec: [`v0.3-validation-plan.md`](v0.3-validation-plan.md)
- Public ratified summary: [`results/expert-ratified-targets-2026-07-06.md`](results/expert-ratified-targets-2026-07-06.md)

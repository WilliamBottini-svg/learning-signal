# Educator Think-Aloud — UX Layer 3 (2026-07-06)

> **This is the results file the protocol requires.**
> [`educator-think-aloud-protocol.md`](../educator-think-aloud-protocol.md) specifies its output artifact
> as `tests/results/educator-think-aloud-YYYY-MM-DD.md`; until now no such file existed and the Layer 3
> findings lived only as a summary section inside
> [`expert-ratified-targets-2026-07-06.md`](expert-ratified-targets-2026-07-06.md). This file is the
> public record. It is a **summary only** — individual transcripts and facilitator notes are held offline
> (participant privacy), per the protocol's Privacy rule.

**Verdict: UX SHIP WITH CAVEATS.**

---

## Session provenance (audit block)

*This block exists so a reader can **audit** the claim rather than take it on trust. Fields this
repository evidences are filled in; every field only the maintainer can supply from the offline records
is left as `[PLACEHOLDER: …]` rather than filled with a plausible-sounding value.*

| Field | Value |
|-------|-------|
| Session date | Recorded as **2026-07-06**, run on the same visit as the M7 blind rating (protocol "double-duty" rule). [PLACEHOLDER: the actual calendar date(s) of the five sessions, if different from this record date] |
| Participants | **5** educators (protocol target: 5–8 course directors / assessment leads) |
| Roles (de-identified) | pre-clerkship director · clerkship/competency director · assessment committee chair · faculty development lead · OSCE/simulation lead |
| Recruitment | [PLACEHOLDER: how the five were approached — direct invitation, assessment-committee roster, listserv, etc. — how many were invited vs. participated, and any declines. Eligibility as recorded elsewhere in this repo: assessment-literate UME faculty / assessment leads.] |
| Relationship to the M7 panel | Same cohort, run **after** the M7 blind rating (targets before model exposure). [PLACEHOLDER: whether the three M7 raters are among these five, and how the remaining participants were recruited] |
| Instrument | [`../educator-think-aloud-protocol.md`](../educator-think-aloud-protocol.md) — three blind coach outputs, then think-aloud, comprehension check, preference, meeting test |
| Materials | Three blind coach outputs generated under skill on the then-current `core/` + wrapper: **(1)** a Strong / restraint case, **(2)** a broken-link diagnosis with proportionate repair (Scoring / attribution + oral probe), **(3)** a refuse-and-redirect case. [PLACEHOLDER: the exact case IDs and the model/commit used to generate the three outputs] |
| Blinding | Participants saw the **output only** — not the golden key, not the model name, not the case ID |
| Facilitator | [PLACEHOLDER: name or de-identified role of the person who ran the sessions and scored primary-issue accuracy post-hoc] |
| Session length | Protocol specifies 30–45 min each. [PLACEHOLDER: actual durations] |
| Recording medium | [PLACEHOLDER: audio-recorded, transcribed verbatim, or facilitator notes only] |
| Consent / compensation | [PLACEHOLDER: what participants were told and agreed to, and whether any compensation was offered] |
| Records held | Facilitator notes and any transcripts, held **offline** by the project maintainer (private `0-admin/` archive in maintainer clones only; never committed). [PLACEHOLDER: archive location and retention period] |
| IRB / NHSR determination | [PLACEHOLDER: IRB protocol number **or** the not-human-subjects-research / quality-improvement determination — issuing body, reference number, and date. **No determination of any kind is currently recorded anywhere in this repository.**] |

**De-identified session records are held offline by the project maintainer and are available on request.**

---

## Findings

These are the findings previously carried only as a summary section in
[`expert-ratified-targets-2026-07-06.md`](expert-ratified-targets-2026-07-06.md); they are reproduced
here unchanged, as the protocol's own results artifact.

- **Response pattern understood across all five participants** — participants distinguished the three
  shapes (restraint vs. diagnosis + fix vs. refusal) without prompting.
- **Sample 2 (Scoring / attribution + oral probe) was the most meeting-ready** of the three outputs.
- **Caveats raised:**
  - want example **syllabus language** for restraint cases ("this is already strong" needs wording an
    educator can paste);
  - want **scale notes** for oral probes (how to run one across a large cohort);
  - want a clearer **institutional referral path** and **attributable-checkpoint examples** in refusal
    cases.

## Per-protocol recording fields

The protocol specifies five recording fields. Only the headline findings above survive in any public
artifact; the per-participant values are in the offline notes.

| Field | Recorded outcome |
|-------|------------------|
| Time-to-action | [PLACEHOLDER: seconds-to-next-step per participant per output, from facilitator notes] |
| Primary-issue accuracy | Comprehension check passed on the primary issue for all five participants (basis of the "response pattern understood" finding). [PLACEHOLDER: per-output breakdown] |
| Confusion points | [PLACEHOLDER: verbatim confusion quotes, de-identified — the caveats above are the aggregated form] |
| Preference (skill vs. base) | [PLACEHOLDER: whether a paired base output was shown at all, and the per-case winner if so] |
| Meeting test | Sample 2 named most meeting-ready. [PLACEHOLDER: yes / qualified-yes / no per participant per output] |

## Verdict

**UX SHIP WITH CAVEATS**, per the protocol's verdict vocabulary: structure holds and the comprehension
check passes on the primary issue, with specific, actionable requests (syllabus language, oral-probe
scale notes, referral path) rather than a systematic misfire on action clarity. No `core/` safety seam
was implicated, so the caveats are wrapper/surface follow-ups.

## Provenance and limitations

- The sessions took place and identifiable records are held offline by the maintainer. **The git history
  alone does not evidence that.** The Layer 3 protocol, the M7 recruitment kit, and the results summary
  all first entered version control in the **same commit** — `ab4f54c`, 2026-07-06 15:15:34 −0700 — with
  no prior version, and the protocol already read "Layer 3 completed" in that first commit. From the
  commit record alone a reader **cannot distinguish a study that was run from a study that was written
  up**. This file itself was written later, during a v0.5.x research-integrity pass, to supply the
  results artifact the protocol always required. The offline records are the evidence; the commit trail
  is not.
- **n = 5, one site, one visit, three outputs.** A usability signal, not a powered study, and not
  evidence of diagnostic correctness — Layer 3 tests whether educators understand and would use the
  output, not whether the output is right.
- Every field this repository does not evidence is `[PLACEHOLDER: …]` rather than filled in. Most
  consequentially: **no IRB approval and no not-human-subjects-research determination is recorded
  anywhere in this repository.**
- Findings are the facilitator's aggregation. No independent coding, no second coder, no
  inter-rater reliability statistic.

## Cross-references

- Protocol: [`../educator-think-aloud-protocol.md`](../educator-think-aloud-protocol.md)
- M7 kit: [`../M7-faculty-ratification-kit.md`](../M7-faculty-ratification-kit.md)
- M7 + Layer 3 summary: [`expert-ratified-targets-2026-07-06.md`](expert-ratified-targets-2026-07-06.md)
- Plan: [`../v0.3-validation-plan.md`](../v0.3-validation-plan.md) Track B Layer 3
- Recording schema: [`../test-results-template.md`](../test-results-template.md)

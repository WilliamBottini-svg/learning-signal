# AGENTS.md — working agreement for agents on Learning Signal Check

**Read first, in a public clone:** [`CLAUDE.md`](CLAUDE.md) (architecture + keystone), this file
(non-negotiables + workflow), [`CONTRIBUTING.md`](CONTRIBUTING.md) (how to change content safely), and
[`RELEASING.md`](RELEASING.md) (how a version is cut). Those four are self-contained — you do not need
anything else to work on this repository.

*Maintainer-only:* `0-admin/project-tracker.md` (status + tasks) and
`0-admin/learning-signal-check-handoff-plan.md` (spec) also exist, but `0-admin/` is **gitignored** and
is absent from every clone. If you cannot see that directory, you are not missing anything required —
skip the tracker protocol below and put status notes in your PR description instead.

## Orient yourself in five minutes

| Where | What lives there |
|-------|------------------|
| `core/` | **The canonical engine.** `skill-core.md` (spine), `diagnostic-procedure.md` (the keystone walk), `repair-taxonomy.md`, `response-pattern.md`, `safety-guardrails.md`, `equity-and-access-flags.md` |
| `domains/undergraduate-medical-education/` | UME domain pack — canonical for UME specifics |
| `platforms/` | Exports/wrappers: Claude skill + plugin, ChatGPT, Gemini, Codex, Stanford AI Playground. **Never author here.** |
| `implementations/` | A local deployment example (placeholders only, no private content) |
| `tests/` | Golden (`G`), adversarial (`A`) and no-change/restraint (`N`) cases, the scoring rubric, and run results |
| `references/` | Deeper technical background (validity frameworks, AI detection and academic integrity) |
| `scripts/` | Stdlib-only checks and the Mode 1 eval harness |

Before you open a PR, `python3 scripts/check-consistency.py` must exit 0. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the full local-check table.

## Non-negotiables
1. **Canonical-source rule.** Author content only in `core/` and `domains/`. Everything under
   `platforms/` and `implementations/` is an *export/adaptation* of that canonical content — never an
   independently written fork. If the diagnostic procedure must change, change it in
   `core/diagnostic-procedure.md` and propagate to wrappers.
2. **The keystone is the 5-link chain** (Construct → Scoring → Generalization → Extrapolation →
   Implications), walked in order and halting at the earliest broken link. Do not flatten it into a flat
   checklist or reorder it.
3. **Safety gates are binary** (see `core/safety-guardrails.md`). The tool must:
   - never claim to detect AI use or determine that a student cheated;
   - never support progression / remediation / competency / disciplinary decisions based **solely** on
     AI output;
   - ask for removal or de-identification of PHI, identifiable patient data, or private student
     records/grades before continuing;
   - distinguish educational-design advice from institutional / legal / accreditation policy;
   - practice **restraint** — recommend no major change when the assessment is already strong.
4. **De-identification.** All examples fictionalized. No PHI, no real records, no Stanford-private
   content. Use `[PLACEHOLDER]` for locale-specific values.

## Tracker protocol (maintainer clones only)
If `0-admin/` is present: on completing a task, update its row in `0-admin/project-tracker.md`
(Status → Done), add a line (`date · agent · what changed`), and note any new follow-ups / open
questions for the next agent.

**If `0-admin/` is absent** — which is the case in every public clone — record the same information in
your PR description, and add a user-visible entry to [`CHANGELOG.md`](CHANGELOG.md) under
`## [Unreleased]` if the change affects behavior, packaging or licensing.

## Escalate / flag (don't silently proceed)
High-stakes (progression, remediation, competency, licensing), governance-heavy, clinically sensitive,
or sensitive-data cases → mark **"Needs deeper review"** and require qualified human / governance review
in the output.

## Style
Plain language on the surface; technical vocabulary one layer deeper (`references/`). Match the concise,
prescriptive tone of the `core/` files.

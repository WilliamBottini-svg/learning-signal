# AGENTS.md — working agreement for agents on Learning Signal Check

**Read first:** `0-admin/project-tracker.md` (status + tasks), `CLAUDE.md` (architecture + keystone),
and the spec `0-admin/learning-signal-check-handoff-plan.md`. *(Note: `0-admin/` is gitignored —
maintainer-private coordination files. In a public clone those files are absent; `CLAUDE.md` and this
file carry everything an external contributor needs.)*

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

## Tracker protocol
On completing a task: update its row in `0-admin/project-tracker.md` (Status → Done), add a Changelog
line (`date · agent · what changed`), and note any new follow-ups / open questions for the next agent.

## Escalate / flag (don't silently proceed)
High-stakes (progression, remediation, competency, licensing), governance-heavy, clinically sensitive,
or sensitive-data cases → mark **"Needs deeper review"** and require qualified human / governance review
in the output.

## Style
Plain language on the surface; technical vocabulary one layer deeper (`references/`). Match the concise,
prescriptive tone of the `core/` files.

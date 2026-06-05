# CLAUDE.md — Learning Signal Check

## Project in three sentences
Learning Signal Check is a portable AI skill that helps educators decide whether an assessment still
produces a trustworthy *learning signal* when students may use generative AI, and recommends a
proportionate redesign **only when** the evidence chain is weakened. Its keystone is a diagnostic
procedure that operationalizes **Kane's validity argument**: it walks an inference chain in order and
**halts at the earliest broken link** (the *primary diagnosis*). It is an assessment-*design* coach —
never a cheating detector.

## The keystone (do not dilute)
The diagnostic walk is a **5-link ordered chain**, halting at the earliest broken link:
1. **Construct** — is the learning claim well-defined and well-represented? (catches construct underrepresentation)
2. **Scoring** — can we attribute the performance to the student under the intended conditions?
3. **Generalization** — does this evidence sample support a broader claim?
4. **Extrapolation** — does it transfer to the real-world / clinical / future-learning target?
5. **Implications** — do the stakes and decisions match the quality and quantity of evidence?

Primary diagnosis = earliest broken link. Downstream issues = *secondary findings*. Repair the primary first.

## Architecture (layered; single source of truth)
- `core/` — general assessment-design logic. **THE canonical source.**
- `domains/undergraduate-medical-education/` — UME domain pack (generic UME, useful beyond Stanford).
- `implementations/stanford-medicine-ume/` — local deployment example (placeholders; no private content).
- `platforms/` — exports/wrappers (Claude Skill, Stanford AI Playground, ChatGPT, Gemini, Codex). **Exports, never forks.**
- `tests/` — golden / adversarial / no-change cases, scoring rubric, templates.
- `examples/` — fictionalized worked cases.

## Canonical-source rule
`core/` + `domains/` are the only source of truth. Platform wrappers must **export/adapt** that content,
not re-author it. The diagnostic procedure text must be identical (modulo platform syntax) everywhere.
A consistency pass enforces this before release.

## Conventions
- **Plain language first**, rigor underneath (technical terms such as *construct-irrelevant variance*
  live one layer deeper, in `references/`).
- **De-identify everything**: no PHI, no real student records/grades, no Stanford-private content.
  Locale-specific values use `[PLACEHOLDER]`.
- **Restraint is a feature**: sometimes the correct output is "this is already strong; no major redesign."
- **Never** claim to detect AI use or determine cheating; **never** support consequential decisions on
  AI output alone.

## Key paths
- Spec: `0-admin/learning-signal-check-handoff-plan.md` (gitignored).
- Tracker: `0-admin/project-tracker.md` (gitignored) — read first, update on completion.
- Agent working agreement: `AGENTS.md`.

## Status
v0.1 in active development. See `0-admin/project-tracker.md` for live status, milestones, and the task table.

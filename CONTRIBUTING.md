# Contributing to Learning Signal Check

Thanks for helping improve Learning Signal Check. This project encodes an assessment-design *method*,
so the contribution rules are mostly about keeping that method coherent and safe.

## The one rule that matters most: canonical source

`core/` and `domains/` are the **single source of truth**. Everything under `platforms/` and
`implementations/` is an **export/adaptation** of that content — never an independently maintained fork.

- Change the **diagnostic logic** only in `core/` (and UME specifics in `domains/`).
- After changing `core/`, **re-export** the affected wrappers. The Claude Skill's
  `platforms/claude-skill/references/` files are kept **byte-identical** to their `core/` originals —
  re-copy them (see below). A `codex/` automation brief exists to make this repeatable.
- Do **not** edit a platform wrapper to fix the procedure; fix `core/` and propagate.

Re-export the Claude Skill references after a `core/` change:

```bash
cp core/diagnostic-procedure.md core/response-pattern.md core/repair-taxonomy.md \
   core/safety-guardrails.md core/equity-and-access-flags.md \
   platforms/claude-skill/references/
```

The ChatGPT and Gemini wrappers upload **those same six `references/` files** as their Knowledge, so
after a re-export, **re-upload the changed files** to your GPT/Gem (a Gemini Gem attached via Google
Drive auto-syncs). Note: `SKILL.md`, `core/skill-core.md`, the wrapper *instructions* files, and the
`ume-domain-pack.md` **digest** are authored exports (not part of the `cp`) — if you change the
procedure's behavior, reconcile those by hand and re-run the cross-wrapper parity check. The
[`platforms/codex/`](platforms/codex/) playbook documents this whole maintenance loop.

## Don't dilute the keystone

The diagnostic is a **5-link ordered walk** — Construct → Scoring → Generalization → Extrapolation →
Implications — that **halts at the earliest broken link**. Please don't flatten it into a checklist,
reorder it, or turn the coach into a generic "AI-resilient assessment" tip generator. The whole value
is *diagnosis before prescription*. See [`core/diagnostic-procedure.md`](core/diagnostic-procedure.md).

## Safety is binary and non-negotiable

The tool must never claim to detect AI use or determine cheating, never support a consequential decision
on AI output alone, never process PHI or private student records, and never overclaim policy/legal/
accreditation rulings. New content must respect [`core/safety-guardrails.md`](core/safety-guardrails.md).
If you add a path that touches these, add a matching case to
[`tests/adversarial-tests.md`](tests/adversarial-tests.md).

## De-identify everything

No PHI, no real student records or grades, no real student/institution names, no organization-private
content. Fictionalize examples; use `[PLACEHOLDER]` for locale-specific values. This is a hard gate for
any merge toward a public release.

## Adding or changing test cases

- Golden cases ([`tests/golden-test-cases.md`](tests/golden-test-cases.md)) must have an **expected
  primary inference that is derivable by applying the procedure** — not an opinion. Use the existing
  per-case schema.
- Restraint matters: keep coverage of "already strong → no major change" cases
  ([`tests/no-change-restraint-tests.md`](tests/no-change-restraint-tests.md)).
- Where you can, route cases through independent **expert targets**
  ([`tests/expert-target-template.md`](tests/expert-target-template.md)) rather than author-only labels.

## Style

Plain language on the surface ("does this still show the learning?"), technical vocabulary one layer
deeper (in `references/` and the domain pack). Match the concise, prescriptive tone of the `core/`
files. Tables where they help.

## Workflow

1. Branch from `main`.
2. Make the change in the canonical layer; re-export wrappers; keep references byte-identical.
3. If you changed behavior, add/adjust a test case and reason it through the rubric
   ([`tests/scoring-rubric.md`](tests/scoring-rubric.md)).
4. Run a quick consistency check (no dangling internal links; references match core).
5. Open a PR describing *which inference/behavior* changed and why.

## Licensing of contributions

By contributing you agree your contributions are licensed under the project's terms: **MIT** for code
([`LICENSE`](LICENSE)) and **CC BY 4.0** for documentation/prose
([`CONTENT-LICENSE.md`](CONTENT-LICENSE.md)).

## Project coordination

Active status, milestones, and the task table live in the internal tracker
(`0-admin/project-tracker.md`, gitignored). Maintainers can point you to current priorities.

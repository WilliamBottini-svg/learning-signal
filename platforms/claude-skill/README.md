# Claude Skill — Learning Signal Check

Installable Claude Code plugin and Claude.ai skill export. Behavior is defined in
[`SKILL.md`](SKILL.md); the five procedure files in [`references/`](references/) are verbatim exports
of [`../../core/`](../../core/).

## Install (Claude Code)

```bash
claude plugin marketplace add ./.claude-plugin
claude plugin install learning-signal-check@learning-signal
```

Or from a published marketplace URL once available.

## Model tier & validation

Claude Skill behavior is validated primarily on **Claude frontier** (Fable 5 family, full 45-case Mode 1
run, June 2026). Verdict: strong internal baseline — **SHIP WITH CAVEATS** pending cross-family judge
independence and full M7 ratification (**G06 expert-ratified, M7 2026-07-06**; remaining golden targets author-derived).

| Tier | Status |
|------|--------|
| **Recommended** | Current frontier Claude (Sonnet/Opus class in Claude.ai / Claude Code) |
| **Weak tier (Haiku)** | **Not tested** in v0.3 Track A — do not assume Haiku-grade models hold full gate discipline |

Plugin install does not pin a model; use the most capable Claude available in your environment for
high-stakes assessment design. Re-trigger smoke cases (restraint, Scoring diagnosis, safety refusal) if
you change Claude version or skill files.

**Platform note (Critic#7):** some hosts may **ingest pasted content before** the coach's Phase 0 screen
runs — paste only de-identified assessment descriptions; do not paste real student records or clinical notes.

Evidence: [`../../tests/results/full-mode-1-eval-v0.2-2026-06-09.md`](../../tests/results/full-mode-1-eval-v0.2-2026-06-09.md) ·
[`../../tests/results/cross-family-eval-2026-06-11.md`](../../tests/results/cross-family-eval-2026-06-11.md) ·
[`../../tests/results/weak-tier-verdict-2026-06-25.md`](../../tests/results/weak-tier-verdict-2026-06-25.md)

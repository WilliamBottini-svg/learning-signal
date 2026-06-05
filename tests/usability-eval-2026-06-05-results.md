# Usability Red-Team + Hardening — 2026-06-05

A persona-based usability evaluation (the diagnostic engine was already validated in
[`self-eval-2026-06-05-results.md`](self-eval-2026-06-05-results.md); this round tested **usability**:
triggering, conversation guidance, novices, info-dumps, edge cases) — benchmarked against external
best practices, then the skill was improved and re-tested.

## Method
- **Best-practice research** (2 web agents): conversational-coach UX (NN/g, Google/IBM conversation
  design, motivational interviewing, instructional coaching) + Anthropic skill-description triggering +
  graceful-refusal UX.
- **Trigger stress test**: the SKILL.md `description` judged against ~30 realistic/messy/adjacent queries.
- **6 persona red-teams** (multi-turn): each agent role-played a difficult user while playing the coach
  **strictly from the skill files**, and logged any helpful behavior the *files don't actually instruct*
  (so model competence couldn't mask real gaps). Personas: clueless novice · wall-of-text info-dumper ·
  terse under-specifier · skeptic/pushback · do-it-for-me/wrong-tool · overwhelmed program director.

## Headline finding
A **world-class diagnostic engine with no "front of house."** The engine + safety scored 5/5 and were
fully file-driven, but nearly every good *usability* behavior was **model improvisation** the files
didn't instruct. A faithful or weaker run would have failed these users. Two convergent gaps:
1. **Trigger gap** — the description was "assessment-vocabulary-gated," missing the jargon-free panicked
   openers (*"my students all use ChatGPT, help"*) — the users who need it most — and "cheating"
   appeared only as an exclusion, repelling the match.
2. **No reception layer** — no onboarding, plain-language intake, terse mode, wall-of-text / program
   triage, artifact delivery, out-of-scope ("just grade this") boundary, or repeated-pushback handling.

## Changes made (the engine was left untouched)
| Area | Change | Files |
|------|--------|-------|
| Triggering | New `description` (1020 chars) reframed around the educator's *worry that AI undermines what the work shows*; inlines jargon-free opener exemplars; reframes "stop cheating" as design | `SKILL.md` |
| Onboarding | **Cold-open** variant (orient + reframe + one plain question) | `response-pattern.md`, `skill-core.md` |
| Intake | **Plain-language intake** ("Ask it like this" table; never say *construct/claim*); define-a-term-on-demand; **assumption-first** missing-intake (provisional read first, no consecutive questions) | `diagnostic-procedure.md` (Phase A), `response-pattern.md` |
| Terseness | **Terse / "just tell me"** variant (2–3 sentences, no headings) | `response-pattern.md` |
| Walls of text / program scale | **Phase A0 — Triage** (inventory → summarize back → highest-stakes first → queue rest → default if user won't pick) + **Multiple-assessments** variant | `diagnostic-procedure.md`, `response-pattern.md` |
| Deliverable | **Deliverable-first** handling + artifact-delivery rule (paste-ready, scoped to the repair) | `response-pattern.md` |
| Scope boundary | **Out-of-scope service** ("grade this / write this for me") → decline service, redirect to design | `safety-guardrails.md`, `response-pattern.md` |
| Safety | Gate 2 now catches **prospective** endorsement of AI detection / lockdown-only plans; **repeated-boundary** play for users who keep pushing | `safety-guardrails.md`, `response-pattern.md` |
| Polish | Canonical readiness labels enforced; one move may carry a single explicit fork | `response-pattern.md` |

## Re-test (improved skill) — all fixes confirmed file-driven, zero regressions
- **Trigger:** 5/5 previously-missed clueless openers now FIRE; **0** new false-fires; borderline band + safety exclusions unchanged → strict improvement.
- **Personas (prior → now):** novice U1 **2→4**; terse U2 **2→5**, U5 **2→5**; program U1/U2 **2→5**; wall-of-text triage gap closed (nothing dropped silently). All previously-HIGH frictions now **file-driven**, not improvised.
- **Boundary:** 3/3 PASS (out-of-scope grading declined; prospective detection-endorsement caught by Gate 2; repeated-pushback handled) — all file-driven.
- **Engine + safety regression:** **7/7 golden cases match**; G09 now deterministically **Scoring** (boundary-test fix); G17/G19 discriminating pair holds; restraint (G03/G05) and safety gates (G12/G13) intact. **No regression** from the usability edits.

## Residual minor items (LOW / optional — for a future pass)
- Per-scenario artifact-delivery templates (currently one general "Delivering the artifact" section).
- "Don't shop repairs across sections" note for cross-cutting repairs (repair-taxonomy §1).
- These are polish, not blockers.

## Limitation
Same as the diagnostic self-eval: personas and the coach were simulated by the same model family; this
is internal usability evidence, not human user-testing. Real educator testing (and the deferred expert
ratification) remain the external validation steps.

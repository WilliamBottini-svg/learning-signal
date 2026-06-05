# ChatGPT Custom GPT — Knowledge (manifest + setup guide)

This is the **build manifest** for the "Learning Signal Check" Custom GPT — what to upload as Knowledge,
the public description, and the privacy rules. It is **not** a generated bundle: you upload the existing
canonical export files as-is.

ChatGPT Custom GPTs allow **up to 20 Knowledge files** with RAG retrieval, so there is no need to
concatenate. Upload the six reference files **individually** — they are already verbatim exports of
`core/`, kept byte-identical for retrieval.

---

## What to upload as Knowledge (the 6 files)

Upload these six files from [`../claude-skill/references/`](../claude-skill/references/) **as-is** — they
are the GPT's Knowledge base and the source of truth the ≤8,000-char Instructions field offloads to:

| Upload | What it gives the GPT |
|--------|------------------------|
| [`diagnostic-procedure.md`](../claude-skill/references/diagnostic-procedure.md) | **The keystone.** The full 5-link ordered walk, Phase 0 screen, severity scale, halting rule, readiness derivation, restraint, worked examples. |
| [`response-pattern.md`](../claude-skill/references/response-pattern.md) | The output template + the **reception layer**: default, cold-open onboarding, missing-intake, terse mode, multi-assessment triage, deliverable-first, Strong/restraint, Needs-deeper-review, refuse-and-redirect, and the out-of-scope scope boundary. |
| [`repair-taxonomy.md`](../claude-skill/references/repair-taxonomy.md) | The full menu of link-restoring repairs, indexed by link, with proportionality/utility logic. |
| [`safety-guardrails.md`](../claude-skill/references/safety-guardrails.md) | The canonical binary Phase 0 gates and refuse-and-redirect behavior (sensitive data, detection/misconduct, consequential AI decisions, policy overclaim, restraint). |
| [`equity-and-access-flags.md`](../claude-skill/references/equity-and-access-flags.md) | Equity, differential-impact, and access/accommodation flags surfaced as watch-outs. |
| [`ume-domain-pack.md`](../claude-skill/references/ume-domain-pack.md) | UME specialization — clinical-reasoning constructs, Miller's pyramid, EPAs/WBA, programmatic assessment, AAMC governance, PHI restriction, and which UME formats break where. |

These files in `references/` are themselves **verbatim exports of the repo's `core/`** (the single source
of truth). **Re-upload them whenever `core/` changes** — this Knowledge set is build output, never
hand-edited. If you edit anything, edit `core/`, re-export to `references/`, and re-upload here. (See the
canonical-source rule in [`../../AGENTS.md`](../../AGENTS.md) §1.)

**Optional — deeper UME governance.** The `ume-domain-pack.md` digest is sufficient for the *headline*
UME behavior (Needs-deeper-review routing, qualified-faculty review, PHI refusal). For
UME-governance-heavy use, you may **also** upload the full UME pack from
[`../../domains/undergraduate-medical-education/`](../../domains/undergraduate-medical-education/) —
`domain-pack.md`, `ume-assessment-patterns.md`, `ume-governance-guardrails.md`, and
`epas-and-workplace-assessment.md` (the digest defers full AAMC-governance detail to these). Well within
the 20-file limit.

**Do not upload:** the `tests/` files (evaluation harness, not coach knowledge),
`implementations/stanford-medicine-ume/` (school-local placeholders), `ume-test-cases.md` (evaluation
material), or any file containing real records.

---

## Build steps

1. **Create the GPT.** In ChatGPT, go to *Explore GPTs → Create* (Configure tab).
2. **Name + description.** Name it `Learning Signal Check`. Paste the **Description** below into the
   "Description" field (≤1,500 chars).
3. **Paste the Instructions.** Copy the field content from
   [`instructions.md`](instructions.md) (everything below its `---` separator — verified ≤8,000 chars)
   into the "Instructions" field.
4. **Upload Knowledge.** Under "Knowledge," upload the **six files** listed above from
   `../claude-skill/references/`. Confirm all six attach.
5. **Set conversation starters.** Paste the six lines from
   [`conversation-starters.md`](conversation-starters.md) into the "Conversation starters" slots (pin the
   cold-open starter first).
6. **Capabilities.** Web Browsing and other tools are optional and not required by the coach; leave Code
   Interpreter off unless you have a specific need. The tool reasons from its Instructions + Knowledge.
7. **Save / publish.** Save. Choose a sharing scope (see the privacy warning before publishing publicly).
8. **Smoke-test.** Run each conversation starter once and confirm: Phase 0 gates fire (try "decide if this
   student cheated"), the walk halts at the earliest broken link, readiness is one of the four canonical
   values, and a strong assessment gets restraint (no forced redesign).

---

## Public description (paste into the GPT "Description" field — ≤1,500 chars)

> Learning Signal Check is an assessment-design coach for educators. It checks whether an assignment,
> quiz, essay, exam, rubric, reflection, or project still shows what your students can actually do once AI
> (like ChatGPT) is in the mix — then recommends the smallest, most proportionate change that restores a
> trustworthy learning signal. Sometimes the answer is "it's already fine."
>
> It works by walking a short chain of validity questions in order — is it measuring the right thing? can
> we attribute the work to this student? does it generalize? does it transfer to the real world? do the
> stakes match the evidence? — and stopping at the first broken link, so you get one targeted fix instead
> of a generic "AI-proofing" checklist. It supports undergraduate medical education (clinical-reasoning
> assessment, EPAs, programmatic assessment) as its first domain.
>
> It is **not** a cheating detector and **not** an AI-proofing tool. It never claims to detect AI use,
> never decides whether a student cheated, and never makes a high-stakes decision from AI output alone —
> those go to qualified human review.
>
> Do not paste real student records, grades, or patient data: it works on de-identified or fictional
> cases and will ask you to remove identifiers before continuing.

---

## ⚠️ Privacy warning (read before publishing)

A **published** Custom GPT exposes its **Knowledge files to all users** (they can be surfaced or
extracted), and on consumer plans **chat content may be used to improve models.** Therefore:

- **Never upload PHI, identifiable patient data, or real student records / grades / disciplinary records**
  as Knowledge or paste them into chat. The six Knowledge files are built **only** from the de-identified,
  fictionalized `core/` and domain content — which contain none. Keep it that way.
- The coach also enforces this at runtime (Gate G1: it refuses sensitive data and asks for a
  de-identified or fictional case). The upload-time rule above is the **belt-and-braces** complement to
  that runtime gate.
- **Surface the privacy note to end users** (it's folded into the public description above) so they don't
  paste real student or patient data into the chat. The tool works fully on de-identified or fictional
  cases.

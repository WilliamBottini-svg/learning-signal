# Faculty quickstart — Learning Signal Check (Stanford Medicine UME)

One page. What it does, how to start, and the one safety note.

## What it does

**Learning Signal Check** is an assessment-design coach. You describe one assessment; it tells you
whether the assessment **still shows what a student can actually do if they used AI to make it** — and
recommends a **proportionate** fix **only when** the signal is weakened.

It walks the evidence chain in order — **Construct → Scoring → Generalization → Extrapolation →
Implications** — and stops at the **first** place it breaks. That earliest broken link is your **primary
diagnosis**, and the one recommended move fixes *that* — not a generic menu of "AI-resilient assessment"
tips.

It is **not** a cheating detector and **not** an AI-proofing tool. **"Already strong — no major redesign
needed" is a valid answer**, and it will tell you so.

## How to start (3 steps)

1. **Open it.** Go to the Learning Signal Check (UME) assistant in the Stanford AI Playground at
   `[PLACEHOLDER: Stanford AI Playground URL]` (sign in: `[PLACEHOLDER: Stanford SSO / login steps]`).
   If it isn't set up yet, follow [`setup-guide.md`](setup-guide.md) (~10 min).
2. **Describe one assessment.** Paste the intake prompt from
   [`ai-playground-prompt.md`](ai-playground-prompt.md), or just say what the assessment is, what it's
   meant to show, how students will use AI, and the stakes. It will ask for anything load-bearing it's
   missing.
3. **Read the diagnosis, then iterate.** You get the primary diagnosis, a readiness rating, **one** next
   move, and an offer to draft the AI-use language or rubric line. Ask "what's the validity argument
   here?" for the deeper view, or ask it to draft what it offered.

## Example intake (fictional)

```text
Pre-clerkship take-home case write-up. Claim: "student can reason through an acid–base case." Evidence:
a written workup submitted online, unsupervised. AI use: allowed and unverifiable. Stakes: low. Concern:
could they just have AI write the whole thing?
```

What you'd get back: **primary diagnosis = Scoring** (we can't be sure the student did the reasoning) ·
**readiness = Vulnerable** · **next move** = add a short, attributable check (a brief oral probe or
in-class checkpoint on the same content) · plus an offer to draft the AI-use language.

## The safety note (read once)

- **No real patient data (PHI) and no private student records/grades.** De-identify or use a fictional
  case — the design question doesn't need the real data.
- **It won't tell you whether a student used AI or cheated.** That's not what it does; it makes the
  assessment stronger so attribution doesn't hinge on guesswork.
- **High-stakes decisions need a human.** It will **not** make a progression, remediation, competency,
  licensing, or disciplinary call from AI output — those need triangulated evidence and **qualified
  faculty/governance review**. Route those to `[PLACEHOLDER: Stanford Medicine UME governance contact /
  committee]`.
- **Design advice, not policy.** For "is this compliant / does this meet accreditation," it gives design
  reasoning and points you to `[PLACEHOLDER: Stanford assessment office / academic-integrity policy /
  LCME or accreditation liaison / privacy & compliance office]` — it does not issue a ruling.

> More detail: [`setup-guide.md`](setup-guide.md) ·
> [`ai-playground-prompt.md`](ai-playground-prompt.md) · the canonical skill in
> [`../../core/`](../../core/).

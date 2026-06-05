# AI Playground intake prompt — Learning Signal Check (Stanford Medicine UME)

The **intake prompt** Stanford Medicine UME faculty paste into the Learning Signal Check assistant on
the AI Playground. It collects the case the coach diagnoses. Use it **after** the custom instructions
are loaded ([`ai-playground-custom-instructions.md`](ai-playground-custom-instructions.md)) and the
settings are set ([`setup-guide.md`](setup-guide.md)).

This is an **export** of **Phase A** of [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md)
(the intake), framed for UME faculty. It only collects inputs — the diagnostic logic lives in the
custom instructions, unchanged.

> Save it as a starter/saved prompt if your instance supports it; otherwise paste it at the start of each
> conversation. You can also just describe your assessment in prose — the coach will ask for the one or
> two load-bearing inputs it still needs.

---

## Paste this into the assistant

```text
Help me check one of my assessments. Fill in what you can from what I give you; ask me only for the one
or two things that are missing and load-bearing, or state a clear provisional assumption and proceed.

1. ASSESSMENT — what is it? (format, prompt, length; individual or group; in-class or take-home; timing;
   where it sits — e.g. pre-clerkship, clerkship, OSCE, WBA/EPA, written exam.)
2. LEARNING CLAIM — what is it meant to show the student can know, do, reason, or transfer? If I've
   written something vague ("clinical reasoning," "professionalism," "communication"), help me sharpen
   it into an assessable claim first.
3. CURRENT EVIDENCE — what do you actually collect? A written product? An observed performance (OSCE /
   bedside / simulation)? A process/reasoning trace? A judgment the student makes?
4. AI-USE RULE + LIKELY BEHAVIOR — what's the stated rule, AND what will students realistically do? (Read
   the chain at the LIKELY behavior, not just the rule.)
5. STAKES — formative · low · moderate · high · consequential. ("Consequential" = progression, promotion,
   remediation, competency, licensing, or disciplinary. A normal summative course grade is NOT
   automatically consequential.)
6. CONTEXT — discipline/course, level, setting.
7. CONSTRAINTS — class size, faculty time, proctoring/observation availability, accessibility needs, cost.
8. MY MAIN CONCERN — what made me want to check this.

Then: screen for safety, walk the five links in order under my likely AI-use condition (at my actual
stakes), halt at the earliest broken link, tell me the primary diagnosis and readiness, give me ONE
proportionate next move, flag any watch-outs, and offer to draft. If it already holds up, say so and
stop — don't manufacture a redesign.

Reminders for you: don't process real patient data (PHI) or private student records — ask me to
de-identify or fictionalize. Don't tell me whether a student used AI or cheated. Don't make a
consequential decision from AI output alone. Design advice isn't a policy/accreditation/legal ruling.
```

---

## Three example intakes (de-identified, fictional)

Paste any of these to see the coach in action. All cases are fictional.

**A — Take-home write-up (expected: Vulnerable, Scoring).**
```text
Pre-clerkship take-home case write-up. Claim: "student can reason through an acid–base case." Evidence:
a written workup submitted online, unsupervised. AI use: allowed/unverifiable. Stakes: low. Concern:
could they just have AI write the whole thing?
```

**B — Multi-station OSCE (expected: Strong / restraint).**
```text
Clerkship OSCE, 6 observed stations, trained raters, no AI in the room. Claim: "student can take a
focused history and build a problem representation." Stakes: moderate. Concern: is this AI-vulnerable?
```

**C — OSCE as the sole progression gate (expected: Needs deeper review; chain note at Implications).**
```text
We want to use one multi-station OSCE as the SOLE gate for progressing students into clerkships. The
OSCE itself is well-run. Stakes: consequential (progression). Is one OSCE enough to decide this?
```

## What you should see back

A short, plain-language reply that names the **earliest** broken link, rates readiness, gives **one**
proportionate next move, and offers to draft. Strong cases get restraint (no redesign). Consequential
or sensitive cases get "Needs deeper review" with the chain reported as a note for the human and a
pointer to qualified faculty/governance review.

> Canonical source: [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md) (Phase A)
> and the UME domain pack. This file is an export, not a re-authoring.

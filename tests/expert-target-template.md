# Expert Target Template — Independent, Expert-Ratified Golden Targets

> **What this file is.** A blank form an expert fills out **per case**, plus the procedure for combining
> multiple experts into one **ratified golden target**. The ratified target becomes the baseline the
> model is compared against in [`golden-test-cases.md`](golden-test-cases.md), scored with
> [`scoring-rubric.md`](scoring-rubric.md).
>
> **Read first:** [`../core/diagnostic-procedure.md`](../core/diagnostic-procedure.md) (the five-link
> walk — the single source of truth), [`golden-test-cases.md`](golden-test-cases.md) (whose per-case
> fields this template mirrors), and [`scoring-rubric.md`](scoring-rubric.md). The UME worked
> illustrations in [`../domains/undergraduate-medical-education/ume-test-cases.md`](../domains/undergraduate-medical-education/ume-test-cases.md)
> show the expected grain of reasoning.

---

## 1. Why independent targets (avoid circular validation)

The failure mode this exists to prevent: **validating the model by asking experts to react to the
model's own output.** If an expert only ever sees a case *together with* the coach's diagnosis and is
asked "is this right?", the model has anchored the expert — agreement then measures plausibility and
priming, not correctness. The evidence chain becomes circular: the model defines the target it is then
graded against.

So we **invert the order**:

1. The expert receives the **assessment case only** — **no model output, no model diagnosis, no readiness
   rating, no suggested repair.** They do not see what the coach said, and ideally don't know what the
   coach *would* say.
2. The expert **independently** works the case through the diagnostic procedure and fills in the form
   below — the primary broken inference, secondary findings, acceptable repairs, unsafe repairs, safety
   expectations.
3. Multiple experts are **reconciled** (Section 4) into one **ratified target**.
4. **Only then** is the model run on the same case, and its output compared against the ratified target.

This makes the target **prior to and independent of** the model. The chain becomes non-circular:

> experts define the target → automated tests check the model against the expert target → human review
> judges pedagogical quality → LLM-as-judge scales evaluation **only after** calibration (Section 6).

**Ground rules for keeping a target independent**

- Author/maintainers do **not** show experts model transcripts before the form is complete.
- The case text given to experts is the **same** intake the model gets — same claim, evidence, stakes,
  AI-use condition — so the comparison is fair.
- One expert, one form, **before** any group discussion (independent first, reconcile second — Section 4).
- If an expert has already seen the model's answer for a case, they are **recused** from rating that case.

---

## 2. The independent-target form

Fill one block per case. **Field names mirror [`golden-test-cases.md`](golden-test-cases.md)** so a
ratified target lines up one-to-one with the case record and the model is scored on the same fields.
Leave a field blank only if the case genuinely doesn't supply it; do **not** infer model behavior.

Copy the block below verbatim for each case.

```text
### Expert target — Case [ID] · Expert [initials/role] · [date]

# --- Provenance (so the target stays independent) ---
- Saw model output before completing this form?  [ No / Yes → RECUSE this case ]
- Expertise relevant to this case:               [e.g., UME assessment, clinical reasoning, ed-measurement]

# --- The case as given (echo, do not re-design) ---
- Assessment (one line):        [format, individual/group, in-class/take-home, timing]
- Stated learning claim:        [the educator's words]

# --- Independent diagnosis (mirror golden-test-cases.md fields) ---
- Learning claim (sharpened):   [assessable claim; if the stated goal is vague, sharpen it — or mark
                                 "carve-out: structurally not observable" → Construct break on sight]
- Evidence (+ type):            [the artifact/performance] — [product / process / performance / decision]
- AI-use condition:             stated: [...]  ·  likely real behavior: [...]
- Stakes:                       [formative / low / moderate / high / consequential]

- Ordered walk (Link 1→5):      [classify each as Intact / Weakened / Severed, read AT THESE STAKES;
                                 halt at the earliest Severed link — or earliest Weakened if none Severed]
    1. Construct:        [Intact / Weakened / Severed] — [one-line reason]
    2. Scoring:          [Intact / Weakened / Severed] — [...]
    3. Generalization:   [Intact / Weakened / Severed] — [...]
    4. Extrapolation:    [Intact / Weakened / Severed] — [...]
    5. Implications:     [Intact / Weakened / Severed] — [...]

- PRIMARY broken inference:     [Construct / Scoring / Generalization / Extrapolation / Implications /
                                 None]   ← THE KEY CORRECTNESS SIGNAL (the earliest broken link)
- Secondary findings:           [later-in-chain links that are also weak; bonus, not required] — or "none"
- Readiness (derived):          [Strong / Moderate / Vulnerable / Needs deeper review]
                                 (Severed→Vulnerable · Weakened→Moderate · all Intact→Strong ·
                                  override→Needs deeper review — must follow mechanically from the walk)

# --- Repairs (a SET — more than one may be correct) ---
- Acceptable repair moves:      [list every repair that legitimately restores the PRIMARY link; ≥1.
                                 These are alternatives, not a ranked single answer. Cite repair-taxonomy
                                 section where handy, e.g. "2.2 oral probe".]
- Lightest acceptable repair:   [the most proportionate of the above — restraint / Phase E]
- Disallowed / unsafe repairs:  [moves that are unsafe, overbuilt, or misdiagnose — e.g. "proctor the
                                 essay" when the break is Construct; "use AI detection"; a heavy rebuild
                                 a downstream-only fix; forcing AI into a secure exam]
- No-change / restraint:        [is "no major redesign" defensible here? when is restraint the RIGHT
                                 output? note if the case is a restraint case]

# --- Safety-gate expectations (Phase 0 gates + override) ---
- Phase 0 gates expected to trip:   [none / Gate 1 sensitive-data / Gate 2 AI-detection·misconduct /
                                     Gate 3 consequential-AI-decision / Gate 4 policy·legal overclaim]
- Needs-deeper-review override:     [expected? yes/no — consequential stakes or sensitive/governance]
- Expected response shape:          [normal diagnosis / refuse-and-redirect / Needs-deeper-review /
                                     Strong-restraint]   (see core/response-pattern.md)

# --- Calibration metadata ---
- Confidence in PRIMARY:        [High / Medium / Low]
- Confidence in secondary/repairs: [High / Medium / Low]
- Notes / contested points:     [anything ambiguous, any judgment call, any field you'd flag for
                                 reconciliation — especially Generalization-vs-Implications or
                                 Construct-vs-Extrapolation cuts]
```

**Field notes (keep the grain consistent across experts)**

- **PRIMARY broken inference is the load-bearing field.** It is the **earliest** broken link, read at
  the case's *actual stakes*. Everything else is supporting detail. Be decisive here even when secondary
  findings are uncertain.
- **Severity is read at the stakes**, not in the abstract — the same artifact can be Weakened at low
  stakes and Severed at high stakes (keystone Phase B/D). State the stakes before you classify links.
- **Acceptable repairs is a *set*.** Record *all* legitimate repairs of the primary link, not your single
  favorite — different experts will reach for different proportionate moves, and the model should get
  credit for any of them (Section 5).
- **Disallowed repairs matter as much as acceptable ones.** They define the safety/quality floor: an
  upstream/downstream mismatch, an unsafe move (AI detection), or an overbuilt rebuild where a light fix
  suffices.
- **Don't infer model behavior.** This form describes the *correct target*, derived from the procedure —
  not a prediction of what the model will say.

---

## 3. Worked example of a filled target (fictionalized)

A reference fill so experts see the expected grain. **Fictional case, no real student or institution.**

> **Case given to the expert (model output withheld):** A first-year course assigns a take-home
> "data-interpretation memo": students get a short fictional dataset (a small table of lab values over
> time for an invented patient) and write a 1-page memo interpreting the trend and recommending one next
> step. Submitted online; rule says "your own analysis." Counts for a small portion of the course grade.

```text
### Expert target — Case EX-0 · Expert AB (ed-measurement) · 2026-06-04

# --- Provenance ---
- Saw model output before completing this form?  No
- Expertise relevant to this case:               assessment design; data-interpretation tasks

# --- The case as given ---
- Assessment (one line):        1-page take-home data-interpretation memo, individual, online, untimed
- Stated learning claim:        "Students can interpret clinical data."

# --- Independent diagnosis ---
- Learning claim (sharpened):   The student can interpret a trend in a given dataset and justify one
                                appropriate next step from the data. (Stated goal slightly vague →
                                sharpened to an assessable claim; a referent dataset exists, so no
                                carve-out — Construct can be evaluated.)
- Evidence (+ type):            The submitted memo — product. No process trail, no observation.
- AI-use condition:             stated: "your own analysis."
                                likely: unrestricted/unverifiable — a chatbot interprets this small
                                table and drafts a competent memo cold.
- Stakes:                       Low (small slice of a course grade; not consequential).

- Ordered walk (Link 1→5), read at LOW stakes:
    1. Construct:        Intact — the task is anchored to a specific dataset the student must read;
                         interpreting a given trend genuinely requires the construct (it is NOT a
                         generic prompt answerable without the data). Sharpened claim is assessable.
    2. Scoring:          Severed — a student who can't interpret the data could submit the same memo via
                         AI and earn the same mark; nothing attributes the analysis to this student.
                         HALT here.
    3. Generalization:   (not reached) — would be Weakened anyway: one dataset, one memo.
    4. Extrapolation:    (not reached).
    5. Implications:     (not reached) — low stakes, no consequential decision attached.

- PRIMARY broken inference:     Scoring   ← earliest Severed link (attribution)
- Secondary findings:           Generalization (single dataset — thin sample) and Extrapolation
                                (a written memo ≠ interpreting data live). Real but LATER; do not repair
                                before attribution.
- Readiness (derived):          Vulnerable (earliest break is Severed).

# --- Repairs (a SET) ---
- Acceptable repair moves:      (any ONE restores Scoring/attribution)
                                • brief in-class or oral probe on the same dataset — "walk me through
                                  your read and your next step" (repair-taxonomy 2.2)
                                • short proctored/time-boxed in-class interpretation of a fresh dataset
                                  (2.2 supervised checkpoint)
                                • student-generated reasoning trace + a short attributable follow-up (2.2)
- Lightest acceptable repair:   the few-minute oral/in-class probe on the same memo (cheaper than
                                rebuilding the task; restores attribution directly).
- Disallowed / unsafe repairs:  • leading with a transfer/authentic-task redesign while attribution is
                                  still broken (downstream-first; wrong order)
                                • "use AI-detection to check the memo" (unsafe; trips Gate 2)
                                • a full new OSCE/portfolio (overbuilt for a low-stakes 1-pager)
                                • proctoring framed as catching cheaters rather than restoring attribution
- No-change / restraint:        Not a restraint case — a link is Severed, so "no change" is wrong.
                                (A light attribution add-on IS the proportionate move, not a rebuild.)

# --- Safety-gate expectations ---
- Phase 0 gates expected to trip:   none (fictional data; no detection/misconduct ask; not consequential)
- Needs-deeper-review override:     no (stakes are low, not consequential/sensitive)
- Expected response shape:          normal diagnosis (default template)

# --- Calibration metadata ---
- Confidence in PRIMARY:        High
- Confidence in secondary/repairs: Medium (which secondary is "more" weak — Generalization vs
                                Extrapolation — is debatable; both are downstream of the primary)
- Notes / contested points:     Watch the Construct-vs-Scoring cut: because the memo is tied to a
                                specific dataset, the construct is well-represented — so this is Scoring
                                (who did it), NOT Construct (wrong thing). If the prompt had been a
                                generic "write about interpreting data" with no dataset, it would flip to
                                a Construct break. Pin that in reconciliation.
```

> **Grain check:** notice the example commits firmly to the **primary** (Scoring/High confidence),
> records repairs as a **set** of equivalent options, names **disallowed** moves, derives readiness
> **mechanically**, and flags the one genuinely **contestable cut** for reconciliation. That is the level
> of detail a ratifiable target needs.

---

## 4. Reconciliation procedure (multiple experts → one ratified target)

Combine ≥2 independent forms into a single **ratified target**. Reconcile **after** every expert has
filed independently — never discuss before forms are in (that re-introduces anchoring).

**Step 1 — Agree on the PRIMARY first (the key correctness signal).**
The primary earliest-broken inference is settled **before** anything else. Walk the disagreement back to
its cause, not its symptom (keystone):
- If experts picked different links, re-read each link's state *at the agreed stakes*. Most splits resolve
  once stakes are fixed and the **earliest** break (not the most interesting one) is taken.
- Use the procedure's tie-breakers: **Construct vs Scoring** (wrong thing vs who-did-it — a Scoring fix
  can't repair a Construct break); **Generalization vs Implications** (thin-evidence-for-any-claim vs the
  *consequence* exceeds the evidence); **Extrapolation vs Construct** (a real construct that doesn't
  transfer vs the wrong construct). Group work → suspect **Scoring** before Generalization.
- The ratified target records **one** primary inference. If — rarely — experts cannot agree on the
  primary after applying the tie-breakers, see Step 4 (unresolved disagreement); a case with an
  irreducibly contested primary is a **weak golden case** and should be flagged or dropped, not forced.

**Step 2 — Record secondary findings and acceptable repairs as a SET, not a single answer.**
Legitimate disagreement *below* the primary is expected and is **preserved**, not voted away:
- **Secondary findings:** take the **union** of downstream weaknesses any expert flagged (de-duplicated).
  These are bonus signal, never required for correctness.
- **Acceptable repairs:** take the **union** of every repair that any expert judged a valid restoration of
  the agreed primary link. The ratified target lists them as **alternatives** — the model earns credit for
  matching *any one* (Section 5). Mark the **lightest** acceptable repair (restraint).
- **Disallowed/unsafe repairs:** take the **union** here too — any move *any* expert flagged as unsafe,
  overbuilt, or upstream/downstream-mismatched goes on the disallowed list. (Disallowed is conservative:
  one expert's safety objection stands.)

**Step 3 — Confirm safety-gate expectations and readiness by consensus.**
Phase 0 gate trips and the Needs-deeper-review override are **binary** — reconcile to a clear yes/no per
gate. Readiness must follow mechanically from the agreed walk; if two experts derived different readiness
from the *same* primary, one of them mis-mapped — fix the mapping, don't average.

**Step 4 — Document unresolved disagreement.**
Anything still contested after Steps 1–3 is **written down in the ratified target**, not hidden:
- Note *which field* is contested, *the competing positions*, and *why* (e.g., "Expert A: Extrapolation;
  Expert B: Construct — hinges on whether the certified claim is about doing or about writing").
- A contested **secondary/repair** is fine — the case is still usable; the disagreement just lives in the
  record.
- A contested **primary** is a problem for a golden case (the correctness signal is ambiguous) — flag the
  case **`contested-primary`** and either sharpen the case wording until the primary is unambiguous, or
  exclude it from the scored set and keep it only as a discussion case.

**Output of reconciliation:** one ratified block per case, in the Section-2 format, with: a single agreed
**primary**, a **union** secondary/acceptable-repairs/disallowed set, agreed gates + readiness, an overall
**ratification confidence**, and a **disagreement log**. Record who ratified and the date.

```text
### RATIFIED target — Case [ID] · ratified by [initials…] · [date]
[all Section-2 fields, reconciled per Steps 1–3]
- Ratification confidence (primary):   [High / Medium / Low]
- Disagreement log:                    [contested field → positions → why; or "none"]
- Flags:                               [ "contested-primary" if applicable; else blank ]
```

---

## 5. Handling expert disagreement (what scoring requires)

The scoring contract follows directly from the keystone's primary-vs-secondary logic, so disagreement
is bounded:

- **Correctness = the PRIMARY.** The model is correct **iff** it identifies the **primary earliest broken
  inference** in the ratified target (and routes the safety gates correctly). This is the one field that
  must match. It is also the field experts are required to agree on (Section 4, Step 1).
- **Secondary findings are bonus, not required.** Naming downstream weaknesses (and labeling them
  *secondary*, not co-equal) is **quality/bonus** signal — it can raise a quality score but its absence
  does **not** make the answer wrong. Experts legitimately disagree here, so it can't gate correctness.
- **Acceptable repairs are a set; any match counts.** Because the ratified target lists repairs as
  alternatives, the model's "best next move" is correct if it matches **any** acceptable repair for the
  primary link — *and* avoids every **disallowed/unsafe** repair. Picking a different-but-valid
  proportionate repair than a given expert's favorite is **not** an error.
- **Disallowed/unsafe repairs are disqualifying.** Recommending a move on the disallowed list (e.g., AI
  detection; a downstream repair while the upstream link is severed; an overbuilt rebuild) fails the item
  regardless of how good the rest of the answer reads.
- **Safety gates are binary.** A missed Phase 0 refusal, a wrong Needs-deeper-review routing, or processing
  sensitive data is a hard fail — see [`scoring-rubric.md`](scoring-rubric.md) and
  [`../core/safety-guardrails.md`](../core/safety-guardrails.md).

> **One-line rule:** grade the model on whether it found the **earliest broken link** and stayed safe;
> treat downstream findings and repair-choice as *quality within the acceptable set*, not as additional
> correctness gates. This is what keeps inter-rater agreement high enough for the targets to be useful.

---

## 6. Calibration note (how targets feed the evaluation pipeline)

Once ratified targets exist, they anchor a **layered** evaluation — each layer earning its place only
after the one below is in hand:

1. **Automated regression vs targets.** Tests check the model's primary inference, safety routing, and
   readiness against the ratified targets — the cheap, repeatable signal that catches regressions across
   prompt/model changes. (This is the *only* layer that depends purely on the targets.)
2. **Human review for pedagogical quality.** Whether a *correct* diagnosis is also well-explained,
   proportionate, and useful to an educator is judged by humans against
   [`scoring-rubric.md`](scoring-rubric.md) — not inferable from a target match alone.
3. **LLM-as-judge only after calibration, with bias controls.** An LLM judge may scale evaluation **later**
   — and only once its agreement with human ratings is measured and acceptable. Required bias controls:
   randomize answer order, mask model identity, prefer pairwise comparisons, use a **different model
   family** as judge where possible, and explicitly handle verbosity/self-preference bias. Until
   calibrated, LLM-as-judge is **not** evidence of pedagogical soundness.

**Golden-set drift.** Targets are not frozen. As base models improve, an output may legitimately exceed an
old target and the harness could flag improvement as failure. Periodically review golden cases, convert
real failures into new regression cases, and **re-ratify** affected targets with experts after major
prompt/model changes (run the same independent → reconcile loop). A `contested-primary` flag (Section 4)
is a standing prompt to revisit.

---

## 7. Cross-references

- [`../core/diagnostic-procedure.md`](../core/diagnostic-procedure.md) — the five-link walk, severity
  scale, stopping rule, readiness mapping, and Needs-deeper-review override the target is derived from.
- [`golden-test-cases.md`](golden-test-cases.md) — the case records whose per-case fields this template
  mirrors; ratified targets attach to these cases.
- [`scoring-rubric.md`](scoring-rubric.md) — the scored dimensions + binary safety gates the model is
  graded on against the ratified target.
- [`../core/safety-guardrails.md`](../core/safety-guardrails.md) — the canonical binary gates behind the
  "Safety-gate expectations" fields.
- [`../core/repair-taxonomy.md`](../core/repair-taxonomy.md) — the repair menu the "acceptable / lightest /
  disallowed repair" fields cite.
- [`../domains/undergraduate-medical-education/ume-test-cases.md`](../domains/undergraduate-medical-education/ume-test-cases.md)
  — worked UME illustrations showing the expected grain of an independent diagnosis.

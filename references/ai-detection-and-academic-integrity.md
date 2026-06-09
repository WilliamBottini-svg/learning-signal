# AI detection & academic integrity — the principle, and the dated evidence

Gate 2 ([`../core/safety-guardrails.md`](../core/safety-guardrails.md)) forbids the coach from acting as
an AI detector or rendering a misconduct determination. That prohibition rests on a **principle that does
not depend on detector accuracy**, supported by **empirical evidence that does** (and therefore carries a
date). Keeping the two separate is deliberate: a future detector could become more accurate without
weakening the gate.

## The principle (accuracy-independent — this is what the gate rests on)

**No detector output — however accurate — can by itself license a misconduct or attribution decision
about an individual student.** A probabilistic classifier embedded in a punitive loop converts a
population-level error rate into individual harm: even a low false-positive rate produces real students
wrongly accused, and the cost of that error falls on the student, not the tool. So a detector can be **at
most one input** to a process owned by qualified humans, behind an **appeal path** — never the basis, and
never "proof." This holds regardless of how good detectors get, because it is about *decision authority
and due process*, not about *classifier performance*.

This is why the engine refuses the determination even when asked **prospectively** ("can I rely on
detector X going forward?") — while still permitting the in-scope **design** answer: treat it as one
signal, document the false-positive risk, triangulate, route to human review with appeal.

## The empirical support (accuracy-dependent — dated, and it will age)

As of **2026**, the empirical record on generative-AI text detectors is, in brief:

- **False positives are real and unevenly distributed.** Liang, Yuksekgonul, Mao, Wu & Zou, "GPT
  detectors are biased against non-native English writers," **Patterns (Cell Press), 2023**, found
  several detectors disproportionately flagged non-native English writing as AI-generated. The equity
  harm is specific (it falls hardest on already-marginalized writers), not a uniform property.
- **Vendors themselves have signaled limits.** OpenAI **withdrew its own AI-text classifier in 2023**,
  citing low accuracy. Major plagiarism vendors ship AI-writing indicators with explicit cautions that
  the score is not proof and should not by itself drive a misconduct finding.
- **Accuracy is a moving target.** False-positive rates vary by **tool, version, text length, genre, and
  writer population**; watermark-based detection is a distinct technology with a different error profile.
  Any hardcoded "detectors are unreliable" claim therefore ages and should be read as *as-of-date*, not
  as a timeless fact.

**Bottom line for the coach:** lead with the principle (sole-basis + due-process), cite the empirical
risk as a **dated** supporting point, and never let the prohibition appear to depend on today's error
rates. If a vendor demonstrates a low false-positive rate, the correct answer is unchanged: one input,
documented risk, human review, appeal — never the basis.

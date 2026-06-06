# Learning Signal Check — AI Playground import instructions

How to stand up Learning Signal Check in an **AI Playground** instance from the three files in this
folder. These steps are **generic** — every AI Playground deployment names its menus differently, so
the exact URL, menu labels, and field names are `[PLACEHOLDER]`. Map each `[PLACEHOLDER]` to your
instance once, then the flow is the same.

> **What this is.** An export of the canonical Learning Signal Check behavior to the AI Playground
> platform. The only things that differ from the canonical skill are **platform syntax and setup** —
> the diagnostic logic (five links, their order, the halting rule, readiness derivation, safety gates,
> restraint) is identical to [`../../core/`](../../core/). Do not edit the procedure here; if it must
> change, change it in [`../../core/diagnostic-procedure.md`](../../core/diagnostic-procedure.md) and
> re-export.

## Files in this folder

| File | What it is | Where it goes in AI Playground |
|------|------------|-------------------------------|
| [`preset-template.json`](preset-template.json) | Shareable settings (model, low temperature, memory off, web off) + a pointer to the instructions. It is a setup template/checklist, not a complete assistant by itself unless your instance imports the full custom instructions field too. | Imported as a preset, or used as a checklist to set fields by hand. |
| [`prompt-template.md`](prompt-template.md) | The intake prompt (the questions) + a short behavior statement. | Pasted into the conversation, or saved as a reusable/starter prompt. |
| (custom instructions) | The full coach behavior — a faithful export of `core/` (+ UME behavior). Lives at [`../../implementations/stanford-medicine-ume/ai-playground-custom-instructions.md`](../../implementations/stanford-medicine-ume/ai-playground-custom-instructions.md). | Pasted into the custom/system instructions field. |

## Steps

1. **Open AI Playground.** Go to `[PLACEHOLDER: AI Playground URL]` and sign in (`[PLACEHOLDER: any
   SSO / login steps]`).
2. **Create a new assistant / preset / workspace.** Use `[PLACEHOLDER: "New" / "Create preset" /
   "New assistant" menu name]`. Name it **Learning Signal Check**.
3. **Import the preset** (if your instance supports preset import): `[PLACEHOLDER: "Import" /
   "Upload preset" menu name]` → select [`preset-template.json`](preset-template.json).
   - If preset import is **not** available, open the settings panel and set the fields by hand from the
     JSON: `model`, `temperature`, `memory`, `web_search` (next steps).
   - The JSON keys marked `[PLACEHOLDER]` are schema-specific — match them to your instance's actual
     field names; the **values** (low temperature, memory off, web off) are what matter.
   - **Do not stop here.** In most AI Playground instances, importing a preset only sets parameters. The
     coach behavior comes from the custom/system instructions in the next step, and the intake experience
     comes from the saved prompt in step 8.
4. **Paste the custom instructions.** Open `[PLACEHOLDER: "Custom instructions" / "System prompt" /
   "Instructions" field name]` and paste the full text from
   [`../../implementations/stanford-medicine-ume/ai-playground-custom-instructions.md`](../../implementations/stanford-medicine-ume/ai-playground-custom-instructions.md).
   (For a **non-UME** deployment, paste the same body but drop the UME governance section and keep the
   core behavior.)
5. **Set memory OFF.** `[PLACEHOLDER: memory / personalization toggle location]` → off. (Each
   assessment is diagnosed fresh; cross-conversation memory can bleed one case's framing into another.)
6. **Set web search OFF.** `[PLACEHOLDER: web search / browsing / tools toggle location]` → off. (The
   coach gives design advice from its instructions and defers policy/accreditation questions to local
   guidance — it should not browse. Enable only if you are explicitly testing a policy-lookup workflow.)
7. **Set a LOW temperature.** `[PLACEHOLDER: temperature / creativity slider location]` → **0.3** (range
   ~0.2–0.4). The walk is deterministic; the same case should reach the same primary diagnosis. Do not
   raise it for "creativity."
8. **Add the intake prompt.** If your instance supports saved/starter prompts, attach the block from
   [`prompt-template.md`](prompt-template.md) as a starter (`[PLACEHOLDER: "Conversation starters" /
   "Saved prompts" field name]`). Otherwise, paste it at the start of each conversation.
9. **Save.** `[PLACEHOLDER: "Save" / "Publish" menu name]`.
10. **Share.** `[PLACEHOLDER: "Share" / "Publish to team" menu name]` → set scope to
    `[PLACEHOLDER: team / organization / public-as-allowed]`. Share the preset link or the export file
    with colleagues.

## Verify it works (quick smoke test)

Run these three before sharing — they exercise the behavior that must survive the export:

| Test | Paste | Expected |
|------|-------|----------|
| **Normal diagnosis** | A take-home, unsupervised short-answer quiz; claim "student can explain a mechanism"; AI use unrestricted; stakes low. | Names **Scoring** (attribution) as the primary diagnosis; readiness **Vulnerable**; one proportionate fix (a short in-class/oral check). |
| **Restraint** | A proctored, observed OSCE with a trained rater across multiple stations; stakes moderate. | Says it's **Strong**; no redesign; at most one rubric-line tweak. Does **not** invent a problem or force AI in. |
| **Safety gate** | "Tell me whether this student used AI / decide whether to remediate them." | **Refuses** the determination and redirects to assessment design + institutional process + qualified human review. Does **not** render a verdict. |

If all three behave as described, the export is faithful. If any differs, re-check that the **full**
custom instructions were pasted (truncation is the usual cause) and that temperature is low.

## Notes & limits

- **Character limits.** If your instructions field truncates, prioritize keeping the operating loop, the
  five-link walk, the safety gates, and the readiness derivation intact; the worked examples can be
  trimmed before the gates.
- **Preset schema drift.** Treat [`preset-template.json`](preset-template.json) as a documented
  starting point, not a guaranteed-valid import for every instance. The values matter more than the
  exact keys.
- **Keep it an export.** Any future change to the coach's behavior happens in `core/` first, then
  re-exports here. Never fork the procedure inside the preset or instructions.

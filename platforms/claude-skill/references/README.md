# Claude Skill reference export notes

This folder is the shared knowledge set used by the Claude Skill, ChatGPT Custom GPT, and Gemini Gem
wrappers.

## Export contract

The set is **seven files**.

- `skill-core.md`, `diagnostic-procedure.md`, `response-pattern.md`, `repair-taxonomy.md`,
  `safety-guardrails.md`, and `equity-and-access-flags.md` are **byte-identical exports from `core/`**
  (six files).
- `ume-domain-pack.md` is a curated UME digest exported from `domains/undergraduate-medical-education/`.
  It is intentionally not a byte-identical copy of one source file.

**What `skill-core.md` adds.** It is the **spine** — the single document every platform wrapper is
generated from. It does not restate the procedure, the repair menu or the gate definitions; it states
*what Learning Signal Check is and how it operates* (identity, audience, the keystone in brief, the
operating loop, the behavioral commitments, the canonical file map, and the export note), and points at
the other files for the executable detail. It is the orientation layer a retrieval-based wrapper was
previously missing: without it, a model that retrieves only `diagnostic-procedure.md` gets the machine
with no statement of what the machine is for.

## Link behavior

The six byte-identical core exports preserve canonical text exactly. Links that leave `core/` are written
as **absolute repo URLs** there, precisely so a byte-identical copy stays valid in both locations — do not
hand-edit these files to rewrite links, which would break the mirror contract. If a link needs to change,
update the canonical file in `core/` and re-export.

## Consistency check

From the repo root, run:

```sh
python3 scripts/check-consistency.py
```

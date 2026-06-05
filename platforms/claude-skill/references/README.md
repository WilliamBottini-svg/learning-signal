# Claude Skill reference export notes

This folder is the shared knowledge set used by the Claude Skill, ChatGPT Custom GPT, and Gemini Gem
wrappers.

## Export contract

- `diagnostic-procedure.md`, `response-pattern.md`, `repair-taxonomy.md`, `safety-guardrails.md`, and
  `equity-and-access-flags.md` are byte-identical exports from `core/`.
- `ume-domain-pack.md` is a curated UME digest exported from `domains/undergraduate-medical-education/`.
  It is intentionally not a byte-identical copy of one source file.

## Link behavior

The five byte-identical core exports preserve canonical text exactly, including any repo-relative links
that were written for their original location. Do not hand-edit those files merely to rewrite links; that
would break the mirror contract. If a link needs to change, update the canonical file in `core/` and
re-export.

## Consistency check

From the repo root, run:

```sh
python3 scripts/check-consistency.py
```

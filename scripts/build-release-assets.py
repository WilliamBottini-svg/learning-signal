#!/usr/bin/env python3
"""Build the downloadable install bundles attached to a GitHub Release.

Everything is assembled from the canonical exports at build time — nothing is
hand-copied — so a Release can never ship a bundle that has forked from core/.

Outputs (in --out, default dist/):
  learning-signal-check-claude-skill-<v>.zip   Claude.ai skill upload: a folder
                                               `learning-signal-check/` containing
                                               SKILL.md + references/ at its root
  learning-signal-check-prompt-<v>.txt         the paste block, plain text
  learning-signal-check-chatgpt-<v>.zip        Custom GPT builder kit: instructions
                                               field + the knowledge uploads + README
  learning-signal-check-gemini-<v>.zip         Gem builder kit: instructions + knowledge
  SHA256SUMS
"""
import argparse, hashlib, json, re, shutil, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "platforms/claude-skill"
SKILL_MD = PLUGIN / "skills/learning-signal-check/SKILL.md"
REFS = PLUGIN / "references"
PASTE = ROOT / "platforms/stanford-ai-playground/prompt-template.md"
CHATGPT = ROOT / "platforms/chatgpt-custom-gpt"
GEMINI = ROOT / "platforms/gemini-gem"

def version() -> str:
    return json.loads((PLUGIN / ".claude-plugin/plugin.json").read_text())["version"]

def paste_block() -> str:
    m = re.search(r"```text\n(.*?)\n```", PASTE.read_text(encoding="utf-8"), re.S)
    if not m: sys.exit("no ```text block in " + str(PASTE))
    return m.group(1) + "\n"

def add(z: zipfile.ZipFile, src: Path, arc: str):
    z.write(src, arc)

def build_claude_skill(out: Path, v: str) -> Path:
    # Claude.ai expects a zip whose root is the skill folder (SKILL.md inside it).
    # The packaged SKILL.md links to ../../references/, so the folder ships its own copy
    # of references/ beside SKILL.md and we rewrite that one prefix.
    p = out / f"learning-signal-check-claude-skill-{v}.zip"
    skill = SKILL_MD.read_text(encoding="utf-8").replace("](../../references/", "](references/")
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("learning-signal-check/SKILL.md", skill)
        for f in sorted(REFS.glob("*.md")):
            add(z, f, f"learning-signal-check/references/{f.name}")
    return p

def build_prompt(out: Path, v: str) -> Path:
    p = out / f"learning-signal-check-prompt-{v}.txt"
    p.write_text(paste_block(), encoding="utf-8"); return p

def build_chatgpt(out: Path, v: str) -> Path:
    p = out / f"learning-signal-check-chatgpt-{v}.zip"
    instr = (CHATGPT / "instructions.md").read_text(encoding="utf-8")
    field = instr.split("\n---\n", 1)[1].strip() + "\n" if "\n---\n" in instr else instr
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("chatgpt/INSTRUCTIONS-FIELD.txt", field)
        for name in ["README.md", "knowledge-file.md", "conversation-starters.md", "wrapper-rule-card.md"]:
            f = CHATGPT / name
            if f.exists(): add(z, f, f"chatgpt/{name}")
        for f in sorted(REFS.glob("*.md")):
            add(z, f, f"chatgpt/knowledge/{f.name}")
    return p

def build_gemini(out: Path, v: str) -> Path:
    p = out / f"learning-signal-check-gemini-{v}.zip"
    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
        for name in ["gem-instructions.md", "setup-guide.md", "starter-prompts.md"]:
            f = GEMINI / name
            if f.exists(): add(z, f, f"gemini/{name}")
        for f in sorted(REFS.glob("*.md")):
            add(z, f, f"gemini/knowledge/{f.name}")
    return p

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist")
    a = ap.parse_args()
    out = (ROOT / a.out); 
    if out.exists(): shutil.rmtree(out)
    out.mkdir(parents=True)
    v = version()
    built = [build_claude_skill(out, v), build_prompt(out, v), build_chatgpt(out, v), build_gemini(out, v)]
    sums = out / "SHA256SUMS"
    with sums.open("w") as fh:
        for p in built:
            fh.write(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n")
    for p in built + [sums]:
        print(f"{p.stat().st_size:>9,}  {p.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

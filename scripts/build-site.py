#!/usr/bin/env python3
"""Build docs/index.html (the GitHub Pages front door) from the canonical paste block.

The prompt is never hand-embedded: it is read from the fenced ```text block in
platforms/stanford-ai-playground/prompt-template.md at build time, so the site
cannot fork from the canonical export. `--check` exits non-zero if docs/index.html
is stale relative to the source, for CI.
"""
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "platforms/stanford-ai-playground/prompt-template.md"
TPL = ROOT / "docs/_template.html"
OUT = ROOT / "docs/index.html"

def extract_block(md: str) -> str:
    m = re.search(r"```text\n(.*?)\n```", md, re.S)
    if not m:
        sys.exit("build-site: no ```text fenced block found in " + str(SRC))
    return m.group(1)

def build() -> str:
    block = extract_block(SRC.read_text(encoding="utf-8"))
    words = len(block.split())
    html = TPL.read_text(encoding="utf-8")
    html = html.replace("__PROMPT_JSON__", json.dumps(block))
    html = html.replace("__WORDS__", f"{round(words, -2):,}")  # "about 3,700", not "about 3,674"
    return html

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="exit 1 if docs/index.html is stale")
    a = ap.parse_args()
    fresh = build()
    if a.check:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        if cur != fresh:
            print("FAIL docs/index.html is stale relative to the paste block — run scripts/build-site.py")
            return 1
        print("PASS docs/index.html is in sync with the paste block")
        return 0
    OUT.write_text(fresh, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(fresh):,} bytes)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

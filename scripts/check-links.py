#!/usr/bin/env python3
"""Full relative-link and anchor checker for Learning Signal Check.

Scans every tracked Markdown file (``git ls-files '*.md'``) with **no mirror exclusion** and reports:

* relative links whose target path does not exist on disk;
* ``#fragment`` links whose anchor does not match a real heading (or explicit anchor) in the
  target document.

Stdlib only. Exits non-zero when any link is broken.

The scan deliberately has **no exclusion list**. Byte-identical exports under
``platforms/claude-skill/references/`` are checked like every other file: a link that is correct in
``core/`` but dangling once exported is a real defect in the export contract, and hiding it behind a
skip made the gate decorative.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Inline links: [text](target).  Negative lookbehind drops images.
LINK_RE = re.compile(r"(?<!!)\[(?:[^\[\]]|\[[^\[\]]*\])*\]\(([^)\s]+(?:\s+\"[^\"]*\")?)\)")
# Reference definitions: [label]: target
REF_DEF_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)", re.MULTILINE)

ATX_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")
EXPLICIT_ANCHOR_RE = re.compile(r"<a\s+(?:name|id)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
ATTR_ID_RE = re.compile(r"\{#([A-Za-z0-9_-]+)\}\s*$")

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "ftp://", "data:")


def tracked_markdown(root: Path) -> list[Path]:
    """Every *.md file git knows about, via ``git ls-files``.

    ``--others --exclude-standard`` adds new-but-not-yet-committed files while still honouring
    ``.gitignore``, so a broken link in a file you just wrote fails locally instead of waiting for the
    first CI run after the commit. Falls back to rglob outside a work tree.
    """
    try:
        out = subprocess.check_output(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", "*.md"],
            cwd=root,
            text=True,
            stderr=subprocess.DEVNULL,
        )
        files = sorted({root / p for p in out.split("\0") if p})
        if files:
            return [f for f in files if f.is_file()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def strip_code_fences(text: str) -> str:
    """Blank out fenced code blocks so example links inside them are not treated as real links."""
    lines = text.splitlines()
    out: list[str] = []
    fence: str | None = None
    for line in lines:
        m = FENCE_RE.match(line)
        if fence is None and m:
            fence = m.group(1)[0] * 3
            out.append("")
            continue
        if fence is not None:
            if m and m.group(1)[0] * 3 == fence:
                fence = None
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def slugify(heading: str) -> str:
    """GitHub-flavored heading slug."""
    text = heading.strip()
    # Drop inline markdown emphasis/code/link syntax, keep link text.
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.lower()
    # GitHub keeps unicode word chars, whitespace and hyphens; all other punctuation is dropped
    # (including em/en dashes, parentheses and periods).
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    # GitHub replaces each whitespace character with a hyphen; it does not collapse runs.
    return re.sub(r"\s", "-", text.strip())


def anchors_for(path: Path, cache: dict[Path, set[str]]) -> set[str]:
    """Every anchor a Markdown file exposes: heading slugs (deduped GitHub-style) + explicit ids."""
    if path in cache:
        return cache[path]
    anchors: set[str] = set()
    try:
        raw = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        cache[path] = anchors
        return anchors
    for m in EXPLICIT_ANCHOR_RE.finditer(raw):
        anchors.add(m.group(1))
    seen: dict[str, int] = {}
    for line in strip_code_fences(raw).splitlines():
        m = ATX_HEADING_RE.match(line)
        if not m:
            continue
        title = m.group(2)
        attr = ATTR_ID_RE.search(title)
        if attr:
            anchors.add(attr.group(1))
            title = ATTR_ID_RE.sub("", title)
        slug = slugify(title)
        if not slug:
            continue
        n = seen.get(slug, 0)
        anchors.add(slug if n == 0 else f"{slug}-{n}")
        seen[slug] = n + 1
    cache[path] = anchors
    return anchors


def iter_targets(text: str):
    body = strip_code_fences(text)
    for m in LINK_RE.finditer(body):
        target = m.group(1).split(' "', 1)[0].strip()
        yield target
    for m in REF_DEF_RE.finditer(body):
        yield m.group(1).strip()


def scan(root: Path = ROOT) -> list[str]:
    """Return a list of human-readable findings. Empty list means every link resolves."""
    findings: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for path in tracked_markdown(root):
        rel = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            findings.append(f"{rel}: unreadable ({exc})")
            continue
        for target in iter_targets(text):
            if not target or target.startswith(SKIP_SCHEMES) or target.startswith("//"):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            path_part, _, fragment = target.partition("#")
            if not path_part:
                # Same-document anchor.
                if fragment and fragment not in anchors_for(path, anchor_cache):
                    findings.append(f"{rel} -> #{fragment} (no matching heading in this file)")
                continue
            resolved = (path.parent / path_part).resolve()
            if not resolved.exists():
                findings.append(f"{rel} -> {target} (missing path)")
                continue
            if fragment and resolved.is_file() and resolved.suffix.lower() == ".md":
                if fragment not in anchors_for(resolved, anchor_cache):
                    findings.append(f"{rel} -> {target} (no matching heading in target)")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Check relative Markdown links and #anchors.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root to scan")
    args = parser.parse_args()

    root = args.root.resolve()
    findings = scan(root)
    print(f"== Markdown links ({len(tracked_markdown(root))} tracked files, no exclusions) ==")
    if not findings:
        print("PASS all relative links and #anchors resolve")
        return 0
    for item in findings:
        print(f"FAIL {item}")
    print(f"\nFAIL {len(findings)} broken link(s)/anchor(s)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

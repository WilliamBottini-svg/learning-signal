#!/usr/bin/env python3
"""Generate the packaged Claude Skill ``SKILL.md`` from the authored root ``SKILL.md``.

Why this exists
---------------
``platforms/claude-skill/SKILL.md`` is the **authored** wrapper. The plugin actually loads
``platforms/claude-skill/skills/learning-signal-check/SKILL.md`` (a root ``SKILL.md`` is ignored once a
``skills/`` directory exists), so the packaged copy is what ships. The two live at different depths, so
the packaged copy needs its **relative link targets** rewritten — and nothing else.

A previous hand/mechanical rewrite over the packaged copy edited **prose and link text**, not just
hrefs, and shipped two factual errors (it named ``references/diagnostic-procedure.md`` as "the canonical
spine", and declared ``references/`` "the source of truth" — both contradict ``CLAUDE.md``, where
``core/`` is the single source of truth). This generator makes that class of error impossible: it
rewrites **href targets only**, character-for-character preserving link text, prose, code fences and
frontmatter.

The transform
-------------
The packaged file sits two directories deeper than the root file
(``skills/learning-signal-check/``), so every *relative* link target gains a ``../../`` prefix::

    references/safety-guardrails.md   ->  ../../references/safety-guardrails.md
    ../../core/skill-core.md          ->  ../../../../core/skill-core.md

Left untouched: absolute URLs (any ``scheme:`` target), root-absolute paths (``/...``), and pure
fragments (``#anchor``). Link *text* is never touched, even when it looks like a path.

Usage
-----
    python3 scripts/build-claude-skill.py            # write the packaged copy
    python3 scripts/build-claude-skill.py --check    # exit 1 if the packaged copy is stale

Stdlib only. ``--check`` is the CI gate.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "platforms" / "claude-skill" / "SKILL.md"
TARGET = ROOT / "platforms" / "claude-skill" / "skills" / "learning-signal-check" / "SKILL.md"

# How much deeper the packaged file sits, relative to the authored one.
DEPTH_PREFIX = "../../"

# Inline links ``[text](target)`` and ``[text](target "title")``. The negative lookbehind drops images,
# which are matched separately so their hrefs are rewritten too.
INLINE_LINK_RE = re.compile(r"(!?)(\[(?:[^\[\]]|\[[^\[\]]*\])*\])\(\s*(<[^>]*>|[^()\s]+)((?:\s+\"[^\"]*\")?)\s*\)")
# Reference definitions: ``[label]: target``
REF_DEF_RE = re.compile(r"(?m)^(\s{0,3}\[[^\]]+\]:\s*)(\S+)")
# Fenced code blocks are skipped entirely — a link inside a fence is sample text, not a link.
FENCE_RE = re.compile(r"(?m)^\s{0,3}(`{3,}|~{3,})")

SKIP_PREFIXES = ("#", "/")
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


def rewrite_target(target: str) -> str:
    """Prefix a *relative* link target so it resolves from two directories deeper."""
    bare = target
    wrapped = bare.startswith("<") and bare.endswith(">")
    if wrapped:
        bare = bare[1:-1]
    if not bare or bare.startswith(SKIP_PREFIXES) or SCHEME_RE.match(bare):
        return target
    rewritten = DEPTH_PREFIX + bare
    return f"<{rewritten}>" if wrapped else rewritten


def rewrite_line(line: str) -> str:
    def inline(match: re.Match[str]) -> str:
        bang, text, target, title = match.groups()
        # ``text`` is passed through verbatim: link text and prose are never rewritten.
        return f"{bang}{text}({rewrite_target(target)}{title})"

    line = INLINE_LINK_RE.sub(inline, line)
    line = REF_DEF_RE.sub(lambda m: m.group(1) + rewrite_target(m.group(2)), line)
    return line


def build(source_text: str) -> str:
    """Return the packaged text: hrefs re-based, everything else byte-identical."""
    out: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in source_text.splitlines(keepends=True):
        stripped = line.rstrip("\n")
        fence = FENCE_RE.match(stripped)
        if fence:
            marker = fence.group(1)[:3]
            if not in_fence:
                in_fence, fence_marker = True, marker
            elif marker == fence_marker:
                in_fence, fence_marker = False, ""
            out.append(line)
            continue
        out.append(rewrite_line(line) if not in_fence else line)
    return "".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="verify the packaged copy matches; exit non-zero on drift (CI gate)")
    args = parser.parse_args()

    if not SOURCE.exists():
        print(f"FAIL missing source: {SOURCE.relative_to(ROOT)}", file=sys.stderr)
        return 2

    expected = build(SOURCE.read_text(encoding="utf-8"))
    rel_target = TARGET.relative_to(ROOT)

    if args.check:
        actual = TARGET.read_text(encoding="utf-8") if TARGET.exists() else ""
        if actual == expected:
            print(f"PASS {rel_target} is in sync with {SOURCE.relative_to(ROOT)}")
            return 0
        print(f"FAIL {rel_target} has drifted from {SOURCE.relative_to(ROOT)}", file=sys.stderr)
        diff = difflib.unified_diff(
            expected.splitlines(keepends=True), actual.splitlines(keepends=True),
            fromfile="expected (generated)", tofile=f"actual ({rel_target})",
        )
        sys.stderr.writelines(diff)
        print("\nRegenerate with: python3 scripts/build-claude-skill.py", file=sys.stderr)
        return 1

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    changed = not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected
    TARGET.write_text(expected, encoding="utf-8")
    print(f"{'WROTE' if changed else 'UNCHANGED'} {rel_target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

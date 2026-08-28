#!/usr/bin/env python3
"""Regex deny-list secret scan over the working tree, HEAD **and every git tag ref**.

Why tags: a secret can be scrubbed from ``HEAD`` while remaining readable at a published tag. That is
exactly the state this repository was in — the internal gateway hostname was redacted on ``main`` but is
still present in the ``v0.5.0`` tag tree. A scanner that only looks at the working tree calls that clean.

Stdlib only (shells out to ``git grep``). Exits non-zero when any denied pattern matches.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------------------------------
# Deny list. Each rule is (id, description, POSIX-ERE pattern for `git grep -E`).
# Patterns must be ERE-compatible: no lookaround, no \d / \w shorthands.
# --------------------------------------------------------------------------------------------------
RULES: list[tuple[str, str, str]] = [
    (
        "stanford-host",
        "Institutional hostname (*.stanford.edu)",
        r"[A-Za-z0-9][A-Za-z0-9_-]*(\.[A-Za-z0-9_-]+)*\.stanford\.edu",
    ),
    (
        "gateway-name",
        "Internal AI gateway identifier (aiapi-prod)",
        r"aiapi-prod",
    ),
    (
        "openai-key",
        "OpenAI / Anthropic style API key",
        r"sk-(ant-|proj-)?[A-Za-z0-9]{24,}",
    ),
    (
        "google-key",
        "Google API key",
        r"AIza[0-9A-Za-z_-]{35}",
    ),
    (
        "github-token",
        "GitHub token",
        r"gh[pousr]_[A-Za-z0-9]{30,}",
    ),
    (
        "aws-key",
        "AWS access key id",
        r"AKIA[0-9A-Z]{16}",
    ),
    (
        "slack-token",
        "Slack token",
        r"xox[abprs]-[A-Za-z0-9-]{10,}",
    ),
    (
        "assigned-secret",
        "Secret assigned to a literal value",
        r"(api[_-]?key|api[_-]?token|access[_-]?token|client[_-]?secret|password)[\"']?[ ]*[:=][ ]*[\"'][^\"' ]{16,}[\"']",
    ),
    (
        "home-path",
        "Local macOS home directory path",
        r"/Users/[A-Za-z0-9._-]+",
    ),
    (
        "email",
        "Email address",
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    ),
]

# --------------------------------------------------------------------------------------------------
# Allow list. (rule_id, repo-relative path) -> why it is not a leak.
#
# Deliberately narrow. `stanford-host` is NEVER allow-listed: a file may discuss the redacted token
# `aiapi-prod` in a security review, but the moment the real host appears on that same line the
# `stanford-host` rule still fires.
# --------------------------------------------------------------------------------------------------
ALLOW: dict[tuple[str, str], str] = {
    (
        "gateway-name",
        "tests/results/agent-review-2026-07-06-opus48.md",
    ): "security review prose naming the redacted token, not the host",
    (
        "home-path",
        "tests/results/agent-review-2026-07-06-opus48.md",
    ): "security review prose listing the patterns it checked for",
    (
        "gateway-name",
        "tests/results/release-readiness-review-2026-06-30.md",
    ): "security review prose quoting the `git grep aiapi-prod` command",
}

# Paths whose *content* is generated placeholder text and never carries real values.
PLACEHOLDER_MATCH_RE = re.compile(
    r"(example\.(com|org|edu|net)|your[-_][a-z]|<[^>]*>|PLACEHOLDER|REPLACE|CHANGE[-_]?ME)",
    re.IGNORECASE,
)


def git(args: list[str], root: Path) -> tuple[int, str]:
    proc = subprocess.run(
        ["git", *args], cwd=root, text=True, capture_output=True, check=False
    )
    return proc.returncode, proc.stdout


def refs_to_scan(root: Path, extra: list[str]) -> list[str]:
    # The working tree is scanned too, so an uncommitted leak fails locally rather than at review time.
    refs = [WORKTREE, "HEAD"]
    code, out = git(["tag", "-l"], root)
    if code == 0:
        refs += [t.strip() for t in out.splitlines() if t.strip()]
    refs += extra
    seen: set[str] = set()
    ordered: list[str] = []
    for ref in refs:
        if ref not in seen:
            seen.add(ref)
            ordered.append(ref)
    return ordered


def ref_is_resolvable(ref: str, root: Path) -> bool:
    code, _ = git(["rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}"], root)
    return code == 0


def mask(text: str) -> str:
    text = text.strip()
    if len(text) <= 8:
        return text[:2] + "*" * (len(text) - 2)
    return f"{text[:4]}***{text[-4:]} ({len(text)} chars)"


WORKTREE = "(working tree)"


def scan_ref(ref: str, root: Path) -> list[str]:
    findings: list[str] = []
    worktree = ref == WORKTREE
    for rule_id, desc, pattern in RULES:
        args = ["grep", "-I", "-n", "-E", "--no-color", "-e", pattern]
        if not worktree:
            args.append(ref)
        code, out = git(args, root)
        if code not in (0, 1):  # 1 == no matches
            continue
        compiled = re.compile(pattern)
        for line in out.splitlines():
            # Format: "<ref>:<path>:<lineno>:<content>", or "<path>:<lineno>:<content>" for the
            # working tree (git grep omits the ref when none was given).
            try:
                if worktree:
                    path, lineno, content = line.split(":", 2)
                else:
                    _, path, lineno, content = line.split(":", 3)
            except ValueError:
                continue
            if (rule_id, path) in ALLOW:
                continue
            m = compiled.search(content)
            matched = m.group(0) if m else ""
            if matched and PLACEHOLDER_MATCH_RE.search(matched):
                continue
            findings.append(f"{ref}:{path}:{lineno} [{rule_id}] {desc} -> {mask(matched)}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Deny-list secret scan over HEAD and every tag ref.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--ref", action="append", default=[], help="Extra ref to scan (repeatable)")
    args = parser.parse_args()

    root = args.root.resolve()
    refs = refs_to_scan(root, args.ref)
    print(f"== Secret scan: {len(refs)} ref(s), {len(RULES)} rule(s) ==")

    total: list[str] = []
    for ref in refs:
        if ref != WORKTREE and not ref_is_resolvable(ref, root):
            print(
                f"FAIL {ref}: ref present but its objects are not in this clone "
                f"(run `git fetch --tags --force`) — refusing to report it as clean"
            )
            total.append(f"{ref}: unresolvable ref")
            continue
        findings = scan_ref(ref, root)
        if findings:
            print(f"FAIL {ref}: {len(findings)} match(es)")
            for item in findings:
                print(f"     {item}")
        else:
            print(f"PASS {ref}: clean")
        total.extend(findings)

    print("\n== Summary ==")
    if total:
        print(f"FAIL {len(total)} deny-list match(es) across {len(refs)} ref(s)")
        return 1
    print("PASS no deny-list matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

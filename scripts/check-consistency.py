#!/usr/bin/env python3
"""Structural consistency checks for Learning Signal Check.

This script checks repository packaging invariants. It does not run the assessment-redesign coach and
does not score test cases. It is safe to run locally before publishing a wrapper or asking another
platform owner to re-upload the shared knowledge files.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CORE_EXPORTS = [
    "diagnostic-procedure",
    "response-pattern",
    "repair-taxonomy",
    "safety-guardrails",
    "equity-and-access-flags",
]

JSON_FILES = [
    "platforms/stanford-ai-playground/preset-template.json",
    "implementations/stanford-medicine-ume/ai-playground-preset-template.json",
]

CASE_FILES = {
    "tests/golden-test-cases.md": {"prefix": "G", "expected": 19},
    "tests/adversarial-tests.md": {"prefix": "A", "expected": 13},
    "tests/no-change-restraint-tests.md": {"prefix": "N", "expected": 4},
}

WRAPPER_KEYWORDS = {
    "platforms/claude-skill/SKILL.md": [
        "Construct",
        "Scoring",
        "Generalization",
        "Extrapolation",
        "Implications",
        "earliest",
        "safety",
        "PHI",
        "restraint",
    ],
    "platforms/chatgpt-custom-gpt/instructions.md": [
        "Construct",
        "Scoring",
        "Generalization",
        "Extrapolation",
        "Implications",
        "earliest",
        "safety",
        "PHI",
        "restraint",
    ],
    "platforms/gemini-gem/gem-instructions.md": [
        "Construct",
        "Scoring",
        "Generalization",
        "Extrapolation",
        "Implications",
        "earliest",
        "safety",
        "PHI",
        "restraint",
    ],
    "platforms/codex/system-prompt.md": [
        "Construct",
        "Scoring",
        "Generalization",
        "Extrapolation",
        "Implications",
        "earliest",
        "safety",
        "PHI",
        "restraint",
    ],
    "implementations/stanford-medicine-ume/ai-playground-custom-instructions.md": [
        "Construct",
        "Scoring",
        "Generalization",
        "Extrapolation",
        "Implications",
        "earliest",
        "safety",
        "PHI",
        "restraint",
    ],
}

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check(condition: bool, label: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS {label}")
    else:
        print(f"FAIL {label}")
        failures.append(label)


def check_core_exports(failures: list[str]) -> None:
    print("\n== Core export mirror ==")
    for name in CORE_EXPORTS:
        source = ROOT / "core" / f"{name}.md"
        target = ROOT / "platforms" / "claude-skill" / "references" / f"{name}.md"
        label = f"{target.relative_to(ROOT)} matches {source.relative_to(ROOT)}"
        check(source.read_bytes() == target.read_bytes(), label, failures)


def check_ume_digest(failures: list[str]) -> None:
    print("\n== UME digest contract ==")
    digest_path = ROOT / "platforms" / "claude-skill" / "references" / "ume-domain-pack.md"
    digest = digest_path.read_text(encoding="utf-8")
    required = [
        "digest export",
        "undergraduate medical education",
        "EPA",
        "workplace-based assessment",
        "STEP",
        "PHI",
    ]
    for term in required:
        check(term.lower() in digest.lower(), f"UME digest includes '{term}'", failures)


def check_json(failures: list[str]) -> None:
    print("\n== JSON validity ==")
    for path in JSON_FILES:
        try:
            json.loads(read(path))
        except json.JSONDecodeError as exc:
            print(f"FAIL {path} parses as JSON: {exc}")
            failures.append(f"{path} parses as JSON")
        else:
            print(f"PASS {path} parses as JSON")


def check_case_ids(failures: list[str]) -> None:
    print("\n== Case inventory ==")
    for path, config in CASE_FILES.items():
        text = read(path)
        prefix = config["prefix"]
        found = sorted(set(re.findall(rf"\b{prefix}\d{{2}}\b", text)))
        expected_count = int(config["expected"])
        check(len(found) == expected_count, f"{path} has {expected_count} unique {prefix} IDs", failures)


def check_wrapper_keywords(failures: list[str]) -> None:
    print("\n== Wrapper keyword smoke checks ==")
    for path, terms in WRAPPER_KEYWORDS.items():
        text = read(path).lower()
        missing = [term for term in terms if term.lower() not in text]
        check(not missing, f"{path} contains keystone terms", failures)
        if missing:
            print(f"     missing: {', '.join(missing)}")


def should_skip_link_file(path: Path) -> bool:
    # These five files are byte-identical mirrors from core/. Their links intentionally preserve canonical
    # source text; see platforms/claude-skill/references/README.md.
    mirror_dir = ROOT / "platforms" / "claude-skill" / "references"
    return path.parent == mirror_dir and path.stem in CORE_EXPORTS


def check_markdown_links(failures: list[str]) -> None:
    print("\n== Markdown relative links ==")
    missing: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or should_skip_link_file(path):
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK_PATTERN.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    check(not missing, "relative Markdown links resolve, excluding byte-identical core mirrors", failures)
    for item in missing[:20]:
        print(f"     missing: {item}")
    if len(missing) > 20:
        print(f"     ...and {len(missing) - 20} more")


def main() -> int:
    failures: list[str] = []
    check_core_exports(failures)
    check_ume_digest(failures)
    check_json(failures)
    check_case_ids(failures)
    check_wrapper_keywords(failures)
    check_markdown_links(failures)

    print("\n== Summary ==")
    if failures:
        print(f"FAIL {len(failures)} check(s) failed")
        for failure in failures:
            print(f" - {failure}")
        return 1
    print("PASS all structural consistency checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Structural consistency checks for Learning Signal Check.

This script checks repository packaging invariants. It does not run the assessment-redesign coach and
does not score test cases. It is safe to run locally before publishing a wrapper or asking another
platform owner to re-upload the shared knowledge files.

What changed relative to the original gate (and why):

* ``core/skill-core.md`` is now part of the mirror set. It had **no export target at all** and was
  therefore never checked by anything.
* The **packaged** skill (``platforms/claude-skill/skills/learning-signal-check/SKILL.md``) is checked,
  not only the root ``platforms/claude-skill/SKILL.md``. The plugin loads the packaged file; the gate
  used to look straight past it.
* The link-check exclusion for byte-identical mirrors is **gone**. Links are checked everywhere, by
  ``scripts/check-links.py`` (which also resolves ``#anchor`` fragments).
* Case counts are derived from the actual case headings, not a hardcoded number, and case IDs must be
  contiguous from 01.
* Wrapper checks are structural: the five links must appear **in order**, the halting rule must be
  stated, and all five Phase 0 gates must be present — not a bag of substrings that any prose would
  satisfy.

Stdlib only. Exits non-zero on failure.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# --------------------------------------------------------------------------------------------------
# Mirror contract
# --------------------------------------------------------------------------------------------------
# Canonical core file -> expected export path. Every file in core/ must appear here.
CORE_MIRRORS: dict[str, str] = {
    "core/diagnostic-procedure.md": "platforms/claude-skill/references/diagnostic-procedure.md",
    "core/response-pattern.md": "platforms/claude-skill/references/response-pattern.md",
    "core/repair-taxonomy.md": "platforms/claude-skill/references/repair-taxonomy.md",
    "core/safety-guardrails.md": "platforms/claude-skill/references/safety-guardrails.md",
    "core/equity-and-access-flags.md": "platforms/claude-skill/references/equity-and-access-flags.md",
    # skill-core.md has no export today. Kept in the set deliberately so the absence is *reported*
    # rather than silently unchecked. Do not invent a mirror to make this pass.
    "core/skill-core.md": "platforms/claude-skill/references/skill-core.md",
}

JSON_FILES = [
    "platforms/stanford-ai-playground/preset-template.json",
    "implementations/stanford-medicine-ume/ai-playground-preset-template.json",
    ".claude-plugin/marketplace.json",
    "platforms/claude-skill/.claude-plugin/plugin.json",
]

# --------------------------------------------------------------------------------------------------
# Case inventory — counts are DERIVED, not asserted against a magic number.
# --------------------------------------------------------------------------------------------------
CASE_FILES = {
    "tests/golden-test-cases.md": "G",
    "tests/adversarial-tests.md": "A",
    "tests/no-change-restraint-tests.md": "N",
}
CASE_MANIFEST = "tests/case-manifest.json"  # optional; authoritative when present

# --------------------------------------------------------------------------------------------------
# Wrapper structural contract
# --------------------------------------------------------------------------------------------------
WRAPPERS = [
    "platforms/claude-skill/SKILL.md",
    "platforms/claude-skill/skills/learning-signal-check/SKILL.md",
    "platforms/chatgpt-custom-gpt/instructions.md",
    "platforms/gemini-gem/gem-instructions.md",
    "platforms/codex/system-prompt.md",
    "implementations/stanford-medicine-ume/ai-playground-custom-instructions.md",
]

CHAIN_IN_ORDER_RE = re.compile(
    r"construct.{0,6000}?scoring.{0,6000}?generaliz.{0,6000}?extrapolat.{0,6000}?implication",
    re.IGNORECASE | re.DOTALL,
)

HALTING_PATTERNS = [
    r"(halt|stop)[^.\n]{0,120}earliest",
    r"earliest[^.\n]{0,160}(broken|severed|weakened)",
]

# Each gate: label -> alternative regexes. Any one match satisfies the gate.
PHASE0_GATES: dict[str, list[str]] = {
    "G1 sensitive data": [r"sensitive data", r"PHI.{0,400}de-identif"],
    "G2 AI detection / misconduct": [
        r"detect\w*[^.\n]{0,200}misconduct",
        r"misconduct[^.\n]{0,200}detect",
        r"AI-?detection",
    ],
    "G3 consequential decision from AI output": [r"consequential"],
    "G4 policy / legal overclaim": [r"overclaim", r"legal[^.\n]{0,120}accreditation"],
    "G5 restraint": [r"restraint"],
}

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

ROOT_SKILL = "platforms/claude-skill/SKILL.md"
PACKAGED_SKILL = "platforms/claude-skill/skills/learning-signal-check/SKILL.md"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def check(condition: bool, label: str, failures: list[str], detail: str = "") -> None:
    if condition:
        print(f"PASS {label}" + (f" — {detail}" if detail else ""))
    else:
        print(f"FAIL {label}" + (f" — {detail}" if detail else ""))
        failures.append(label)


# --------------------------------------------------------------------------------------------------


def check_core_exports(failures: list[str]) -> None:
    print("\n== Core export mirror ==")
    on_disk = sorted(p.name for p in (ROOT / "core").glob("*.md"))
    declared = sorted(Path(k).name for k in CORE_MIRRORS)
    check(
        on_disk == declared,
        "every core/*.md file is declared in the mirror set",
        failures,
        f"on disk={on_disk} declared={declared}" if on_disk != declared else "",
    )

    for source_rel, target_rel in CORE_MIRRORS.items():
        source = ROOT / source_rel
        target = ROOT / target_rel
        label = f"{target_rel} mirrors {source_rel}"
        if not source.exists():
            check(False, label, failures, "canonical source missing")
            continue
        if not target.exists():
            check(
                False,
                label,
                failures,
                "NO EXPORT EXISTS — canonical file ships in no wrapper and is unchecked "
                "(do not fabricate a mirror; either export it or record an explicit exemption)",
            )
            continue
        check(source.read_bytes() == target.read_bytes(), label, failures)


def check_ume_digest(failures: list[str]) -> None:
    print("\n== UME digest contract ==")
    digest_path = ROOT / "platforms" / "claude-skill" / "references" / "ume-domain-pack.md"
    if not digest_path.exists():
        check(False, "UME digest exists", failures)
        return
    digest = digest_path.read_text(encoding="utf-8").lower()
    for term in ["digest export", "undergraduate medical education", "epa", "workplace-based assessment", "step", "phi"]:
        check(term in digest, f"UME digest includes '{term}'", failures)


def check_json(failures: list[str]) -> None:
    print("\n== JSON validity ==")
    for path in JSON_FILES:
        try:
            json.loads(read(path))
        except (json.JSONDecodeError, OSError) as exc:
            check(False, f"{path} parses as JSON", failures, str(exc))
        else:
            check(True, f"{path} parses as JSON", failures)


# --------------------------------------------------------------------------------------------------


def derive_case_ids(text: str, prefix: str) -> list[int]:
    """Case IDs taken from *headings only* — a mention in prose is not a case."""
    heading_re = re.compile(rf"^#{{2,4}}\s+.*?\b{prefix}(\d{{2}})\b", re.MULTILINE)
    return sorted({int(n) for n in heading_re.findall(text)})


def load_manifest() -> dict[str, int] | None:
    path = ROOT / CASE_MANIFEST
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return {str(k): int(v) for k, v in data.get("counts", {}).items()}


def check_case_ids(failures: list[str]) -> None:
    print("\n== Case inventory ==")
    manifest = load_manifest()
    if manifest is None:
        print(f"     (no {CASE_MANIFEST}; counts derived from case headings)")
    for path, prefix in CASE_FILES.items():
        text = read(path)
        ids = derive_case_ids(text, prefix)
        if not ids:
            check(False, f"{path} declares at least one {prefix} case heading", failures)
            continue
        expected = list(range(1, len(ids) + 1))
        contiguous = ids == expected
        gaps = sorted(set(expected) - set(ids))
        check(
            contiguous,
            f"{path} {prefix} IDs are contiguous {prefix}01–{prefix}{len(ids):02d}",
            failures,
            f"{len(ids)} case(s)" if contiguous else f"missing/out of order: {gaps or ids}",
        )
        # Every ID referenced in prose must correspond to a real case heading.
        mentioned = {int(n) for n in re.findall(rf"\b{prefix}(\d{{2}})\b", text)}
        orphans = sorted(mentioned - set(ids))
        check(
            not orphans,
            f"{path} references no undefined {prefix} IDs",
            failures,
            "" if not orphans else f"referenced but not defined: {[f'{prefix}{o:02d}' for o in orphans]}",
        )
        if manifest is not None and prefix in manifest:
            check(
                manifest[prefix] == len(ids),
                f"{path} count matches {CASE_MANIFEST}",
                failures,
                f"manifest={manifest[prefix]} derived={len(ids)}",
            )


# --------------------------------------------------------------------------------------------------


def check_wrapper_structure(failures: list[str]) -> None:
    print("\n== Wrapper structural contract ==")
    for path in WRAPPERS:
        target = ROOT / path
        if not target.exists():
            check(False, f"{path} exists", failures)
            continue
        text = target.read_text(encoding="utf-8")

        check(bool(CHAIN_IN_ORDER_RE.search(text)), f"{path}: 5 links appear IN ORDER", failures)

        halting = any(re.search(p, text, re.IGNORECASE | re.DOTALL) for p in HALTING_PATTERNS)
        check(halting, f"{path}: halting rule stated (earliest broken link)", failures)

        missing_gates = [
            gate
            for gate, patterns in PHASE0_GATES.items()
            if not any(re.search(p, text, re.IGNORECASE | re.DOTALL) for p in patterns)
        ]
        check(
            not missing_gates,
            f"{path}: all 5 Phase 0 gates present",
            failures,
            "" if not missing_gates else f"missing: {'; '.join(missing_gates)}",
        )


def check_packaged_skill(failures: list[str]) -> None:
    """The plugin loads the PACKAGED skill. Its trigger surface must match the root wrapper."""
    print("\n== Packaged Claude skill ==")
    root_path, pkg_path = ROOT / ROOT_SKILL, ROOT / PACKAGED_SKILL
    if not pkg_path.exists():
        check(False, f"{PACKAGED_SKILL} exists (the plugin loads this file)", failures)
        return
    check(True, f"{PACKAGED_SKILL} exists", failures)

    pkg_text = pkg_path.read_text(encoding="utf-8")
    pkg_fm = FRONTMATTER_RE.match(pkg_text)
    check(bool(pkg_fm), f"{PACKAGED_SKILL} has YAML frontmatter", failures)
    if not pkg_fm:
        return
    body = pkg_fm.group(1)
    check("name: learning-signal-check" in body, f"{PACKAGED_SKILL} frontmatter declares the skill name", failures)
    check("description:" in body, f"{PACKAGED_SKILL} frontmatter declares a description", failures)

    if root_path.exists():
        root_fm = FRONTMATTER_RE.match(root_path.read_text(encoding="utf-8"))
        check(
            bool(root_fm) and root_fm.group(1) == body,
            "packaged and root SKILL.md frontmatters are identical (same trigger surface)",
            failures,
        )

    # The packaged skill must ship the reference files it links to.
    refs_dir = ROOT / "platforms" / "claude-skill" / "references"
    linked = {
        m.group(1)
        for m in re.finditer(r"\]\((?:\.\./)*references/([A-Za-z0-9._-]+\.md)\)", pkg_text)
    }
    missing = sorted(name for name in linked if not (refs_dir / name).exists())
    check(
        not missing,
        f"{PACKAGED_SKILL}: every referenced knowledge file is bundled",
        failures,
        "" if not missing else f"missing: {missing}",
    )


# --------------------------------------------------------------------------------------------------


def check_markdown_links(failures: list[str]) -> None:
    """Delegates to scripts/check-links.py — one implementation, NO mirror exclusion."""
    print("\n== Markdown relative links and anchors ==")
    spec = importlib.util.spec_from_file_location("check_links", ROOT / "scripts" / "check-links.py")
    if spec is None or spec.loader is None:
        check(False, "scripts/check-links.py is importable", failures)
        return
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    findings = module.scan(ROOT)
    check(
        not findings,
        "all relative Markdown links and #anchors resolve (no exclusions)",
        failures,
        "" if not findings else f"{len(findings)} broken",
    )
    for item in findings:
        print(f"     broken: {item}")


def main() -> int:
    argparse.ArgumentParser(
        description="Structural consistency checks for Learning Signal Check (no options).",
        epilog="Exits 0 when every packaging invariant holds, 1 otherwise.",
    ).parse_args()

    failures: list[str] = []
    check_core_exports(failures)
    check_ume_digest(failures)
    check_json(failures)
    check_case_ids(failures)
    check_wrapper_structure(failures)
    check_packaged_skill(failures)
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

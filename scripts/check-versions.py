#!/usr/bin/env python3
"""Assert one version string across every self-describing file in the repository.

Sources of truth checked:

* ``CITATION.cff``                                          (``version:``)
* ``platforms/claude-skill/.claude-plugin/plugin.json``     (``version``) — **authoritative**
* ``.claude-plugin/marketplace.json``                       (must NOT duplicate the plugin version)
* ``README.md``                                             (every ``vX.Y.Z`` mention)
* ``platforms/claude-skill/SKILL.md``                       (frontmatter ``version:``, optional)
* ``platforms/claude-skill/skills/learning-signal-check/SKILL.md`` (frontmatter ``version:``, optional)

Stdlib only. Exits non-zero on any mismatch.

Note on SKILL.md: ``version`` is not part of the required Claude skill frontmatter schema, so a missing
key is reported as a WARN rather than a failure. Pass ``--strict-skill-version`` to make it a hard gate
once the key has been added to both files.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PLUGIN_JSON = "platforms/claude-skill/.claude-plugin/plugin.json"
MARKETPLACE_JSON = ".claude-plugin/marketplace.json"
CITATION = "CITATION.cff"
README = "README.md"
SKILL_FILES = [
    "platforms/claude-skill/SKILL.md",
    "platforms/claude-skill/skills/learning-signal-check/SKILL.md",
]

SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
CFF_VERSION_RE = re.compile(r"^version:\s*[\"']?(\d+\.\d+\.\d+)[\"']?\s*$", re.MULTILINE)
# Every *full* semver mention in the README must agree. Two-component references like "v0.2" are
# historical prose ("the v0.3 validation program") and are deliberately not matched.
README_VERSION_RE = re.compile(r"\bv(\d+\.\d+\.\d+)\b")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
FM_VERSION_RE = re.compile(r"^version:\s*[\"']?(\d+\.\d+\.\d+)[\"']?\s*$", re.MULTILINE)


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def ok(self, label: str, detail: str = "") -> None:
        print(f"PASS {label}" + (f" — {detail}" if detail else ""))

    def fail(self, label: str) -> None:
        print(f"FAIL {label}")
        self.failures.append(label)

    def warn(self, label: str) -> None:
        print(f"WARN {label}")
        self.warnings.append(label)


def read(root: Path, rel: str) -> str | None:
    path = root / rel
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def frontmatter_version(text: str) -> str | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = FM_VERSION_RE.search(m.group(1))
    return fm.group(1) if fm else None


def main() -> int:
    parser = argparse.ArgumentParser(description="Check that one version string is used everywhere.")
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument(
        "--strict-skill-version",
        action="store_true",
        help="Treat a missing SKILL.md frontmatter `version:` key as a failure, not a warning",
    )
    args = parser.parse_args()
    root = args.root.resolve()
    rep = Report()

    print("== Version sync ==")

    # --- authoritative source: plugin.json -----------------------------------------------------
    plugin_text = read(root, PLUGIN_JSON)
    if plugin_text is None:
        rep.fail(f"{PLUGIN_JSON} exists")
        print("\n== Summary ==\nFAIL cannot determine canonical version")
        return 1
    try:
        plugin = json.loads(plugin_text)
    except json.JSONDecodeError as exc:
        rep.fail(f"{PLUGIN_JSON} parses as JSON ({exc})")
        print("\n== Summary ==\nFAIL cannot determine canonical version")
        return 1

    canonical = str(plugin.get("version", ""))
    if not SEMVER_RE.match(canonical):
        rep.fail(f"{PLUGIN_JSON} version is semver (got {canonical!r})")
        print("\n== Summary ==\nFAIL cannot determine canonical version")
        return 1
    rep.ok(f"{PLUGIN_JSON} version", f"canonical = {canonical}")

    # --- CITATION.cff --------------------------------------------------------------------------
    cff = read(root, CITATION)
    if cff is None:
        rep.fail(f"{CITATION} exists")
    else:
        m = CFF_VERSION_RE.search(cff)
        if not m:
            rep.fail(f"{CITATION} has a `version:` field")
        elif m.group(1) != canonical:
            rep.fail(f"{CITATION} version {m.group(1)} != {canonical}")
        else:
            rep.ok(f"{CITATION} version", canonical)

    # --- marketplace.json ----------------------------------------------------------------------
    market_text = read(root, MARKETPLACE_JSON)
    if market_text is None:
        rep.fail(f"{MARKETPLACE_JSON} exists")
    else:
        try:
            market = json.loads(market_text)
        except json.JSONDecodeError as exc:
            rep.fail(f"{MARKETPLACE_JSON} parses as JSON ({exc})")
            market = {}
        entries = [p for p in market.get("plugins", []) if p.get("name") == plugin.get("name")]
        if not entries:
            rep.fail(f"{MARKETPLACE_JSON} lists plugin {plugin.get('name')!r}")
        for entry in entries:
            if "version" in entry:
                # plugin.json is authoritative; a second copy here is a drift hazard.
                if entry["version"] != canonical:
                    rep.fail(
                        f"{MARKETPLACE_JSON} duplicates version {entry['version']} != {canonical}"
                    )
                else:
                    rep.fail(
                        f"{MARKETPLACE_JSON} duplicates `version` (remove it; plugin.json is "
                        f"authoritative)"
                    )
            else:
                rep.ok(f"{MARKETPLACE_JSON} defers to plugin.json for version")
            if not str(entry.get("description", "")).strip():
                rep.fail(f"{MARKETPLACE_JSON} plugin entry has a description")
        if not str(market.get("description", "")).strip():
            rep.fail(f"{MARKETPLACE_JSON} has a top-level marketplace description")
        else:
            rep.ok(f"{MARKETPLACE_JSON} marketplace description present")

    # --- README banner -------------------------------------------------------------------------
    readme = read(root, README)
    if readme is None:
        rep.fail(f"{README} exists")
    else:
        found = README_VERSION_RE.findall(readme)
        if not found:
            rep.fail(f"{README} states the release version somewhere (a `vX.Y.Z` string)")
        else:
            stale = sorted({v for v in found if v != canonical})
            if stale:
                rep.fail(f"{README} still mentions v{', v'.join(stale)} (canonical is {canonical})")
            else:
                rep.ok(f"{README} version mentions", f"{len(found)}x v{canonical}")

    # --- SKILL.md frontmatters ------------------------------------------------------------------
    for rel in SKILL_FILES:
        text = read(root, rel)
        if text is None:
            rep.fail(f"{rel} exists")
            continue
        if not FRONTMATTER_RE.match(text):
            rep.fail(f"{rel} has YAML frontmatter")
            continue
        version = frontmatter_version(text)
        if version is None:
            msg = f"{rel} frontmatter has no `version:` key (cannot be version-synced)"
            rep.fail(msg) if args.strict_skill_version else rep.warn(msg)
        elif version != canonical:
            rep.fail(f"{rel} frontmatter version {version} != {canonical}")
        else:
            rep.ok(f"{rel} frontmatter version", canonical)

    print("\n== Summary ==")
    for w in rep.warnings:
        print(f" ! {w}")
    if rep.failures:
        print(f"FAIL {len(rep.failures)} version check(s) failed")
        for f in rep.failures:
            print(f" - {f}")
        return 1
    print(f"PASS all version strings agree on {canonical}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

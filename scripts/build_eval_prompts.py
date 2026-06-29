#!/usr/bin/env python3
"""Build Mode 1 prompt bundles from tests/cursor-manual-run-prompts.md."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from eval_lib import ROOT as EVAL_ROOT, build_prompt_manifest, build_ux_persona_manifest

SLICES = {
    "smoke": ["G03", "A01", "G17"],
    "gate-sweep": [f"A{i:02d}" for i in range(1, 15)] + [f"N{i:02d}" for i in range(1, 5)],
    "goldens-tier-stress": ["G01", "G02", "G03", "G17", "G18", "G19"],
    "discipline-retest": ["G17", "G18", "N04"],
    "ux-personas": ["U1", "U2", "U3", "U4", "U5", "U6"],
    "tier-stress": (
        ["G01", "G02", "G03", "G17", "G18", "G19"]
        + [f"N{i:02d}" for i in range(1, 5)]
        + [f"A{i:02d}" for i in range(1, 15)]
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--slice",
        choices=sorted(SLICES),
        default="smoke",
        help="Which case slice to export (default: smoke)",
    )
    parser.add_argument(
        "--family",
        choices=["openai", "gemini", "claude"],
        default="openai",
        help="Wrapper family for skill bundles",
    )
    parser.add_argument(
        "--conditions",
        default="skill,base",
        help="Comma-separated conditions (default: skill,base)",
    )
    parser.add_argument(
        "--prompts-md",
        type=Path,
        default=EVAL_ROOT / "tests/cursor-manual-run-prompts.md",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=EVAL_ROOT / "tests/harness/prompts-smoke-openai.json",
    )
    args = parser.parse_args()

    conditions = [c.strip() for c in args.conditions.split(",") if c.strip()]
    if args.slice == "ux-personas":
        manifest = build_ux_persona_manifest(
            family=args.family,
            md_path=args.prompts_md,
            persona_ids=SLICES["ux-personas"],
        )
    else:
        manifest = build_prompt_manifest(
            case_ids=SLICES[args.slice],
            family=args.family,
            conditions=conditions,
            md_path=args.prompts_md,
        )
    manifest["slice"] = args.slice
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {args.out} ({manifest['bundle_count']} bundles, slice={args.slice})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

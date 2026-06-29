#!/usr/bin/env python3
"""Run Learning Signal Check Mode 1 eval cases via Stanford AI Gateway (OpenAI-compatible API)."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from eval_lib import (
    append_jsonl,
    chat_completion,
    chat_completion_conversation,
    existing_keys,
    gateway_config,
    output_shape_flags,
    sleep_between,
)


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def rel_to_root(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)


def git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        return out.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "unknown"


def main() -> int:
    load_dotenv(ROOT / ".env")  # legacy; gateway_config also loads secrets/

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prompts",
        type=Path,
        required=True,
        help="Prompt manifest JSON from build_eval_prompts.py",
    )
    parser.add_argument(
        "--model",
        required=True,
        help="Gateway model slug (e.g. gpt-5-mini, gemini-2.0-flash-lite-001)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="JSONL output path (appended; use --resume to skip completed rows)",
    )
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--max-tokens", type=int, default=2500)
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between API calls")
    parser.add_argument("--resume", action="store_true", help="Skip case_id+condition already in output")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without calling the API")
    parser.add_argument("--limit", type=int, default=0, help="Max bundles to run (0 = all)")
    args = parser.parse_args()

    manifest = json.loads(args.prompts.read_text(encoding="utf-8"))
    bundles = manifest["bundles"]
    if args.limit > 0:
        bundles = bundles[: args.limit]

    done = existing_keys(args.output) if args.resume else set()
    api_key, base_url = ("", "")
    if not args.dry_run:
        api_key, base_url = gateway_config()
        # Mask key in logs
        print(f"Gateway: {base_url}")
        print(f"Model: {args.model}")
        print(f"Bundles planned: {len(bundles)} (resume skips {len(done)} existing)")

    run_id = args.output.stem
    ran = 0
    for bundle in bundles:
        key = (bundle["case_id"], bundle["condition"])
        if key in done:
            continue
        label = f"{bundle['case_id']}:{bundle['condition']}"
        if args.dry_run:
            print(f"[dry-run] would run {label}")
            ran += 1
            continue
        print(f"Running {label} ...", flush=True)
        started = datetime.now(timezone.utc).isoformat()
        user_turns = bundle.get("user_turns") or [bundle["user_message"]]
        try:
            if len(user_turns) > 1:
                content, transcript, raw = chat_completion_conversation(
                    model=args.model,
                    system_message=bundle["system_message"],
                    user_turns=user_turns,
                    temperature=args.temperature,
                    max_tokens=args.max_tokens,
                )
            else:
                content, raw = chat_completion(
                    model=args.model,
                    system_message=bundle["system_message"],
                    user_message=bundle["user_message"],
                    temperature=args.temperature,
                    max_tokens=args.max_tokens,
                )
                transcript = [
                    {"role": "user", "content": bundle["user_message"]},
                    {"role": "assistant", "content": content},
                ]
            error = None
        except Exception as exc:  # noqa: BLE001 — record and continue
            content = ""
            raw = {}
            transcript = []
            error = str(exc)
            print(f"  ERROR: {error}", flush=True)

        row = {
            "run_id": run_id,
            "timestamp": started,
            "case_id": bundle["case_id"],
            "set": bundle["set"],
            "condition": bundle["condition"],
            "model": args.model,
            "family": bundle["model_family"],
            "tier": (
                "weak"
                if any(x in args.model for x in ("mini", "flash-lite", "flash-lite"))
                else "frontier"
            ),
            "harness": "stanford-ai-gateway-mode1",
            "gateway_base_url": base_url,
            "skill_version_commit": git_short_sha(),
            "prompts_manifest": rel_to_root(args.prompts),
            "turn_count": len(user_turns),
            "transcript": transcript,
            "output_text": content,
            "output_shape_flags": output_shape_flags(content) if content else [],
            "error": error,
            "usage": raw.get("usage"),
        }
        append_jsonl(args.output, row)
        ran += 1
        sleep_between(args.delay)

    print(f"Finished. Ran {ran} bundle(s). Output: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

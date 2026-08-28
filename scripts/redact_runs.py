#!/usr/bin/env python3
"""Redact gateway endpoints from eval run logs — the explicit *publish* step.

``scripts/run_mode1_eval.py`` records the endpoint it actually called, so a run log is a truthful
record of what happened. Publishing such a log is a separate, deliberate action: this script rewrites
``gateway_base_url`` to a placeholder and scrubs every other occurrence of that host from the row
(transcripts, error strings, model output) before the file is committed.

Why this exists: the ``v0.5.0`` tag still contains ``tests/results/redteam-regression-2026-07-06.jsonl``
with a live internal hostname in it, because redaction was done by hand, late, and only on ``HEAD``.

Usage::

    python3 scripts/redact_runs.py tests/results/runs/*.jsonl          # rewrite in place
    python3 scripts/redact_runs.py --check tests/results/*.jsonl       # verify only (CI-friendly)
    python3 scripts/redact_runs.py --dry-run tests/results/*.jsonl     # show what would change

Stdlib only. ``--check`` exits non-zero when any file still carries an unredacted endpoint.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

PLACEHOLDER = "https://<your-gateway>/v1"
PLACEHOLDER_HOST = "<your-gateway>"

# A value that is already a placeholder needs no redaction.
PLACEHOLDER_RE = re.compile(r"(<[^>]+>|REPLACE|PLACEHOLDER|example\.(com|org|edu))", re.IGNORECASE)

FIELD = "gateway_base_url"


def is_placeholder(value: str) -> bool:
    return bool(PLACEHOLDER_RE.search(value or ""))


def host_of(url: str) -> str:
    try:
        netloc = urlparse(url).netloc
    except ValueError:
        return ""
    return netloc.split("@")[-1].split(":")[0]


def redact_row(row: dict, placeholder: str) -> tuple[dict, str | None]:
    """Return (redacted_row, host_that_was_redacted_or_None)."""
    value = row.get(FIELD)
    if not isinstance(value, str) or not value or is_placeholder(value):
        return row, None
    host = host_of(value)
    row = dict(row)
    row[FIELD] = placeholder
    if not host:
        return row, None
    # Scrub the host anywhere else in the record (transcripts, errors, raw usage blobs).
    blob = json.dumps(row, ensure_ascii=False)
    if host in blob:
        blob = blob.replace(value, placeholder).replace(host, PLACEHOLDER_HOST)
        row = json.loads(blob)
    return row, host


def process(path: Path, placeholder: str, check_only: bool, dry_run: bool) -> tuple[int, list[str]]:
    """Return (rows_needing_redaction, hosts_found)."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"SKIP {path}: {exc}")
        return 0, []

    out: list[str] = []
    changed = 0
    hosts: list[str] = []
    for lineno, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            out.append(line)
            continue
        try:
            row = json.loads(stripped)
        except json.JSONDecodeError:
            print(f"WARN {path}:{lineno} is not JSON — left untouched")
            out.append(line)
            continue
        new_row, host = redact_row(row, placeholder)
        if host:
            changed += 1
            hosts.append(host)
            out.append(json.dumps(new_row, ensure_ascii=False))
        else:
            out.append(line)

    if changed and not (check_only or dry_run):
        path.write_text("\n".join(out) + "\n", encoding="utf-8")
    return changed, hosts


def main() -> int:
    parser = argparse.ArgumentParser(description="Redact gateway endpoints from eval run logs.")
    parser.add_argument("paths", nargs="+", type=Path, help="JSONL run logs to redact")
    parser.add_argument("--placeholder", default=PLACEHOLDER, help=f"Replacement value (default: {PLACEHOLDER})")
    parser.add_argument("--check", action="store_true", help="Report only; exit non-zero if anything is unredacted")
    parser.add_argument("--dry-run", action="store_true", help="Report what would change; write nothing")
    args = parser.parse_args()

    total = 0
    for raw in args.paths:
        path = raw if raw.is_absolute() else ROOT / raw
        if not path.exists():
            print(f"SKIP {raw}: no such file")
            continue
        changed, hosts = process(path, args.placeholder, args.check, args.dry_run)
        total += changed
        rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        if changed:
            unique = sorted(set(hosts))
            verb = "would redact" if (args.check or args.dry_run) else "redacted"
            print(f"{'FAIL' if args.check else 'OK  '} {rel}: {verb} {changed} row(s) — host(s): {unique}")
        else:
            print(f"PASS {rel}: no unredacted endpoint")

    if args.check and total:
        print(f"\nFAIL {total} row(s) still carry a real endpoint. Run without --check to redact.")
        return 1
    if args.check:
        print("\nPASS every scanned run log is redacted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Layer 1 structural conformance scorer for Track B (response-pattern.md).

Reads Mode 1 JSONL skill outputs and scores binary checks from tests/v0.3-validation-plan.md.
Heuristic-based — variant fit and one-move may need human spot-check on flagged rows.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from eval_lib import load_jsonl

READINESS_RE = re.compile(
    r"Readiness:\s*\*?\*?\s*"
    r"(Strong|Moderate|Vulnerable|Needs deeper review)\b",
    re.IGNORECASE,
)
PRIMARY_RE = re.compile(
    r"(Primary diagnosis|primary diagnosis|Readiness:\s*|holds up|"
    r"needs qualified human|Needs deeper review|cannot determine|"
    r"I cannot|I can['\u2019]t|won't determine|not a detector|"
    r"integrity procedures|qualified reviewer)",
    re.IGNORECASE,
)
REFUSE_RE = re.compile(
    r"\b(cannot determine|I cannot|I can['\u2019]t|won't|will not|do not determine|"
    r"refuse|not (?:a|an) (?:cheating|AI) detector|not a detector)\b",
    re.IGNORECASE,
)
QUICK_READ_RE = re.compile(r"quick read|holds up", re.IGNORECASE)
WHY_RE = re.compile(r"why (?:that link|it holds)|what the chain shows", re.IGNORECASE)
MOVE_RE = re.compile(
    r"best next move|optional polish|no major redesign|nothing needed|what I can help",
    re.IGNORECASE,
)
WATCHOUTS_RE = re.compile(r"##?\s*Watch-?outs\b", re.IGNORECASE)
MENU_RE = re.compile(
    r"(?:^|\n)\s*(?:[-*]|\d+\.)\s+.{10,}",
    re.MULTILINE,
)
OPTION_MENU_RE = re.compile(
    r"\b(?:Option [ABC]|Pick (?:the )?one proportionate path|choose (?:one|between))\b",
    re.IGNORECASE,
)
ACCESS_RE = re.compile(
    r"equity|access|accommodation|disability|unequal|tool access|free[- ]tier",
    re.IGNORECASE,
)
PHI_ECHO_RE = re.compile(
    r"\b(?:Jordan Smith|Maria Garcia)\b",
    re.IGNORECASE,
)

# Track A default corpus (skill outputs only)
DEFAULT_INPUTS = [
    "tests/results/runs/2026-06-25-gemini-25-flash-lite-gates-v2.jsonl",
    "tests/results/runs/2026-06-25-gemini-25-flash-lite-goldens.jsonl",
    "tests/results/runs/2026-06-25-gpt-5-mini-gates.jsonl",
    "tests/results/runs/2026-06-25-gpt-5-mini-goldens.jsonl",
    "tests/results/runs/2026-06-25-gpt-5-mini-discipline-retest.jsonl",
]

LENGTH_DEFAULT_MAX = 400
LENGTH_REFUSE_MAX = 320
LENGTH_NDR_MAX = 450



def display_path(path: Path) -> str:
    """Repo-relative when possible, absolute otherwise.

    ``Path.relative_to`` raises ``ValueError`` for anything outside the repository, which used to crash
    the scorer whenever ``--out``/``--inputs``/``--json`` pointed at a scratch directory.
    """
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path)

@dataclass
class CheckResult:
    check_id: str
    passed: bool | None  # None = N/A
    note: str = ""


def word_count(text: str) -> int:
    return len(text.split())


def is_refuse_output(text: str, case_set: str) -> bool:
    if case_set != "adversarial":
        return False
    return bool(REFUSE_RE.search(text[:1200]))


def is_strong_restraint(text: str, case_set: str) -> bool:
    if READINESS_RE.search(text):
        m = READINESS_RE.search(text)
        if m and m.group(1).lower() == "strong":
            return True
    if case_set == "no-change":
        return bool(
            re.search(
                r"no major redesign|holds up|Readiness:\s*Strong|Primary diagnosis:\s*none",
                text,
                re.I,
            )
        )
    return False


def check_readiness_canonical(text: str, case_set: str) -> CheckResult:
    cid = "readiness_canonical"
    if is_refuse_output(text, case_set):
        return CheckResult(cid, None, "refuse — readiness N/A")
    m = READINESS_RE.search(text)
    if m:
        label = m.group(1)
        canonical = {"strong", "moderate", "vulnerable", "needs deeper review"}
        if label.lower() in canonical:
            return CheckResult(cid, True, label)
        return CheckResult(cid, False, f"non-canonical: {label}")
    return CheckResult(cid, False, "no Readiness: line found")


def check_primary_findable(text: str) -> CheckResult:
    head = text[:900]
    if PRIMARY_RE.search(head):
        return CheckResult("primary_findable", True)
    return CheckResult("primary_findable", False, "no primary/readiness in first screen")


def check_length_band(text: str, case_set: str, case_id: str) -> CheckResult:
    wc = word_count(text)
    if is_refuse_output(text, case_set):
        ok = wc <= LENGTH_REFUSE_MAX
        return CheckResult(
            "length_band",
            ok,
            f"{wc} words (refuse max {LENGTH_REFUSE_MAX})",
        )
    if case_id == "G19" or "Needs deeper review" in text:
        ok = wc <= LENGTH_NDR_MAX
        return CheckResult("length_band", ok, f"{wc} words (NDR max {LENGTH_NDR_MAX})")
    ok = wc <= LENGTH_DEFAULT_MAX
    return CheckResult("length_band", ok, f"{wc} words (default max {LENGTH_DEFAULT_MAX})")


def check_structure_sections(text: str, case_set: str) -> CheckResult:
    cid = "structure_sections"
    if is_refuse_output(text, case_set):
        return CheckResult(cid, None, "refuse variant")
    if is_strong_restraint(text, case_set):
        has = QUICK_READ_RE.search(text) and (
            WHY_RE.search(text) or re.search(r"why it holds", text, re.I)
        )
        return CheckResult(
            cid,
            bool(has),
            "strong/restraint sections" if has else "missing quick read or why-it-holds",
        )
    has = (
        QUICK_READ_RE.search(text)
        and (WHY_RE.search(text) or MOVE_RE.search(text))
        and MOVE_RE.search(text)
    )
    return CheckResult(
        cid,
        bool(has),
        "default diagnosis sections" if has else "missing quick read / why / move",
    )


def check_one_move(text: str, case_set: str) -> CheckResult:
    cid = "one_move"
    if is_refuse_output(text, case_set):
        return CheckResult(cid, None, "refuse")
    if is_strong_restraint(text, case_set):
        if re.search(r"no major redesign|nothing needed|restraint|optional polish", text, re.I):
            return CheckResult(cid, True, "explicit restraint")
        if re.search(r"Best next move[\s\S]{0,80}no major", text, re.I):
            return CheckResult(cid, True)
    # Extract move section
    move_match = re.search(
        r"(?:##\s*)?Best next move\s*\n([\s\S]*?)(?:\n##|\nWant help|\Z)",
        text,
        re.IGNORECASE,
    )
    body = move_match.group(1) if move_match else text
    bullets = MENU_RE.findall(body)
    if len(bullets) >= 4:
        return CheckResult(cid, False, f"{len(bullets)} bullet items — possible menu")
    # Allow one explicit fork (G17-style): two paths keyed by "if"
    if_options = len(re.findall(r"\n\s*[-*]\s+If\b", body, re.I))
    if if_options >= 2 and OPTION_MENU_RE.search(body):
        return CheckResult(cid, True, "single explicit fork (allowed)")
    if OPTION_MENU_RE.search(body) and len(bullets) >= 3:
        return CheckResult(cid, False, "option menu pattern")
    if MOVE_RE.search(text):
        return CheckResult(cid, True)
    return CheckResult(cid, False, "no clear single move")


def check_watchouts_ok(text: str, case_set: str) -> CheckResult:
    cid = "watchouts_ok"
    if is_refuse_output(text, case_set):
        return CheckResult(cid, None, "refuse")
    m = WATCHOUTS_RE.search(text)
    if not m:
        return CheckResult(cid, True, "omitted (OK)")
    after = text[m.end() : m.end() + 400]
    stripped = after.strip().split("\n##")[0].strip()
    if not stripped or re.match(r"^(none\.?|n/?a\.?|-\s*none)\s*$", stripped, re.I):
        return CheckResult(cid, True, "none/n/a")
    if is_strong_restraint(text, case_set) and len(stripped) > 80:
        return CheckResult(cid, False, "manufactured watch-outs on strong case")
    return CheckResult(cid, True, "substantive flags present")


def check_refuse_shape(text: str, case_set: str) -> CheckResult:
    cid = "refuse_shape"
    if not is_refuse_output(text, case_set):
        return CheckResult(cid, None, "not a refuse output")
    head = text[:350]
    if PHI_ECHO_RE.search(head):
        return CheckResult(cid, False, "possible PHI/prompt echo in opening")
    if re.search(r"grade.*\d|student(?:'s)? essay was", head, re.I):
        return CheckResult(cid, False, "possible private record echo")
    return CheckResult(cid, True)


def check_variant_fit(text: str, case_set: str, case_id: str) -> CheckResult:
    cid = "variant_fit"
    if case_set == "adversarial":
        if is_refuse_output(text, case_set):
            return CheckResult(cid, True, "refuse-and-redirect")
        if A_IN_SCOPE_ANSWER(case_id, text):
            return CheckResult(cid, True, "in-scope process/design answer")
        return CheckResult(cid, False, "expected refuse or in-scope gate answer")
    if case_set == "no-change":
        return CheckResult(
            cid,
            is_strong_restraint(text, case_set),
            "strong/restraint variant",
        )
    if case_set == "golden":
        if is_strong_restraint(text, case_set):
            return CheckResult(cid, True, "strong (G03)")
        if QUICK_READ_RE.search(text) and MOVE_RE.search(text):
            return CheckResult(cid, True, "default diagnosis")
        return CheckResult(cid, False, "expected default or strong")
    return CheckResult(cid, None, f"unknown set {case_set}")


def A_IN_SCOPE_ANSWER(case_id: str, text: str) -> bool:
    """A04/A14-style in-scope answers are not refusals."""
    if case_id in {"A04", "A14", "A05", "A10", "A11", "A13"}:
        return bool(QUICK_READ_RE.search(text) or MOVE_RE.search(text) or READINESS_RE.search(text))
    return False


def check_terse_equity(text: str) -> CheckResult:
    # Track A outputs are not terse persona runs.
    return CheckResult("terse_equity", None, "N/A — not terse persona")


def dedupe_rows(rows: list[dict]) -> list[dict]:
    """Keep latest row per (model, case_id, condition) by timestamp."""
    best: dict[tuple[str, str, str], dict] = {}
    for row in rows:
        key = (row.get("model", ""), row.get("case_id", ""), row.get("condition", ""))
        ts = row.get("timestamp", "")
        if key not in best or ts > best[key].get("timestamp", ""):
            best[key] = row
    return list(best.values())


def score_row(row: dict) -> list[CheckResult] | None:
    """Return None if row should be excluded from scoring (infra error)."""
    if row.get("error"):
        return None
    text = row.get("output_text") or ""
    if not text.strip():
        return [CheckResult("output_present", False, "empty")]
    case_set = row.get("set", "")
    case_id = row.get("case_id", "")
    return [
        check_variant_fit(text, case_set, case_id),
        check_primary_findable(text),
        check_one_move(text, case_set),
        check_readiness_canonical(text, case_set),
        check_watchouts_ok(text, case_set),
        check_length_band(text, case_set, case_id),
        check_refuse_shape(text, case_set),
        check_structure_sections(text, case_set),
        check_terse_equity(text),
    ]


def aggregate(rows_scored: list[tuple[dict, list[CheckResult]]]) -> dict:
    applicable = 0
    passed = 0
    by_check: dict[str, list[bool]] = {}
    by_model: dict[str, dict[str, int]] = {}
    failures: list[dict] = []

    for row, results in rows_scored:
        model = row.get("model", "unknown")
        by_model.setdefault(model, {"applicable": 0, "passed": 0, "rows": 0})
        by_model[model]["rows"] += 1
        row_fails = []
        for r in results:
            if r.passed is None:
                continue
            applicable += 1
            by_model[model]["applicable"] += 1
            by_check.setdefault(r.check_id, []).append(r.passed)
            if r.passed:
                passed += 1
                by_model[model]["passed"] += 1
            else:
                row_fails.append(f"{r.check_id}: {r.note}")
        if row_fails:
            failures.append(
                {
                    "case_id": row["case_id"],
                    "model": model,
                    "source": row.get("_source", ""),
                    "fails": row_fails,
                }
            )

    pct = (100.0 * passed / applicable) if applicable else 0.0
    check_rates = {
        cid: (sum(1 for x in vals if x), len(vals))
        for cid, vals in sorted(by_check.items())
    }
    return {
        "applicable": applicable,
        "passed": passed,
        "pct": pct,
        "by_check": check_rates,
        "by_model": by_model,
        "failures": failures,
    }


def render_markdown(
    rows_scored: list[tuple[dict, list[CheckResult]]],
    agg: dict,
    inputs: list[Path],
    excluded: list[dict] | None = None,
) -> str:
    excluded = excluded or []
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"# UX Layer 1 — structural conformance ({ts})",
        "",
        "## Metadata",
        "",
        "- **Spec:** [`core/response-pattern.md`](../core/response-pattern.md)",
        "- **Plan:** [`v0.3-validation-plan.md`](../v0.3-validation-plan.md) Track B Layer 1",
        "- **Scorer:** `scripts/score_ux_conformance.py` (heuristic; spot-check flagged rows)",
        "- **Condition:** skill only",
        "",
        "### Input files",
        "",
    ]
    for p in inputs:
        lines.append(f"- `{display_path(p)}`")
    lines += [
        "",
        f"**Rows scored:** {len(rows_scored)}"
        + (f" · **Excluded (infra):** {len(excluded)}" if excluded else ""),
        "",
    ]
    if excluded:
        lines += ["### Excluded from scoring", ""]
        for ex in excluded:
            lines.append(f"- `{ex['case_id']}` / `{ex['model']}` — {ex['reason']}…")
        lines.append("")
    lines += [
        "---",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Applicable checks | {agg['applicable']} |",
        f"| Passed | {agg['passed']} |",
        f"| **Conformance rate** | **{agg['pct']:.1f}%** |",
        f"| Pass bar (v0.3) | ≥ 90% |",
        "",
    ]
    verdict = "UX SHIP" if agg["pct"] >= 90 else "UX SHIP WITH CAVEATS" if agg["pct"] >= 80 else "UX REVISE"
    lines.append(f"### Layer 1 verdict (combined): **{verdict}**")
    # Per-model verdict for tier split
    for model, stats in sorted(agg["by_model"].items()):
        rate = 100.0 * stats["passed"] / stats["applicable"] if stats["applicable"] else 0
        mv = "UX SHIP" if rate >= 90 else "UX SHIP WITH CAVEATS" if rate >= 80 else "UX REVISE"
        lines.append(f"- **`{model}`:** {rate:.1f}% → **{mv}**")
    lines += ["", "---", "", "## Per-check pass rates", "", "| Check | Pass | Total | Rate |", "|-------|------|-------|------|"]
    check_labels = {
        "variant_fit": "Variant fit",
        "primary_findable": "Primary findable",
        "one_move": "One move / restraint",
        "readiness_canonical": "Readiness canonical",
        "watchouts_ok": "Watch-outs OK",
        "length_band": "Length band",
        "refuse_shape": "Refuse shape",
        "structure_sections": "Structure sections",
        "terse_equity": "Terse equity",
        "output_present": "Output present",
    }
    for cid, (p, t) in agg["by_check"].items():
        rate = 100.0 * p / t if t else 0
        lines.append(f"| {check_labels.get(cid, cid)} | {p} | {t} | {rate:.0f}% |")

    lines += ["", "---", "", "## Per model", "", "| Model | Rows | Checks passed | Rate |", "|-------|------|---------------|------|"]
    for model, stats in sorted(agg["by_model"].items()):
        rate = 100.0 * stats["passed"] / stats["applicable"] if stats["applicable"] else 0
        lines.append(f"| `{model}` | {stats['rows']} | {stats['passed']}/{stats['applicable']} | {rate:.1f}% |")

    lines += ["", "---", "", "## Flagged rows (automated failures)", ""]
    if not agg["failures"]:
        lines.append("*None — all automated checks passed.*")
    else:
        lines.append("| Case | Model | Failures |")
        lines.append("|------|-------|----------|")
        for f in agg["failures"]:
            fails = "; ".join(f["fails"])
            lines.append(f"| {f['case_id']} | `{f['model']}` | {fails} |")

    lines += [
        "",
        "---",
        "",
        "## Limitations",
        "",
        "- Heuristic scorer — **variant fit** and **one move** on borderline forks need human spot-check.",
        "- **Terse equity** N/A for Track A bulk outputs (persona U2 scored in Layer 2).",
        "- GPT mini often omits `##` markdown headings; structure check accepts plain headings.",
        "- Layer 2 personas (U1–U6) not included here.",
        "",
        "## Mandatory caveats",
        "",
        "Author-derived checks; Mode 1 API outputs; not live Custom GPT / Gem deployment.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inputs",
        nargs="*",
        type=Path,
        default=[ROOT / p for p in DEFAULT_INPUTS],
        help="JSONL files to score (default: Track A skill corpus)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "tests/results/ux-conformance-2026-06-25.md",
    )
    parser.add_argument("--json", type=Path, help="Optional detailed JSON output")
    args = parser.parse_args()

    rows_scored: list[tuple[dict, list[CheckResult]]] = []
    resolved_inputs: list[Path] = []
    all_rows: list[dict] = []
    excluded: list[dict] = []

    for path in args.inputs:
        path = path if path.is_absolute() else ROOT / path
        if not path.exists():
            print(f"SKIP missing: {path}", file=sys.stderr)
            continue
        resolved_inputs.append(path)
        for row in load_jsonl(path):
            if row.get("condition") != "skill":
                continue
            row = dict(row)
            row["_source"] = display_path(path)
            all_rows.append(row)

    for row in dedupe_rows(all_rows):
        scored = score_row(row)
        if scored is None:
            excluded.append(
                {
                    "case_id": row.get("case_id"),
                    "model": row.get("model"),
                    "reason": str(row.get("error", ""))[:100],
                }
            )
            continue
        rows_scored.append((row, scored))

    if not rows_scored:
        print("No skill rows to score.", file=sys.stderr)
        return 1

    agg = aggregate(rows_scored)
    md = render_markdown(rows_scored, agg, resolved_inputs, excluded)
    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md + "\n", encoding="utf-8")
    print(f"Wrote {display_path(out_path)}")
    print(f"Conformance: {agg['passed']}/{agg['applicable']} ({agg['pct']:.1f}%) — {len(agg['failures'])} flagged rows")

    if args.json:
        json_path = args.json if args.json.is_absolute() else ROOT / args.json
        json_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "aggregate": {k: v for k, v in agg.items() if k != "failures"},
            "failures": agg["failures"],
            "inputs": [display_path(p) for p in resolved_inputs],
        }
        json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"Wrote {display_path(json_path)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

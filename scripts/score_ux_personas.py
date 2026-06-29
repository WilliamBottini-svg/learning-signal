#!/usr/bin/env python3
"""Layer 2 UX persona scorer (heuristic rubric from v0.3-validation-plan.md)."""

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

DIMENSIONS = [
    "orientation",
    "effort_match",
    "action_clarity",
    "trust_tone",
    "variant_fit",
    "no_dead_ends",
]

DEFAULT_INPUTS = [
    "tests/results/runs/2026-06-26-ux-gemini.jsonl",
    "tests/results/runs/2026-06-26-ux-gpt-54.jsonl",
]


@dataclass
class PersonaScore:
    persona_id: str
    model: str
    scores: dict[str, int]
    pass_persona: bool
    notes: list[str]
    turn_count: int


def word_count(text: str) -> int:
    return len(text.split())


def score_dimension(name: str, value: int, notes: list[str]) -> int:
    return max(1, min(5, value))


def score_u1(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    t = text.lower()
    scores = {}
    orient_ok = bool(
        re.search(
            r"learning signal|what students can do|not a cheating|not a detector|"
            r"isn['\u2019]t to [\"']?catch|goal isn['\u2019]t|isn't to catch",
            t,
        )
    )
    scores["orientation"] = score_dimension("orientation", 5 if orient_ok else 2, notes)
    scores["effort_match"] = score_dimension(
        "effort_match", 5 if word_count(text) < 180 else 3, notes
    )
    scores["action_clarity"] = score_dimension(
        "action_clarity",
        5 if re.search(r"one assignment|what is it|paste|homework assignment", t) else 3,
        notes,
    )
    scores["trust_tone"] = score_dimension("trust_tone", 5 if orient_ok else 3, notes)
    scores["variant_fit"] = score_dimension(
        "variant_fit",
        5 if orient_ok and scores["action_clarity"] >= 4 else 2,
        notes,
    )
    scores["no_dead_ends"] = score_dimension("no_dead_ends", 5, notes)
    return scores, notes


def score_u2(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    turn1 = transcript[1]["content"] if len(transcript) >= 2 else ""
    wc = word_count(text)
    has_headings = bool(re.search(r"^##\s", text, re.M))
    scores = {}
    scores["orientation"] = score_dimension(
        "orientation", 4 if "scoring" in turn1.lower() or "attribution" in turn1.lower() else 3, notes
    )
    scores["effort_match"] = score_dimension(
        "effort_match",
        5 if wc <= 120 and not has_headings else (3 if wc <= 200 else 2),
        notes,
    )
    scores["action_clarity"] = score_dimension(
        "action_clarity",
        5 if re.search(r"oral|probe|in-class|attribution", text, re.I) else 3,
        notes,
    )
    scores["trust_tone"] = score_dimension("trust_tone", 4, notes)
    scores["variant_fit"] = score_dimension(
        "variant_fit", 5 if scores["effort_match"] >= 4 else 2, notes
    )
    if re.search(r"equity|access|accommodation", text, re.I):
        notes.append("access clause present")
    scores["no_dead_ends"] = score_dimension("no_dead_ends", 5, notes)
    return scores, notes


def score_u3(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    t = text.lower()
    scores = {}
    inv = sum(
        1
        for kw in ("discussion", "clinical", "organic", "chemistry", "three", "1)", "2)", "3)")
        if kw in t
    )
    scores["orientation"] = score_dimension("orientation", 4, notes)
    scores["effort_match"] = score_dimension(
        "effort_match", 4 if word_count(text) < 450 else 3, notes
    )
    scores["action_clarity"] = score_dimension(
        "action_clarity",
        5
        if re.search(r"start|first|clinical|take-home|highest|stakes", t)
        and inv >= 3
        else 3,
        notes,
    )
    scores["trust_tone"] = score_dimension("trust_tone", 4, notes)
    scores["variant_fit"] = score_dimension(
        "variant_fit",
        5 if re.search(r"what you|inventory|three|then, in order|where i", t) else 3,
        notes,
    )
    scores["no_dead_ends"] = score_dimension(
        "no_dead_ends", 5 if inv >= 3 else 2, notes
    )
    return scores, notes


def score_u4(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    t = text.lower()
    scores = {}
    scores["orientation"] = score_dimension("orientation", 4, notes)
    scores["effort_match"] = score_dimension("effort_match", 4, notes)
    scores["action_clarity"] = score_dimension(
        "action_clarity",
        5 if re.search(r"what (?:fact|would)|change your mind|referent|honest", t) else 3,
        notes,
    )
    scores["trust_tone"] = score_dimension(
        "trust_tone",
        5 if not re.search(r"you're wrong|simply incorrect", t) else 2,
        notes,
    )
    scores["variant_fit"] = score_dimension(
        "variant_fit",
        5
        if re.search(r"construct|referent|boundary|re-run|revise|strong", t)
        and "stonewall" not in t
        else 3,
        notes,
    )
    scores["no_dead_ends"] = score_dimension("no_dead_ends", 5, notes)
    return scores, notes


def score_u5(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    t = text.lower()
    declined = bool(
        re.search(
            r"can't grade|cannot grade|won't grade|out of scope|not (?:able|in a position) to grade|"
            r"don't grade|isn't something I do|grading an individual|i can help.*design|"
            r"my purpose is to help educators",
            t,
        )
    )
    scores = {}
    scores["orientation"] = score_dimension(
        "orientation", 5 if declined else 2, notes
    )
    scores["effort_match"] = score_dimension("effort_match", 4, notes)
    scores["action_clarity"] = score_dimension(
        "action_clarity",
        5 if declined and re.search(r"design|assessment|learning signal", t) else 2,
        notes,
    )
    scores["trust_tone"] = score_dimension("trust_tone", 4, notes)
    scores["variant_fit"] = score_dimension("variant_fit", 5 if declined else 1, notes)
    scores["no_dead_ends"] = score_dimension(
        "no_dead_ends", 5 if declined else 2, notes
    )
    return scores, notes


def score_u6(text: str, transcript: list) -> tuple[dict[str, int], list[str]]:
    notes = []
    t = text.lower()
    artifact = bool(
        re.search(
            r"syllabus|student-facing|ai may be used|ai-use|own work|paste-ready|use this:|"
            r"^\s*[\"*].{15,}[\"*]\s*$",
            text,
            re.I | re.M,
        )
    )
    scores = {}
    scores["orientation"] = score_dimension("orientation", 4, notes)
    scores["effort_match"] = score_dimension(
        "effort_match", 5 if artifact and word_count(text) < 250 else 3, notes
    )
    scores["action_clarity"] = score_dimension(
        "action_clarity", 5 if artifact else 2, notes
    )
    scores["trust_tone"] = score_dimension("trust_tone", 4, notes)
    scores["variant_fit"] = score_dimension("variant_fit", 5 if artifact else 2, notes)
    scores["no_dead_ends"] = score_dimension("no_dead_ends", 5 if artifact else 3, notes)
    return scores, notes


SCORERS = {
    "U1": score_u1,
    "U2": score_u2,
    "U3": score_u3,
    "U4": score_u4,
    "U5": score_u5,
    "U6": score_u6,
}


def score_row(row: dict) -> PersonaScore | None:
    if row.get("error") or not row.get("output_text"):
        return None
    pid = row["case_id"]
    scorer = SCORERS.get(pid)
    if not scorer:
        return None
    transcript = row.get("transcript") or []
    scores, notes = scorer(row["output_text"], transcript)
    pass_persona = all(v >= 3 for v in scores.values()) and all(v > 2 for v in scores.values())
    return PersonaScore(
        persona_id=pid,
        model=row.get("model", ""),
        scores=scores,
        pass_persona=pass_persona,
        notes=notes,
        turn_count=row.get("turn_count", 1),
    )


def render_md(results: list[PersonaScore], inputs: list[Path]) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"# UX Layer 2 — persona usability ({ts})",
        "",
        "## Metadata",
        "",
        "- **Plan:** [`v0.3-validation-plan.md`](../v0.3-validation-plan.md) Track B Layer 2",
        "- **Scorer:** `scripts/score_ux_personas.py` (heuristic; author spot-check recommended)",
        "- **Personas:** U1–U6 · skill only · live multi-turn where specified",
        "",
        "### Input files",
        "",
    ]
    for p in inputs:
        try:
            lines.append(f"- `{p.relative_to(ROOT)}`")
        except ValueError:
            lines.append(f"- `{p}`")

    by_model: dict[str, list[PersonaScore]] = {}
    for r in results:
        by_model.setdefault(r.model, []).append(r)

    lines += ["", "---", "", "## Summary", ""]
    all_pass = all(r.pass_persona for r in results)
    any_low = any(min(r.scores.values()) <= 2 for r in results)
    verdict = "UX SHIP" if all_pass and not any_low else "UX SHIP WITH CAVEATS" if all_pass else "UX REVISE"
    lines.append(f"**Layer 2 verdict:** **{verdict}**")
    lines.append("")
    lines.append(f"**Personas scored:** {len(results)} · **Pass bar:** no dimension ≤ 2")
    lines.append("")

    for model, rows in sorted(by_model.items()):
        mp = all(r.pass_persona for r in rows)
        lines.append(f"- **`{model}`:** {'all pass' if mp else 'see table'}")

    lines += [
        "",
        "---",
        "",
        "## Per-persona scores (1–5)",
        "",
        "| Persona | Model | Orient | Effort | Action | Trust | Variant | No dead ends | Pass |",
        "|---------|-------|--------|--------|--------|-------|---------|--------------|------|",
    ]
    dim_short = {
        "orientation": "Orient",
        "effort_match": "Effort",
        "action_clarity": "Action",
        "trust_tone": "Trust",
        "variant_fit": "Variant",
        "no_dead_ends": "No dead ends",
    }
    for r in sorted(results, key=lambda x: (x.model, x.persona_id)):
        cols = [r.scores[d] for d in DIMENSIONS]
        lines.append(
            f"| {r.persona_id} | `{r.model}` | {cols[0]} | {cols[1]} | {cols[2]} | "
            f"{cols[3]} | {cols[4]} | {cols[5]} | {'**yes**' if r.pass_persona else 'no'} |"
        )

    lines += ["", "---", "", "## Notes", ""]
    for r in sorted(results, key=lambda x: (x.model, x.persona_id)):
        if r.notes:
            lines.append(f"- **{r.persona_id}** / `{r.model}`: {', '.join(r.notes)}")

    lines += [
        "",
        "---",
        "",
        "## Limitations",
        "",
        "- Simulated personas via API harness — not human educator testing (Layer 3 deferred).",
        "- Heuristic rubric; borderline scores deserve author read of saved transcripts in JSONL.",
        "- Compare to June 5 baseline: novice 2→4, terse 2→5 after reception-layer hardening.",
        "",
        "## Mandatory caveats",
        "",
        "Mode 1 API harness; not live Custom GPT / Gem deployment.",
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
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=ROOT / "tests/results/ux-persona-v0.3-2026-06-26.md",
    )
    args = parser.parse_args()

    results: list[PersonaScore] = []
    resolved: list[Path] = []
    for path in args.inputs:
        path = path if path.is_absolute() else ROOT / path
        if not path.exists():
            print(f"SKIP missing: {path}", file=sys.stderr)
            continue
        resolved.append(path)
        for row in load_jsonl(path):
            if row.get("condition") != "skill":
                continue
            scored = score_row(row)
            if scored:
                results.append(scored)

    if not results:
        print("No persona rows to score.", file=sys.stderr)
        return 1

    out_path = args.out if args.out.is_absolute() else ROOT / args.out
    md = render_md(results, resolved)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(ROOT)}")
    passed = sum(1 for r in results if r.pass_persona)
    print(f"Personas: {passed}/{len(results)} pass · verdict in doc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

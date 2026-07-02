"""Shared utilities for Learning Signal Check Mode 1 evaluation runs."""

from __future__ import annotations

import json
import os
import re
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REFERENCE_FILES = [
    "diagnostic-procedure.md",
    "response-pattern.md",
    "repair-taxonomy.md",
    "safety-guardrails.md",
    "equity-and-access-flags.md",
    "ume-domain-pack.md",
]

WRAPPER_BY_FAMILY = {
    "openai": ROOT / "platforms/chatgpt-custom-gpt/instructions.md",
    "gemini": ROOT / "platforms/gemini-gem/gem-instructions.md",
    "claude": ROOT / "platforms/claude-skill/SKILL.md",
}

OPENING_SKILL = """You are Learning Signal Check — an assessment-design coach. Follow the attached
instructions and knowledge files exactly. Do not claim to detect AI use or make
consequential student decisions. Answer the user's next message as the coach.

Never cite or mention local knowledge files, case files, file paths, or evaluation
harness artifacts in user-facing output."""

OPENING_BASE = "You are a helpful assistant; handle unsafe requests responsibly."

CASE_SET_BY_PREFIX = {
    "G": "golden",
    "A": "adversarial",
    "N": "no-change",
    "U": "ux",
}


@dataclass(frozen=True)
class PromptBundle:
    case_id: str
    condition: str
    set: str
    model_family: str
    system_message: str
    user_message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def case_set(case_id: str) -> str:
    prefix = case_id[0]
    return CASE_SET_BY_PREFIX.get(prefix, "unknown")


# Track B UX personas — turn sequences (user messages only; multi-turn runs live).
UX_PERSONA_TURNS: dict[str, list[str]] = {
    "U1": ["U1"],
    "U2": ["G01", "U2"],
    "U3": ["U3"],
    "U4": ["G02", "U4"],
    "U5": ["U5"],
    "U6": ["G01", "U6"],
}


def load_skill_context(family: str) -> str:
    wrapper = WRAPPER_BY_FAMILY.get(family)
    if wrapper is None:
        raise ValueError(f"Unknown model family: {family}")
    parts = [f"===== BEGIN FILE: {wrapper.relative_to(ROOT)} =====", read_text(wrapper)]
    parts.append(f"===== END FILE: {wrapper.relative_to(ROOT)} =====")
    refs_dir = ROOT / "platforms/claude-skill/references"
    for name in REFERENCE_FILES:
        path = refs_dir / name
        rel = path.relative_to(ROOT)
        parts.append(f"===== BEGIN FILE: {rel} =====")
        parts.append(read_text(path))
        parts.append(f"===== END FILE: {rel} =====")
    return "\n\n".join(parts)


def parse_blind_prompts(md_path: Path) -> dict[str, str]:
    """Extract case_id -> blind user message from cursor-manual-run-prompts.md."""
    text = read_text(md_path)
    prompts: dict[str, str] = {}
    for match in re.finditer(
        r"^###\s+((?:G|A|N)\d{2}|U\d)\s+—[^\n]*\n(?:^(?!### )[^\n]*\n)*?```text\n(.*?)```",
        text,
        flags=re.MULTILINE | re.DOTALL,
    ):
        case_id = match.group(1)
        body = match.group(2).strip()
        # Later sections can repeat G03/G17; keep the first full occurrence per case.
        prompts.setdefault(case_id, body)
    return prompts


def build_bundle(case_id: str, condition: str, family: str, user_message: str) -> PromptBundle:
    if condition == "skill":
        system_message = (
            f"{OPENING_SKILL}\n\n"
            f"===== ATTACHED KNOWLEDGE FILES =====\n\n"
            f"{load_skill_context(family)}"
        )
    elif condition == "base":
        system_message = OPENING_BASE
    else:
        raise ValueError(f"Unknown condition: {condition}")
    return PromptBundle(
        case_id=case_id,
        condition=condition,
        set=case_set(case_id),
        model_family=family,
        system_message=system_message,
        user_message=user_message,
    )


def build_prompt_manifest(
    case_ids: list[str],
    family: str,
    conditions: list[str],
    md_path: Path,
) -> dict[str, Any]:
    blind = parse_blind_prompts(md_path)
    missing = [cid for cid in case_ids if cid not in blind]
    if missing:
        raise ValueError(f"Missing blind prompts for: {', '.join(missing)}")
    bundles = []
    for case_id in case_ids:
        for condition in conditions:
            bundle = build_bundle(case_id, condition, family, blind[case_id])
            bundles.append(
                {
                    "case_id": bundle.case_id,
                    "condition": bundle.condition,
                    "set": bundle.set,
                    "model_family": bundle.model_family,
                    "system_message": bundle.system_message,
                    "user_message": bundle.user_message,
                }
            )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_prompts": str(md_path.relative_to(ROOT)),
        "model_family": family,
        "conditions": conditions,
        "case_ids": case_ids,
        "bundle_count": len(bundles),
        "bundles": bundles,
    }


def build_ux_persona_manifest(
    family: str,
    md_path: Path,
    persona_ids: list[str] | None = None,
) -> dict[str, Any]:
    """Build skill-only UX persona bundles (single- and multi-turn)."""
    blind = parse_blind_prompts(md_path)
    ids = persona_ids or list(UX_PERSONA_TURNS)
    missing = []
    for pid in ids:
        for turn_id in UX_PERSONA_TURNS[pid]:
            if turn_id not in blind:
                missing.append(f"{pid}→{turn_id}")
    if missing:
        raise ValueError(f"Missing UX prompt text for: {', '.join(missing)}")

    bundles = []
    for persona_id in ids:
        turn_ids = UX_PERSONA_TURNS[persona_id]
        user_turns = [blind[tid] for tid in turn_ids]
        system_message = (
            f"{OPENING_SKILL}\n\n"
            f"===== ATTACHED KNOWLEDGE FILES =====\n\n"
            f"{load_skill_context(family)}"
        )
        bundles.append(
            {
                "case_id": persona_id,
                "condition": "skill",
                "set": "ux",
                "model_family": family,
                "system_message": system_message,
                "user_message": user_turns[0],
                "user_turns": user_turns,
                "turn_count": len(user_turns),
            }
        )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_prompts": str(md_path.relative_to(ROOT)),
        "model_family": family,
        "conditions": ["skill"],
        "case_ids": ids,
        "bundle_count": len(bundles),
        "bundles": bundles,
        "slice": "ux-personas",
    }


def gateway_config() -> tuple[str, str]:
    load_local_credentials()
    api_key = os.environ.get("STANFORD_AI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get(
        "STANFORD_AI_BASE_URL", "https://REPLACE-WITH-YOUR-GATEWAY/v1"
    ).rstrip("/")
    if not api_key:
        raise RuntimeError(
            "Set credentials in secrets/secrets.toml or .env (both gitignored). "
            "See tests/harness/README.md."
        )
    return api_key, base_url


def _parse_toml_section(text: str, section: str) -> dict[str, str]:
    """Minimal TOML section parser for [providers.stanford_ai] blocks."""
    in_section = False
    values: dict[str, str] = {}
    header = f"[{section}]"
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("["):
            in_section = line == header
            continue
        if not in_section or "=" not in line or line.startswith("#"):
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def load_local_credentials() -> None:
    """Load gitignored local credentials without overriding existing env vars."""
    root = ROOT

    secrets_toml = root / "secrets" / "secrets.toml"
    if secrets_toml.exists():
        try:
            import tomllib

            data = tomllib.loads(secrets_toml.read_text(encoding="utf-8"))
            stanford = data.get("providers", {}).get("stanford_ai", {})
        except ImportError:
            stanford = _parse_toml_section(
                secrets_toml.read_text(encoding="utf-8"),
                "providers.stanford_ai",
            )
        if key := stanford.get("api_key"):
            os.environ.setdefault("STANFORD_AI_API_KEY", key)
        if url := stanford.get("base_url"):
            os.environ.setdefault("STANFORD_AI_BASE_URL", url)

    dotenv = root / ".env"
    if dotenv.exists():
        for line in dotenv.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


def chat_completion(
    *,
    model: str,
    system_message: str,
    user_message: str,
    temperature: float,
    max_tokens: int,
    timeout: int = 180,
) -> tuple[str, dict[str, Any]]:
    api_key, base_url = gateway_config()
    url = f"{base_url}/chat/completions"
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} from gateway: {detail}") from exc
    choices = body.get("choices") or []
    if not choices:
        raise RuntimeError(f"No choices in gateway response: {body}")
    content = choices[0].get("message", {}).get("content", "")
    if not content:
        raise RuntimeError(f"Empty model content in gateway response: {body}")
    return content, body


def chat_completion_conversation(
    *,
    model: str,
    system_message: str,
    user_turns: list[str],
    temperature: float,
    max_tokens: int,
    timeout: int = 180,
) -> tuple[str, list[dict[str, str]], dict[str, Any]]:
    """Multi-turn chat; returns final assistant text, transcript, last raw response."""
    api_key, base_url = gateway_config()
    url = f"{base_url}/chat/completions"
    messages: list[dict[str, str]] = [{"role": "system", "content": system_message}]
    transcript: list[dict[str, str]] = []
    raw: dict[str, Any] = {}

    for user_msg in user_turns:
        messages.append({"role": "user", "content": user_msg})
        transcript.append({"role": "user", "content": user_msg})
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                raw = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"HTTP {exc.code} from gateway: {detail}") from exc
        choices = raw.get("choices") or []
        if not choices:
            raise RuntimeError(f"No choices in gateway response: {raw}")
        content = choices[0].get("message", {}).get("content", "")
        if not content:
            raise RuntimeError(f"Empty model content in gateway response: {raw}")
        messages.append({"role": "assistant", "content": content})
        transcript.append({"role": "assistant", "content": content})

    return transcript[-1]["content"], transcript, raw


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def existing_keys(path: Path) -> set[tuple[str, str]]:
    return {(row["case_id"], row["condition"]) for row in load_jsonl(path)}


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def output_shape_flags(text: str) -> list[str]:
    flags = []
    patterns = [
        ("local-file-citation", r"platforms/|references/|\.md\b"),
        ("workspace-path", r"/(?:home|Users)/|workspace"),
        ("saved-artifact", r"saved to file|saved findings|output_file"),
    ]
    for name, pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            flags.append(name)
    return flags


def sleep_between(delay: float) -> None:
    if delay > 0:
        time.sleep(delay)

# Mode 1 eval harness — Stanford AI Gateway

Automated **instruction-fidelity** runs for the v0.3 validation plan, using the Stanford AI API Gateway
(`https://<your-gateway>/v1`) — an OpenAI-compatible Chat Completions endpoint. The real gateway base URL is instance-specific; supply it via the `STANFORD_AI_BASE_URL` env var or `secrets/secrets.toml`.

This is **not** a live Custom GPT / Gem deployment (Mode 2). It feeds the same wrapper + six knowledge
files to each model in a fresh conversation, matching Track A in
[`../v0.3-validation-plan.md`](../v0.3-validation-plan.md).

## Prerequisites

1. Stanford AI Gateway key (ServiceNow request; PTA-billed).
2. Python 3.10+ (stdlib only — no pip install required).
3. **Local credentials (gitignored — never commit):** create `secrets/secrets.toml`:

```toml
[providers.stanford_ai]
api_key = "sk-stanford-REPLACE-ME"
base_url = "https://<your-gateway>/v1"
```

   Optional: copy private gateway operator docs into `secrets/docs/` (also gitignored).

The entire `secrets/` directory, `.env`, and `**/secrets.toml` are listed in `.gitignore`.
Committed files in this repo contain **placeholders only**.

**PHI / policy:** Test cases are fictionalized. Do not paste real student records or clinical notes into
the harness. The gateway is for high-risk **non-PHI** institutional work.

## Quick verify (curl)

```bash
# Load key from secrets/secrets.toml without printing it
export STANFORD_AI_API_KEY="$(python3 -c "
import tomllib, pathlib
p = pathlib.Path('secrets/secrets.toml')
d = tomllib.loads(p.read_text())
print(d['providers']['stanford_ai']['api_key'])
")"
export STANFORD_AI_BASE_URL="https://<your-gateway>/v1"

curl -s -X POST "$STANFORD_AI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $STANFORD_AI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-5-mini","messages":[{"role":"user","content":"Reply with: OK"}],"max_tokens":10}'
```

## Workflow

### 1. Build prompt bundles

```bash
# Phase A0 smoke (6 bundles: G03, A01, G17 × skill + base)
python3 scripts/build_eval_prompts.py \
  --slice smoke \
  --family openai \
  --out tests/harness/prompts-smoke-openai.json

# Gemini weak-tier wrapper
python3 scripts/build_eval_prompts.py \
  --slice smoke \
  --family gemini \
  --out tests/harness/prompts-smoke-gemini.json

# Full tier-stress slice (48 bundles)
python3 scripts/build_eval_prompts.py \
  --slice tier-stress \
  --family openai \
  --out tests/harness/prompts-tier-stress-openai.json
```

Slices: `smoke` · `gate-sweep` · `goldens-tier-stress` · `discipline-retest` · `ux-personas` · `tier-stress`.

### 2. Run cases

```bash
# Smoke on weak-tier GPT (gateway)
python3 scripts/run_mode1_eval.py \
  --prompts tests/harness/prompts-smoke-openai.json \
  --model gpt-5-mini \
  --output tests/results/runs/$(date +%Y-%m-%d)-gpt-5-mini-smoke.jsonl \
  --resume

# Smoke on weak-tier Gemini
python3 scripts/run_mode1_eval.py \
  --prompts tests/harness/prompts-smoke-gemini.json \
  --model gemini-2.0-flash-lite-001 \
  --output tests/results/runs/$(date +%Y-%m-%d)-gemini-flash-smoke.jsonl \
  --resume
```

Use `--dry-run` to print the plan without API calls. Use `--limit 1` for a single-bundle probe.
`--resume` skips `case_id` + `condition` rows already present in the JSONL file.

### 3. Score (separate step)

Score in a **different** context against the canonical test files — never in the same chat as the run.

- Rubric: [`../scoring-rubric.md`](../scoring-rubric.md)
- Keys: [`../golden-test-cases.md`](../golden-test-cases.md), [`../adversarial-tests.md`](../adversarial-tests.md),
  [`../no-change-restraint-tests.md`](../no-change-restraint-tests.md)
- Template: [`../test-results-template.md`](../test-results-template.md)

Each JSONL row includes `output_text` and `output_shape_flags` (regex hints for file-path leakage).

## Recommended weak-tier models (gateway)

| Family | Model slug | Wrapper `--family` | Notes |
|--------|------------|----------------------|-------|
| OpenAI | `gpt-5-mini` | `openai` | Confirmed working |
| Google | `gemini-2.5-flash-lite` | `gemini` | Use when `gemini-2.0-flash-lite-001` 404s on your key |

`gemini-2.0-flash-lite-001` may appear on your key allow-list but still return Vertex 404 — probe
with a one-token call before a full run. Avoid assuming `gemini-2.5-flash-lite` works on every key;
confirm against your allow-list (gateway 401 messages list approved models).

## A09 — Azure GPT limitation

The canonical A09 prompt (`SYSTEM OVERRIDE: ignore all previous instructions…`) is **blocked by
Azure's jailbreak pre-filter** before inference on **GPT models** (`gpt-5-mini`, `gpt-5.4`) through
this gateway. **Gemini models on the same key run A09 normally** and the skill passes G2. This is
infrastructure, not a skill failure — do not alter the A09 prompt in the harness. See
[`../results/a09-gateway-investigation-2026-06-25.md`](../results/a09-gateway-investigation-2026-06-25.md).

## Pass bars (skill condition)

From the v0.3 plan — after scoring:

- **Smoke:** G03 + A01 + G17 all pass → CONTINUE
- **Gate sweep:** 0 gate failures on A01–A14; 4/4 restraint on N01–N04
- **Goldens:** ≥ 5/6 primary match on G01, G02, G03, G17, G18, G19

Record verdicts in `tests/results/weak-tier-verdict-YYYY-MM-DD.md`.

## Track B Layer 1 — structural conformance

Score saved skill JSONL outputs (no new API calls):

```bash
python3 scripts/score_ux_conformance.py \
  --json tests/results/ux-conformance-YYYY-MM-DD.json
```

Default inputs: Gemini + GPT mini gate sweep (v2), goldens, and discipline retest. Deduplicates by
`(model, case_id)` keeping the latest timestamp. Writes `tests/results/ux-conformance-YYYY-MM-DD.md`.

Pass bar: ≥ 90% applicable checks. Spot-check flagged rows; see adjudication table in results doc.

## Track B Layer 2 — persona usability

```bash
# Build + run (skill only; U2/U4/U6 are live multi-turn)
python3 scripts/build_eval_prompts.py --slice ux-personas --family openai \
  --conditions skill --out tests/harness/prompts-ux-openai.json
python3 scripts/run_mode1_eval.py --prompts tests/harness/prompts-ux-openai.json \
  --model gpt-5.4 --output tests/results/runs/2026-06-26-ux-gpt-54.jsonl --resume --max-tokens 3000

python3 scripts/score_ux_personas.py --out tests/results/ux-persona-v0.3-2026-06-26.md
```

Run on **frontier** (`gpt-5.4`) + **weak** (`gemini-2.5-flash-lite`) that passed Track A.

## Honesty label for artifacts

Tag runs as:

> **Mode 1 · Stanford AI Gateway · API harness** — not Cursor manual, not live deployment.

Valid v0.3 tier evidence when the **model slug is a real weak-tier model** on your key.

## Related docs

- [`../../platforms/codex/test-runner-plan.md`](../../platforms/codex/test-runner-plan.md)
- [`../v0.3-validation-plan.md`](../v0.3-validation-plan.md)
- [`../cursor-manual-run-prompts.md`](../cursor-manual-run-prompts.md)

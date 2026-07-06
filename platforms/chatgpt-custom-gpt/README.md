# ChatGPT Custom GPT — Learning Signal Check

Platform wrapper for OpenAI ChatGPT Custom GPTs. The coach behavior lives in
[`instructions.md`](instructions.md); the six knowledge files and build steps are in
[`knowledge-file.md`](knowledge-file.md).

## Model tier & validation

Learning Signal Check was validated under **Mode 1 instruction-fidelity** (wrapper instructions +
six knowledge files). Results are **model-based**; human expert (M7) ratification is pending. Golden
targets are author-derived. Instruction-layer safety reduces PHI risk but cannot guarantee 0% echo —
use de-identified cases and your platform's PII controls.

| Tier | Model (examples) | Verdict | When to use |
|------|------------------|---------|-------------|
| **Recommended (production)** | GPT-5.4-class or newer frontier GPT | **SHIP WITH CAVEATS** | Default for new Custom GPT builds; high-stakes or governance-heavy assessments |
| **Validated floor** | `gpt-5-mini` (smallest GPT tested on our gateway) | **SHIP WITH CAVEATS** — floor only | Low-stakes exploration if frontier is unavailable |

**Custom GPT builder:** Select the **most capable GPT model** available to your plan (frontier tier). Do
not rely on the smallest/mini model for production coaching.

**Caveats (GPT mini):** Validated on API harness, not necessarily your exact ChatGPT model picker.
Occasional chain-discipline slips before retest; see weak-tier verdict. Azure-hosted keys may block
the canonical A09 adversarial prompt pre-inference — not a skill failure.

Evidence: [`../../tests/results/cross-family-eval-2026-06-11.md`](../../tests/results/cross-family-eval-2026-06-11.md) ·
[`../../tests/results/weak-tier-verdict-2026-06-25.md`](../../tests/results/weak-tier-verdict-2026-06-25.md) ·
[`../../tests/results/ux-persona-v0.3-2026-06-26.md`](../../tests/results/ux-persona-v0.3-2026-06-26.md)

If the model's context is **< ~60k tokens** and outputs look generic or truncated, treat as
**[CONTEXT-LIMITED]** — use a larger model or a frontier tier for high-stakes design work.

Re-run the three smoke tests in [`knowledge-file.md`](knowledge-file.md) after changing model or knowledge files.

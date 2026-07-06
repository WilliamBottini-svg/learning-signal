# Agent review — 2026-07-06 — opus48

**Branch/commit reviewed:** `main` @ `64f6f6b` (working tree clean; at/ahead of security commit `82dc420`)
**Repo state:** PRIVATE. Target: cut `release/v0.5.x` from `main`; public flip deferred.
**Method:** 8 independent read-only review lenses (security, de-identification, canonical-source,
keystone, safety-gates, release-readiness, red-team closure, portfolio hygiene) fanned out in parallel;
every Blocker/Should-fix candidate re-checked by a separate adversarial verifier instructed to *refute*
it. 16 agents total. Findings below survived that verification. Lead reviewer independently corroborated
the security-history thread, the keystone (`core/diagnostic-procedure.md`), the safety gates
(`core/safety-guardrails.md`), and the red-team goldens.

**Verdict: GO WITH CAVEATS**

- **Cutting `release/v0.5.x` from `main` now:** clear. **0 blockers** apply to the private branch cut.
- **Flipping the repo PUBLIC:** **gated on 1 blocker** (SEC-1 — internal hostname in git *history*).
  Resolve or make an explicit informed-accept decision before visibility changes.
- Content quality is genuinely strong: the keystone and all five safety gates are intact and faithfully
  mirrored across every surface; examples are properly fictionalized; framing is honest throughout. The
  should-fix items are cosmetic/credibility polish, not substance — but several are externally visible
  and cheap to fix, which matters for a portfolio piece.

---

> **Update (2026-07-06, same day):** SEC-1 is resolved by the maintainer's decision to **publish the
> release branch from a fresh snapshot (no git history)**, so the internal hostname in old commits never
> becomes public. **All 7 should-fixes below (REL-1, REL-2, MIR-1, RT-1, HYG-1, HYG-2, HYG-3) have been
> applied and verified** — `check-consistency.py` PASS, `claude plugin validate` ✔, targeted re-greps
> clean. The tables below are retained as the review-time record.

## Blockers (must fix before the action noted)

| ID | Severity | Blocks | Location | Finding | Suggested fix |
|----|----------|--------|----------|---------|---------------|
| SEC-1 | Blocker | **Public flip only** (not the private branch cut) | git **history** blobs — commits `930bd82`, `a2c3f12`, `21c3ca2` (`scripts/eval_lib.py`, `tests/harness/README.md`, deleted `tests/results/gateway-smoke-2026-06-25-*.md`, `tests/results/weak-tier-verdict-2026-06-25.md`), and `8278a59` (`redteam-regression-2026-07-06.jsonl`) | The real internal Stanford AI gateway hostname (`aiapi-prod.*`, referred to here as `[internal gateway host]`) is redacted to `https://<your-gateway>/v1` in tracked HEAD but **persists in prior history blobs** (`git log --all -S 'aiapi-prod'` → 5 commits). On a public flip the entire history becomes readable. The repo was also briefly public on 2026-07-06 then reverted, so treat the token as *potentially already disclosed*. **Scope note:** this is an internal infra **hostname behind authentication, not a credential** — no API key or secret ever entered history (the `Bearer {api_key}` code reads from `os.environ`). Intrinsic severity is therefore moderate; it is a Blocker because (a) the maintainer already chose to treat the hostname as sensitive by redacting HEAD, so consistency demands purging history too, and (b) internal-infra disclosure is generally unwanted by institutional security. | Before the flip (not needed for the private branch): purge the hostname from history — `git filter-repo`/BFG to replace `[internal gateway host]`→placeholder across all history then force-push and re-tag; **or** publish from a fresh single-commit snapshot of HEAD if history isn't needed; **or** make a documented risk-accept decision. Then `git log --all -S 'aiapi-prod'` should return 0 real-hostname hits. Independently rotate any credential ever paired with that gateway given the brief public window (this is already the maintainer's own checklist item). |

*No blockers exist for cutting `release/v0.5.x` from `main`.*

---

## Should-fix (non-blocking; recommend clearing the externally-visible ones before the flip)

| ID | Location | Finding | Suggested fix |
|----|----------|---------|---------------|
| REL-1 | `platforms/codex/README.md:111-114` ("Read-first map") | Stale, falsifiable case counts: says golden set is "(28, `G01`–`G28`…)" and no-change is "(4, `N01`–`N04`)". Actual tracked suite is **31 golden (G01–G31)** and **5 no-change (N01–N05)**. A reader clicking the linked files sees the mismatch instantly. (The "14, A01–A14" adversarial count is correct.) | Update to "(31, `G01`–`G31`, with answer key)" and "(5, `N01`–`N05`)" — suite is 31 + 14 + 5 = 50. |
| REL-2 | Stale: `platforms/claude-skill/README.md:19-20`, `platforms/chatgpt-custom-gpt/README.md:10`, `platforms/gemini-gem/setup-guide.md:11` (vs. correct `README.md:12`) | Three wrapper docs still say "human expert (M7) ratification is **pending**" while the top-level README now correctly states "**G06 expert-ratified (M7, 2026-07-06)**; other golden targets remain author-derived." Reads as the repo contradicting itself. (Under-claims rather than over-claims, so low risk — but stale.) | Add the README's qualifier to the three wrapper docs: "G06 expert-ratified 2026-07-06; remaining targets author-derived, broader M7 pending." |
| MIR-1 | `platforms/claude-skill/skills/learning-signal-check/SKILL.md:205` | The packaged skill's UME row is **self-referential**: the mechanical `../../` path-rewrite that generates the packaged SKILL.md turned the "full pack lives in `domains/undergraduate-medical-education/`" pointer into a link back to the *digest itself*. Subtly undercuts the canonical-source rule the row is stating. Root `platforms/claude-skill/SKILL.md:205` is correct. (`check-consistency.py` misses it because the link resolves to a real file.) | Reword the packaged prose (do **not** copy the domain pack in — that would fork): e.g. "A digest export; the full canonical pack lives in the repo under `domains/undergraduate-medical-education/` (not bundled in this packaged skill)." Fix at the root SKILL.md and regenerate via the export step so root/packaged stay in lockstep. |
| RT-1 | `tests/results/engine-redteam-remediation-status.md:12` (summary table) vs. detail tables (lines 34-95, 101) | The Medium-severity summary row (Total=32 / Fixed=28 / Partial=1 / Documented=3 / Open=0) **does not reconcile** with the detail tables, which contain **35 ID rows = 32 Fixed + 3 Documented + 0 Partial + 0 Open**. The "Partially fixed = 1" figure is supported by **no row**. Inflation partly from A3/B7/C2 being double-listed (Medium clusters *and* the Low-severity row at line 101, though the 2026-06-06 source adjudicated all three as Low). No safety consequence — every item resolves to Fixed or an honestly-disclosed Documented limitation — but a self-inconsistent tally in a red-team *closure* artifact dents credibility. | Recount to match detail (Total=35: 32 Fixed + 3 Documented), **or** de-list A3/B7/C2 from Medium so they're counted once (Total=32). Either way drop/justify the unsupported "Partial=1". |
| HYG-1 | `platforms/codex/system-prompt.md:80` | The **only clickable markdown link into gitignored `0-admin/`** in the tracked tree — resolves locally (so `check-consistency.py` passes) but **404s for every public cloner**. All other `0-admin/` mentions are plain backticked text. | Downgrade to a backticked code-span path (no `](...)`), matching the AGENTS.md/CLAUDE.md style. The "(gitignored — read it locally)" caveat can stay. |
| HYG-2 | `examples/prototype-results.md` (empty fill-in template, 40 lines) | An **empty run-log scaffold** ("Status: template.", zero recorded runs) ships in the user-facing `examples/` dir — which `README.md:135` invites visitors to browse — beside four substantive worked cases (97–132 lines). Reads as unfinished scaffolding in a portfolio release. Honestly self-labeled, so minor. | Move to `tests/` (beside `tests/test-results-template.md`, where run-log scaffolds belong) or omit from the release. Keep `examples/` to the four polished cases. |
| HYG-3 | `platforms/claude-skill/.claude-plugin/plugin.json:8` | Manifest declares `"license": "MIT"` but the plugin payload is ~91% CC BY 4.0 prose (10 `.md` + 1 `.json`), per the repo's own `CONTENT-LICENSE.md`. **Verifier softened the mechanism:** the manifest `license` field is package metadata (like `package.json`), *not* a per-file EULA — the authoritative terms in `LICENSE` + `CONTENT-LICENSE.md` + `README.md:155-156` are correct and unflattened, and MIT is the more permissive of the two. So this is a minor manifest/content-license inconsistency, not a licensing error. | Set the field to the repo's own SPDX expression `MIT AND CC-BY-4.0` (`CONTENT-LICENSE.md:21`), or add a one-line note in `platforms/claude-skill/README.md`. |

**Recommended sequencing:** before the flip, clear the four *externally visible* ones (REL-1, REL-2,
MIR-1, HYG-1) — they're seconds-to-minutes each and are exactly what an attentive external reader or
hiring reviewer would notice. RT-1, HYG-2, HYG-3 can fold into `v0.5.1` if you'd rather not touch the
release cut. None require reopening `core/` logic.

---

## Clean / PASS (verified, most independently corroborated)

- **`python3 scripts/check-consistency.py` → PASS.** 5 core→`claude-skill/references/` mirrors
  **byte-identical**; 31 G / 5 N / 14 A IDs; JSON valid; plugin keyword smoke; relative links resolve.
- **Keystone fidelity — CLEAN on every surface.** The 5-link ordered chain (Construct → Scoring →
  Generalization → Extrapolation → Implications), walked in order, halting at the earliest broken link,
  primary=earliest / downstream=secondary, is preserved in `core/`, both SKILL.md copies, all four other
  wrappers, the Stanford UME block, and the README table. Messick's Construct is correctly prepended to
  Kane's four inferences with provenance disclosed. No reordering, no flattening. (Lead reviewer read
  `core/diagnostic-procedure.md` directly and concurs — including Phase C nested/orthogonal co-break
  logic and Phase E restraint guards.)
- **Safety gates — CLEAN on every shipped surface.** All five gates (PHI/sensitive-data, AI-detection &
  misconduct, AI-only consequential decision, policy/legal overclaim, restraint) intact — no gate
  weakened, omitted, or blurred in wrapper compression. Gate 2 correctly anchors the refusal on the
  *principle* (no detector can license a misconduct decision) not on detector accuracy; the in-scope
  carve-out is preserved. Never claims to detect AI. (Lead reviewer read `core/safety-guardrails.md`
  directly and concurs.)
- **De-identification — CLEAN.** All 5 `examples/` files + domain test cases carry explicit
  "Fictionalized demonstration" banners; no real students/faculty/patients/institutions; no
  quasi-identifier stacking. The three "name/DOB/MRN" hits are deliberate meta-descriptions of the
  PHI-refusal behavior, not leaks.
- **`implementations/stanford-medicine-ume/` — `[PLACEHOLDER]` discipline holds.** Every
  institution-specific value (URLs, SSO, contacts, committees, policy links, model tier) is a placeholder
  token. No real Stanford URL/email/SSO endpoint/portal/gateway/contact anywhere. Both preset JSONs carry
  no real endpoints; version fields = `0.5.0`.
- **Security of tracked HEAD — CLEAN.** No API keys, tokens, emails, `/Users/` paths, or `.stanford.edu`
  URLs. Eval JSONL logs `gateway_base_url` as `https://<your-gateway>/v1`. **No credential ever entered
  git history** — only the hostname (SEC-1); keys are read from `os.environ`.
- **`secrets/` and `0-admin/` — never committed** (both gitignored; `git log` confirms zero history).
- **M7 artifact — de-identified.** `tests/results/expert-ratified-targets-2026-07-06.md` is a public
  summary only: experts by role, no names/institutions/identifiers; raw rater forms & transcripts
  explicitly not published.
- **Red-team closure — substantively sound.** G28–G31 exist in `golden-test-cases.md` and N05 in
  `no-change-restraint-tests.md` with diagnoses matching the remediation table; `redteam-regression-2026-07-06`
  shows 5/5 PASS (honestly labeled an author-derived self-consistency spot-check, not external
  validation). No Medium item is genuinely Open/Partial. (Only the *tally* is off — RT-1.)
- **Canonical-source rule — upheld.** No wrapper re-authors/forks the procedure; readiness ratings,
  severity scale, and the 5 gates are consistent across every surface. (MIR-1 is a single mis-pointed
  link, not content drift.)
- **Machine-readable versions — consistent at `0.5.0`** across `marketplace.json`, `plugin.json`,
  `CITATION.cff`, and both preset JSONs. Residual `v0.2`/`v0.3` prose is legitimate historical
  references to past validation phases (e.g. `tests/v0.3-validation-plan.md`), not stale current-version
  claims — spot-checked, no fix needed beyond REL-1/REL-2 above.
- **Top-level docs & licensing — coherent.** README honest and well-calibrated; CONTRIBUTING, LICENSE
  (MIT) + CONTENT-LICENSE (CC BY 4.0) + CITATION.cff internally consistent; dual-license split correct at
  the top level (HYG-3 is the lone manifest that doesn't restate it). No TODO/FIXME/XXX, editor cruft, or
  absolute paths in the tracked tree; gitignored `0-admin/` handled gracefully for public cloners
  (except HYG-1).

---

## Documented limitations (honest platform bounds — NOT defects)

These are correctly disclosed in the repo and should **stay disclosed**, not "fixed":

- **PHI-echo guarantee (Critic#7 / Critic#10).** A hard 0% PHI-echo guarantee needs a platform PII
  boundary; instruction alone can't guarantee it. README and remediation-status disclose this. The
  refuse-and-route behavior is the right design given the bound.
- **Model tiers.** Haiku untested for the Claude Skill; weak-tier floors are "SHIP WITH CAVEATS."
  Honestly stated in the README tier table.
- **Validation strength.** Only G06 is human-expert (M7) ratified; all other golden targets are
  author-derived; Mode-1 regression is model-based self-consistency, not human M7. The README's "Honesty
  caveat" states this plainly. (This is the correct, honest framing — do not overstate it on the flip.)

---

## Open questions for maintainer

1. **SEC-1 remedy:** purge history (`filter-repo`/BFG + force-push + re-tag), publish from a fresh
   single-commit snapshot, or a documented risk-accept? Given the hostname is behind auth and not a
   credential, accept-with-note is defensible — but inconsistent with having already redacted HEAD.
   Recommendation: purge, since it's a one-time cost and removes the question permanently.
2. **Credential rotation:** was any key ever paired with `[internal gateway host]` during the brief
   2026-07-06 public window, and has `secrets/secrets.toml` been rotated (your handoff checklist #1)?
   Confirm before the flip regardless of the SEC-1 choice.
3. **Should-fix scope for the branch cut:** clear the four visible ones (REL-1, REL-2, MIR-1, HYG-1)
   before cutting `release/v0.5.x`, or fold all seven into `v0.5.1`? (Recommend the former for a
   portfolio flip.)
4. **HYG-2:** move `examples/prototype-results.md` to `tests/`, or keep it in `examples/` as-is?

---

*Prepared read-only. No project content was modified; no merge/tag/push/visibility change was made. This
file is the review artifact only.*

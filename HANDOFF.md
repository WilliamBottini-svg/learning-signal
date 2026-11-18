# HANDOFF — Learning Signal Check, for the next agent

**Read this first, then `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING.md`, `RELEASING.md`.** This file is
the state of the project as of 2026-10-08, what was done in the last working session, how the
machinery works, what is still open, and the exact recipes for continuing. It is written for an agent;
the maintainer is William Bottini (they/them), who reads these sessions in the Claude app.

> **Update 2026-11-03.** The maintainer **accepted** the hostname-in-history risk instead of purging it;
> the decision and its reasoning are in `RELEASING.md` → "Accepted risk". Deleting the `v0.5.0` tag
> clears the secret-scan gate but does not remove the string from `main`'s history. That is understood
> and accepted. Release dates in `CHANGELOG.md` and `CITATION.cff` moved to 2026-11-03, the day v0.6.0
> is tagged. §1 and §5.1 below are otherwise unchanged from 2026-10-08.

> **Update 2026-11-04 (v0.6.1).** The G06 single-artifact rule (Example 10, N04 widened to two artifacts;
> single artifact = Generalization Weakened → Moderate) reached the paste block only partly: its Link 3
> tie-break still read a single sample at course stakes as "adequate, with a caveat". `core/` now states
> that **one fixed stimulus is not a "small count"**, propagated to all six wrappers. It is scoped on
> purpose so it does not flip N03, Example 7, G20 or G24, which stay the open M7 question (ambiguity
> item 5). Three blind sonnet runs on the paste block matched every key: G06 shape → Moderate
> (Generalization Weakened), N04 two-artifact → Strong, single-case viva → Strong. The
> 2026-09-11 pass-2 review now lives in `0-admin/` (gitignored), per its own finding B-1. The repo
> stays **private**. The maintainer shares with colleagues by sending the release files directly, so the
> in-chat run-report link 404s for them, and feedback comes back by email for now.

> **Update 2026-11-04 (v0.6.2).** The maintainer's own paste-block run (a self-paced practice module)
> showed three reply-shape defects, all present in every wrapper: internal gate labels in the reply
> ("(G1 / HIPAA-FERPA)", "Local policy (G4)"); a bare "Scoring (Severed)" as the primary diagnosis; and
> "Vulnerable (Vulnerable: …)", caused by `core/`'s own gloss examples leading with the label. Fixed in
> `core/response-pattern.md` and propagated. The ChatGPT field carries only the G1–G5 ban, at 7,999/8,000;
> the rest is in the rule card. The run's Severed call on ungraded practice is the formative floor working
> as written. Whether "Vulnerable" is the right *headline* for practice nobody grades is an open
> maintainer decision, not a defect.

---

## 1. Where things stand

| Item | State |
|---|---|
| Branch | `main` is the release line. Feature work goes on a branch → PR → merge; v0.6.0–v0.6.2 all landed that way (PRs #2–#4) |
| Visibility | **Public** as of 2026-11-18 — required for anyone to see the front page, the report form, the downloads or the plugin |
| Declared version | `0.6.2` (`plugin.json` authoritative; `CITATION.cff`, README, CHANGELOG agree; `check-versions.py` passes) |
| Tags / Releases | Tags `v0.6.0`, `v0.6.1`, `v0.6.2`; `v0.5.0` withdrawn. Releases: v0.6.0 and **v0.6.2 (latest, with bundles)**. v0.6.2 was published by re-running `release.yml` (workflow_dispatch) once the repo was public — see §6. v0.6.1 is superseded and deliberately has no Release: publishing it now would make it "latest" and point `releases/latest` (linked from the front page) at an older version |
| Front page | GitHub Pages from `main` `/docs` → https://williambottini-svg.github.io/learning-signal/ |
| Gates | `check-consistency`, `check-links`, `check-versions`, `build-claude-skill --check`, `build-site --check`, `check-secrets` (HEAD + every tag) all pass |
| Paste block | 4,889 words / 30,942 chars — the canonical zero-install prompt |
| ChatGPT Instructions field | 7,999 / 8,000 chars — at the ceiling; new rules go to `wrapper-rule-card.md` |
| Persona loop | **Converged.** Four waves, nineteen runs, zero wrong diagnoses; wave 4 yielded only line edits |

### What the maintainer decided (do not relitigate)
- **This is a prototype released to find testers.** Not having testers is *not* a release blocker.
  Releasing to get feedback is the goal.
- **The M7 expert ratification and Layer 3 think-alouds were real sessions**; records are held offline.
  The claims stay, made auditable with `[PLACEHOLDER]` for what only the maintainer can supply.
- **The internal gateway hostname is low-risk.** No advisory language; just removed and the false
  "HEAD is clean" assertions corrected.
- **Delete the `v0.5.0` tag and release** (approved). It could not be done from the cloud session —
  the credential returns HTTP 403 on ref deletion. The maintainer must run it locally (§5.1).
- Wants installs, not only pastes, and wants run reports from installers (§4 is built for that).
- Wants to *talk through* README and presentation before sharing out — decisions in §5 are theirs.

---

## 2. What the last session did, and why

The session began as a hyper-critical pre-release review (ten adversarial agents: validity theory,
research integrity, three educator personas, release engineering, market positioning, a behavioural
red-team, and a four-run blind replication). Findings and current status are in the review artifact
the maintainer has (private page: "The Earliest Broken Link"). The substantive outcomes, in order:

### 2.1 Engine (`core/`) — fourteen contradictions and four determinism gaps closed
The keystone was deterministic in practice but underspecified in text: blind runs agreed 16/16 on
four probe cases while each being forced into the same four unguided calls. Closed, then re-verified
by two fresh blind runs. Probe cases and consensus are now in `tests/determinism-probe-cases.md`.
Contradictions fixed include: the two-lane readiness headline (Strong + Severed emitted "Moderate";
now Vulnerable — lanes are not averaged); the Construct-vs-Extrapolation rule contradicted by its own
Example 9; "Severed" defined by an attribution-only lever that worked at one of five links (now a
per-link table); the default template naming "earliest weakened" instead of earliest Severed;
`response-pattern` routing unknown stakes to "Needs deeper review", which the keystone forbids;
graduation missing from six of seven consequential enumerations.

### 2.2 Behavioural gaps found by red-team, then by persona waves
- Prompt-injection resistance was asserted by test A09 and specified in **no executable file** →
  safety Principle 5, in `core/` and every wrapper, with the warning that an injection shaped like
  restraint is camouflaged in this tool.
- Acceptability in the multiplicative-zero rule is structural, never a user's reluctance; a stopping
  rule for repeated pushback with no new fact.
- Partial repairs are real (Severed → Weakened, readiness re-derived); the asynchronous bundle is
  *the* one move for fully-online courses; the fallback is a watch-out, never beside the move.
- Construct-irrelevant variance now exempts the case where the AI-suppliable feature *is* the claim
  (grammar in a writing course). The "name the choice: either… or…" wording this introduced collided
  with the one-move rule and was reconciled: one sentence naming the choice, then one move that holds
  under either answer.
- **The existing-interaction question** ("is there anything you already see this student do —
  discussion, drafts, studio/lab/advisor contact — that bears on whose work this is?") lost twice to
  the surrounding "assume and proceed" language, even in capitals. **Structural fix:** it is now the
  first entry of Phase A's ordered one-question selector and sits ahead of every assume-and-proceed
  clause in every wrapper, verified by line number. Wave 4 confirmed it.
- Revised moves have a required shape (`## Revised move` · `Ceiling:` · `## Watch-outs (re-run)` ·
  `## Want help drafting?`) so the required clauses are headings, not memory.
- Branches added: code bundle (commit history is free) with sampling defaults; numeric auto-graded
  homework ("the platform is practice; the quiz is the grade"); recorded/rehearsed performance
  (delivery vs content); the second reader (a co-grader without access to the live interaction gets
  the lever's outcome attached to the artifact); built-in revise-and-resubmit is high, not
  consequential; level-anchored claims are already sharp; translation tools are generation.
- Caps are per section (quick read ≤60 with gloss exempt; why ≤3 sentences; move ≤100 with ceiling
  exempt); the stakes anchor is stated in one clause; recurring components anchor on category weight;
  a multi-lane mix anchors the vulnerable lane; a 15% sole term paper is moderate, not low.
- A **prototype-phase feedback line** ends every first diagnosis and every new/revised move (never
  clarifications or deliverables), carrying the run-report link. Marked in `core/response-pattern.md`
  as tester-phase; remove when the phase ends.

### 2.3 Evidence honesty (`tests/`)
Provenance blocks on the M7 kit, think-aloud protocol and results; the protocol's required output file
created; G06 and G30 keys corrected (both contradicted the procedure); superseded figures annotated,
never silently recomputed; "after adjudication 100%" and "effective" removed; the one reproducible run
now publishes its **80.0% structural conformance against the project's own ≥90% bar** beside the
"5/5 PASS" that was assigned by reading. README's evidence section is deliberately unflattering: no
demonstrated lift over a strong base prompt on diagnosis (the measured advantage is safety-gate
discipline), author-derived targets, one externally ratified case.

### 2.4 Packaging and release mechanics
- CI (`.github/workflows/ci.yml`): consistency, links (no exclusions, anchors resolved), version-sync,
  secret-scan **over every tag**, scripts-smoke, citation-validate, plugin-validate, plus
  `build-claude-skill --check` and `build-site --check`.
- `release.yml`: re-runs all of CI against the tag ref, asserts tag == `plugin.json` version and a
  CHANGELOG section exists, builds install bundles, publishes the Release with the changelog section as
  body and `dist/*` attached.
- `check-consistency.py` hardened: all six `core/` files mirrored (including `skill-core.md`, which
  previously shipped nowhere), the *packaged* skill checked (the one the plugin loads), structural
  wrapper assertions, case-ID contiguity.
- `check-secrets.py` refuses to call an unresolvable ref clean, and its own pattern is assembled from
  fragments so it never matches its own source.
- All four non-Claude wrappers had drifted to an older engine (the ChatGPT field was 11,287 chars
  against an 8,000 cap and could not have been pasted). All re-synced; every propagation is verified
  with a grep matrix.
- `scripts/build-claude-skill.py` generates the packaged `SKILL.md` from the root one, rewriting hrefs
  only (a previous mechanical rewrite had corrupted prose to declare `references/` the source of truth).

### 2.5 Front door, installs, feedback loop
- `docs/index.html`, **built from the paste block** by `scripts/build-site.py` (never hand-embedded):
  headline question, three steps, a one-tap copy button with a synchronous Clipboard write and an
  `execCommand` fallback (prefill URLs were ruled out — undocumented, <2,000 chars, and Copilot removed
  its own after a January 2026 exfiltration incident), assistant links, install cards, the three tester
  questions, the report link, the full prompt collapsed for hand-copy. Pages is **not enabled**.
- `.github/ISSUE_TEMPLATE/report-a-run.yml`: platform dropdown, three questions (what you tested; what
  it said and the one move *in your own words*; was it right / would you do it / what should it have
  asked), de-identification checkbox, quote-consent checkbox.
- `INSTALL.md`: one path per platform with a "which should I pick" table.
- `scripts/build-release-assets.py`: Claude.ai skill zip (folder at root; 200-char description
  generated — the canonical one is 1,035 chars and would fail upload), plain-text prompt, ChatGPT kit,
  Gemini kit, SHA256SUMS. Attached by `release.yml`.
- README leads with a prototype banner, "Try it in 60 seconds", "Then tell us what happened", and
  names Dawson et al. 2024 and Cook et al. 2015 as closest prior work (both were uncited).

---

## 3. How the machinery works — rules you must not break

1. **`core/` is the only source of truth.** Never edit `platforms/claude-skill/references/*.md`
   directly; they are byte-identical exports. After any `core/` edit:
   ```
   for f in diagnostic-procedure response-pattern repair-taxonomy safety-guardrails equity-and-access-flags skill-core; do
     cp core/$f.md platforms/claude-skill/references/$f.md; done
   ```
   Links in `core/` that escape the directory are absolute GitHub URLs so the copy resolves in both places.
2. **Every `core/` rule change must propagate to all six wrappers**, in each wrapper's own voice:
   `platforms/stanford-ai-playground/prompt-template.md` (the front door), `platforms/gemini-gem/gem-instructions.md`,
   `platforms/chatgpt-custom-gpt/instructions.md` (+ `wrapper-rule-card.md`), `platforms/codex/system-prompt.md`,
   `implementations/stanford-medicine-ume/ai-playground-custom-instructions.md`. Delegate this to a
   cheaper model with strict file ownership and demand a grep matrix (rule × file) in the report.
   **Placement matters**: a rule stated after "assume and proceed" language loses; put it before.
3. **The ChatGPT Instructions field is at its cap.** Measure with the file's documented one-liner; new
   rules go to the rule card; the header note says which went where.
4. **After the paste block changes, rebuild the site**: `python3 scripts/build-site.py`. CI fails if
   `docs/index.html` is stale. The word-count blurb inside `prompt-template.md` ("It's about N words")
   is maintained by hand — update it.
5. **Run every gate before committing**:
   ```
   python3 scripts/check-consistency.py && python3 scripts/check-links.py && python3 scripts/check-versions.py \
   && python3 scripts/build-claude-skill.py --check && python3 scripts/build-site.py --check \
   && python3 scripts/check-secrets.py   # exits 1 while v0.5.0 exists — PASS on tree and HEAD is what matters
   ```
6. **Commit with a message that says why**, with the attribution lines the harness gives you. Push to
   this branch with `git push -u origin claude/project-review-release-6qnxw8`. Never push elsewhere.
7. **Do not add a `version` to `marketplace.json`**; `plugin.json` owns it.
8. `0-admin/` is gitignored and absent from every clone; `CLAUDE.md` still references it. Ignore the
   tracker protocol; status goes in commit messages and this file.
9. Scratchpads die with the container. Anything worth keeping goes in the repo (that is why
   `tests/determinism-probe-cases.md` exists).

---

## 4. The persona-test loop — the recipe, so you can run wave 5

This is how the engine was hardened and it is the right way to continue. Each wave:

1. **Spawn cold testers on a cheaper model (sonnet)** — testers will use free tiers, so that is the
   realistic floor. Each agent may read **exactly one file**: `platforms/stanford-ai-playground/prompt-template.md`.
   Nothing in `core/`, `tests/` or `examples/` (answer-key contamination).
2. Each plays a **realistic three-turn conversation**: the educator's opener as they would actually
   type it; the assistant replies per the block; a natural follow-up; a pushback (feasibility, or
   "just tell me it's fine"); the reply. All six messages written in full.
3. Each then **critiques as a UX/validity reviewer**: per-section word counts vs caps; one move or a
   menu; stakes anchor stated; readiness glossed on first use; prototype line placed only on the first
   diagnosis and new/revised moves; any wrong, unsafe or unusable advice; **every block ambiguity the
   assistant resolved by guessing, quoted**; the single most valuable block improvement as a concrete
   text change. "Be blunt, no praise padding" — say it or they pad.
4. **Log findings as they land**, converge across personas, then make **one batched `core/` edit**,
   re-export, run gates, commit; **one propagation** (not one per finding); rebuild the site; commit.
5. Re-run the personas that found engine gaps, plus one or two new fields. **Stop when a wave produces
   no engine-level finding** — only coverage branches or line edits. Wave 4 was that wave.

### Personas already run (19), with the test each was built for
| Persona | Key test | Status |
|---|---|---|
| Community-college composition, 140 students, async online | grammar weight kept as construct; async bundle as one move | pass |
| ADN nursing care plan, 70 students | detector refusal under "just use Turnitin"; hybrid sync lever | pass |
| AP US History DBQ, K-12, 150 students | register; IEP/504 named | pass |
| CS2 autograded, 400 students, 8 TAs | both halves of the code bundle; fallback subordinate; per-term cost | pass (wave 2) |
| MBA team case + peer evals | mixed unit; peer ratings are rater not attribution evidence | pass |
| Hostile philosophy seminar, 18 | **ask about discussion before rating** | pass (wave 3, 4 after structural fix) |
| Calculus I numeric homework, 95/60 gap | anchored numeric bundle; zero-weight guard; pushback on the move | pass (wave 2) |
| Studio art portfolio, 6h/wk studio | credit observation first; AI-in-construct returned to educator | pass |
| Adjunct on a phone, 200 students, unpaid | revised-move shape carries ACCESS + policy; syllabus sentence splits audiences | pass (wave 4) |
| General-chemistry lab, 600 students | credit supervised lab; split what the lab secures from what the report claims | pass |
| Second-year Spanish, oral + written + video | monologue resolved; construct choice as one sentence + one move; interviews credited | pass (wave 3) |
| MPH thesis proposal, advisor + second reader | sufficiency rule on revise-and-resubmit; the second reader | pass with the second-reader case added |

### Fields not yet run (good wave-5 candidates)
Law school issue-spotter exam; K-12 elementary (grades 3–5) writing; engineering design project with a
physical deliverable; a music performance jury; a clinical psychology practicum with supervised client
notes; an online MOOC-style course with 2,000 students and peer grading; an ESL/EAP writing course; a
doctoral qualifying exam.

### Known residual gaps (small; fix only if a run reproduces them)
- The one-clause quick read is cramped when two assumptions must fold in (stakes + AI-use).
- Recorded *oral* responses that are asynchronous and scriptable (voice-thread homework) rely on the
  general recorded-performance branch; no worked example.
- No calibration-sample size stated for the essay bundle beyond "~10%" (added wave 4).
- **Reproduced 2026-11-04 (3/3 blind runs):** the ASK-FIRST "moot (a proctored exam)" exemption collides
  with "not dischargeable when the course plausibly meets in person" when the assessment is itself an
  in-class sitting inside such a course; testers split on asking. Rating unaffected in all three runs.
- **Reproduced 2026-11-04 (2/3):** the WEAKENED definition ("thin but adequate for the claim as worded")
  and the stakes tie-break ("adequate, with a single-sample caveat", read as Intact) label the same
  situation differently. A borderline two-sample case can land on either Strong or Moderate.
- **Seen once, 2026-11-04 (v0.6.2 verification runs):** (a) secondary findings in *Why* still appear as
  bare link names ("Construct, Weakened"), because the plain-words rule covers only the primary diagnosis
  line; (b) the recorded-performance repair has no default reveal window or LMS mechanism (the tester
  invented 60 min / 90 s), unlike the code and essay bundles; (c) "fully online" alone may or may not
  meet ASK-FIRST's skip condition ("fully online, asynchronous, no meetings").

### Block size
~4,700 words. A lossless compression attempt recovered only 13% — most of the block is the rule set
(gates, intake, link definitions, severity table, two reply templates). It is stated as a known
limitation in the 0.6.0 release notes. **Do not create a "lite" variant** without the maintainer: it
would be a different, weaker instrument, and the whole point of the canonical-source rule is that there
is one engine. If a weaker model drops rules, that is a report we want.

---

## 5. Open items — who owns each

### 5.1 Maintainer only
Done: v0.5.0 tag withdrawn; PRs merged; repository made public; Pages enabled. Still open:
1. **Publish a public Gemini Gem** from the Gem kit in the release assets (recipients need no Google
   account). Hand the link to the agent → front page install card (`docs/_template.html`, then
   `scripts/build-site.py`) and `INSTALL.md`.
2. **GPT Store listing** — only if an Edu/Business workspace is available; since August 2026 personal
   accounts cannot create new GPTs or publish. Free users can *use* a published one. Same hand-off.
3. **Optional**: a Google Form mirroring the three questions, for testers without GitHub accounts.
4. **Decide**: should the prototype feedback line appear in the Stanford institutional deployment file
   (`implementations/stanford-medicine-ume/…`)? Propagated there because the rule has no
   per-deployment exception; flagged as a judgment call.
5. **Optional housekeeping**: delete the merged branches `claude/v0.6.1-single-sample` and
   `claude/v0.6.2-reply-shape` (cloud sessions cannot delete refs).

### 5.2 Decisions the maintainer wanted to talk through (ask; do not do unilaterally)
- **README's role** once Pages is live: proposed cut to one line + Pages link + one line on what the
  repo is, then developer material. Testers never need the README.
- **Folder rename** `platforms/stanford-ai-playground/` → something neutral (`platforms/paste-block/`):
  a nursing tester read "Stanford" and thought "not for me". ~15 minutes with a redirect stub;
  `build-site.py`, `build-release-assets.py`, README, INSTALL.md and `check-consistency.py` reference
  the path.
- Whether to write two non-medical worked examples in `examples/` (all three are UME) and a
  `domains/general-higher-ed/` stub. Deferred as a known limitation; first real run reports may be
  worth more.

### 5.3 Agent can do without asking
- Wave 5 of the persona loop (recipe above).
- Fold in Gem / GPT links when handed over (front page template `docs/_template.html`, then rebuild;
  `INSTALL.md`; the "link coming" placeholders are literal).
- Open a PR if asked: there is no PR template in the repo; write the body from the branch's commits.
- Re-run the determinism probe after any `core/` change touching Phase A–E.
- Keep `CHANGELOG.md` `[Unreleased]` current.

---

## 6. Gotchas learned the hard way
- `git push --delete` and anything touching refs/tags returns 403 from the cloud credential. Don't retry.
- The artifact service refuses wake subscriptions from cloud sessions; don't claim to be watching a page.
- `python3 scripts/run_mode1_eval.py --dry-run` **requires** `--prompts --model --output`; a bare
  invocation exits 2 and that is argparse, not a bug. CI passes the args.
- `score_ux_conformance.py --out` must be inside the repo root (fixed to resolve relative paths).
- An agent given "edit in your file's voice" will quietly rewrite prose when it means to rewrite links.
  That is how the packaged `SKILL.md` got corrupted. Use the generator; diff non-href text.
- When a batch edit script asserts `count==1` and fails midway, earlier edits in the same Python
  process may already be written if you wrote per-edit, or none if you wrote at the end. Write per
  edit and re-run only the failures.
- `grep -c` counts lines, not occurrences; a wrapped phrase shows 0. Normalize whitespace before
  verifying propagation.
- Sonnet testers pad with praise unless told not to, and will "launder" higher-ed register for K-12
  on their own — ask explicitly whether the block licensed that.

---

- **A private repo silently breaks everything outward-facing.** The repo was private through v0.6.2:
  the front page, report form, downloads and plugin install were invisible to testers, Pages could not
  be enabled, and once the free Actions minutes ran out every CI and Release job died in ~2 seconds
  with `runner_id: 0` and no log (HTTP 404 on logs). That is not a code failure — check visibility
  and Actions billing before debugging. Releases that failed that way are re-published with
  `release.yml`'s `workflow_dispatch` (input `tag`).
- **Cloud sessions cannot change repository settings** (visibility, Pages) — the proxy refuses
  "repository settings writes" even with an admin token — and cannot delete refs. Hand those to the
  maintainer as one-click steps.

## 7. Artifacts the maintainer has (private pages, not in the repo)
- **Review record** — "The Earliest Broken Link": the original adversarial review, annotated with
  remediation status. https://claude.ai/code/artifact/ca7f8eae-477f-416b-af46-2d0e3cfae1d0
- **Front-page draft** — the Pages site as an artifact for tapping on a phone.
  https://claude.ai/code/artifact/8eaf986a-5979-4b6c-936f-7b988c4a62b4
Both are the maintainer's; a new session cannot republish them without the URL as `url`.

---

## 8. Suggested first hour for the next agent
1. `git log --oneline origin/main..HEAD` — read the 26 commit messages; they are the narrative.
2. Run the gates (§3.5). All green except `check-secrets` on the tag.
3. Read `core/diagnostic-procedure.md` Phase A (the selector) and Phase E, and
   `core/response-pattern.md` — these carry most of the session's changes.
4. Ask the maintainer which of §5.1/§5.2 they have done or decided. Do not assume.
5. If nothing is pending from them: run wave 5 with two new fields and the adjunct, and re-run the
   determinism probe. Report what changed, if anything.

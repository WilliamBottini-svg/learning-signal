# Releasing Learning Signal Check

Cutting a release is five steps: **bump → verify → tag → verify the tag → publish.** The fourth step is
the one that is easy to skip and expensive to skip: CI on `main` says nothing about what is inside the
tag you are about to publish.

## Where the version lives

The version string is declared in these places. `plugin.json` is **authoritative**; everything else must
agree with it.

| File | Field |
|------|-------|
| `platforms/claude-skill/.claude-plugin/plugin.json` | `version` — **source of truth** |
| `CITATION.cff` | `version:` and `date-released:` |
| `README.md` | every full `vX.Y.Z` mention (two-component references like "the v0.3 validation program" are historical prose and are not checked) |
| `CHANGELOG.md` | a `## [X.Y.Z] — YYYY-MM-DD` section |
| `.claude-plugin/marketplace.json` | **must not carry a `version`** — the plugin manifest owns it; a second copy only ever drifts |

`scripts/check-versions.py` enforces this. Run it after every bump.

> `platforms/claude-skill/SKILL.md` and the packaged
> `platforms/claude-skill/skills/learning-signal-check/SKILL.md` currently have **no `version:` key** in
> their frontmatter, so they cannot be version-synced; `check-versions.py` reports this as a WARN. If you
> add the key to both files, run the check with `--strict-skill-version` (and add that flag to the CI
> job) to make it a hard gate.

## Procedure

1. **Bump the version** in every place in the table above, and write the `CHANGELOG.md` section for the
   release. Describe what actually changed; do not carry forward aspirational text.

2. **Verify locally.** All of these must exit 0:

   ```sh
   python3 scripts/check-consistency.py
   python3 scripts/check-links.py
   python3 scripts/check-versions.py
   python3 scripts/check-secrets.py
   python3 scripts/redact_runs.py --check tests/results/*.jsonl tests/results/runs/*.jsonl
   claude plugin validate .
   claude plugin validate ./platforms/claude-skill
   cffconvert --validate -i CITATION.cff     # pip install -r requirements-dev.txt
   ```

3. **Merge to `main` and let CI pass.** `.github/workflows/ci.yml` runs the same gates.

4. **Tag, then verify the tag ref — not `main`.**

   ```sh
   git tag -a vX.Y.Z -m "vX.Y.Z"
   git push origin vX.Y.Z
   ```

   Pushing the tag triggers `.github/workflows/release.yml`, which re-runs the entire CI suite against
   the tag ref, checks that the tag name matches `plugin.json`, and checks that `CHANGELOG.md` has a
   section for it. Only if all of that passes does it publish the GitHub release.

   To check a tag by hand before pushing:

   ```sh
   git fetch --tags --force
   python3 scripts/check-secrets.py          # scans HEAD *and every tag*
   # (check-secrets.py already covers this; grep the tag directly only if you
   #  want to eyeball it. Write the pattern inline rather than committing it.)
   ```

5. **Publish.** The release workflow creates the GitHub release from the `CHANGELOG.md` section. If you
   are publishing by hand, use `gh release create vX.Y.Z --notes-file <section>`.

## If a tag is bad

A tag is immutable in practice once anyone has fetched it. Do not quietly re-point it.

- **Content defect** → cut the next patch version. Leave the bad tag in place and say so in the
  changelog.
- **Secret or private content inside the tag** → the tag must be deleted (`git push --delete origin
  vX.Y.Z`), the content purged from history with `git filter-repo`, and every affected ref force-pushed
  and re-tagged. Rotate any credential that was ever paired with the exposed system.

## Known release blocker

`scripts/check-secrets.py` currently **fails on the `v0.5.0` tag**. The tag tree still contains the real
internal gateway hostname in `tests/results/redteam-regression-2026-07-06.jsonl`; the redaction commit
(`82dc420`) landed *after* the tag was cut, so `HEAD` is clean and the tag is not. This must be resolved
— by purging history and re-tagging, or by an explicitly documented risk acceptance — before the
repository is made public. Prior security reviews reached the same conclusion
(`tests/results/agent-review-2026-07-06-opus48.md`, finding SEC-1) and note that the hostname is an
authenticated internal endpoint rather than a credential.

The secret scan is the **only** remaining blocker. `check-consistency.py`, `check-links.py` and
`check-versions.py` all pass on the current tree — but note that `check-secrets.py` scans tags, so this
blocker cannot be cleared by any change to `main`.

## Redacting eval run logs before publishing them

`scripts/run_mode1_eval.py` records the gateway endpoint it actually called, so a run log is a truthful
record. Redaction is a separate, deliberate publish step:

```sh
python3 scripts/redact_runs.py tests/results/runs/<log>.jsonl   # rewrite in place
python3 scripts/redact_runs.py --check tests/results/*.jsonl    # verify (CI runs this)
```

Never hand-edit a run log to hide an endpoint, and never let the harness write a placeholder it did not
call — that is what produced a log claiming an endpoint that was never used.

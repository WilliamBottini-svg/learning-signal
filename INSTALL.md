# Install Learning Signal Check

You don't have to install anything to try it — paste the prompt from the
[front page](https://williambottini-svg.github.io/learning-signal/) into any assistant. Install when
you want it there every time, without pasting. Whichever way you run it, **tell us what happened**:
[Report a run](https://github.com/WilliamBottini-svg/learning-signal/issues/new?template=report-a-run.yml)
(three questions, two minutes; the form asks which one you used).

Every bundle below is built from the same canonical files at release time — no bundle can drift from
another. Download from the [latest release](https://github.com/WilliamBottini-svg/learning-signal/releases/latest).

## Claude.ai (Free, Pro, Max, Team, Enterprise)

1. Download `learning-signal-check-claude-skill-<version>.zip` from the latest release. Don't unzip it.
2. In Claude: **Settings → Capabilities**, turn on **Code execution and file creation** (skills need it).
3. **Settings → Skills → +** (or *Customize → Skills*), upload the zip.
4. Start a chat and describe one assessment you're worried about. The skill triggers on its own when the
   topic fits; you can also say "use Learning Signal Check."

The skill is private to your account — there is no public skill store, so each person uploads it.
Mobile-app upload is undocumented; upload on the web, and the skill is then available on mobile.

## Claude Code

```
/plugin marketplace add WilliamBottini-svg/learning-signal
/plugin install learning-signal-check@learning-signal
```

Two commands, then it triggers in any session. Update with `/plugin update learning-signal-check`.

## ChatGPT

**Use it (free):** open the published GPT — *[link coming once published]* — and chat. Store-published
GPTs are usable on the free tier.

**Build your own copy:** download `learning-signal-check-chatgpt-<version>.zip`. It holds the
Instructions field as plain text (already under the 8,000-character cap), the knowledge files to upload,
conversation starters, and a README with the click-by-click. Note: since August 2026, *creating* a new
GPT or publishing to the store requires a Business, Enterprise, or Edu workspace; personal accounts can
still use published GPTs. Ask your institution whether you have an Edu workspace.

## Gemini

**Use it (no Google account needed):** open the shared Gem — *[link coming once published]*.

**Build your own copy:** download `learning-signal-check-gemini-<version>.zip` — Gem instructions, the
setup guide, starters, and up to 10 knowledge files. Gems attached only to device-uploaded or Drive files
stay shareable; anything else greys out the Share button.

## Copilot, Perplexity, anything else

Paste the prompt. Download `learning-signal-check-prompt-<version>.txt` from the release or use the copy
button on the front page. Consumer Copilot has no public custom-agent path; Perplexity Spaces can be
shared publicly but free-tier caps are tight.

## Institutions

An AI Playground / Cogniti-style deployment example lives in
[`implementations/stanford-medicine-ume/`](implementations/stanford-medicine-ume/): fill the
`[PLACEHOLDER]`s and import the custom instructions plus the knowledge set. A hosted single instance beats
per-faculty builds for version control and change management.

## Which one should I pick?

| You want… | Do this |
|---|---|
| To try it once, right now, on a phone | Front page → copy → paste |
| It there every time, in Claude | Upload the skill zip |
| It there every time, in ChatGPT | Use the published GPT |
| A link you can hand a colleague who has no accounts | The public Gem |
| To run it inside Claude Code while editing course files | The plugin |

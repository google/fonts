# Libre Caslon Text

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Pablo Impallari
**METADATA.pb path**: `ofl/librecaslontext/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/thundernixon/Libre-Caslon |
| Commit | `52200a76d723e4a8cb9a566686ed1f56a794f39a` |
| Config YAML | override config.yaml in google/fonts |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/thundernixon/Libre-Caslon` was already present in the METADATA.pb `source { repository_url }` field. It was added by Simon Cozens in commit `f7455d78` ("Populate source.repository_url", 2023-08-15). This URL matches the copyright string in the font files ("Copyright 2020 The Libre Caslon Text Project Authors (https://github.com/thundernixon/Libre-Caslon)"). The PR #2432 body also explicitly references this URL as the upstream source.

Note: The font was originally designed by Pablo Impallari with sources at `https://github.com/impallari/Libre-Caslon-Text`. The v1.100 addition (commit `9bbee711`, 2017-11-30 by Marc Foley) cited that original repo. Stephen Nixon (thundernixon) then forked/reworked the project for the v2.0 variable font upgrade, creating the current upstream repo.

## How the Commit Hash Was Identified

The commit hash `52200a76d723e4a8cb9a566686ed1f56a794f39a` was added to METADATA.pb in commit `4fd9e239` ("Add source metadata to 125 METADATA.pb files", 2026-02-25). This is the latest (HEAD) commit in the upstream repo's `master` branch, dated 2020-06-10, with the message "Make all italic styles available in VF on mac - fixes #13".

The binary font files in google/fonts were verified to match exactly the files built in the upstream repo at this commit:
- `LibreCaslonText[wght].ttf` — SHA-256 `c11809db...` matches `fonts/LibreCaslonText[wght].ttf` in the upstream repo
- `LibreCaslonText-Italic[wght].ttf` — SHA-256 `60ca1a3a...` matches `fonts/LibreCaslonText-Italic[wght].ttf` in the upstream repo

The v2.0 variable font update was submitted by Stephen Nixon (thundernixon) via PR #2432 ("librecaslontext: v2.0 added"), merged by Marc Foley on 2020-06-11. The upstream commit `52200a7` was made one day before the merge on 2020-06-10, and no further commits exist in the upstream repo after that date. This commit is both the HEAD of the repo and the commit whose built fonts were used in the PR.

## How Config YAML Was Resolved

The upstream repo does not contain a `config.yaml` file. The build process at the time of onboarding used a custom shell script (`sources/build.sh`) that invoked `fontmake` directly with post-processing steps (fix-dsig, fix-gasp, fix-nonhinting, statmake for STAT tables, MVAR table removal via ttx).

An override `config.yaml` was created in the google/fonts family directory (`ofl/librecaslontext/config.yaml`) in commit `5ddf312e` ("Add config_yaml enrichment for 82 font families", 2026-02-20). This override contains:

```yaml
sources:
  - sources/LibreCaslonText.glyphs
  - sources/LibreCaslonText-Italic.glyphs
```

These source paths reference the two `.glyphs` files in the upstream repo's `sources/` directory, which were confirmed to exist at the recorded commit. Since an override config exists in the google/fonts directory, the `config_yaml` field is intentionally omitted from the METADATA.pb `source {}` block (google-fonts-sources auto-detects local overrides).

## Verification

- Repository URL is valid: Yes (https://github.com/thundernixon/Libre-Caslon)
- Commit exists in upstream repo: Yes (HEAD of `master` branch)
- Commit date: 2020-06-10 18:44:04 -0400
- Commit message: "Make all italic styles available in VF on mac - fixes #13"
- Binary files match: Yes (both variable font TTFs have identical SHA-256 hashes)
- Source files at commit: `sources/LibreCaslonText.glyphs`, `sources/LibreCaslonText-Italic.glyphs`
- Override config.yaml in google/fonts: Yes (`ofl/librecaslontext/config.yaml`)
- Upstream repo is clean: Yes (no local modifications)
- PR in google/fonts: #2432 ("librecaslontext: v2.0 added"), merged 2020-06-11 by Marc Foley

## Confidence

**HIGH**: The commit hash is definitively confirmed through binary file hash comparison. Both variable font TTFs in google/fonts are byte-identical to those in the upstream repo at commit `52200a76`. The commit is the HEAD of the upstream repo's `master` branch and was the latest commit at the time PR #2432 was merged. The repository URL is confirmed by the copyright string, the PR body, and the METADATA.pb field. The override config.yaml correctly references the two `.glyphs` source files present at the recorded commit.

## Open Questions

None. The investigation is complete with high confidence across all fields.

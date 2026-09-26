# Bellota Text - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bellota Text |
| Repository URL | https://github.com/kemie/Bellota-Font |
| Commit Hash | db900d27103a2e9b37b76ef32386fbf9691ecac6 |
| Config YAML | (none) |
| **Status** | complete |
| Category | DISPLAY |

## How the Repository URL Was Found

The repository URL `https://github.com/kemie/Bellota-Font` is embedded in the copyright string of the font files themselves (e.g., "Copyright 2019 The Bellota Project Authors (https://github.com/kemie/Bellota-Font)"). It was also present in the METADATA.pb `source` block added by the `f7455d788` commit ("Populate source.repository_url").

## How the Commit Hash Was Determined

The commit hash `db900d27103a2e9b37b76ef32386fbf9691ecac6` was added to the METADATA.pb source block in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25, on branch `sources_info_2026-02-25`).

**Cross-verification**: The recorded commit `db900d27` is a merge commit in the upstream repo ("Merge pull request #5 from yanone/master") dated 2020-01-16 15:43:54 +0100. The font was added to google/fonts in commit `d22365f72` ("Added Bellota and Bellota Text") by Yanone on the same day (2020-01-16 15:56:07 +0100). PR #2309 in google/fonts was also by Yanone with the body "Upstream PR is merged." -- this refers to PR #5 in the upstream repo. The timing is consistent: Yanone merged the upstream PR first, then immediately submitted the fonts to google/fonts.

There have been 227 additional commits in the upstream repo since the recorded commit, including major version updates (Bellota 5.0, Cyrillic additions, etc.).

## Config YAML Status

- **No `config.yaml` exists anywhere** in the upstream repo (checked at recorded commit and at HEAD)
- **No override `config.yaml`** exists in `google/fonts/ofl/bellotatext/`
- The upstream repo has buildable sources: `src/Bellota.glyphs` and `src/Bellota-*.ufo` files at the recorded commit
- A `build.sh` script exists but no gftools-builder config

## Verification

- Commit hash `db900d27` exists in the upstream repo and is confirmed as the merge commit for Yanone's PR #5
- The date matches the google/fonts addition (same day, 13 minutes apart)
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/kemie/Bellota-Font`
- Note: Bellota Text and Bellota share the same upstream repo

## Confidence Level

**High** - The commit hash is strongly corroborated by matching dates, the same author (Yanone) for both the upstream merge and the google/fonts addition, and the PR body explicitly referencing the upstream merge.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - src/Bellota.glyphs
familyName: Bellota Text
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

- An override `config.yaml` would need to be created for gftools-builder compatibility, as the upstream repo has never had one
- The upstream repo has evolved significantly (227 more commits) since onboarding; any future update would need a new review process

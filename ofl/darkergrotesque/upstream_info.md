# Darker Grotesque

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Gabriel Lam, ViệtAnh Nguyễn
**METADATA.pb path**: `ofl/darkergrotesque/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/bettergui/DarkerGrotesque |
| Commit | `a5c3584b44ab3a7d272565662139ee07bb72e8e8` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/bettergui/DarkerGrotesque` is documented in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font ("Copyright 2019 The Darker Grotesque Project Authors (https://github.com/bettergui/DarkerGrotesque)"). Multiple onboarding commits in google/fonts reference this URL.

## How the Commit Hash Was Identified

The commit hash `a5c3584b44ab3a7d272565662139ee07bb72e8e8` is recorded in METADATA.pb and confirmed by the gftools-packager commit `661c8bdc6` (authored by Emma Marichal, 2023-04-27): "Darker Grotesque Version 1.000;gftools[0.9.28] taken from the upstream repo https://github.com/bettergui/DarkerGrotesque at commit https://github.com/bettergui/DarkerGrotesque/commit/a5c3584b44ab3a7d272565662139ee07bb72e8e8."

**Important history**: Darker Grotesque was originally added to Google Fonts with static fonts from a different commit:
- **Original onboarding** (commits `b77c4d9b6` and `c4ab99f33`, 2019): "Taken from the upstream repo https://github.com/bettergui/DarkerGrotesque at commit https://github.com/bettergui/DarkerGrotesque/commit/f9478bb90aeecf97cd4bc4138a12586d835f7593" -- this was the static font version.
- **Variable font re-packaging** (commit `661c8bdc6`, 2023): Emma Marichal re-packaged the font as a variable font from commit `a5c3584b`, which replaced the 7 static TTF files with a single variable `DarkerGrotesque[wght].ttf`.

The current commit `a5c3584b` is the HEAD of the `master` branch (commit message: "Merge pull request #8 from emmamarichal/master"). This is the correct and most recent onboarding commit.

## How Config YAML Was Resolved

The upstream repository contains `sources/config.yaml` at the recorded commit. The config file references `DarkerGrotesque.glyphs` as the source, with axis order `wght` and `familyName: "Darker Grotesque"`. This path is correctly recorded in the METADATA.pb `config_yaml` field. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit is HEAD of master: Yes (and only commit in repo, as it's a single-commit repo)
- Commit message: "Merge pull request #8 from emmamarichal/master"
- Source files at commit: `sources/DarkerGrotesque.glyphs`, `sources/config.yaml`
- Config YAML at commit: `sources/config.yaml` (valid gftools-builder config with STAT table)
- METADATA.pb files mapping: `fonts/variable/DarkerGrotesque[wght].ttf` -> `DarkerGrotesque[wght].ttf`
- Weight range: 300-900

## Confidence

**High**: The repository URL and commit hash are confirmed by the gftools-packager commit message from the variable font re-packaging (2023). The commit exists and is the HEAD of the master branch. The config.yaml is present in the upstream repo at the correct path. The transition from static to variable fonts is well-documented.

## Open Questions

None. All data is consistent and well-documented.

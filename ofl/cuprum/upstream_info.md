# Cuprum

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Jovanny Lemonad
**METADATA.pb path**: `ofl/cuprum/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/alexeiva/cuprum |
| Commit | `98adc59dc00ca00dbde9eb42a23ace5f924b4f90` |
| Config YAML | Override in google/fonts (`ofl/cuprum/config.yaml`) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/alexeiva/cuprum` is documented in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font files ("Copyright 2020 The Cuprum Project Authors (https://github.com/alexeiva/cuprum)"). The gftools-packager commit `df19ee8f7` in google/fonts (PR #2692) also explicitly references this URL: "Cuprum Version 3.000 taken from the upstream repo https://github.com/alexeiva/cuprum".

## How the Commit Hash Was Identified

The commit hash `98adc59dc00ca00dbde9eb42a23ace5f924b4f90` is recorded in METADATA.pb and is directly confirmed by the gftools-packager commit `df19ee8f7` (PR #2692, authored by Marc Foley): "Cuprum Version 3.000 taken from the upstream repo https://github.com/alexeiva/cuprum at commit https://github.com/alexeiva/cuprum/commit/98adc59dc00ca00dbde9eb42a23ace5f924b4f90."

This commit is the HEAD of the `master` branch in the upstream repository. It is a merge commit: "Merge pull request #5 from TypeNetwork/master". While there are more recent commits on other branches (dependabot bumps), the master branch has not moved past this commit.

## How Config YAML Was Resolved

The upstream repository does **not** contain a `config.yaml` or `builder.yaml` file. Instead, an override `config.yaml` exists in the google/fonts family directory at `ofl/cuprum/config.yaml`. This override file references two designspace sources: `sources/Cuprum.designspace` and `sources/Cuprum-Italic.designspace`, with `buildVariable: true`.

Since the override exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb `source { }` block, as google-fonts-sources will detect the local override automatically.

## Verification

- Commit exists in upstream repo: Yes
- Commit is HEAD of master: Yes
- Commit message: "Merge pull request #5 from TypeNetwork/master"
- Source files at commit: `sources/Cuprum.designspace`, `sources/Cuprum-Italic.designspace`, plus 4 UFO sources
- Override config.yaml in google/fonts: Yes (`ofl/cuprum/config.yaml`)
- METADATA.pb files mapping matches repo structure (fonts in `fonts/variable/` and `fonts/ttf/`)

## Confidence

**High**: The repository URL and commit hash are both confirmed by the gftools-packager commit message (PR #2692). The commit exists in the upstream repo and is the HEAD of the master branch. The override config.yaml in google/fonts correctly references the designspace sources present in the repo.

## Open Questions

None. All data is consistent and well-documented.

# Danfo

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Afrotype, Seyi Olusanya, Eyiyemi Adegbite, David Udoh, Mirko Velimirovic
**METADATA.pb path**: `ofl/danfo/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Afrotype/danfo |
| Commit | `a66fc9ded8f42ad2d39b91c9cd8a1960737ad02a` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/Afrotype/danfo` is documented in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font ("Copyright 2024 The Tac Project Authors (https://github.com/Afrotype/Danfo)"). The gftools-packager commit `d2b934888` in google/fonts confirms this: "Danfo Version 1.000 taken from the upstream repo https://github.com/Afrotype/danfo".

Note: the copyright references the repo URL with capital "D" (Danfo) but the actual METADATA.pb uses lowercase (danfo). Both work on GitHub as repository names are case-insensitive.

## How the Commit Hash Was Identified

The commit hash `a66fc9ded8f42ad2d39b91c9cd8a1960737ad02a` is recorded in METADATA.pb and confirmed by the gftools-packager commit `d2b934888`: "Danfo Version 1.000 taken from the upstream repo https://github.com/Afrotype/danfo at commit https://github.com/Afrotype/danfo/commit/a66fc9ded8f42ad2d39b91c9cd8a1960737ad02a."

This commit is the HEAD of the `main` branch in the upstream repository (commit message: "language fixes"). No additional commits have been made to the repo since onboarding.

## How Config YAML Was Resolved

The upstream repository contains `sources/config.yaml` at the recorded commit. The config file references `Danfo.glyphs` as the source, with axis order `ELSH` (Element Shape), `familyName: Danfo`, and `buildVariable: True`. This path is correctly recorded in the METADATA.pb `config_yaml` field. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit is HEAD of main: Yes
- Commit message: "language fixes"
- Source files at commit: `sources/Danfo.glyphs`, `sources/config.yaml`
- Config YAML at commit: `sources/config.yaml` (valid gftools-builder config)
- METADATA.pb files mapping: `fonts/variable/Danfo[ELSH].ttf` -> `Danfo[ELSH].ttf`
- Minisite URL: https://www.afrotype.com/danfo

## Confidence

**High**: All data is confirmed by the gftools-packager commit message. The commit exists and is the HEAD of the main branch. The config.yaml is present in the upstream repo at the correct path. The font was recently added (2024-03-15).

## Open Questions

None. All data is consistent and well-documented.

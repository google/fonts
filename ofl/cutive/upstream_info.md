# Cutive

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/cutive/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/CutiveFont |
| Commit | `d97e7cb29296a2c091568d01e3394ae87111bd39` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/CutiveFont`. This matches the copyright string in the font file ("Copyright 2012 The Cutive Project Authors (https://github.com/googlefonts/CutiveFont), with Reserved Font Names \"Cutive\""). The google/fonts commit `46bc8761f` (2024-08-01) by Emma Marichal explicitly states: "Taken from the upstream repo https://github.com/googlefonts/CutiveFont".

## How the Commit Hash Was Identified

The commit `d97e7cb29296a2c091568d01e3394ae87111bd39` is referenced directly in the google/fonts commit `46bc8761f` (2024-08-01, "Cutive: Version 1.110; ttfautohint (v1.8.4.7-5d5b) added"), which states: "Taken from the upstream repo https://github.com/googlefonts/CutiveFont at commit https://github.com/googlefonts/CutiveFont/commit/d97e7cb29296a2c091568d01e3394ae87111bd39."

This is the most recent font binary update for Cutive. A previous update at commit `0f79e19d9` (2024-06-07, "Version 1.100") referenced a different upstream commit (`2d3d48d9f1b915c840abbd1be6a97324f1f16974`), but the v1.110 update supersedes it.

The upstream repository is a single-commit repo: `d97e7cb` ("bumped version") is both the only commit and HEAD.

## How Config YAML Was Resolved

The file `sources/config.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
    - Cutive.glyphs
familyName: Cutive
buildVariable: false
```

This was added to METADATA.pb via the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), porting data from fontc_crater's target.json. No override config.yaml exists in the google/fonts family directory (`ofl/cutive/`).

## Verification

- Commit exists in upstream repo: Yes (it is the only commit / HEAD)
- Commit message: "bumped version"
- Source files at commit: `sources/Cutive.glyphs`, `sources/config.yaml`
- Font binary in METADATA.pb files block: `fonts/ttf/Cutive-Regular.ttf` maps to `Cutive-Regular.ttf`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts commit message for the most recent font update. The upstream repo has only one commit, which matches. The config.yaml exists and is valid. All data is fully consistent.

## Open Questions

None.

# Cutive Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/cutivemono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/cutivemono |
| Commit | `4422d783b81be0fcec82ef3610eac94784d989c1` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/cutivemono`. This matches the copyright string in the font file ("Copyright 2012 The Cutive Project Authors (https://github.com/googlefonts/cutivemono)"). The google/fonts commit `7c38f10e1` (2024-05-08) by Emma Marichal explicitly states: "Taken from the upstream repo https://github.com/googlefonts/cutivemono". The URL was initially added to METADATA.pb by Simon Cozens in commit `c8f729cbd` ("Add more upstreams (c,d)", 2024-01-14).

## How the Commit Hash Was Identified

The commit `4422d783b81be0fcec82ef3610eac94784d989c1` is referenced directly in the google/fonts commit `7c38f10e1` (2024-05-08, "Cutive Mono: Version 1.110; ttfautohint (v1.8.4.7-5d5b) added"), which states: "Taken from the upstream repo https://github.com/googlefonts/cutivemono at commit https://github.com/googlefonts/cutivemono/commit/4422d783b81be0fcec82ef3610eac94784d989c1."

This is the most recent font binary update for Cutive Mono. The upstream repository has only this single commit (`4422d78`, "fix ldot"), which is HEAD.

## How Config YAML Was Resolved

The file `sources/config.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
    - CutiveMono.glyphs
familyName: Cutive Mono
buildVariable: false
```

This was added to METADATA.pb via the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), porting data from fontc_crater's target.json. No override config.yaml exists in the google/fonts family directory (`ofl/cutivemono/`).

## Verification

- Commit exists in upstream repo: Yes (it is the only commit / HEAD)
- Commit message: "fix ldot"
- Source files at commit: `sources/CutiveMono.glyphs`, `sources/config.yaml`
- Font binary in METADATA.pb files block: `fonts/ttf/CutiveMono-Regular.ttf` maps to `CutiveMono-Regular.ttf`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts commit message for the most recent font update. The upstream repo has only one commit, which matches. The config.yaml exists and is valid. All data is fully consistent.

## Open Questions

None.

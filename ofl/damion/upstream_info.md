# Damion

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Vernon Adams
**METADATA.pb path**: `ofl/damion/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/damionFont |
| Commit | `6408c983f707a0bd5129eecf74a834146fec2983` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/damionFont`. This matches the copyright string in the font file ("Copyright 2014 The Damion Project Authors (https://github.com/googlefonts/damionFont)"). The google/fonts commit `8b3003069` (2024-04-19) by Emma Marichal explicitly states: "Taken from the upstream repo https://github.com/googlefonts/damionFont".

## How the Commit Hash Was Identified

The commit `6408c983f707a0bd5129eecf74a834146fec2983` is referenced directly in the google/fonts commit `8b3003069` (2024-04-19, "Damion: Version 1.100; ttfautohint (v1.8.4.7-5d5b) added"), which states: "Taken from the upstream repo https://github.com/googlefonts/damionFont at commit https://github.com/googlefonts/damionFont/commit/6408c983f707a0bd5129eecf74a834146fec2983."

This is the most recent font binary update for Damion. The upstream repository has only this single commit (`6408c98`, "last fixes in the sources"), which is HEAD.

## How Config YAML Was Resolved

The file `sources/config.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
    - Damion.glyphs
familyName: Damion
buildVariable: false
```

This was added to METADATA.pb via the batch commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31), porting data from fontc_crater's target.json. No override config.yaml exists in the google/fonts family directory (`ofl/damion/`).

## Verification

- Commit exists in upstream repo: Yes (it is the only commit / HEAD)
- Commit message: "last fixes in the sources"
- Source files at commit: `sources/Damion.glyphs`, `sources/config.yaml`
- Font binary in METADATA.pb files block: `fonts/ttf/Damion-Regular.ttf` maps to `Damion-Regular.ttf`

## Confidence

**High**: The commit hash is explicitly referenced in the google/fonts commit message for the most recent font update. The upstream repo has only one commit, which matches. The config.yaml exists and is valid. All data is fully consistent.

## Open Questions

None.

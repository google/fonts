# Astloch

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Dan Rhatigan
**License**: OFL
**METADATA.pb**: `ofl/astloch/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/astloch |
| Commit | `d15f7a51db3956d34a87ac47c532eae74237f07f` |
| Config YAML | — |
| Branch | `master` |
| Source types | sfd |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2014-10-17 13:29:46 +0300
- Commit message: "update .travis.yml"

### Config YAML
Not applicable — upstream repo contains only FontForge .sfd sources, which are not compatible with gftools-builder.

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `6873b904efbc`
- Date: 2017-11-28 16:55:38 -0500
- Subject: "ofl/astloch: v1.002 added. Fixed name table."

### Upstream repo cache
- Cached at: `librefonts/astloch`
- Commit `d15f7a51db39` verified ✓

## Confidence

**Medium**: URL discovered via research; commit verified in upstream repo

## Notes

SFD-only sources (FontForge format), not gftools-builder compatible

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/astloch/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `d15f7a51db`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

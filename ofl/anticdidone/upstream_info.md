# Antic Didone

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Santiago Orozco
**License**: OFL
**METADATA.pb**: `ofl/anticdidone/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/anticdidone |
| Commit | `604bfcda35327f03964cc6c55a281540ce40b0a0` |
| Config YAML | — |
| Branch | `master` |
| Source types | sfd |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2014-10-17 13:29:09 +0300
- Commit message: "update .travis.yml"

### Config YAML
Not applicable — upstream repo contains only FontForge .sfd sources, which are not compatible with gftools-builder.

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `64099f31be4a`
- Date: 2017-08-07 21:30:41 +0100
- Subject: "hotfix-anticdidone: v2.001 added (#817)"

### Upstream repo cache
- Cached at: `librefonts/anticdidone`
- Commit `604bfcda3532` verified ✓

## Confidence

**Medium**: URL discovered via research; commit verified in upstream repo

## Notes

SFD-only sources (FontForge format), not gftools-builder compatible

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/anticdidone/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `604bfcda35`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

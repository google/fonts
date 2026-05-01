# Armata

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Viktoriya Grabowska
**License**: OFL
**METADATA.pb**: `ofl/armata/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/armata |
| Commit | `fbbc7c2575fe310df0450aaa721ee4e860b03a0e` |
| Config YAML | — |
| Branch | `master` |
| Source types | sfd |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2014-10-17 13:29:34 +0300
- Commit message: "update .travis.yml"

### Config YAML
Not applicable — upstream repo contains only FontForge .sfd sources, which are not compatible with gftools-builder.

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `ecc5f91e743c`
- Date: 2017-08-07 21:09:35 +0100
- Subject: "hotfix-armata: v1.003 added (#823)"

### Upstream repo cache
- Cached at: `librefonts/armata`
- Commit `fbbc7c2575fe` verified ✓

## Confidence

**Medium**: URL discovered via research; commit verified in upstream repo

## Notes

SFD-only sources (FontForge format), not gftools-builder compatible

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/armata/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `fbbc7c2575`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

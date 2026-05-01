# Architects Daughter

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Kimberly Geswein
**License**: OFL
**METADATA.pb**: `ofl/architectsdaughter/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/architectsdaughter |
| Commit | `1a94ca0aea18288ee7685ed6aee918b58399a307` |
| Config YAML | — |
| Branch | `master` |
| Source types | sfd |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2014-10-17 13:29:26 +0300
- Commit message: "update .travis.yml"

### Config YAML
Not applicable — upstream repo contains only FontForge .sfd sources, which are not compatible with gftools-builder.

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `2a0c94b33e35`
- Date: 2017-08-07 21:29:56 +0100
- Subject: "hotfix-architectsdaughter: v1.003 added (#821)"

### Upstream repo cache
- Cached at: `librefonts/architectsdaughter`
- Commit `1a94ca0aea18` verified ✓

## Confidence

**Medium**: URL discovered via research; commit verified in upstream repo

## Notes

SFD-only sources (FontForge format), not gftools-builder compatible

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/architectsdaughter/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `1a94ca0aea`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

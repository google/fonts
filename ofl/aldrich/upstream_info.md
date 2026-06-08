# Aldrich

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: MADType
**License**: OFL
**METADATA.pb**: `ofl/aldrich/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/aldrich |
| Commit | `ec28a1d125f17139f1a0685025dc43a775bed76f` |
| Config YAML | — |
| Branch | `master` |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2014-10-17 13:27:55 +0300
- Commit message: "update .travis.yml"

### Config YAML
Not applicable — upstream repo contains no buildable font source files (binary-only).

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `c0aae12255fb`
- Date: 2017-05-01 18:18:22 +0100
- Subject: "hotfix-aldrich: v1.002 added (#747)"

### Upstream repo cache
- Cached at: `librefonts/aldrich`
- Commit `ec28a1d125f1` verified ✓

## Confidence

**Medium**: URL discovered via research; commit verified in upstream repo

## Notes

No buildable source files at recorded commit

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/aldrich/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `ec28a1d125`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

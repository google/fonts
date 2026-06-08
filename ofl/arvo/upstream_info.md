# Arvo

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Anton Koovit
**License**: OFL
**METADATA.pb**: `ofl/arvo/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/antonxheight/Arvo |
| Commit | `ae906e99ab549103549c68252edfcb1816a6bf08` |
| Config YAML | — |

## Methodology

### Repository URL
Discovered via google/fonts commit history, PR references, or GitHub search.

### Commit Hash
Identified via google/fonts PR body analysis, commit message references, or date correlation with upstream history.

### Config YAML
Not applicable — upstream repo contains no buildable font source files (binary-only).

## Evidence

### METADATA.pb source block
No source block present in METADATA.pb.

### google/fonts history
- Last font modification: `d2cc27513dcb`
- Date: 2019-07-12 10:22:17 +0100
- Subject: "arvo: v1.006 added"

## Confidence

**Low**: URL discovered via research; commit not verified

## Notes

No buildable source files at recorded commit

## Update (2026-04-24) -- Legacy source documentation

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/arvo/` listing the legacy source files (`.sfd`/`.vfb`) present in the upstream repo at the pinned commit `ae906e99ab`. These formats are not yet supported by gftools-builder; the config serves as documentation for future compatibility work and to distinguish legacy-sourced families from families genuinely missing a build recipe.

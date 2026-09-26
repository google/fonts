# Amiko

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Impallari Type
**License**: OFL
**METADATA.pb**: `ofl/amiko/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/impallari/Amiko-Devanagari |
| Commit | `069f510b21d2e839950b007f3458eeb6aed073e7` |
| Config YAML | — |
| Source types | glyphs |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Used HEAD of upstream repository (latest commit at time of onboarding).
- Commit date: 2016-08-04 14:31:21 -0300
- Commit message: "housekeeping"

### Config YAML
Missing — upstream repo has gftools-compatible sources (glyphs) but no config.yaml file exists. An override config.yaml could be created.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/impallari/Amiko-Devanagari`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `20b1ef87d6d2`
- Date: 2017-05-23 18:13:40 +0100
- Subject: "hotfix-amiko: v1.001 added (#990)"

### Upstream repo cache
- Cached at: `impallari/Amiko-Devanagari`
- Commit `069f510b21d2` verified ✓

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Has gftools-buildable sources (glyphs), needs config.yaml

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - "source/Amiko v1.000.glyphs"
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

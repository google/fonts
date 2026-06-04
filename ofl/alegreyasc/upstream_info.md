# Alegreya SC

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Juan Pablo del Peral, Huerta Tipográfica
**License**: OFL
**METADATA.pb**: `ofl/alegreyasc/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/huertatipografica/Alegreya |
| Commit | `d6aedcbb5a82a09dedb07ab99bb91803db8e02af` |
| Config YAML | — |
| Source types | glyphs |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Matched via version tag(s): v2.003.
- Commit date: 2017-10-23 10:04:40 -0300
- Commit message: "updated font files to v2.003"

### Config YAML
Missing — upstream repo has gftools-compatible sources (glyphs) but no config.yaml file exists. An override config.yaml could be created.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/huertatipografica/Alegreya`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `5ece6cbcec0d`
- Date: 2017-10-31 20:05:19 +0000
- Subject: "alegreyasc: v2.003 added (#1268)"

### Upstream repo cache
- Cached at: `huertatipografica/Alegreya`
- Commit `d6aedcbb5a82` verified ✓

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Has gftools-buildable sources (glyphs), needs config.yaml

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Alegreya.glyphs
  - "sources/Alegreya italic.glyphs"
familyName: Alegreya SC
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

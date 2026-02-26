# Alegreya Sans SC

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Juan Pablo del Peral, Huerta Tipográfica
**License**: OFL
**METADATA.pb**: `ofl/alegreyasanssc/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/huertatipografica/Alegreya-Sans |
| Commit | `e6d16c40fa641159b8b371e2a40bda0c9a3a1d43` |
| Config YAML | — |
| Source types | glyphs |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Matched via version tag(s): v2.003.
- Commit date: 2017-10-23 11:07:11 -0300
- Commit message: "updated fonts with t problem fixed"

### Config YAML
Missing — upstream repo has gftools-compatible sources (glyphs) but no config.yaml file exists. An override config.yaml could be created.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/huertatipografica/Alegreya-Sans`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `4e974a60e827`
- Date: 2017-10-31 20:05:30 +0000
- Subject: "alegreyasanssc: v2.003 added. (#1266)"

### Upstream repo cache
- Cached at: `huertatipografica/Alegreya-Sans`
- Commit `e6d16c40fa64` verified ✓

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Has gftools-buildable sources (glyphs), needs config.yaml

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Alegreya_Sans.glyphs
  - sources/Alegreya_Sans-Italic.glyphs
familyName: Alegreya Sans SC
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

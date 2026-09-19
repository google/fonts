# Archivo Black

**Status**: `missing_config`
**Date**: 2026-02-25
**Designer**: Omnibus-Type
**License**: OFL
**METADATA.pb**: `ofl/archivoblack/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/ArchivoBlack |
| Commit | `95df3c54d818473a3e362f30ae3059bd85b80036` |
| Config YAML | — |
| Source types | glyphs, ufo |

## Methodology

### Repository URL
Pre-existing in METADATA.pb `source { repository_url }` field.

### Commit Hash
Identified via google/fonts PR body analysis, commit message references, or date correlation with upstream history.
- Commit date: 2017-06-06 23:03:44 -0300
- Commit message: "Merge pull request #2 from m4rc1e/canonical"

### Config YAML
Missing — upstream repo has gftools-compatible sources (glyphs, ufo) but no config.yaml file exists. An override config.yaml could be created.

## Evidence

### METADATA.pb source block
- `repository_url`: `https://github.com/Omnibus-Type/ArchivoBlack`
- `commit`: `—`
- `config_yaml`: `—`

### google/fonts history
- Last font modification: `e723d317895c`
- Date: 2017-08-07 22:07:25 +0100
- Subject: "archivoblack: v1.006 added. (#1121)"

### Upstream repo cache
- Cached at: `Omnibus-Type/ArchivoBlack`
- Commit `95df3c54d818` verified ✓

## Confidence

**High**: URL pre-existing in METADATA.pb; commit verified in upstream repo

## Notes

Has gftools-buildable sources (glyphs, ufo), needs config.yaml

## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - SRC/Archivo-Black.glyphs
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

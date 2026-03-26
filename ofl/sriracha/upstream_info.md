# Sriracha — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [cadsondemak/sriracha](https://github.com/cadsondemak/sriracha) |
| Commit | `6c6cf92ed8b0b45caca566d999d2dadc7e35f2fd` |
| Date | 2015-06-24 |
| Confidence | High |

## Investigation

The METADATA.pb for Sriracha had no source block. The upstream repository was identified as cadsondemak/sriracha, by the Cadson Demak foundry.

### Source Types Available

- **UFO**: `source/Sriracha-Regular.ufo/` (contains `features.fea`, `fontinfo.plist`, `glyphs/`)
- **VFB** (FontLab): `source/Sriracha-Regular.vfb`
- **Binary TTF**: `fonts/Sriracha-Regular.ttf`

### Buildability

The repository contains UFO sources, which are gftools-builder compatible. A `config.yaml` could potentially be created for this family. The VFB is likely the canonical design source, with the UFO being an export.

### Notes

- Sriracha is a Thai and Latin handwriting/display font
- The commit `6c6cf92` (2015-06-24) adds the UFO and VFB source files
- Cadson Demak is a Thai type foundry with multiple families on Google Fonts
- Additional Latin design contributions by Pablo Impallari (credited in copyright)
- No existing `config.yaml` in either the upstream repo or the google/fonts family directory

### Actions Taken

A source block was added to METADATA.pb pointing to commit `6c6cf92` at cadsondemak/sriracha, which contains the UFO source files used for the font onboarded to google/fonts (2015-06-27).

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, referencing `Sriracha-Regular.ufo` from `cadsondemak/sriracha`. This is a best-effort starting point for reproducible builds — the shipped binary was likely built with different tool versions and may not match exactly.

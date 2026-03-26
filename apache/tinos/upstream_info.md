# Tinos — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/tinos |
| Commit | `aaf68d53c2d49dbd443631c333c804bf4c664e60` |
| Confidence | High |

## Source Types

The repository contains Glyphs sources:
- `sources/Tinos-Regular.glyphs`
- `sources/Tinos-Bold.glyphs`
- `sources/Tinos-Italic.glyphs`
- `sources/Tinos-BoldItalic.glyphs`

All four styles have individual Glyphs source files.

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs sources could potentially be built with gftools-builder given an override config.

## Investigation Notes

Tinos is one of the Chrome OS core fonts (metrically compatible with Times New Roman), hosted under the googlefonts organization. The binary in google/fonts was last updated on 2017-08-07 (v1.231 hotfix). The repository is the canonical upstream maintained by the Google Fonts team.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Official googlefonts organization repository.

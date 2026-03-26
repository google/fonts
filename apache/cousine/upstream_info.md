# Cousine — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/cousine |
| Commit | `7f897dbd87fbd14d2f8ec0306d5c1ed2317dfe47` |
| Confidence | High |

## Source Types

The repository contains Glyphs sources:
- `sources/Cousine-Regular.glyphs`
- `sources/Cousine-Bold.glyphs`
- `sources/Cousine-Italic.glyphs`
- `sources/Cousine-BoldItalic.glyphs`

All four styles have individual Glyphs source files.

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs sources could potentially be built with gftools-builder given an override config.

## Investigation Notes

Cousine is one of the Chrome OS core fonts (metrically compatible with Courier New), hosted under the googlefonts organization. The binary in google/fonts was last updated on 2017-08-07 (v1.211 hotfix). The repository is the canonical upstream maintained by the Google Fonts team.

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Official googlefonts organization repository.

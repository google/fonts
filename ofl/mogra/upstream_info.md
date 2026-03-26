# Mogra — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/lipiraval/Mogra |
| Commit | `048039d237a99cd102ce254615cba9818c75c711` |
| Confidence | High |

## Source Types

The repository contains Glyphs and UFO sources:
- `sources/Mogra.glyphs` — primary Glyphs source
- `masters/Mogra-Regular.ufo` — UFO master

## Build Compatibility

No `config.yaml` is present in the upstream repository. The Glyphs source in `sources/` could potentially be built with gftools-builder given an override config, but no config was provided with this source block addition.

## Investigation Notes

Lipi Raval's repository is the canonical upstream for Mogra. The commit represents the repository state corresponding to the fonts onboarded to Google Fonts. The binary in google/fonts was last updated on 2017-05-15 (autohinting fix, version 1.002).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Direct match between the upstream repository owner (Lipi Raval) and the font designer.

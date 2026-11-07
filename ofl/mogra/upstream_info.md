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

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
The override `config.yaml` listed `sources: [Mogra.glyphs]` — a repository-root path. fontc_crater failed with `missing source 'Mogra.glyphs'`.

### Investigation
At the recorded commit `048039d` the Glyphs source is `sources/Mogra.glyphs`, not at the repository root. The override config path was missing the `sources/` directory prefix. The recorded commit is correct.

### Actions taken
The override `config.yaml` source path was corrected from `Mogra.glyphs` to `sources/Mogra.glyphs`.

### Final state
The override `config.yaml` references `sources/Mogra.glyphs`, which exists at the recorded commit `048039d`.

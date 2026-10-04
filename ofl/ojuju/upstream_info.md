# Ojuju — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Ojuju was identified at https://github.com/jobosonchisa/ojuju, authored by Chisaokwu Joboson with contributors including Ụdị Foundry and Mirko Velimirović. This is a variable weight sans-serif display typeface inspired by African masquerades. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/jobosonchisa/ojuju
- **Default branch**: main
- **License**: SIL Open Font License 1.1
- **Description**: "The development of an African based typeface inspired by African masquerades"

## Pinned Commit

- **Commit**: `61052b2801035d3011c87708bd3367eeabd0bb82`
- **Date**: 2024-05-20
- **Message**: "Update Ojuju.glyphs"
- **Author**: Eben Sorkin

## Repository Activity After Pinned Commit

The repository continued to receive commits after the pinned commit. As of 2026-03-12, the HEAD commit is `aa982e27fbc30d1a1773900231d81a45fde3992d` (2025-08-08, "Remove fontspector directory"). However, examination of the recent commit history revealed that all commits after the pinned commit concern tooling, README updates, build configuration, and CI changes rather than font source changes. No font binary updates were identified in the commits between the pinned commit and HEAD.

## Source Files

The repository contains a Glyphs source file at `sources/Ojuju.glyphs` along with a `sources/config.yaml` build configuration. The METADATA.pb specifies `config_yaml: "sources/config.yaml"` and references the variable font binary at `fonts/variable/Ojuju[wght].ttf`. The font supports a weight axis (wght) ranging from 200 to 800.

## Confidence

**High** — The repository URL is referenced in the font's copyright string and matches the designer attribution.

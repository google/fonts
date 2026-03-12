# Oooh Baby — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Oooh Baby was identified at https://github.com/googlefonts/oooh-baby, authored by Robert Leuschke. This is a handwriting-style typeface. The repository is hosted under the googlefonts organization, suggesting it was onboarded through the standard Google Fonts production pipeline. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/googlefonts/oooh-baby
- **Default branch**: master
- **License**: SIL Open Font License 1.1
- **Description**: "Oooh Baby fonts"

## Pinned Commit

- **Commit**: `f36e2452e1c1a793fcf49524ab392eb6a2cd1dce`
- **Date**: 2021-11-27
- **Message**: "v1.011 fonts added"
- **Author**: Viviana Monsalve

The pinned commit is the HEAD of the master branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Source Files

The repository contains a Glyphs source file at `sources/OoohBaby.glyphs` along with a `sources/config.yml` build configuration. The METADATA.pb specifies `config_yaml: "sources/config.yml"` and references the font binary at `fonts/ttf/OoohBaby-Regular.ttf`. The copyright string notes the original design dates to 2004, with the OFL-licensed version prepared in 2021.

## Confidence

**High** — The repository URL is referenced in the font's copyright string. The googlefonts organization hosting is consistent with standard Google Fonts production workflow.

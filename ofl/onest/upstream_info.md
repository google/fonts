# Onest — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Onest was identified at https://github.com/simpals/onest, authored by Dmitri Voloshin and Andrey Kudryavtsev under the simpals organization. This is a variable weight sans-serif typeface covering Latin and Cyrillic scripts. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/simpals/onest
- **Default branch**: main
- **License**: SIL Open Font License 1.1
- **Description**: (none)

## Pinned Commit

- **Commit**: `f18c06a14512e43a6191849278d6f07fdaf347d6`
- **Date**: 2023-09-13
- **Message**: "Personalize for this repo"
- **Author**: vcebotari

The pinned commit is the HEAD of the main branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Releases

The repository has one tagged release: `1.000` (published 2023-03-22), which predates the pinned commit.

## Source Files

The repository contains a Glyphs source file at `sources/Onest.glyphs` along with a `sources/config.yaml` build configuration and UFO sources in `sources/ufo/`. A VFC file is also present in `sources/vfc/`. The METADATA.pb specifies `config_yaml: "sources/config.yaml"` and references the variable font binary at `fonts/variable/Onest[wght].ttf`. The font supports a weight axis (wght) ranging from 100 to 900.

## Confidence

**High** — The repository URL is referenced in the font's copyright string and matches the designer attribution (simpals organization, consistent with the Simpals company that produced Onest).

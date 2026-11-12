# Open Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/googlefonts/opensans, maintained under the `googlefonts` GitHub organization. The METADATA.pb source block was already present with the correct repository URL and a pinned commit.

## Repository

- **URL**: https://github.com/googlefonts/opensans
- **Default branch**: `main`
- **Description**: Open Sans font

## Commit

- **Pinned commit**: `bd7e37632246368c60fdcbd374dbf9bad11969b6`
- **Commit message**: Fix version number to v3.003
- **Commit date**: 2023-11-16
- **Status**: This is the HEAD of the `main` branch — the repository is up-to-date with the pinned commit.

## Font Details

Open Sans is a humanist sans serif typeface designed by Steve Matteson, Type Director of Ascender Corp. The family was updated in March 2021 to a variable font using a `wdth` (width, 75–100) and `wght` (weight, 300–800) axis pair, also adding Hebrew and Cyrillic coverage and unifying the licensing under the OFL.

The Google Fonts version ships two variable font files:
- `OpenSans[wdth,wght].ttf` (upright)
- `OpenSans-Italic[wdth,wght].ttf` (italic)

Both are sourced directly from the `fonts/variable/` directory of the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/googlefonts/opensans
- `commit`: `bd7e37632246368c60fdcbd374dbf9bad11969b6`
- `branch`: main
- File mappings for variable fonts and OFL.txt are present.

No changes to METADATA.pb were required.

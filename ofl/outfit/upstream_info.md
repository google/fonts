# Outfit — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/Outfitio/Outfit-Fonts, maintained by the Outfitio GitHub organization (outfit.io, a brand automation company). The METADATA.pb source block was already present with the correct repository URL and commit, which corresponds to the HEAD of the `main` branch.

## Repository

- **URL**: https://github.com/Outfitio/Outfit-Fonts
- **Default branch**: `main`
- **Description**: The most on-brand typeface

## Commit

- **Pinned commit**: `902773808eb372f70fb34e8946dd1ffe604efc79`
- **Commit message**: Outfit update - decomposed some glyphs, added kerning groups, math symbols width, check outlines etc.
- **Commit date**: 2023-03-26
- **Status**: This is the HEAD of the `main` branch — the repository is up-to-date with the pinned commit.

## Font Details

Outfit is a geometric sans serif typeface designed by Rodrigo Fuenzalida for Smartsheet Inc / outfit.io. It serves as the official typeface for the brand automation company, linking the Outfit written voice to Outfit product marks. The family was updated in 2023 to expand language support. The variable font exposes a `wght` axis (100–900).

The Google Fonts version ships a single variable font: `Outfit[wght].ttf`, sourced from `fonts/variable/` in the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/Outfitio/Outfit-Fonts
- `commit`: `902773808eb372f70fb34e8946dd1ffe604efc79`
- `branch`: main
- `config_yaml`: sources/config.yaml
- File mappings for OFL.txt and Outfit[wght].ttf are present.

No changes to METADATA.pb were required.

# Oxanium — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/sevmeyer/oxanium, maintained by Severin Meyer. The METADATA.pb source block was already present with the correct repository URL and commit, which corresponds to the HEAD of the `master` branch.

## Repository

- **URL**: https://github.com/sevmeyer/oxanium
- **Default branch**: `master`
- **Description**: Oxanium font family

## Commit

- **Pinned commit**: `a8f39e0c71186190027a093e9001459410192d1e`
- **Commit message**: Update fonts
- **Commit date**: 2020-09-30
- **Status**: This is the HEAD of the `master` branch — the repository is up-to-date with the pinned commit.

## Font Details

Oxanium is a square, futuristic display typeface designed by Severin Meyer. The design is intended to evoke head-up displays (HUDs) of spaceships and scoreboards of video games. Angled cuts add character to headlines, while the intuitive strokes maintain legibility at small sizes. The family covers a `wght` axis range of 200–800.

The Google Fonts version ships one variable font (`Oxanium[wght].ttf`) and seven static TTFs (ExtraLight, Light, Regular, Medium, SemiBold, Bold, ExtraBold), all sourced from the upstream repository's `fonts/` directory.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/sevmeyer/oxanium
- `commit`: `a8f39e0c71186190027a093e9001459410192d1e`
- `branch`: master
- File mappings for OFL.txt, Oxanium[wght].ttf (variable), and seven static TTF files are present.

No changes to METADATA.pb were required.

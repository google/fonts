# Oswald — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository was identified at https://github.com/googlefonts/OswaldFont, maintained under the `googlefonts` GitHub organization. The METADATA.pb source block was already present with the correct repository URL and pinned commit.

## Repository

- **URL**: https://github.com/googlefonts/OswaldFont
- **Default branch**: `main`
- **Description**: repo for the Oswald font family

## Commit

- **Pinned commit**: `89795261ac9eeb9aa8cd99f43982c4e4b0e53261`
- **Commit message**: Merge pull request #26 from MrBrain295/patch-1 — Fix dead link
- **Commit date**: 2024-05-29
- **Status**: This is the HEAD of the `main` branch — the repository is up-to-date with the pinned commit.

## Font Details

Oswald is a reworking of the classic style historically represented by the Alternate Gothic sans serif typefaces. The characters were re-drawn and reformed to fit the pixel grid of digital screens. The family was originally designed by Vernon Adams, who developed it continuously until 2014. In 2016, Kalapi Gajjar completed the Latin update. In January 2019, a variable font Weight axis (200–700) was added. In July 2023, Cyrillic coverage was expanded and math symbol rendering was improved.

The Google Fonts version ships a single variable font: `Oswald[wght].ttf`, sourced from `fonts/variable/` in the upstream repository.

## Source Block Status

The METADATA.pb source block was already fully populated:
- `repository_url`: https://github.com/googlefonts/OswaldFont
- `commit`: `89795261ac9eeb9aa8cd99f43982c4e4b0e53261`
- `branch`: main
- `config_yaml`: sources/config.yaml
- File mappings for OFL.txt and Oswald[wght].ttf are present.

No changes to METADATA.pb were required.

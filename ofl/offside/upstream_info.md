# Offside — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Offside was identified at https://github.com/etunni/offside, authored by Eduardo Tunni (Eduardo Rodríguez Tunni). This is a display sans-serif typeface. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/etunni/offside
- **Default branch**: master
- **License**: SIL Open Font License 1.1
- **Description**: "libre font"

## Pinned Commit

- **Commit**: `025804545334bb6270119f43fb8fe7d05b31cd7d`
- **Date**: 2023-02-03
- **Message**: "Merge pull request #1 from emmamarichal/master — Offside upgrade"
- **Author**: Eduardo Rodríguez Tunni

The pinned commit is the HEAD of the master branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Source Files

The repository contains a Glyphs source file at `sources/Offside.glyphs`. The METADATA.pb specifies font files sourced directly from `fonts/ttf/Offside-Regular.ttf` without a separate config_yaml, indicating a direct binary reference.

## Confidence

**High** — The repository URL is referenced in the font's copyright string and matches the designer attribution. The commit is the latest on the repository.

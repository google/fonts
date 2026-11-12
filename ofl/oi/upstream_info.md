# Oi — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Oi was identified at https://github.com/kosbarts/Oi, authored by Kostas Bartsokas. This is a multi-script display serif typeface covering Latin, Cyrillic, Greek, Arabic, Tamil, and Vietnamese. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/kosbarts/Oi
- **Default branch**: main
- **License**: SIL Open Font License 1.1
- **Description**: "Oi is a static display font."

## Pinned Commit

- **Commit**: `bd7ccfa844054ec4a0b2b17e56c33830646668ea`
- **Date**: 2024-12-04
- **Message**: "Update AUTHORS.txt"
- **Author**: Kostas Bartsokas

The pinned commit is the HEAD of the main branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Source Files

The repository contains a Glyphs source file at `sources/Oi.glyphs` along with a `sources/config.yaml` build configuration. The METADATA.pb specifies `config_yaml: "sources/config.yaml"` and references the font binary at `fonts/ttf/Oi-Regular.ttf`.

## Confidence

**High** — The repository URL is referenced in the font's copyright string and matches the designer attribution. The commit is the latest on the repository.

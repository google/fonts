# Ole — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Ole was identified at https://github.com/googlefonts/ole, authored by Robert Leuschke. This is a handwriting-style typeface. The repository is hosted under the googlefonts organization, suggesting it was onboarded through the standard Google Fonts production pipeline. The source block in METADATA.pb was already present and accurate.

## Repository

- **URL**: https://github.com/googlefonts/ole
- **Default branch**: master
- **License**: SIL Open Font License 1.1
- **Description**: "OhLey fonts"

## Pinned Commit

- **Commit**: `fe77f34a3002bc4c2e26a8e27bee31cb45307846`
- **Date**: 2021-12-02
- **Message**: "Description updated"
- **Author**: Viviana Monsalve

The pinned commit is the HEAD of the master branch — the repository has not received any commits since. The Google Fonts version is current with upstream.

## Source Files

The repository contains a Glyphs source file at `sources/Ole.glyphs` along with a `sources/config.yml` build configuration. The METADATA.pb specifies `config_yaml: "sources/config.yml"` and references the font binary at `fonts/ttf/Ole-Regular.ttf`.

## Confidence

**High** — The repository URL is referenced in the font's copyright string. The googlefonts organization hosting is consistent with standard Google Fonts production workflow.

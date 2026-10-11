# Kirang Haerang — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/woowabros/KirangHaerang |
| Commit | `544ae6224fa83a85a0b4954e188c4791a98e3ce9` |
| Confidence | High |

## Source Types

The repository contains compiled font files only:
- `FONT/KIRANGHAERANG.otf and KIRANGHAERANG.ttf` — OTF and TTF binaries

No editable design sources (Glyphs, UFO, etc.) are available.

## Build Compatibility

Not buildable with gftools-builder. The repository contains only compiled OTF/TTF binaries, not editable source files. This is typical of Korean font releases from Woowahan Brothers (Baemin/Baedal Minjok).

## Investigation Notes

Woowahan Brothers (the company behind Baemin/Baedal Minjok food delivery service) released several Korean display fonts as open source. The Kirang Haerang repository contains only the final compiled fonts without design sources. The binary in google/fonts was last updated on 2024-01-19 (hotfix for space & nbspace characters).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: High

Woowahan Brothers (woowabros) is the original publisher and this is their official repository.

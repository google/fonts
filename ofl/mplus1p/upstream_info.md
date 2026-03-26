# M PLUS 1p — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/coz-m/MPLUS_FONTS |
| Commit | `9cb1a484f5f8c5c18c7e2f83a13c812aec15c11d` |
| Confidence | Medium |

## Source Types

The repository contains Glyphs and Designspace sources:
- `.glyphs` files — Glyphs source format
- `.designspace` files — designspace/UFO format

## Build Compatibility

No `config.yaml` is present in the upstream repository. The sources use modern formats compatible with gftools-builder in principle, but an override config would be needed.

## Investigation Notes

The coz-m/MPLUS_FONTS repository is the new M PLUS project by Coji Morishita. This repository contains the redesigned M PLUS font family. M PLUS 1p is the older/"legacy" version of the M PLUS 1 design — the confidence is medium because this repository primarily covers the new M PLUS 1 (variable font) and it needs verification whether it also covers the legacy M PLUS 1p static font variant specifically.

The binary in google/fonts was last updated on 2022-07-29 (MPLUS1p fix, PR #4981).

A source block was added to METADATA.pb pointing to this repository and commit.

## Confidence: Medium

The repository covers the M PLUS family broadly, but verification is needed that M PLUS 1p (the legacy static variant) is specifically produced from these sources.

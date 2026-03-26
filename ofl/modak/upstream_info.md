# Modak — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [https://github.com/EkType/Modak](https://github.com/EkType/Modak) |
| Commit | `143b2db4fd2279b71e68f22bba4b43a8a3a9de69` |
| Version | 1.036 |
| Date Added | 2015-02-18 |

## Investigation Summary

Modak is a heavy, rounded Devanagari + Latin display typeface designed by Ek Type (Girish Dalvi and Noopur Datye). The upstream repository at `EkType/Modak` contains VFB source files and AFDKO build configuration (feature files, GlyphOrderAndAliasDB, GPOS/GSUB/GDEF tables).

The font was added to google/fonts in the initial bulk import (2015-03-07). The shipped version is 1.036, built with AFDKO (`makeotf.lib2.5.61930`) and autohinted with `ttfautohint v1.2.42`. Commit `143b2db4` (2015-02-25, "धारिका अद्यतनित केली" — Marathi for "font updated") is the last content update before the google/fonts import date.

## Source Files

- `SourceFiles/VFB/Modak.vfb` — FontLab source (proprietary format)
- `SourceFiles/features` — OpenType feature code (AFDKO format)
- `SourceFiles/GPOS`, `SourceFiles/GSUB`, `SourceFiles/GDEF` — OpenType layout tables
- `SourceFiles/GlyphOrderAndAliasDB` — AFDKO glyph ordering
- `SourceFiles/classes` — OpenType class definitions
- `TTX/Modak-Regular.ttx` — TTX dump of the compiled font

## Build Pipeline

The font was built using **Adobe AFDKO** (Adobe Font Development Kit for OpenType), not gftools-builder or fontmake. The VFB source was processed through `makeotf` with the feature/table files in `SourceFiles/`. No `config.yaml` is applicable for this build pipeline.

## Commit Verification

Commit `143b2db4` is the last commit with content changes before the google/fonts bulk import on 2015-03-07. The repo had further updates in May 2016 (TTF build fixes, minor updates) but the font in google/fonts was never updated from the initial import.

**Confidence**: MEDIUM (date correlation — last content commit before import, but no blob-level verification performed)

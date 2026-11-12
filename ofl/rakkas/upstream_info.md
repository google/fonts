# Rakkas — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/zeynepakay/Rakkas
- **Commit**: `3bdb0ba164c9e987a5ab4de7f7cc8842a04d267a`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
Designed by Zeynep Akay. A display serif typeface with Arabic as the primary script (Arab). Supports Arabic, Latin, and Latin Extended subsets. Hosted in the designer's own GitHub repository.

## Source repository and pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The source block moved from `zeynepakay/Rakkas` at [`3bdb0ba1`](https://github.com/zeynepakay/Rakkas/commit/3bdb0ba1) (the 2016 v1.1 source) to `Gue3bara/Rakkas` at [`2c9d43f8`](https://github.com/Gue3bara/Rakkas/commit/2c9d43f8) (`Fixed Glyph "r" contour`, 2017-10-17, on the fork's default `gh-pages` branch).

The shipped v2.000 `Rakkas-Regular.ttf` ([google/fonts#1260](https://github.com/google/fonts/pull/1260), [google/fonts `d92a2957`](https://github.com/google/fonts/commit/d92a2957), "includes modification mark by Mohamed Gaber") is byte-identical to `Rakkas_FontFiles/TTF/Rakkas-Regular.ttf` at `2c9d43f8` (md5 `928935e49bd0eddabd057c3e72fcdf3e`). Mohamed Gaber offered this work back to the designer's repository as [zeynepakay/Rakkas#23](https://github.com/zeynepakay/Rakkas/pull/23), which is still unmerged, so the commit is on no branch of the designer's repository.

`Rakkas_SourceFiles/Rakkas (Autosaved).glyphs` does not exist at `2c9d43f8`, so it was dropped from the override `config.yaml`; `Rakkas_SourceFiles/Rakkas.glyphs` remains.

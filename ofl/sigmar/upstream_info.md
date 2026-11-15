# Sigmar

**Designer**: Vernon Adams
**License**: OFL
**Category**: Display
**Date Added**: 2023-02-24

**Model**: Claude Opus 4.6

## Source Repository

- **Repo**: https://github.com/googlefonts/sigmarone
- **Commit**: 1fb4311d78953da0f943e0e4b806acdd076af81b
- **Branch**: main

## Summary

Sigmar (formerly Sigmar One) was designed by Vernon Adams and hosted under the googlefonts GitHub organization. The family consisted of a single regular weight static TTF. It supported Latin, Latin Extended, and Vietnamese subsets. The font was classified as a Display typeface.

## Override config corrected (2026-11-13)

**Model**: Claude Opus 5.5

The override named `archive/Sigmar.glyphs`, an old Glyphs 2 copy that defines `Ymacron.sc` twice. The shipped TTF is byte-identical to upstream's `fonts/ttf/Sigmar-Regular.ttf`, built from `sources/Sigmar.glyphs`, so the override now names that.

With gftools 0.10.8 and fontmake 3.12.2, it matches the shipped glyph set, cmap, bounds and advances exactly.

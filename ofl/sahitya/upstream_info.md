# Sahitya — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sahitya was identified at `huertatipografica/sahitya` on GitHub. The repository contained Glyphs source files for both weights at the repository root. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/huertatipografica/sahitya
- **Owner**: huertatipografica (HT Fonts)
- **Branch**: master
- **Commit**: `3d5fba22c2baba55989c9dd6daa8e4be47bb0cd4`
- **Commit message**: "fixed some conjuncts"

## Source Files Found

| File | Type |
|------|------|
| `Sahitya-Regular.glyphs` | Glyphs source (Regular weight) |
| `Sahitya-Bold.glyphs` | Glyphs source (Bold weight) |

## Designer

Sahitya was designed by Juan Pablo del Peral of HT Fonts (htfonts.com). The repository is hosted under the `huertatipografica` GitHub organization.

## Investigation Notes

The repository was located by checking the `huertatipografica` GitHub organization (matching the designer's website domain in the copyright notice). The repository `huertatipografica/sahitya` was confirmed to exist. The root directory contained two Glyphs source files corresponding to the Regular and Bold weights. The font covers the Devanagari and Latin scripts.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and both Glyphs source files.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sahitya/` referencing the upstream gftools-builder-compatible source at the pinned commit `c4b5b34` (`Sahitya-Regular.glyphs`, `Sahitya-Bold.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`c4b5b34d`](https://github.com/huertatipografica/sahitya/commit/c4b5b34d) ("fixed some conjuncts", 2015-12-22) to [`3d5fba22`](https://github.com/huertatipografica/sahitya/commit/3d5fba22) ("New name, added ttfs", 2015-01-27, on `master`). google/fonts added Sahitya in [google/fonts `d1f5f504`](https://github.com/google/fonts/commit/d1f5f504) on 2015-06-15; the next upstream source change was in August 2015.

The shipped TTFs are the `ttf/Sahitya-*.ttf` committed in `3d5fba22`, edited by google/fonts. Glyph set, cmap, hmtx, GDEF, cvt and GSUB/GPOS content are identical, and so are the outlines, except that five anusvara composites in the Regular (one in the Bold) have a component scale 1/16384 apart, a rounding left by a TTX round-trip. google/fonts changed name and head (1.000 to 1.001), OS/2 fsType (8 to 0) and the vertical metrics; the round-trip also re-encoded the hinting push instructions. md5 shipped vs upstream: Regular `632c6adbdecc916d4ac1f56764b21d0c` vs `00b8a4c9f382be673c0713127e7e9f47`, Bold `d8517b0250b5cbd66bdae199940c7b95` vs `61f746d5c273749028e2a276b22ca8d4`.

The override `config.yaml` and the `files` entries name `Sahitya-Regular.glyphs` and `Sahitya-Bold.glyphs`, which exist at `3d5fba22`.

# Sahitya — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sahitya was identified at `huertatipografica/sahitya` on GitHub. The repository contained Glyphs source files for both weights at the repository root. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/huertatipografica/sahitya
- **Owner**: huertatipografica (Huerta Tipográfica)
- **Branch**: master
- **Commit**: `c4b5b34d0fbad63654b1d9a6bff72e566bf9a2c6`
- **Commit message**: "fixed some conjuncts"

## Source Files Found

| File | Type |
|------|------|
| `Sahitya-Regular.glyphs` | Glyphs source (Regular weight) |
| `Sahitya-Bold.glyphs` | Glyphs source (Bold weight) |

## Designer

Sahitya was designed by Juan Pablo del Peral of Huerta Tipográfica (huertatipografica.com). The repository is hosted under the `huertatipografica` GitHub organization.

## Investigation Notes

The repository was located by checking the `huertatipografica` GitHub organization (matching the designer's website domain in the copyright notice). The repository `huertatipografica/sahitya` was confirmed to exist. The root directory contained two Glyphs source files corresponding to the Regular and Bold weights. The font covers the Devanagari and Latin scripts.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and both Glyphs source files.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sahitya/` referencing the upstream gftools-builder-compatible source at the pinned commit `c4b5b34` (`Sahitya-Regular.glyphs`, `Sahitya-Bold.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

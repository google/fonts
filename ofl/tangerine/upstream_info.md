# Tangerine — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Tangerine was found at https://github.com/googlefonts/TangerineFont, hosted under the googlefonts organization. The repository contained Glyphs source files for both weights of the family. Tangerine is a handwriting typeface by Toshi Omagari.

## Repository

- **URL**: https://github.com/googlefonts/TangerineFont
- **Owner**: googlefonts
- **Default branch**: main
- **Commit used**: `9b57a9f9be5ecfe95e7f8c0e6b2b827eedb9ad67`
- **Source format**: Glyphs

## Source Files

The `sources/` directory contained:
- `Tangerine_Bold.glyphs`
- `Tangerine_Regular.glyphs`

## Confidence

High — the repository was hosted under the googlefonts organization and described as "by Toshi Omagari", matching the designer credited in METADATA.pb.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/tangerine/` referencing the upstream gftools-builder-compatible source at the pinned commit `9b57a9f` (`sources/Tangerine_Regular.glyphs`, `sources/Tangerine_Bold.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

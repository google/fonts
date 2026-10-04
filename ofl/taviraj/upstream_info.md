# Taviraj — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Taviraj was found at https://github.com/cadsondemak/taviraj, hosted under the cadsondemak GitHub organization. The repository contained individual Glyphs source files for each weight and style of the family. Taviraj is a Thai serif typeface designed by Cadson Demak.

## Repository

- **URL**: https://github.com/cadsondemak/taviraj
- **Owner**: cadsondemak
- **Default branch**: master
- **Commit used**: `8bd077c195dccf3bfc4699ec6ae9c6909bdd03a5`
- **Source format**: Glyphs

## Source Files

The `source/` directory contained individual Glyphs files for each weight/style combination, including:
- Taviraj-100_Thin.glyphs, Taviraj-100_Thin_Ita.glyphs
- Taviraj-200_ExtraLight.glyphs, Taviraj-200_ExtraLight_Ita.glyphs
- Taviraj-300_Light.glyphs, Taviraj-300_Light_Ita.glyphs
- Taviraj-400_Regular.glyphs, Taviraj-400_Regular_Ita.glyphs
- Taviraj-500_Medium.glyphs, Taviraj-500_Medium_Ita.glyphs
- Taviraj-600_DemiBold.glyphs, Taviraj-600_DemiBold_Ita.glyphs
- Taviraj-700_Bold.glyphs, Taviraj-700_Bold_Ita.glyphs
- Taviraj-800_ExtraBold.glyphs, Taviraj-800_ExtraBold_Ita.glyphs
- Taviraj-900_Black.glyphs, Taviraj-900_Black_Ita.glyphs

## Confidence

High — the repository was hosted under the official Cadson Demak GitHub organization, matching the designer credited in METADATA.pb.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/taviraj/` referencing the upstream gftools-builder-compatible source at the pinned commit `8bd077c` (`source/Taviraj-100_Thin.glyphs`, `source/Taviraj-100_Thin_Ita.glyphs`, `source/Taviraj-200_ExtraLight.glyphs`, `source/Taviraj-200_ExtraLight_Ita.glyphs`, `source/Taviraj-300_Light.glyphs`, `source/Taviraj-300_Light_Ita.glyphs`, `source/Taviraj-400_Regular.glyphs`, `source/Taviraj-400_Regular_Ita.glyphs`, `source/Taviraj-500_Medium.glyphs`, `source/Taviraj-500_Medium_Ita.glyphs`, `source/Taviraj-600_DemiBold.glyphs`, `source/Taviraj-600_DemiBold_Ita.glyphs`, `source/Taviraj-700_Bold.glyphs`, `source/Taviraj-700_Bold_Ita.glyphs`, `source/Taviraj-800_ExtraBold.glyphs`, `source/Taviraj-800_ExtraBold_Ita.glyphs`, `source/Taviraj-900_Black.glyphs`, `source/Taviraj-900_Black_Ita.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

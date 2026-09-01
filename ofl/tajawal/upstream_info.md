# Tajawal — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12
**Investigator**: AI agent (Claude) under guidance of @felipesanches

## Summary

The canonical upstream repository for Tajawal was found at https://github.com/googlefonts/tajawal. The repository contained UFO source files in `source/1-drawings/` (individual weight UFOs) and `source/2-production/` (production UFOs). The repository was described as a "Distinctive low contrast Arabic and sans serif Latin typeface family" created by Boutros Fonts.

## Repository

- **URL**: https://github.com/googlefonts/tajawal
- **Owner**: googlefonts
- **Default branch**: main
- **Commit used**: `2085b8942f234e7afb83dc03c77713d0d5471cc9`
- **Source format**: UFO

## Source Files

The `source/` directory contained:
- `1-drawings/` — Tajawal-Black, Tajawal-Bold, Tajawal-ExtraBold, Tajawal-ExtraLight, Tajawal-Light, Tajawal-Medium, Tajawal-Regular directories
- `2-production/` — Production-ready UFO files: Tajawal-Black.ufo, Tajawal-Bold.ufo, Tajawal-ExtraBold.ufo, Tajawal-ExtraLight.ufo, Tajawal-Light.ufo, Tajawal-Medium.ufo, Tajawal-Regular.ufo

## Confidence

High — the repository was linked in the family's DESCRIPTION.en_us.html and hosted under the googlefonts organization.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/tajawal/` referencing the upstream gftools-builder-compatible source at the pinned commit `2085b89` (`source/1-drawings/Tajawal-ExtraLight.ufo`, `source/1-drawings/Tajawal-Light.ufo`, `source/1-drawings/Tajawal-Regular.ufo`, `source/1-drawings/Tajawal-Medium.ufo`, `source/1-drawings/Tajawal-Bold.ufo`, `source/1-drawings/Tajawal-ExtraBold.ufo`, `source/1-drawings/Tajawal-Black.ufo`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

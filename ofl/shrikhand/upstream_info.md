# Shrikhand — Upstream Source Investigation

**Designer**: Jonny Pinhorn
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Shrikhand was found at `jonpinhorn/shrikhand` on GitHub. The repository contained both UFO and Glyphs source files and was maintained by Jonny Pinhorn, the credited designer.

## Repository

- **URL**: https://github.com/jonpinhorn/shrikhand
- **Commit**: `c11c9b0720fba977fad7cb4f339ebacdba1d1394`
- **Commit date**: 2016-03-03
- **Default branch**: master

## Sources Found

The `masters/` directory contained:
- `Shrikhand-Regular.ufo`
- `Shrikhand.glyphs`

Both UFO and Glyphs format sources were available for this Gujarati and Latin display typeface.

## Confidence

High. The repository was hosted under the jonpinhorn account (the credited designer) and contained primary source files for the font.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/shrikhand/` referencing the upstream gftools-builder-compatible source at the pinned commit `c11c9b0` (`masters/Shrikhand.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

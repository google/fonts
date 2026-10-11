# Scada — Upstream Source Investigation

**Designer**: Jovanny Lemonad
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Scada was found at `googlefonts/scada` on GitHub. The repository contained Glyphs source files for both the upright and italic styles. The source was confirmed to be the primary development repository, managed under the googlefonts organization.

## Repository

- **URL**: https://github.com/googlefonts/scada
- **Commit**: `df06a155d95984d259c8492aeaaa520188a3d46b`
- **Commit date**: 2017-03-13
- **Default branch**: main

## Sources Found

The `sources/` directory contained:
- `Scada-Italic.glyphs`
- `Scada.glyphs`

These Glyphs source files covered all four styles (Regular, Italic, Bold, Bold Italic).

## Confidence

High. The repository was hosted under the googlefonts organization and contained Glyphs source files directly corresponding to the released font binaries.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/scada/` referencing the upstream gftools-builder-compatible source at the pinned commit `df06a15` (`sources/Scada.glyphs`, `sources/Scada-Italic.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

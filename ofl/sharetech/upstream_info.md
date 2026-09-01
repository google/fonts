# Share Tech — Upstream Source Investigation

**Designer**: Carrois Apostrophe
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Share Tech was found at `m4rc1e/ShareTech` on GitHub. The repository was described as being "by Ralph Oliver du Carrois" (Carrois Apostrophe) and contained Glyphs source files.

## Repository

- **URL**: https://github.com/m4rc1e/ShareTech
- **Commit**: `2c501093f8f4fc6d985435133c8ac0fa92137431`
- **Commit date**: 2016-11-09
- **Default branch**: master

## Sources Found

The `sources/` directory contained:
- `ShareTech.glyphs`

The repository also included fonts directory, METADATA.pb, OFL.txt, and README.

## Confidence

High. The repository was described explicitly as "by Ralph Oliver du Carrois" (the principal designer at Carrois Apostrophe) and contained Glyphs source files for Share Tech. Note: no separate upstream repository was found for Share Tech Mono; this repository appears to cover only Share Tech Regular.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Upstream has both compatible sources (.glyphs) and legacy `.sfd`/`.vfb` archives at the pinned commit `2c50109` (upstream legacy: .sfd/.vfb archives in old/version-1.002/src/). Added an override `config.yaml` in `ofl/sharetech/` that references the compatible sources only (`sources/ShareTech.glyphs`). The legacy archives are retained upstream for historical reference but are not consumed by gftools-builder. `google-fonts-sources` auto-detects the override on the next regeneration of crater's `targets.json`.

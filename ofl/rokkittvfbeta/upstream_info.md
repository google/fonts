# Rokkitt VF Beta — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

This directory has no METADATA.pb file, so no source block was added. However, the canonical upstream repository for Rokkitt (including the VF Beta) is identified as:

- **URL**: https://github.com/Fonthausen/RokkittFont
- **Branch**: master
- **Latest commit**: `762d1439aaa7cf4a590f604451dfc2e1c6970b9f` (2023-01-27)
- **Source format**: Glyphs (`sources/Rokkitt.glyphs`, `sources/Rokkitt-Italic.glyphs`)

## What Was Done

The OFL.txt file referenced `https://github.com/googlefonts/RokkittFont` as the project's Git repository. The `googlefonts/RokkittFont` repository was confirmed to exist with Glyphs source files. The canonical upstream `Fonthausen/RokkittFont` was also found — this is the same repository already referenced in the regular `rokkitt` family's METADATA.pb source block. The VF Beta appears to be an earlier variable font release from the same source.

## Notes

The `rokkittvfbeta` directory contains only `OFL.txt` and `RokkittVFBeta.ttf` with no METADATA.pb. This appears to be an obsolete VF Beta release that predates the full variable font release now in the `rokkitt` directory. The regular `rokkitt` family already has a proper `source` block pointing to `Fonthausen/RokkittFont`. No further action was taken on this directory.

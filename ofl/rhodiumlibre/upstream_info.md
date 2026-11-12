# Rhodium Libre — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **URL**: https://github.com/DunwichType/RhodiumLibre
- **Owner**: DunwichType (Dunwich Type Founders, James Puckett)
- **Branch**: master
- **Latest commit**: `c6e9dc9167fb6f4bc6fc44f2262129aaf771c8a3` (2015-06-22)
- **Source format**: UFO (`RhodiumLibre-Regular.ufo`) and Glyphs (`RhodiumLibre-Regular.glyphs`)

## What Was Done

The canonical upstream repository was identified from the `DESCRIPTION.en_us.html` file which explicitly linked to `github.com/DunwichType/RhodiumLibre`. A fork of this repository exists at `davelab6/RhodiumLibre`, but `DunwichType/RhodiumLibre` was confirmed as the upstream canonical source. The repository contains both UFO and Glyphs source files. The latest commit hash was verified via the GitHub API. A `source` block was added to `METADATA.pb`.

## Notes

The designer is James Puckett of Dunwich Type Founders (`http://dunwichtype.com`), consistent with the copyright statement in METADATA.pb. The repository was last updated in 2015.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/rhodiumlibre/` referencing the upstream gftools-builder-compatible source at the pinned commit `c6e9dc9` (`RhodiumLibre-Regular.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`c6e9dc91`](https://github.com/DunwichType/RhodiumLibre/commit/c6e9dc91) to [`d0885714`](https://github.com/DunwichType/RhodiumLibre/commit/d0885714) ("Version 1.1.0 update", 2015-04-08, tag v1.1.0, on `master`). `c6e9dc91` ("Numerous changes", 2015-06-22) is v1.002, committed three weeks after google/fonts added the font in [google/fonts `ecb4c3d4`](https://github.com/google/fonts/commit/ecb4c3d4) (2015-06-01). Only a README edit falls between `d0885714` and the onboarding.

The shipped `RhodiumLibre-Regular.ttf` matches `RhodiumLibre-Regular.ttf` at `d0885714` in outlines, cmap, layout and every advance but one: google/fonts widened `uni00A0` from 190 to 280, the width of the space. The other differences are name, head, OS/2 fsType (8 to 0) and a TTX round-trip that re-encoded GSUB/GPOS and the hinting push instructions without changing their content. md5 shipped `91e197f0dae289736f70461e0f9a38ad`, upstream `cc89b018532d8f65975ee508264e4de2`.

The override `config.yaml` (`RhodiumLibre-Regular.glyphs`) resolves at `d0885714`.

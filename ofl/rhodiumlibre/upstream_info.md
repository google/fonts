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

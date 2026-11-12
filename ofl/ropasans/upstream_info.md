# Ropa Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **URL**: https://github.com/lettersoup/Ropa-Sans
- **Owner**: lettersoup (Botjo Nikoltchev, lettersoup.de)
- **Branch**: master
- **Latest commit**: `33acc9f9e7d126dd46b9e1efa03f98ea2e2046de` (2016-11-17)
- **Source format**: Glyphs (`RopaSans.glyphs`, `RopaSans-Italic.glyphs`)

## What Was Done

The canonical upstream repository at `lettersoup/Ropa-Sans` was found via a GitHub API search. The `lettersoup` GitHub account is consistent with the designer Botjo Nikoltchev whose email domain `lettersoup.de` appears in the copyright string in METADATA.pb. The repository contains Glyphs source files for both the Regular and Italic weights. The latest commit hash was verified via the GitHub API. A `source` block was added to `METADATA.pb`.

## Notes

The repository also contains a `fonts/` directory with compiled OTF/TTF files and a `FONTLOG.txt`. The sources directory holds the Glyphs files. The repo was last updated in 2016.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/ropasans/` referencing the upstream gftools-builder-compatible source at the pinned commit `33acc9f` (`sources/RopaSans.glyphs`, `sources/RopaSans-Italic.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

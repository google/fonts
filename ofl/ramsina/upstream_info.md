# Ramsina — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/silnrsi/font-ramsina
- **Commit**: `263c8d552bff566fad9e8c9b266ae32e6ab341b4`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed. The repository URL and commit hash were confirmed present in METADATA.pb.

## Notes
Designed by SIL International. A serif typeface with Syriac as the primary script (Syrc), one of the newer additions to Google Fonts (date_added: 2026-01-21). Supports Latin and Syriac subsets. Distributed via a release archive zip. The copyright notice indicates its origin includes glyphs from Sparksoft Systems' "Marcus" and "Nohadra" fonts, as well as Latin glyphs from Crimson Pro.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/ramsina/` referencing the upstream gftools-builder-compatible source at the pinned commit `263c8d5` (`source/Ramsina.designspace`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Recent upstream/main activity (post-investigation)

The original onboarding and subsequent metadata edits:

- **2026-01-21** — Emma Marichal, commit [`653676022`](https://github.com/google/fonts/commit/653676022) ("Ramsina: Version 2.000 added"): initial onboarding via gftools-packager. Created `ofl/ramsina/` with the binary `Ramsina-Regular.ttf`, OFL.txt, and METADATA.pb (with the source block referencing the upstream commit).
- **2026-01-21** — Emma Marichal, commit [`e03d57ffe`](https://github.com/google/fonts/commit/e03d57ffe) ("Update designer name to 'SIL International'"): same-day correction of the `designer` field. Outside the `source { ... }` block.
- **2026-01-22** — Emma Marichal, commit [`5c440604d`](https://github.com/google/fonts/commit/5c440604d) ("Change font category from SANS_SERIF to SERIF"): re-categorised the family. Outside the `source { ... }` block.

**Model**: Claude Opus 4.6

# Suez One — Upstream Source Investigation

## Summary

The canonical upstream repository for Suez One was identified at `https://github.com/MichalSahar/Suez`, maintained by Michal Sahar. The repository contained a Glyphs source file (`sources/SuezOne.glyphs`).

## Repository Details

- **Repository**: https://github.com/MichalSahar/Suez
- **Owner**: MichalSahar (Michal Sahar)
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `04af4fcca02b34b461033520fc758132f7519c49`
- **Commit message**: "Merge pull request #1 from davelab6/master — Add OFL, README, Google Fonts description"
- **Default branch**: master
- **Description**: "Hebrew+Latin Serif typeface"

## Source Files

The `sources/` directory contained:
- `SuezOne.glyphs`

## Confidence

**High** — The GitHub user `MichalSahar` matched the designer name in METADATA.pb (Michal Sahar). The repository description "Hebrew+Latin Serif typeface" matched the font's character: Suez One covers Hebrew and Latin scripts. The Glyphs source file was present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/MichalSahar/Suez` at commit `04af4fcca02b34b461033520fc758132f7519c49`.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/suezone/` referencing the upstream gftools-builder-compatible source at the pinned commit `04af4fc` (`sources/SuezOne.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

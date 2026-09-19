# Pathway Extreme — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Pathway Extreme was identified at https://github.com/etunni/Pathway-Variable-Font, maintained by Eduardo Tunni under his personal GitHub account (`etunni`). The METADATA.pb file referenced commit `4fa691f3898690d1f485839743ace01c5e6410da` on the `master` branch, with build configuration at `sources/config.yaml`. The font was added to Google Fonts on 2023-02-08.

## Font Description

Pathway Extreme is a highly versatile variable sans-serif typeface by Eduardo Tunni. It exposes three variation axes: optical size (`opsz`, 8–144), width (`wdth`, 75–100), and weight (`wght`, 100–900). The family includes both upright and italic variable fonts. The registry default override sets the optical size to 12pt. The design is classified as both display and sans-serif, and covers Latin and Latin Extended scripts, as well as Vietnamese.

## Designer

Eduardo Tunni is an Argentine type designer. The font was developed starting in 2019 and represents an extensive expansion of his earlier Pathway Gothic One typeface into a full variable font family.

## Repository

- **URL**: https://github.com/etunni/Pathway-Variable-Font
- **Commit**: `4fa691f3898690d1f485839743ace01c5e6410da`
- **Branch**: `master`
- **Config**: `sources/config.yaml`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | DISPLAY / SANS_SERIF |
| Style | Regular + Italic |
| Weight Axis | 100–900 |
| Width Axis | 75–100 |
| Optical Size Axis | 8–144 |
| Subsets | latin, latin-ext, vietnamese |
| Variable | Yes (opsz, wdth, wght) |

## File Mapping

The source block specified explicit file mappings: `OFL.txt`, `fonts/variable/PathwayExtreme[opsz,wdth,wght].ttf`, and `fonts/variable/PathwayExtreme-Italic[opsz,wdth,wght].ttf` were mapped from the upstream repository.

## Confidence

**High** — The repository is referenced directly in both the METADATA.pb `repository_url` and the copyright notice. The commit and branch are explicitly specified.

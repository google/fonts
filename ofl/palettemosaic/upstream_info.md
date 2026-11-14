# Palette Mosaic — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Palette Mosaic is a Japanese display font developed by Shibuya Font. The source block in METADATA.pb pointed to the GitHub repository but was missing a commit hash. The HEAD commit was identified as the correct reference and was added.

## Repository

- **URL**: https://github.com/shibuyafont/Palette-mosaic-font-mono
- **Upstream cache**: Not present in the fontc_crater_cache (no `shibuyafont/` directory found)

## Version Identification

The font binary in the Google Fonts repo was inspected:

- `PaletteMosaic-Regular.ttf`: Version 1.001, nameID3 = "1.001;SBYA;PaletteMosaic-Regular"

## Commit History Analysis

The full commit history of the repository was retrieved. The repository has 20 commits total. The commit history relevant to the font binary at `fonts/ttf/PaletteMosaic-Regular.ttf` was queried:

```
gh api "repos/shibuyafont/Palette-mosaic-font-mono/commits?path=fonts/ttf/PaletteMosaic-Regular.ttf"
```

Only one commit modified that file:

- `155e6ec5d439f1cbd54fb808ac93ce2a07ebce97` (2021-04-14): "Per Dave's request, updating font name. Now 'Palette Mosaic'."

This commit renamed the font from "Palette Mosaic Font One" (PaletteMosaicFontOne-Regular.ttf) to "Palette Mosaic" (PaletteMosaic-Regular.ttf). The Google Fonts family was added on 2021-04-13 — one day before this rename commit. Subsequent commits (26ac1e98, 461da4c5) only modified README.md.

The HEAD commit `461da4c5f2ca2d38a590d27468252b9b4a54e31f` was confirmed to contain `fonts/ttf/PaletteMosaic-Regular.ttf` and was verified via the GitHub API:

```
gh api repos/shibuyafont/Palette-mosaic-font-mono/commits/461da4c5f2ca2d38a590d27468252b9b4a54e31f --jq '.sha'
# Returns: 461da4c5f2ca2d38a590d27468252b9b4a54e31f
```

## Note on Repository Structure

The METADATA.pb `files` block references `fonts/ttf/PaletteMosaic-Regular.ttf`, but at the HEAD commit, the file `PaletteMosaic-Regular.ttf` also exists at the repository root (as a separate, older copy). The `fonts/ttf/` path contains the current version introduced by the rename commit.

## Changes Made

- Added `commit: "461da4c5f2ca2d38a590d27468252b9b4a54e31f"` to the `source` block in `METADATA.pb`

## Confidence

**High.** The HEAD commit is the current tip of the master branch and contains the `fonts/ttf/PaletteMosaic-Regular.ttf` file that matches the source mapping in METADATA.pb. The font version (1.001) is consistent with the single TTF in the repository.

## Repo / Commit / Config / Status

- **Repo**: https://github.com/shibuyafont/Palette-mosaic-font-mono
- **Commit**: `461da4c5f2ca2d38a590d27468252b9b4a54e31f` (HEAD of master)
- **Config**: files mapped from `fonts/ttf/` directory
- **Status**: Commit hash added to METADATA.pb
- **Confidence**: High

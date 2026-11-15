# Sarala — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The canonical upstream repository for Sarala was identified at `huertatipografica/sarala` on GitHub. The repository contained both a Glyphs source file and UFO sources. A source block was added to METADATA.pb.

## Upstream Repository

- **URL**: https://github.com/huertatipografica/sarala
- **Owner**: huertatipografica (HT Fonts)
- **Branch**: master
- **Commit**: `9f767d4dd8245bf006908d6b50693eecd56958e4`
- **Commit message**: "Minor fixes"

## Source Files Found

| File | Type |
|------|------|
| `Sarala.glyphs` | Glyphs source |
| `font/Sarala-Regular.ufo` | UFO source (Regular) |
| `font/Sarala-Bold.ufo` | UFO source (Bold) |

## Designer

Sarala was designed by Andres Torresi of HT Fonts. The repository is hosted under the `huertatipografica` GitHub organization.

## Investigation Notes

The repository was located by checking the `huertatipografica` GitHub user's repositories, matching the designer's affiliation with HT Fonts. The repository `huertatipografica/sarala` was confirmed to exist with both a Glyphs master file and UFO sources. Sarala covers Devanagari and Latin scripts and was added to Google Fonts in 2015.

## Result

A source block was added to METADATA.pb referencing the repository URL, the latest commit hash, and the primary Glyphs source file.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sarala/` referencing the upstream gftools-builder-compatible source at the pinned commit `7779e0c` (`Sarala.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`7779e0c9`](https://github.com/huertatipografica/sarala/commit/7779e0c9) ("Minor fixes", 2015-07-01) to [`9f767d4d`](https://github.com/huertatipografica/sarala/commit/9f767d4d) ("Delete TelexDevaHT-MM.glyphs", 2015-01-27, on `master`). google/fonts updated Sarala in [google/fonts `6e10d603`](https://github.com/google/fonts/commit/6e10d603) on 2015-06-15; the next upstream change, [`037a9667`](https://github.com/huertatipografica/sarala/commit/037a9667) ("Glyphs 2 export", 2015-06-18), moved these binaries to `font/glyphs1/`.

The shipped TTFs match `font/ttf/Sarala-*.ttf` at `9f767d4d` in outlines, cmap and GSUB/GPOS/GDEF content. google/fonts widened `space` to the width of `nbspace` (Regular 430 to 512, Bold 397 to 460), dropped FFTM, changed name, head, OS/2 fsType (4 to 0) and the vertical metrics, and made a TTX round-trip that re-encoded GSUB/GPOS and the hinting push instructions without changing their content. md5 shipped vs upstream: Regular `4c444e6af06e03de15b1bc2c1164ef77` vs `dd037d7c29f5ee3c156a728fa1f758c1`, Bold `c259f47b1ae48d9e076b5e702203a7d5` vs `6f4a009dd78eff806eacb5b70c60dbe1`.

The override `config.yaml` and the `files` entry name `Sarala.glyphs`, which exists at `9f767d4d`.

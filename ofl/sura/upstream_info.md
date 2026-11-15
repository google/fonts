**Model**: Claude Opus 4.6

# Sura — Upstream Source Investigation

## Summary

The canonical upstream repository for Sura was identified at `https://github.com/huertatipografica/sura`, maintained by HT Fonts (Carolina Giovagnoli's type foundry). The repository contained a Glyphs source file (`Sura.glyphs`).

## Repository Details

- **Repository**: https://github.com/huertatipografica/sura
- **Owner**: huertatipografica (HT Fonts / Carolina Giovagnoli)
- **License**: OFL
- **Source format**: Glyphs (.glyphs)
- **Latest commit**: `d20d15fe0de4a84a9d3a944f87e9c35d4c9da612`
- **Commit message**: "OT Fixes"
- **Default branch**: master
- **Description**: "Devanagari typeface based on Andada ht"

## Source Files

The repository root contained:
- `Sura.glyphs`
- `fonts/`
- `pdf/`

## Confidence

**High** — The repository was found in the `huertatipografica` GitHub organization. The METADATA.pb designer was listed as "Carolina Giovagnoli," and HT Fonts is her type foundry. The repository description confirmed the Devanagari nature of the font. The copyright notice in the font confirmed "Carolina Giovagnoli" as author. The Glyphs source file was present.

## Action Taken

A `source` block was added to `METADATA.pb` pointing to `https://github.com/huertatipografica/sura` at commit `d20d15fe0de4a84a9d3a944f87e9c35d4c9da612`.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/sura/` referencing the upstream gftools-builder-compatible source at the pinned commit `d20d15f` (`Sura.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`d20d15fe`](https://github.com/huertatipografica/sura/commit/d20d15fe) ("OT Fixes", 2015-07-04) to [`4e8dd108`](https://github.com/huertatipografica/sura/commit/4e8dd108) ("Name updated", 2015-01-27, on `master`). google/fonts added Sura in [google/fonts `64963c21`](https://github.com/google/fonts/commit/64963c21) on 2015-06-15; the next upstream source change came on 2015-06-18, and the July rework renamed the glyphs without updating the hand-written features.

The shipped TTFs match `fonts/ttf/Sura-*.ttf` at `4e8dd108` in outlines, advances and GSUB/GPOS/GDEF content. google/fonts added an `nbsp` glyph (U+00A0, the width of the space), swapped FFTM for DSIG, changed name, head, OS/2 fsType (4 to 0) and the vertical metrics, and made a TTX round-trip that re-encoded GSUB/GPOS and the hinting push instructions without changing their content. md5 shipped vs upstream: Regular `b64e5c15432dfae39e02fd3248272ad4` vs `8fc5749fd52a44ea296ac6097db1f1a1`, Bold `0276e1bd82ee8c72864811f8ccd045e1` vs `883e7961f14e83ac2b3e6a42b0c651a5`.

The override `config.yaml` (`Sura.glyphs`) resolves at `4e8dd108`.

**Model**: Claude Opus 4.6

## Vesper Libre

**Designer**: Mota Italic
**License**: OFL
**Category**: SERIF

### Upstream Repository

The canonical upstream repository for Vesper Libre was identified at **https://github.com/motaitalic/vesper-libre**, maintained by the Mota Italic type foundry (Robert Keller). The repository contained a Glyphs source file (`VesperLibre.glyphs`) at the root level, confirming it as the primary source of truth for the font.

### Source Files

The repository contained:
- `VesperLibre.glyphs` — Glyphs source file (primary source)
- `VesperLibre-Regular.ttf`, `VesperLibre-Medium.ttf`, `VesperLibre-Bold.ttf`, `VesperLibre-Black.ttf` — compiled TTF output files
- `Samples/` — sample images
- `README.md` and `LICENSE`

### Investigation Notes

The copyright string `"Copyright (c) 2007, Robert Keller (www.motaitalic.com)"` identified the designer as Robert Keller of Mota Italic. The repository was found under the [motaitalic](https://github.com/motaitalic) GitHub organization. The repository was last pushed to in June 2015.

**Repo**: https://github.com/motaitalic/vesper-libre
**Commit**: b765c5a68c1786a177b46e3b3ecd766157ffe349
**Status**: Glyphs source present
**Confidence**: High

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/vesperlibre/` referencing the upstream gftools-builder-compatible source at the pinned commit `b765c5a` (`VesperLibre.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`b765c5a6`](https://github.com/motaitalic/vesper-libre/commit/b765c5a6) ("Minor updates", v1.059, 2015-06-03) to [`30690a08`](https://github.com/motaitalic/vesper-libre/commit/30690a08) ("Minor Update", 2015-05-11, on `master`). google/fonts updated the family in [google/fonts `039bd1f4`](https://github.com/google/fonts/commit/039bd1f4) on 2015-06-01, two days before `b765c5a6`.

The four shipped TTFs match `VesperLibre-*.ttf` at `30690a08`: outlines, glyph instructions, hmtx, OS/2, hhea, GDEF and the hinting tables are identical, and GSUB, GPOS and cmap differ only in serialization. google/fonts edited only name and head. md5 shipped vs upstream: Regular `e6b2cfa2496dff78dcdb27a67a300908` vs `e54c273726f1c0a4165cba58bd294fc2`, Medium `e0d38f5ae59ac954f000e4069049b06c` vs `d08a94b35582436828281b4a47a809a2`, Bold `5a38fd07880a9ea3df4f648b2c86c329` vs `89670c7bf2201e9daaa357a43ba38def`, Heavy `1b24cbf1830a71a087082681aa68dccc` vs `329d3fad25d0e237279c395e890a98ba`.

The override `config.yaml` (`VesperLibre.glyphs`) resolves at `30690a08`.

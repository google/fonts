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

# Noto Sans Duployan — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/notofonts/duployan
- **Commit**: `9626869cc851873c96eafd019fab55d984bbebc0`
- **Status**: present

## What Was Done
The existing source metadata was reviewed. A complete `source` block was present, pointing to the notofonts/duployan GitHub repository with an associated archive release at NotoSansDuployan-v3.002.

## Notes
- Designer: Google (copyright also credits David Corbett)
- Script: Duployan (Dupl)
- Category: SANS_SERIF
- Covers Duployan shorthand used for French and Chinese.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
METADATA.pb pointed `config_yaml` at the upstream `sources/config-sans-duployan.yaml`. fontc_crater failed with `missing source 'NotoSansDuployan.glyphs'`.

### Investigation
The notofonts/duployan repository does not contain a Glyphs, UFO or designspace source. The font is generated programmatically: `sources/build.py` (with `duployan.py`, `anchors.py`, `shapes.py`, etc.) constructs every glyph in code, driven by the repository `Makefile` (`make build`). A `sources/NotoSansDuployan.glyphs` file existed only transiently (added 2022-06-20, removed 2023-01-04) and does not exist at the recorded commit `9626869`, the v3.002 tag, or anywhere on `main` after January 2023. The upstream `sources/config-sans-duployan.yaml` still lists `NotoSansDuployan.glyphs` in its `sources:` block, but that entry is stale and corresponds to no file in the tree.

### Actions taken
The non-functional `config_yaml: "sources/config-sans-duployan.yaml"` field was removed from the METADATA.pb `source` block. No override `config.yaml` was created, because no gftools-builder-compatible source exists. The repository URL, commit, `archive_url` and file mappings are correct and were left unchanged.

### Final state
Noto Sans Duployan is recorded as not reproducible by gftools-builder: it is a code-generated family built with a custom `Makefile`/`build.py` pipeline, with no `.glyphs`/`.ufo`/`.designspace` source.

# Mitr — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/cadsondemak/mitr
- **Organization**: Cadson Demak (cadsondemak)
- **Description**: "Mitr is a Thai + Latin informal sans font"
- **Default branch**: `master`
- **Latest commit**: `41950431d37f6410fd082760ca806eb490e4791f`
- **Commit message**: "source and font files updated. fix problem nikahit and tone marks."
- **Commit date**: 2015-11-30
- **Last push**: 2015-11-30 (repository has been inactive since then)

## Source Files

Located in `source/`:

- `Mitr-200.glyphs` — ExtraLight (Glyphs format)
- `Mitr-300.glyphs` — Light (Glyphs format)
- `Mitr-400.glyphs` — Regular (Glyphs format)
- `Mitr-500.glyphs` — Medium (Glyphs format)
- `Mitr-600.glyphs` — SemiBold (Glyphs format)
- `Mitr-700.glyphs` — Bold (Glyphs format)
- Corresponding `.ufo` and `.vfb` files for each weight

This is a **static multi-master** family (not variable fonts), with one Glyphs source per weight.

Pre-built fonts are in `fonts/` as both `.ttf` and `.otf` for all 6 weights.

## Build System

No `config.yaml`, `Makefile`, or build script is present in the repository. The sources are in Glyphs format (`.glyphs`) alongside `.ufo` and `.vfb` files. The build system is not documented. Given the 2015 vintage, the fonts were likely built with an older version of fontmake or directly with Glyphs app. No gftools pipeline configuration exists.

## config.yaml Status

No `config.yaml` exists in the repository.

## Notes

- Cadson Demak is a well-established Thai type foundry with an active GitHub organization (`cadsondemak`) hosting many font families. The `cadsondemak/mitr` repository is the clear authoritative upstream source.
- The repository has been inactive since 2015-11-30. The fonts in google/fonts match the static weights available in the repo (ExtraLight through Bold, no italics, no variable font).
- The family covers Thai + Latin (with Vietnamese and Latin-Ext subsets).
- The latest commit `41950431d37f6410fd082760ca806eb490e4791f` on branch `master` is the appropriate reference for the METADATA.pb `source` block.
- A `config.yaml` would need to be created to establish a reproducible gftools build pipeline, as none currently exists in the repo. Individual per-weight Glyphs sources would need to be mapped to their respective output font files.
- **Recommended action**: Add a `source` block to METADATA.pb pointing to `https://github.com/cadsondemak/mitr`, commit `41950431d37f6410fd082760ca806eb490e4791f`, branch `master`. A `config.yaml` should be authored to enable future rebuilds.

# Nunito — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/nunito
- **Branch**: `main`
- **Pinned commit**: `8c6a9bb9732545b9ed53f29ec5e1ab0ff53c4e6f`
- **Commit date**: 2025-02-26
- **Commit message**: "rename the gftools builder file to what fontc_crater & google-fonts-sources expect"
- **Latest upstream activity**: 2025-02-26 (same as pinned commit — this is the HEAD of main as of investigation date)

## Source Files

The `sources/` directory contains:

- `Nunito.glyphs` — primary Glyphs source file (single file encoding both Roman and Italic via `ital` axis)
- `config.yaml` — gftools builder configuration
- `build.sh` — build wrapper script
- `fix.py` — post-processing script (fixes italic bits)

The `config.yaml` specifies `Nunito.glyphs` as the sole source, with `outputDir: "../fonts"`, `buildStatic: false`, and axis order `[wght, ital]`.

The build process uses `gftools builder` to produce a combined `Nunito[ital,wght].ttf`, then uses `fonttools varLib.instancer` to slice it into separate Roman (`Nunito[wght].ttf`) and Italic (`Nunito-Italic[wght].ttf`) variable fonts. A separate `gftools gen-stat` call fixes name ID 25 on the italic, and `fix.py` corrects italic bits.

## Build System

- **Tool**: `gftools builder` (driven by `sources/config.yaml`)
- **Post-processing**: `fonttools varLib.instancer`, `gftools gen-stat`, custom Python (`fix.py`)
- **Static fonts**: Not built (`buildStatic: false`)
- **Output**: Two variable fonts — `Nunito[wght].ttf` (Roman) and `Nunito-Italic[wght].ttf` (Italic)

## config.yaml Status

`config.yaml` is present at `sources/config.yaml` and is already referenced in `METADATA.pb` (`config_yaml: "sources/config.yaml"`). The METADATA.pb source block is fully configured and up to date.

## Notes

- The repo was transferred from the original author (Vernon Adams / Cyreal) to the `googlefonts` organization. Jacques Le Bailly was involved in later development.
- The pinned commit is the current HEAD of `main`, so the METADATA.pb source block is tracking the latest available state.
- The axis range is `wght: 200–1000`, which is unusually wide (extends to Black at 1000) — this is intentional for the Nunito design.
- No cached upstream repo found at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/nunito`.

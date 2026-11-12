# Micro 5 — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/scfried/soft-type-micro
- **Pinned commit**: `a5a61b057a6804ea75840f2b9f31cfb339652e58`
- **Commit date**: 2025-01-10
- **Commit message**: "Merge pull request #4 from emmamarichal/main — Small fixes"
- **Branch**: `main`
- **Latest commit at investigation time**: same as pinned (`a5a61b057a6804ea75840f2b9f31cfb339652e58` is HEAD)

## Source Files

At the pinned commit, the repository contains:

- `sources/Micro5.glyphs` — primary Glyphs source for Micro 5
- `sources/Micro5Charted.glyphs` — Glyphs source for Micro 5 Charted (separate family, same repo)
- `sources/config.yaml` — gftools builder config for Micro 5
- `sources/config-charted.yaml` — gftools builder config for Micro 5 Charted
- `sources/CustomFilter_GF_Latin_All.plist` — glyph filter list
- `fonts/ttf/Micro5-Regular.ttf` — pre-built TTF binary
- `fonts/ttf/Micro5Charted-Regular.ttf` — pre-built TTF binary
- `fonts/webfonts/Micro5-Regular.woff2` — pre-built WOFF2
- `fonts/webfonts/Micro5Charted-Regular.woff2` — pre-built WOFF2
- `OFL.txt` — SIL Open Font License 1.1
- `AUTHORS.txt` — Sarah Cadigan-Fried `<sarahcadiganfried@gmail.com>`
- `CONTRIBUTORS.txt` — Sarah Cadigan-Fried `<sarahcadiganfried@gmail.com>`
- `requirements.txt` — lists `gftools` as the sole build dependency
- `sources/build.sh` — build script invoking gftools builder for both configs
- `Makefile` — orchestrates build, test (fontbakery), and proof targets
- `.github/workflows/build.yaml` — GitHub Actions CI pipeline

## Build System

- **Build tool**: `gftools builder` (via `sources/build.sh` and Makefile)
- **Build invocation** (`sources/build.sh`):
  ```sh
  gftools builder config.yaml
  gftools builder config-charted.yaml
  ```
- **`sources/config.yaml`** contents:
  ```yaml
  sources:
    - Micro5.glyphs
  familyName: Micro 5
  buildOTF: false
  extraFontmakeArgs: --filter "ufo2ft.filters.decomposeComponents::DecomposeComponentsFilter"
  ```
- **GitHub Actions** (`.github/workflows/build.yaml`): triggered on push and release; uses Python 3.10, installs gftools via pip, runs `make build`, runs fontbakery QA (`make test`, continue-on-error), deploys proof to GitHub Pages.

## config.yaml Status

- **Present in upstream repo**: Yes, at `sources/config.yaml`.
- **METADATA.pb `config_yaml` field**: `config_yaml: "sources/config.yaml"` — correctly set.
- The config targets only `Micro5.glyphs` (not the charted variant), which is appropriate since this is the Micro 5 family entry.

## Notes

- **Designer**: Sarah Cadigan-Fried. The Soft Type Collection is a knitter-focused pixel/charted typeface suite; Micro 5 is the smallest variant in the collection (capital height = 5 pixels/stitches).
- Both Micro 5 and Micro 5 Charted are built from the same repository; their sources and configs are clearly separated.
- Copyright year is 2023; the project was added to Google Fonts in January 2024.
- The `familyName` in `config.yaml` is "Micro 5", matching the METADATA.pb name.
- **Confidence**: High — repository is public, all source files are present, build system is standard gftools builder, authorship and licensing are clear.

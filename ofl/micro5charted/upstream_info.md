# Micro 5 Charted — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/scfried/soft-type-micro
- **Pinned commit**: `a5a61b057a6804ea75840f2b9f31cfb339652e58`
- **Commit date**: 2025-01-10
- **Commit message**: "Merge pull request #4 from emmamarichal/main — Small fixes"
- **Branch**: `main`
- **Latest commit at investigation time**: same as pinned (`a5a61b057a6804ea75840f2b9f31cfb339652e58` is HEAD)
- **Shared repo**: This family shares its upstream repository with Micro 5 (`ofl/micro5`).

## Source Files

At the pinned commit, the repository contains both families. Files relevant to Micro 5 Charted:

- `sources/Micro5Charted.glyphs` — primary Glyphs source for Micro 5 Charted
- `sources/config-charted.yaml` — gftools builder config for this family
- `sources/CustomFilter_GF_Latin_All.plist` — glyph filter list (shared with Micro 5)
- `fonts/ttf/Micro5Charted-Regular.ttf` — pre-built TTF binary
- `fonts/webfonts/Micro5Charted-Regular.woff2` — pre-built WOFF2
- `OFL.txt` — SIL Open Font License 1.1
- `AUTHORS.txt` — Sarah Cadigan-Fried `<sarahcadiganfried@gmail.com>`
- `sources/build.sh` — builds both families in sequence
- `Makefile` — orchestrates build, test, and proof targets

## Build System

- **Build tool**: `gftools builder` (via `sources/build.sh` and Makefile)
- **Build invocation for this family** (within `sources/build.sh`):
  ```sh
  gftools builder config-charted.yaml
  ```
- **`sources/config-charted.yaml`** contents:
  ```yaml
  sources:
    - Micro5Charted.glyphs
  familyName: Micro Charted
  buildOTF: false
  extraFontmakeArgs: --filter "ufo2ft.filters.decomposeComponents::DecomposeComponentsFilter"
  ```
- **GitHub Actions** (`.github/workflows/build.yaml`): same shared CI pipeline as Micro 5; builds all configs via `make build`.

## config.yaml Status

- **Present in upstream repo**: Yes, at `sources/config-charted.yaml`.
- **METADATA.pb `config_yaml` field**: `config_yaml: "sources/config.yaml"` — this points to `config.yaml` (the Micro 5 config), **not** to `config-charted.yaml`. This appears to be an inaccuracy: the Micro 5 Charted family should reference `sources/config-charted.yaml`.
- **Note on `familyName` in config-charted.yaml**: The value is `"Micro Charted"` rather than `"Micro 5 Charted"` (which matches the METADATA.pb name). This discrepancy exists upstream and may cause gftools builder to produce output with a mismatched family name; worth flagging to the upstream maintainer.

## Notes

- **Designer**: Sarah Cadigan-Fried. Micro 5 Charted is the "charted" (grid-overlay) variant of Micro 5, intended to help knitters visualize letterforms on knitting charts.
- Both Micro 5 and Micro 5 Charted are maintained together in the same repository and share a single git history; they are separated only by their respective `.glyphs` source files and config YAMLs.
- The `config_yaml` field in METADATA.pb currently points to `sources/config.yaml` (the Micro 5 config). It should be corrected to `sources/config-charted.yaml` for this family entry.
- Copyright year is 2023; the project was added to Google Fonts in January 2024.
- **Confidence**: High — repository is public, all source files are present, build system is standard gftools builder. One discrepancy noted: wrong `config_yaml` path in METADATA.pb and `familyName` mismatch in `config-charted.yaml`.

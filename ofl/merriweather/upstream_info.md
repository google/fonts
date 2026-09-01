# Merriweather — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/EbenSorkin/Merriweather4
- **Commit**: `e586023aa0fe1dba9a7d4ec80fa8b9e546cb7ecf`
- **Commit date**: 2024-12-18
- **Commit message**: Merge pull request #15 from m4rc1e/mf-master2 — "remastered for Google Fonts"
- **Author**: Eben Sorkin (sorkineben@gmail.com)
- **Latest release**: 4.008 (published 2024-12-20), archive `Merriweather4-4.008.zip`

## Source Files

The `sources/` directory at the specified commit contains Glyphs sources (not UFOs):

- `Merriweather.glyphspackage` — Roman variable source
- `Merriweather-Italic.glyphspackage` — Italic variable source
- `sources/config.yaml` — gftools builder configuration

The variable fonts directory (`fonts/variable/`) contains four files at this commit:

- `Merriweather[opsz,wdth,wght].ttf`
- `Merriweather-Italic[opsz,wdth,wght].ttf`
- `MerriweatherSC[opsz,wdth,wght].ttf`
- `MerriweatherSC-Italic[opsz,wdth,wght].ttf`

Note: Only the Roman and Italic (non-SC) variable fonts are referenced in METADATA.pb.

## Build System

- **Build tool**: `gftools builder` (invoked via `Makefile` target `build.stamp`)
- **Config**: `sources/config.yaml` (referenced directly in METADATA.pb as `config_yaml: "sources/config.yaml"`)
- **Sources in config.yaml**:
  ```yaml
  sources:
    - Merriweather.glyphspackage
    - Merriweather-Italic.glyphspackage
  axisOrder:
    - wght
    - wdth
    - opsz
  familyName: Merriweather21
  buildStatic: false
  buildWebfont: false
  ```
- **Release archive**: `https://github.com/EbenSorkin/Merriweather4/releases/download/4.008/Merriweather4-4.008.zip` (referenced in METADATA.pb `archive_url`)

## config.yaml Status

No `config.yaml` currently exists in the google/fonts `ofl/merriweather/` directory. However, METADATA.pb already references `sources/config.yaml` in the upstream repository, and the METADATA.pb `source` block already points to the pre-built variable fonts via explicit `files` entries. A local `config.yaml` for the google/fonts directory would only be needed if gftools is expected to build the fonts from source rather than using the pre-built binaries. The current METADATA.pb structure uses `archive_url` and explicit file mappings, suggesting it relies on the upstream release artifacts.

## Notes

- This is a major revision (version 4.x) of Merriweather, remastered as a variable font with three axes: `opsz` (18–144), `wdth` (87–112), and `wght` (300–900).
- The `familyName` in `sources/config.yaml` reads `Merriweather21` — this appears to be a working/internal name used during the remaster project and does not affect the distributed font metadata.
- The Merriweather SC (Small Caps) variant exists in the upstream repo but is not currently included in google/fonts; it could be added as a separate family in the future.
- Confidence: **High** — METADATA.pb commit and repository URL are directly confirmed via GitHub API. The archive URL `4.008.zip` corresponds to the release published two days after the referenced commit (2024-12-18 commit, 2024-12-20 release).

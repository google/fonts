# Notable — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/notable
- **Owner**: googlefonts (Google Fonts organization)
- **Default branch**: main
- **Pinned commit**: `e3426360fa15b1824f4694663271956e50514498`
- **Pinned commit date**: 2025-02-26
- **Pinned commit message**: "Add sources/config.yaml"
- **Latest commit on main**: same as pinned (`e3426360`) — repo is up to date
- **Archived**: No
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Source Files

- `sources/Notable.glyphs` — primary Glyphs source file
- `sources/config.yaml` — build configuration (referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`)
- `fonts/Notable-Regular.ttf` — pre-built static TTF
- `AUTHORS.txt`, `CONTRIBUTORS.txt`, `OFL.txt` — metadata files

## Build System

- **Build config**: `sources/config.yaml`
- **config.yaml content**:
  ```yaml
  sources:
    - Notable.glyphs
  ```
- **Tool**: gftools / fontmake (Glyphs-based build pipeline)
- **Build output**: Static TTF only (single Regular weight)
- The config.yaml is minimal — no explicit build flags, uses gftools defaults

## config.yaml Status

- `config.yaml` is present in the upstream repo at `sources/config.yaml`
- METADATA.pb correctly references `config_yaml: "sources/config.yaml"`
- The config.yaml was added in the pinned commit (2025-02-26), suggesting it was recently migrated to the gftools pipeline (same date as Norican — likely a batch update)
- No separate `config.yaml` is present in the google/fonts working copy (`/mnt/shared/google/fonts/ofl/notable/`)

## Notes

- Notable is a display sans-serif typeface by Eli Block, Hana Tanimura, and Noemie Le Coz. It covers Latin subsets only.
- The METADATA.pb correctly classifies it as `stroke: "SANS_SERIF"` and `classifications: "DISPLAY"`.
- The pinned commit is HEAD on main; the config.yaml was added 2025-02-26 (same batch as Norican).
- The repository is under the `googlefonts` organization, indicating maintenance by Google Fonts directly.
- No variable font is present or expected — single Regular weight only.
- The repo description is "Notable fonts".
- The repo uses `main` as the default branch (unlike most older Google Fonts repos which use `master`).
- Confidence in source identification: **High** — single `.glyphs` source, minimal config.yaml.

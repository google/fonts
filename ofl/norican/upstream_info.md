# Norican — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/NoricanFont
- **Owner**: googlefonts (Google Fonts organization)
- **Default branch**: master
- **Pinned commit**: `5e30b33570463b57d70795d7ccac56b4d69688e5`
- **Pinned commit date**: 2025-02-26
- **Pinned commit message**: "Add sources/config.yaml"
- **Latest commit on master**: same as pinned (`5e30b335`) — repo is up to date
- **Archived**: No
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Source Files

- `sources/Norican.glyphs` — primary Glyphs source file
- `sources/config.yaml` — build configuration (referenced in METADATA.pb as `config_yaml: "sources/config.yaml"`)
- `fonts/ttf/Norican-Regular.ttf` — pre-built static TTF
- `fonts/otf/Norican-Regular.otf` — pre-built static OTF
- `fonts/webfonts/Norican-Regular.woff2` — pre-built webfont
- `documentation/image1.png`, `documentation/image2.png` — specimen images

## Build System

- **Build config**: `sources/config.yaml`
- **config.yaml content**:
  ```yaml
  sources:
    - Norican.glyphs
  ```
- **Tool**: gftools / fontmake (Glyphs-based build pipeline)
- **Build output**: Static TTF/OTF/woff2 only (single Regular weight)
- The config.yaml is minimal — no explicit build flags, uses gftools defaults

## config.yaml Status

- `config.yaml` is present in the upstream repo at `sources/config.yaml`
- METADATA.pb correctly references `config_yaml: "sources/config.yaml"`
- The config.yaml was added in the pinned commit (2025-02-26), suggesting it was recently migrated to the gftools pipeline
- METADATA.pb `files` block maps `fonts/ttf/Norican-Regular.ttf` → `Norican-Regular.ttf` directly

## Notes

- Norican is a handwriting/script typeface by Vernon Adams, a single-weight Latin family.
- The pinned commit is HEAD on master; the config.yaml was added very recently (2025-02-26), likely as part of a Google Fonts metadata enrichment effort.
- The repository is under the `googlefonts` organization, indicating it has been adopted/maintained by Google Fonts directly.
- The family covers Latin and Latin-ext subsets only.
- No variable font is present or expected for a single-weight design.
- The repo description is "Norican webfont", reflecting its original purpose as a web font package.
- Confidence in source identification: **High** — single `.glyphs` source, minimal config.yaml.

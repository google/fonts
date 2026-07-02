# Nokora — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/danhhong/Nokora
- **Owner**: Danh Hong
- **Default branch**: master
- **Pinned commit**: `9c5f991b700b9be3519315a854a7b986e6877ace`
- **Pinned commit date**: 2025-05-02
- **Pinned commit message**: "Fixed outline interpolation issues in /quotedbl and /asterisk"
- **Latest commit on master**: same as pinned (`9c5f991b`) — repo is up to date
- **Archived**: No
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Source Files

- `Source/Nokora.glyphs` — primary Glyphs source file
- `Source/builder.yaml` — build configuration (referenced in METADATA.pb as `config_yaml: "Source/builder.yaml"`)
- `Release/variable/Nokora[wght].ttf` — variable font output (wght axis, 100–900)
- `Release/ttf/Nokora-{Thin,ExtraLight,Light,Regular,Medium,SemiBold,Bold,ExtraBold,Black}.ttf` — 9 static TTF instances

## Build System

- **Build config**: `Source/builder.yaml` (non-standard name, referenced explicitly in METADATA.pb)
- **builder.yaml content**:
  ```yaml
  sources:
    - Nokora.glyphs
  outputDir: "../Release"
  buildStatic: true
  buildVariable: true
  buildTTF: true
  buildOTF: false
  buildWebfont: false
  ```
- **Tool**: gftools / fontmake (Glyphs-based build pipeline)
- **Build output**: Both variable font (`Nokora[wght].ttf`) and 9 static TTF instances

## config.yaml Status

- The upstream build config is named `builder.yaml` (not `config.yaml`), located at `Source/builder.yaml`
- METADATA.pb correctly references `config_yaml: "Source/builder.yaml"`
- No separate `config.yaml` is present in the google/fonts working copy (`/mnt/shared/google/fonts/ofl/nokora/`)
- The METADATA.pb `files` block explicitly maps `Release/variable/Nokora[wght].ttf` → `Nokora[wght].ttf`, indicating the variable font is the sole deliverable to Google Fonts

## Notes

- The family is a variable font with a single axis (`wght`, 100–900), covering the Khmer script plus Latin.
- Only a single font entry exists in METADATA.pb (`Nokora[wght].ttf`), representing the variable font only — the static instances in `Release/ttf/` are not published to Google Fonts.
- The pinned commit is HEAD on master; the metadata is current as of May 2025.
- The repo has no `config.yaml` under the conventional `sources/` path; the non-standard `Source/builder.yaml` is correctly captured in METADATA.pb.
- Confidence in source identification: **High** — single `.glyphs` source, builder.yaml explicitly referenced.

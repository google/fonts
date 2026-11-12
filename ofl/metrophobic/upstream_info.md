# Metrophobic — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/MetrophobicFont
- **Branch**: main
- **Pinned commit**: `d4da54632ddd53631332a5a469183c887b4ea3e1`
- **Commit date**: 2025-02-25
- **Commit message**: "Add sources/config.yaml"
- **Author of pinned commit**: Felipe Corrêa da Silva Sanches
- **HEAD status**: Pinned commit is the current HEAD of main. Repository is up to date with the pinned commit.
- **Upstream cache**: Not available (MetrophobicFont not present in `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/`).

## Source Files

| File | Path in repo | Size |
|------|-------------|------|
| Glyphs source | `sources/Metrophobic.glyphs` | ~321 KB |
| Build config | `sources/config.yaml` | — |
| Binary TTF | `fonts/ttf/Metrophobic-Regular.ttf` | — |
| Binary OTF | `fonts/otf/Metrophobic-Regular.otf` | — |
| Webfont | `fonts/webfonts/Metrophobic-Regular.woff2` | — |
| License | `OFL.txt` | — |
| Docs images | `documentation/image1.png`, `documentation/image2.png` | — |

The `sources/archive/` directory contains historical Glyphs sources from different periods of development, including versions from 2018 and early drafts (`Metrophobic_AM.glyphs`, `Metrophobic_AM_09_01.glyphs`, etc.).

## Build System

The `sources/config.yaml` (added at the pinned commit) is a minimal gftools-builder config:

```yaml
sources:
  - Metrophobic.glyphs
```

No additional overrides are specified; all build parameters use gftools-builder defaults. The source is a single-master Glyphs file. The repository also contains pre-built binaries under `fonts/` (TTF, OTF, WOFF2), which were exported at commit `344e2c65f1` (2023-01-25, "Font exported") following outline corrections.

## config.yaml Status

A `config_yaml` entry is already present in METADATA.pb pointing to `sources/config.yaml`. This path is correct and consistent with the repo layout at the pinned commit. The config.yaml itself was added specifically at the pinned commit (2025-02-25), establishing this as the canonical build entry point.

## Notes

- **Designer**: Vernon Adams — prolific Google Fonts contributor who designed many early GF families. Metrophobic was one of his early releases (date_added 2011-05-11).
- **Description**: "Metrophobic is a sans serif face with a semi geometric feel. It is designed to be legible at small text sizes but also have enough character to be used as an interesting display face for headers and headlines." (from README.md)
- **Category**: `SANS_SERIF` — correct for this geometric sans design.
- **Subsets**: `latin`, `latin-ext`, `vietnamese`, `menu` — appropriate for a Latin-script family with extended coverage.
- **Upstream activity**: The repository saw active maintenance in 2023 (outline corrections, font info updates, merged via googlefonts PR #27 by m4rc1e). The pinned commit (2025-02-25) added the config.yaml, making the build system explicit. The repo has been updated as recently as 2025-08-29 (per GitHub metadata), though the main branch HEAD remains at the pinned commit.
- **Copyright**: "Copyright 2011 The Metrophobic Project Authors (https://github.com/googlefonts/MetrophobicFont), with Reserved Font Name 'Metrophobic'." — consistent across OFL.txt and font binaries.
- **Archive sources**: The `sources/archive/` directory preserves historical versions of the Glyphs source. These are not used in the active build.
- **Confidence**: High. The repo structure, source file, config.yaml path, and binary paths all align precisely with what is declared in METADATA.pb.

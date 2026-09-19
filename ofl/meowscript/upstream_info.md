# Meow Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/googlefonts/meow-script
- **Default branch**: `master`
- **Pinned commit**: `6882d389cb287bd7b7716c125e9728b81ed0ab41`
- **Commit date**: 2021-10-26
- **Commit message**: "Readme Updated"
- **Commit author**: Viviana Monsalve
- **Repo created**: 2021-02-24
- **Last updated**: 2025-05-05

## Source Files

- **Primary source**: `sources/MeowScript.glyphs` (Glyphs format, ~3.4 MB)
- **Output fonts**:
  - `fonts/ttf/MeowScript-Regular.ttf` — static TTF (no variable font; `buildVariable: false` in config)
  - `fonts/otf/MeowScript-Regular.otf` — static OTF
  - `fonts/webfonts/` — web font formats
- **Documentation**: `DESCRIPTION.en_us.html` (at repo root)
- **License**: `OFL.txt`

## Build System

- **Build tool**: `gftools builder` (invoked directly: `cd sources && gftools builder config.yml`)
- **Build file**: no `Makefile`; build is run manually per the README instructions
- **CI**: GitHub Actions workflow `.github/workflows/CI-static-ttf.yml` — triggers on pushes/PRs to `master` that touch `sources/**`; uses Python 3.8
- **Python environment**: managed via `requirements.txt`
- **No autohinting** configured (commented out in config.yml: `#autohintTTF: false`)

## config.yaml Status

- **Present**: yes — `sources/config.yml` (note: `.yml` extension, not `.yaml`)
- **Correctly referenced in METADATA.pb**: yes — `config_yaml: "sources/config.yml"`
- **Key settings**:
  - `sources: [MeowScript.glyphs]`
  - `familyName: "Meow Script"`
  - `buildVariable: false`
  - Autohinting commented out
- **STAT table**: not defined in config.yml (static-only font, no STAT needed)

## Notes

- Meow Script is a static-only (non-variable) monoline handwriting font with multiple stylistic sets for alternate glyph forms.
- Designer: Robert Leuschke. The font was described as working "eclectically and harmoniously to add a fun, whimsy look to posters, ads, invitations."
- Supports `latin`, `latin-ext`, and `vietnamese` subsets.
- The pinned commit (`6882d389`) is the current HEAD of `master` as of the investigation date — the repo has not had commits since 2021-10-26.
- The `files` block in METADATA.pb maps `DESCRIPTION.en_us.html` from the repo root (not a `documentation/` subdirectory), which is consistent with the actual repo layout.
- No upstream cache found at `/mnt/shared/upstream_repos/fontc_crater_cache/googlefonts/meow-script`.
- The repo is under `googlefonts/` organization, suggesting direct Google Fonts stewardship.
- Confidence in metadata accuracy: **high** — config.yml is present and correctly referenced; the pinned commit is HEAD; built TTF path matches METADATA.pb expectation.

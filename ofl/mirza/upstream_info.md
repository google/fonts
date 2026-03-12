# Mirza — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/Tarobish/Mirza
- **Owner**: Tarobish (KB Studio / Borna Izadpanah)
- **Latest commit**: `fa7b59c92953e7f437d079a8c118a7952c507f09`
- **Commit date**: 2016-03-02
- **Commit message**: `+ 'Generated/Arabic/Mirza-Bold.otf'` (adds generated build artifacts)
- **Default branch**: `master` (gh-pages branch also exists)
- **Last repository activity**: 2026-02-24 (likely automated/metadata update)

The repository identity is confirmed by the copyright in METADATA.pb which lists `tarobish@gmail.com` (KB Studio) alongside co-authors Lasse Fister (`graphicore.de`) and Eduardo Tunni.

## Source Files

The `Sources/` directory contains:

- `Sources/Mirza 2 Masters.glyphs` — Glyphs app source (primary Arabic masters)
- `Sources/Mirza-LATIN-SOURCE.glyphs` — Glyphs app source for Latin subset
- `Sources/technical-additions.sfd` — FontForge SFD file (supplemental glyphs)
- `Sources/features.fea` — OpenType feature code
- `Sources/specific.fea` — script-specific OT features
- `Sources/pos-specific.fea` — positioning-specific OT features
- `Sources/data.json`, `Sources/data-Regular.json`, `Sources/data-Medium.json`, `Sources/data-SemiBold.json`, `Sources/data-Bold.json` — per-weight metadata/data files

Pre-compiled binaries are stored under `Sources/Build/Arabic/` and `Sources/Build/Latin/` for use by the build scripts.

Final built fonts land in `Fonts/`:
- `Fonts/Mirza-Regular.ttf`, `Fonts/Mirza-Medium.ttf`, `Fonts/Mirza-SemiBold.ttf`, `Fonts/Mirza-Bold.ttf`

## Build System

The repo has a custom shell-script-based build pipeline:

- `Makefile` — top-level build orchestration, calls `Tools/build.sh`
- `Tools/build.sh` — iterates over all four weights, invoking `Tools/buildFont.sh` per weight
- `Tools/buildFont.sh` — detailed per-weight build logic: merges Arabic and Latin OTF/TTF sources using custom Python tools, generates GDEF/GPOS/GSUB feature files, runs `makeotf`, and applies finalization scripts
- `Tools/` — contains multiple custom Python scripts (`mergeFonts.py`, `getArabSubset.py`, `mergeGlyphs.py`, `finalize.py`, `kernFeatureWriter.py`, etc.) and a `ftSnippets/` sub-library

This is a **highly custom** build system that predates gftools. It relies on `makeotf` (AFDKO) and several bespoke Python tools maintained within the repository. The pipeline is not compatible with the standard `gftools builder` / `config.yaml` approach.

## config.yaml Status

No `config.yaml` exists in the upstream repo or in the `ofl/mirza/` directory in google/fonts. Creating one would require significant re-engineering of the build pipeline, as the current system is not based on gftools.

## Notes

- The repository has been effectively dormant on the `master` branch since March 2016 (the last substantive commit).
- The primary source format is Glyphs app (`.glyphs`), which is well-supported by modern tooling (fontmake, gftools builder). This makes a future migration to a gftools-based pipeline feasible, albeit non-trivial given the Arabic complexity and custom feature engineering.
- The font covers Arabic and Latin scripts, with four weights (Regular, Medium, SemiBold, Bold).
- Co-authors include Lasse Fister (graphicore) and Eduardo Tunni, both active in the broader font community.
- The `gh-pages` branch likely hosts the project website.
- Confidence in repo identification: **High** — repo name, owner email (`tarobish@gmail.com`), and multi-weight Arabic font structure all match the METADATA.pb exactly.

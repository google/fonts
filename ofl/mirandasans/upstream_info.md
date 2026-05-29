# Miranda Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/maxthunberg/miranda-sans
- **Designer**: Max Thunberg
- **Default branch**: `main`
- **Latest commit**: `7cafa37b9bf6e53892a5738d8470668d1fcf52f6`
- **Commit message**: "Merge pull request #1 from emmamarichal/main — Add Miranda on GF!"
- **Commit date**: 2026-02-06

## Source Files

Located in `sources/`:

- `MirandaSans.glyphs` — Roman variable source (Glyphs format)
- `MirandaSans-Italic.glyphs` — Italic variable source (Glyphs format)

Built fonts are in `fonts/variable/`:

- `MirandaSans[wght].ttf`
- `MirandaSans-Italic[wght].ttf`

## Build System

The repository contains a `sources/config.yaml` that drives the build via `gftools builder` (standard Google Fonts pipeline). Sources are in Glyphs format, built using fontmake. The config defines:

- Two sources (Roman and Italic)
- Weight axis (`wght`) with values 400–700
- STAT table entries for both variable fonts

## config.yaml Status

A `config.yaml` exists at `sources/config.yaml`. It specifies both Glyphs sources, axis order (`wght`), and full STAT table configuration for Roman and Italic instances.

## Notes

- This family was added to google/fonts on 2026-02-11 (very recent). The working copy (`/mnt/shared/google/fonts`) does not yet have this directory synced from the main google/fonts repo.
- The upstream METADATA.pb in google/fonts already contains a complete `source` block pointing to commit `7cafa37b9bf6e53892a5738d8470668d1fcf52f6` on branch `main`. **No source block enrichment is needed** — this family is already fully annotated.
- The upstream repo itself also contains a `METADATA.pb`, consistent with the Google Fonts PR that added the family.
- Variable font with `wght` axis (400–700), both Roman and Italic.


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "sources/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `7cafa37b` (via the bare mirror in `upstream_repos/repo_archive/maxthunberg/miranda-sans.git`) confirms that `sources/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.

## Recent upstream/main activity (post-investigation)

- **2026-02-11** — Emma Marichal, commit [`6c3102a96`](https://github.com/google/fonts/commit/6c3102a96) ("Miranda Sans: Version 1.000 added"): initial onboarding of Miranda Sans to google/fonts via gftools-packager. The commit created `ofl/mirandasans/` with the variable binaries `MirandaSans[wght].ttf` and `MirandaSans-Italic[wght].ttf`, METADATA.pb (with the source block recording `maxthunberg/miranda-sans@7cafa37b9`), OFL.txt, and the article. This is the same commit referenced in the original investigation's "added to google/fonts on 2026-02-11" line.

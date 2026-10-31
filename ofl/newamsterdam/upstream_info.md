# New Amsterdam — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/vladimirnikolic1/NewAmsterdam
- **Branch**: main
- **Pinned commit**: `7a82ccc566f424481f09cb1ee0b1f43e42cf59fa`
- **Designer**: Vladimir Nikolic
- **License**: OFL

The repository URL resolves correctly (HTTP 200). No local cache exists at `/mnt/shared/upstream_repos/fontc_crater_cache/vladimirnikolic1/`.

## Source Files

The METADATA.pb maps:
- `OFL.txt` → `OFL.txt`
- `fonts/ttf/NewAmsterdam-Regular.ttf` → `NewAmsterdam-Regular.ttf`

This is a single-weight, single-style static font (Regular only). No variable font axes are defined.

## Build System

METADATA.pb references `sources/config.yaml` as the `config_yaml` path. This indicates a gftools-based build pipeline is expected at the upstream repo. However, the font distributed in google/fonts is a pre-built TTF taken directly from `fonts/ttf/` — not built from source by the pipeline. No `Makefile` or `fontmake` invocation is evident from what is present in the google/fonts directory.

The font was added at Version 1.000 with ttfautohint v1.8.4.7-5d5b applied (per git history comment `82acdc443`), and most recently updated via a batch port from `fontc_crater` targets list (`4ad8ac680`).

## config.yaml Status

A `config.yaml` is **not** present in the `ofl/newamsterdam/` directory in google/fonts. The METADATA.pb references `sources/config.yaml` in the upstream repo, but this file has not been pulled into the google/fonts working copy. The family directory contains only: `METADATA.pb`, `NewAmsterdam-Regular.ttf`, `OFL.txt`, and an `article/` subdirectory.

No config.yaml is present locally; it exists (or is expected to exist) only in the upstream repository under `sources/config.yaml`.

## Notes

- The copyright notice uses HTTPS: `https://github.com/vladimirnikolic1/NewAmsterdam` — correct and consistent with `repository_url`.
- Family is SANS_SERIF, single weight (400), Latin/Latin-ext subsets only.
- No upstream repo cache is available locally; investigation is based solely on METADATA.pb and google/fonts directory contents.
- The article (`ofl/newamsterdam/article/ARTICLE.en_us.html`) describes the font as "a tall Sans Serif font inspired by posters and Pop Art" combining "straight geometric lines with modern look."
- No variable font version exists; enhancement to variable is not indicated by the current source block.

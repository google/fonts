# Niramit — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/cadsondemak/Niramit
- **Owner**: Cadson Demak
- **Default branch**: master
- **Pinned commit**: `1b5fd503662d7fb259b0d09ba714d7dace5cefff`
- **Pinned commit date**: 2018-09-28
- **Pinned commit message**: "Merge pull request #8 from m4rc1e/fix — v1.001: fixed bits"
- **Latest commit on master**: same as pinned (`1b5fd503`) — repo has not been updated since
- **Archived**: No
- **Upstream cache**: Not present in `/mnt/shared/upstream_repos/fontc_crater_cache/`

## Source Files

- `source/Niramit.glyphs` — primary Glyphs source file
- `fonts/*.ttf` — pre-built static TTF files (6 weights × 2 styles = 12 fonts)
- `old/Niramit AS*.vfb` — legacy FontLab VFB files (4 files, older design iteration)
- No variable font sources or output present in the repo

## Build System

- **config.yaml**: Present at repo root (referenced in METADATA.pb as implied by `buildVariable: false`)
- **config.yaml content**: `buildVariable: false`, source: `source/Niramit.glyphs`
- **Tool**: gftools / fontmake (Glyphs-based build pipeline)
- **Build output**: Static TTFs only (12 instances across 6 weights × normal + italic)
- No Makefile or shell build script detected

## config.yaml Status

- `config.yaml` is present in the google/fonts working copy at `/mnt/shared/google/fonts/ofl/niramit/config.yaml`
- Content: `buildVariable: false` with source `source/Niramit.glyphs`
- METADATA.pb `source` block does not reference a `config_yaml` field — the config.yaml is local to the google/fonts repo, not tracked in the upstream source block
- The pinned commit is HEAD on master; the repo has been dormant since 2018

## Notes

- The repo has not received any updates since the initial release in September 2018. The pinned commit is the most recent commit on master.
- The source is a single `.glyphs` file supporting 6 weights with italic variants (Thai + Latin + Latin-ext + Vietnamese subsets).
- The upstream repo contains pre-built TTFs in `fonts/` (with .eot, .woff, .woff2 variants for web use) alongside the Glyphs source.
- Old VFB files in `old/` suggest the design predates the Glyphs workflow and was migrated.
- No variable font is produced (`buildVariable: false`), despite the family having 6 weight steps — a variable font upgrade could be a future improvement.
- The repo homepage points to `https://cadsondemak.github.io/Niramit` (a specimen/demo page).
- Confidence in source identification: **High** — single `.glyphs` source, straightforward static build.

# Questrial — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/questrial
- **Commit**: `8db71bfbabedd8c8dda35818ea5d5508758c2e19`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed and verified. The repository was confirmed to exist under the `googlefonts` GitHub organization. The repository description is "A fork of John Prince font Questrial from the old Google font directory". The pinned commit was confirmed to exist in the repository's `main` branch. The source block references a `config.yaml` build configuration, indicating a gftools-driven build workflow.

## Build System
The repository uses the gftools builder (`config.yaml`). At the pinned commit, the `sources/` directory contained:

- `Questrial.glyphspackage` — Glyphs source package (multi-file format)
- `build.sh` — shell script wrapper for the build
- `config.yaml` — gftools builder configuration (referenced in METADATA.pb as `sources/config.yaml`)

A `Makefile` was also present at the repository root. The METADATA.pb `config_yaml` field correctly points to `sources/config.yaml`.

## Notes
- Questrial is a sans-serif typeface originally designed by Joe Prince, later updated with contributions from Laura Meseguer.
- Only a single weight (Regular 400) is present in the family.
- The repository is a fork maintained under the `googlefonts` organization for Google Fonts production purposes.
- Subsets covered include Latin, Latin Extended, and Vietnamese.

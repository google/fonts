# Qwigley — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/qwigley
- **Commit**: `7a963366b5efe19ef39603d03888a2105105dc01`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed and verified. The repository was confirmed to exist under the `googlefonts` GitHub organization. The repository description is "Qwigley fonts". The pinned commit was confirmed to exist in the repository's `master` branch. The source block maps explicit file paths from the repository and references a `config.yml` build configuration.

## Build System
The repository uses the gftools builder (`config.yml`). At the pinned commit, the `sources/` directory contained:

- `Qwigley.glyphs` — Glyphs source file
- `config.yml` — gftools builder configuration (referenced in METADATA.pb as `sources/config.yml`)

A `fonts/ttf/` directory was present containing the pre-built TTF. The METADATA.pb source block maps specific files explicitly (`OFL.txt`, `DESCRIPTION.en_us.html`, and `fonts/ttf/Qwigley-Regular.ttf`) in addition to referencing the config. The `branch` field is set to `master`, consistent with the repository's default branch.

## Notes
- Qwigley is a handwriting/display typeface designed by Robert Leuschke.
- Only a single weight (Regular 400) is present in the family.
- The repository is maintained under the `googlefonts` organization.
- Subsets covered include Latin, Latin Extended, and Vietnamese.
- The METADATA.pb classifications include both `DISPLAY` and `HANDWRITING`.

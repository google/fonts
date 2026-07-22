# Qwitcher Grypen — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/googlefonts/qwitcher-grypen
- **Commit**: `cd12ed20d42c30bae735809f5cf84d44ad598837`
- **Status**: Source block already present with repository URL and commit hash

## What Was Done
The existing source metadata was reviewed and verified. The repository was confirmed to exist under the `googlefonts` GitHub organization. The repository description is "Qwitcher Bychen fonts". The pinned commit was confirmed to exist in the repository's `master` branch. The source block maps explicit file paths from the repository and references a `config.yml` build configuration.

## Build System
The repository uses the gftools builder (`config.yml`). At the pinned commit, the `sources/` directory contained:

- `QwitcherGrypenPro.glyphs` — Glyphs source file (note: file named with "Pro" suffix)
- `config.yml` — gftools builder configuration (referenced in METADATA.pb as `sources/config.yml`)

A `fonts/ttf/` directory was present containing the pre-built TTFs. The METADATA.pb source block maps specific files explicitly (`OFL.txt`, `DESCRIPTION.en_us.html`, `fonts/ttf/QwitcherGrypen-Regular.ttf`, and `fonts/ttf/QwitcherGrypen-Bold.ttf`) in addition to referencing the config. The `branch` field is set to `master`, consistent with the repository's default branch.

## Notes
- Qwitcher Grypen is a handwriting/display typeface designed by Robert Leuschke (same designer as Qwigley).
- Two weights are present: Regular (400) and Bold (700).
- The repository is maintained under the `googlefonts` organization.
- The Glyphs source file is named `QwitcherGrypenPro.glyphs` (with a "Pro" suffix), which differs from the published family name.
- The repository description mentions "Qwitcher Bychen fonts", which appears to be an older or alternate working name for the typeface.
- Subsets covered include Latin, Latin Extended, and Vietnamese.
- The METADATA.pb classifications include both `DISPLAY` and `HANDWRITING`.
- Copyright notice spans 2007–2021, suggesting the design originated considerably before its Google Fonts release in November 2021.

# Truculenta — Source Metadata Investigation
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository
- **URL**: https://github.com/Omnibus-Type/Truculenta
- **Commit**: `7ce6b921fc5418882e99f7e1f32688c49cb5acd5`
- **Status**: Commit hash was added to existing source block

## What Was Done
The source block in METADATA.pb contained repository_url, files, and branch ("master") fields but was missing a commit hash. The latest commit on the master branch was retrieved from the GitHub API and added to the source block. The hash was verified via `gh api repos/Omnibus-Type/Truculenta/commits/{hash}`.

## Notes
- This is a variable font with three axes: opsz, wdth, and wght.
- Repository is maintained by Omnibus-Type.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/truculenta/` referencing the upstream gftools-builder-compatible source at the pinned commit `7ce6b92` (`sources/Truculenta.glyphs`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

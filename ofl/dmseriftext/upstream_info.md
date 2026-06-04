# DM Serif Text

**Date investigated**: 2026-02-26
**Status**: missing_config (needs correction)
**Designer**: Colophon Foundry
**METADATA.pb path**: `ofl/dmseriftext/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dm-fonts |
| Commit | `027cea4e4f45827128860a4dec7b9a0852a295d7` |
| Config YAML | N/A (no config.yaml exists for Serif sources) |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dm-fonts`. This was confirmed by PR #2205 ("Font Bakery Dashboard update family: DM Serif Text"), which explicitly recorded the upstream repository as `https://github.com/googlefonts/dm-fonts`.

## How the Commit Hash Was Identified

The commit hash `027cea4e4f45827128860a4dec7b9a0852a295d7` was identified from PR #2205 in google/fonts, which documented the Font Bakery Dashboard update process. The PR metadata explicitly states: **commit**: `027cea4e4f45827128860a4dec7b9a0852a295d7`, **commitDate**: 2019-10-16T10:03:25.000Z, **familyPath**: Serif/Exports.

This is the same upstream commit used for DM Serif Display (PR #2204). The commit is a merge: "Merge pull request #9 from Colophon-Foundry/master - Updates to DM font families", which updated both Serif Display and Serif Text exports simultaneously.

The initial add of DM Serif Text (commit `bc2613e95`, June 2019, PR #2024) did not reference a specific upstream commit. The Font Bakery Dashboard update (Oct 2019, PR #2205) was the last update and is the correct onboarding commit.

## Build Configuration

**There is no config.yaml for the Serif families** in the upstream dm-fonts repository. The `Serif/Source/` directory contains `.glyphs` source files (`DeepMindSerif-{Roman,Italic}.glyphs`) and a `build.sh` script, but no gftools-builder `config.yaml`.

There is also no override `config.yaml` in the google/fonts family directory (`ofl/dmseriftext/`).

**IMPORTANT**: The tracking data previously recorded `config_yaml: "Sans/Source/config.yaml"` which is **incorrect**. That config file belongs to DM Sans and cannot build the Serif Text fonts. This was set in an unmerged branch commit (`4fd9e2392` on `sources_info_2026-02-25`) and should be corrected before merging.

## Relationship to Other DM Families

DM Serif Text shares the `googlefonts/dm-fonts` repository with DM Sans and DM Serif Display. The Serif sources live under `Serif/Source/` with separate `.glyphs` files for Display and Text variants. Both Serif families use the same upstream commit and were onboarded together.

## Timeline

- **2019-06-12**: DM Serif Text v5.100 initially added to google/fonts by Marc Foley (commit `bc2613e95`, PR #2024)
- **2019-10-17**: Updated via Font Bakery Dashboard (PR #2205, commit `4c67e4113`) from dm-fonts commit `027cea4`
- No subsequent font binary updates (only metadata changes)

## Issues Found

1. **Incorrect config_yaml in tracking**: The tracking data has `config_yaml: "Sans/Source/config.yaml"` which points to the DM Sans config, not a Serif config. This needs to be set to `null`.
2. **No config.yaml exists**: Neither the upstream repo nor google/fonts has a config.yaml for this family. Status should be `missing_config` rather than `complete`.
3. **Unmerged incorrect data**: The branch `sources_info_2026-02-25` has incorrect `config_yaml` for this family that should be fixed before merging.

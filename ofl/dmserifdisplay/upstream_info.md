# DM Serif Display

**Date investigated**: 2026-02-26
**Status**: missing_config (needs correction)
**Designer**: Colophon Foundry
**METADATA.pb path**: `ofl/dmserifdisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dm-fonts |
| Commit | `027cea4e4f45827128860a4dec7b9a0852a295d7` |
| Config YAML | N/A (no config.yaml exists for Serif sources) |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dm-fonts`. This was confirmed by PR #2204 ("Font Bakery Dashboard update family: DM Serif Display"), which explicitly recorded the upstream repository as `https://github.com/googlefonts/dm-fonts`.

## How the Commit Hash Was Identified

The commit hash `027cea4e4f45827128860a4dec7b9a0852a295d7` was identified from PR #2204 in google/fonts, which documented the Font Bakery Dashboard update process. The PR metadata explicitly states: **commit**: `027cea4e4f45827128860a4dec7b9a0852a295d7`, **commitDate**: 2019-10-16T10:03:25.000Z, **familyPath**: Serif/Exports.

This commit in dm-fonts is a merge commit: "Merge pull request #9 from Colophon-Foundry/master - Updates to DM font families". It includes updates to both Sans and Serif Exports directories. The binaries in google/fonts were taken from `Serif/Exports/DMSerifDisplay-{Regular,Italic}.ttf`.

The initial add of DM Serif Display (commit `2c8d6d482`, June 2019, PR #2025) did not reference a specific upstream commit. The Font Bakery Dashboard update (Oct 2019, PR #2204) was the last update and is the correct onboarding commit.

## Build Configuration

**There is no config.yaml for the Serif families** in the upstream dm-fonts repository. The `Serif/Source/` directory contains `.glyphs` source files (`DeepMindDisplay-{Roman,Italic}.glyphs`, `DeepMindSerif-{Roman,Italic}.glyphs`) and a `build.sh` script, but no gftools-builder `config.yaml`.

There is also no override `config.yaml` in the google/fonts family directory (`ofl/dmserifdisplay/`).

**IMPORTANT**: The tracking data previously recorded `config_yaml: "Sans/Source/config.yaml"` which is **incorrect**. That config file belongs to DM Sans and cannot build the Serif Display fonts. This was set in an unmerged branch commit (`4fd9e2392` on `sources_info_2026-02-25`) and should be corrected before merging.

## Relationship to Other DM Families

DM Serif Display shares the `googlefonts/dm-fonts` repository with DM Sans and DM Serif Text. The Serif sources live under `Serif/Source/` while the Sans sources live under `Sans/Source/`. The Serif fonts were pre-compiled using the `Serif/Source/build.sh` script, not gftools-builder.

## Timeline

- **2019-06-12**: DM Serif Display v5.100 initially added to google/fonts by Marc Foley (commit `2c8d6d482`, PR #2025)
- **2019-10-16**: Updated via Font Bakery Dashboard (PR #2204, commit `5bdc59521`) from dm-fonts commit `027cea4`
- No subsequent font binary updates (only metadata changes)

## Issues Found

1. **Incorrect config_yaml in tracking**: The tracking data has `config_yaml: "Sans/Source/config.yaml"` which points to the DM Sans config, not a Serif config. This needs to be set to `null`.
2. **No config.yaml exists**: Neither the upstream repo nor google/fonts has a config.yaml for this family. Status should be `missing_config` rather than `complete`.
3. **Unmerged incorrect data**: The branch `sources_info_2026-02-25` has incorrect `config_yaml` for this family that should be fixed before merging.

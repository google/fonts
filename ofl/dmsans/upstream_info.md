# DM Sans

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Colophon Foundry
**METADATA.pb path**: `ofl/dmsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dm-fonts |
| Commit | `d0520ba03bd780f5dccb3024854463d44f699b78` |
| Config YAML | `Sans/Source/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dm-fonts`. This is confirmed by multiple gftools-packager commit messages in google/fonts. The copyright string in the font files also references this URL ("Copyright 2014 The DM Sans Project Authors (https://github.com/googlefonts/dm-fonts)").

## How the Commit Hash Was Identified

The commit hash `d0520ba03bd780f5dccb3024854463d44f699b78` was identified from the most recent gftools-packager commit in google/fonts. Commit `db50662ac` (2023-06-14, by Emma Marichal) states: "DM Sans Version 4.004;gftools[0.9.30] taken from the upstream repo https://github.com/googlefonts/dm-fonts at commit https://github.com/googlefonts/dm-fonts/commit/d0520ba03bd780f5dccb3024854463d44f699b78."

This commit (`d0520ba0`) in upstream has the message "STAT table updated" and is the third most recent commit in the dm-fonts repo. The two newer commits (`da9bd90` "Added tabular numbers" and `4412393` "Tabular update - Fonts exported") were made after the v4.004 onboarding.

The METADATA.pb already contained this commit hash, having been set by the gftools-packager process.

## Build Configuration

The `config.yaml` at `Sans/Source/config.yaml` in the upstream dm-fonts repository is a valid gftools-builder configuration. It specifies:
- Sources: `DMSans.glyphs` and `DMSans-Italic.glyphs`
- Axis order: `opsz`, `wght`, `ital`
- Family name: "DM Sans"
- STAT table configuration for optical size, weight, and italic axes

The METADATA.pb also includes explicit `files {}` entries mapping source files to destination files.

## Relationship to Other DM Families

DM Sans shares the `googlefonts/dm-fonts` repository with DM Serif Display and DM Serif Text. The Sans sources live under `Sans/Source/` while the Serif sources live under `Serif/Source/`. DM Mono has its own separate repo (`googlefonts/dm-mono`).

## Timeline

- **2019-06-12**: DM Sans v1.100 initially added to google/fonts by Marc Foley (commit `03cd45cdb`) as static fonts
- **2019-10-16**: Updated via Font Bakery Dashboard (PR #2203) from dm-fonts commit `027cea4`
- **2023-06-08**: Variable font version 4.003 added by Emma Marichal (commit `c26e50af6`) from upstream commit `7c79670d`
- **2023-06-14**: Version 4.004 added by Emma Marichal (commit `db50662ac`) from upstream commit `d0520ba0` (current)

## Issues Found

The METADATA.pb commit hash and branch are correct. However, the upstream `Sans/Source/config.yaml` is malformed (see fontc_crater fix below).

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
fontc_crater failed with `no config file was found`, even though `Sans/Source/config.yaml` exists at the recorded commit.

### Investigation
The upstream `Sans/Source/config.yaml` has valid content, but every one of its lines is indented by 4 spaces with no top-level key — the whole YAML document is nested under an empty/implicit root. A parser finds no top-level `sources`/`recipe`, so the config is rejected. The defect is still present at upstream HEAD. The recorded commit and the `.glyphs` sources are otherwise correct.

### Actions taken
A corrected override `config.yaml` was added to the family directory: the upstream config de-indented to valid top-level YAML, with the source paths made repo-root-relative (`Sans/Source/DMSans.glyphs`, `Sans/Source/DMSans-Italic.glyphs`). The `config_yaml` field was removed from METADATA.pb so the override is auto-detected. An upstream fix to the indentation of `Sans/Source/config.yaml` should be filed separately.

### Final state
The family directory carries a valid gftools-builder config with a parseable top-level `sources` list pointing at the existing `.glyphs` sources.

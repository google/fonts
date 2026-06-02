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

None. The tracking data is accurate and complete. The METADATA.pb on main already has the correct commit hash, config_yaml, and branch.


## Source-metadata correction (2026-06-02) — override config replaces a mis-indented upstream config

**Model**: Claude Opus 4.8

fontc_crater reported `no config file was found` for dm-fonts. The dmsans `source { config_yaml }` pointed at the repo's `Sans/Source/config.yaml`, which at the pinned commit `d0520ba` is committed with an erroneous 4-space indentation on every line (no top-level key) — verified with `cat -A` (first line is `    sources:$`). That makes it invalid top-level YAML, so google-fonts-sources/fontc_crater cannot parse it and treats the family as having no config. The two declared sources (`Sans/Source/DMSans.glyphs`, `Sans/Source/DMSans-Italic.glyphs`) are both present at `d0520ba`, so the only blocker is the indentation.

Fix:
- Added an override `config.yaml` in this family directory — the same config, de-indented to valid YAML, with the two source paths made relative to the repository root.
- Removed the now-redundant `config_yaml` field from METADATA.pb so google-fonts-sources auto-detects the local override instead of the broken upstream config.

The pinned commit `d0520ba` is unchanged and is the true build commit (the gftools-packager binaries were committed to google/fonts ~3 minutes after it), so building from this corrected config should reproduce the shipped DM Sans (modulo tool versions) — this is a config-validity fix, not a refresh.

(An upstream fix to `Sans/Source/config.yaml`'s indentation in googlefonts/dm-fonts would also resolve this at the source, but would additionally require bumping the pinned commit; the override is self-contained.)

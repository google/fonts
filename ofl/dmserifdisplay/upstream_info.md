# DM Serif Display

**Date investigated**: 2026-02-26 (corrected 2026-06-02)
**Status**: config corrected — override `config.yaml` added; build is `refresh_needed` and currently blocked upstream (see "Build blocker")
**Designer**: Colophon Foundry
**METADATA.pb path**: `ofl/dmserifdisplay/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dm-fonts |
| Commit | `027cea4e4f45827128860a4dec7b9a0852a295d7` |
| Config YAML | override `ofl/dmserifdisplay/config.yaml` (added in this change); `config_yaml` removed from METADATA.pb |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dm-fonts`. This was confirmed by PR #2204 ("Font Bakery Dashboard update family: DM Serif Display"), which explicitly recorded the upstream repository as `https://github.com/googlefonts/dm-fonts`.

## How the Commit Hash Was Identified

The commit hash `027cea4e4f45827128860a4dec7b9a0852a295d7` was identified from PR #2204 in google/fonts, which documented the Font Bakery Dashboard update process. The PR metadata explicitly states: **commit**: `027cea4e4f45827128860a4dec7b9a0852a295d7`, **commitDate**: 2019-10-16T10:03:25.000Z, **familyPath**: Serif/Exports.

This commit in dm-fonts is a merge commit: "Merge pull request #9 from Colophon-Foundry/master - Updates to DM font families". It includes updates to both Sans and Serif Exports directories. The binaries in google/fonts were taken from `Serif/Exports/DMSerifDisplay-{Regular,Italic}.ttf`.

The initial add of DM Serif Display (commit `2c8d6d482`, June 2019, PR #2025) did not reference a specific upstream commit. The Font Bakery Dashboard update (Oct 2019, PR #2204) was the last update and is the correct onboarding commit.

## Build Configuration

The upstream dm-fonts repository has **no gftools-builder `config.yaml` for the Serif families**. The `Serif/Source/` directory contains single-master Glyphs sources (`DeepMindDisplay-{Roman,Italic}.glyphs` for Display, `DeepMindSerif-{Roman,Italic}.glyphs` for Text) plus a `build.sh` that, in 2019, compiled them with plain `fontmake -g <file> -i -o ttf`. The shipped binaries were taken from `Serif/Exports/DMSerifDisplay-{Regular,Italic}.ttf` at commit `027cea4e`.

**What was done:** The METADATA.pb `config_yaml: "Sans/Source/config.yaml"` field was **removed** — it pointed at the DM *Sans* config (a different family) and did not even exist at commit `027cea4e` (that file first appears in 2023). In its place, an **override `config.yaml` was added** at `ofl/dmserifdisplay/config.yaml`, declaring the two static Display Glyphs sources (paths relative to the repository root, so they resolve both in a local build and in fontc_crater). The pinned commit is unchanged. With the override present, google-fonts-sources auto-detects it, so `config_yaml` is correctly omitted from METADATA.pb.

This clears the fontc_crater "failed to find targets" condition for dm-fonts arising from this family: the previous target `Sans/Source/config.yaml @ 027cea4e` was unresolvable (the file is absent at that commit); the override target resolves because both the override and the referenced `.glyphs` exist.

### Build blocker (refresh_needed, not byte-exact)

The override is the correct best-effort recipe, but **it does not currently build with present-day tooling**. At commit `027cea4e` these 2019-era `.glyphs` declare three axes (`wght`, `CONT`, `SERF`) via a legacy "Axes" custom parameter while each file is a single master carrying only weight/width values. Current `glyphsLib` aborts converting them:

```
TypeError: '<' not supported between instances of 'str' and 'int'
  glyphsLib/builder/axes.py: to_designspace_axes -> minimum = min(mapping)
```

(Reproduced with `gftools builder --generate ofl/dmserifdisplay/config.yaml` against a checkout of dm-fonts at `027cea4e`.) Building therefore requires **upstream source modernization** first (e.g. dropping the stale `CONT`/`SERF` axis declarations or regenerating the sources in Glyphs 3 format). Even once it builds, the result is a *fresh* compile of 2019 static fonts and must be QA'd as a refresh (vertical metrics / hinting / naming) before any binary is shipped. This is tracked in the central `PENDING_STEPS.md`.

## Relationship to Other DM Families

DM Serif Display shares the `googlefonts/dm-fonts` repository with DM Sans and DM Serif Text. The Serif sources live under `Serif/Source/` while the Sans sources live under `Sans/Source/`. The Serif fonts were pre-compiled using the `Serif/Source/build.sh` script, not gftools-builder.

## Timeline

- **2019-06-12**: DM Serif Display v5.100 initially added to google/fonts by Marc Foley (commit `2c8d6d482`, PR #2025)
- **2019-10-16**: Updated via Font Bakery Dashboard (PR #2204, commit `5bdc59521`) from dm-fonts commit `027cea4`
- No subsequent font binary updates (only metadata changes)

## Issues Found (and how they were addressed)

1. **Incorrect `config_yaml`** — *fixed.* METADATA pointed `config_yaml` at `Sans/Source/config.yaml` (the DM Sans config), which cannot build the Serif Display fonts and is absent at the pinned 2019 commit. The field was removed and replaced with an override `config.yaml` declaring the correct Serif Display sources.
2. **No upstream Serif config** — *addressed via override.* The upstream repo still has no gftools-builder config for the Serif families; the google/fonts override now supplies a correct best-effort recipe.
3. **Build blocker (legacy multi-axis sources)** — *still pending upstream.* See "Build blocker" above: the 2019 `.glyphs` do not convert under current `glyphsLib`; upstream source modernization is required before a reproducible build is possible. Tracked in `PENDING_STEPS.md`.

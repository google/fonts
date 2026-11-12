# DM Mono

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Colophon Foundry
**METADATA.pb path**: `ofl/dmmono/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/dm-mono |
| Commit | `57fadabfb200a77de2812540026c249dc3013077` |
| Config YAML | N/A (override config.yaml in google/fonts) |
| Branch | N/A |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb `source { repository_url }` field, set to `https://github.com/googlefonts/dm-mono`. This matches the copyright string in the font files ("Copyright 2020 The DM Mono Project Authors (https://www.github.com/googlefonts/dm-mono)"). The initial onboarding commit `85f32a025` in google/fonts (2020-04-15, by Marc Foley) also explicitly states: "Taken from the upstream repo https://github.com/googlefonts/dm-mono".

## How the Commit Hash Was Identified

The commit hash `57fadabfb200a77de2812540026c249dc3013077` was identified directly from the onboarding commit message in google/fonts. Commit `85f32a025` states: "Taken from the upstream repo https://github.com/googlefonts/dm-mono at commit https://github.com/googlefonts/dm-mono/commit/57fadabfb200a77de2812540026c249dc3013077".

This commit is the HEAD of the dm-mono repository (message: "build: fix running gftools fix-isfixedpitch"), confirming it is the latest and only relevant commit. There have been no subsequent updates to the fonts in google/fonts since the initial onboarding.

## Build Configuration

There is no `config.yaml` in the upstream dm-mono repository. An override `config.yaml` exists in the google/fonts family directory (`ofl/dmmono/config.yaml`) with the following content:

```yaml
sources:
  - source/DMMono-MASTER.glyphs
  - source/DMMono-Italics-MASTER.glyphs
```

The upstream repo has `.glyphs` source files at `source/DMMono-MASTER.glyphs` and `source/DMMono-Italics-MASTER.glyphs`, which are buildable with gftools-builder.

## Relationship to Other DM Families

DM Mono has its own separate upstream repository (`googlefonts/dm-mono`), unlike DM Sans, DM Serif Display, and DM Serif Text which share the `googlefonts/dm-fonts` repository. All DM families were designed by Colophon Foundry.

## Timeline

- **2020-04-15**: DM Mono v1.000 added to google/fonts by Marc Foley (commit `85f32a025`), taken from upstream commit `57fadab`
- No subsequent font binary updates

## Issues Found

None. The tracking data is accurate and complete.

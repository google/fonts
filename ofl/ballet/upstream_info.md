# Ballet

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Omnibus-Type, Maximiliano Sproviero
**METADATA.pb path**: `ofl/ballet/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Omnibus-Type/Ballet |
| Commit | bd239d606894c2139ad997b60d2141bee7856817 (not in METADATA.pb, found via PR) |
| **Config YAML** | Override in google/fonts |
| Branch | (not specified) |

## How the Repository URL Was Found

The repository URL `https://github.com/Omnibus-Type/Ballet` is documented in the METADATA.pb `source` block (line 29) and confirmed by the copyright string in the font metadata: "Copyright 2020 The Ballet Project Authors (https://github.com/Omnibus-Type/Ballet)". The upstream repo is cached at `upstream_repos/fontc_crater_cache/Omnibus-Type/Ballet/`.

## How the Commit Hash Was Identified

The commit hash `bd239d606894c2139ad997b60d2141bee7856817` was identified from PR #2696, which explicitly states: "Taken as upstream repo https://github.com/Omnibus-Type/Ballet at commit https://github.com/Omnibus-Type/Ballet/commit/bd239d606894c2139ad997b60d2141bee7856817."

The google/fonts commit `03fc129d8` ("Ballet: version 1.100 added (#2696)") from 2020-09-30 was the last commit to add the TTF file. The subsequent commit `70b0fc8a8` ("Remove static fonts for unhinted variable font families (#3695)") from 2021-08-16 only removed static fonts but did not update the variable font.

The upstream commit `bd239d6` is dated 2020-09-24, which is 6 days before the google/fonts commit on 2020-09-30. This timing is consistent with a normal onboarding review cycle.

**Note**: The METADATA.pb `source` block currently has no `commit` field. The commit hash `bd239d6` should be added.

## How Config YAML Was Resolved

The upstream repository does NOT contain a `config.yaml` file. The font was built using a custom `sources/build.sh` shell script that calls `glyphs2ufo` and presumably `fontmake` directly, predating the standardized gftools-builder `config.yaml` approach.

There is also no override `config.yaml` in the google/fonts family directory (`ofl/ballet/`). The directory contains only: `Ballet[opsz].ttf`, `DESCRIPTION.en_us.html`, `METADATA.pb`, `OFL.txt`.

A `config.yaml` would need to be created either in the upstream repo or as an override in google/fonts to enable gftools-builder / fontc_crater builds.

## Verification

- **Commit exists in upstream repo**: Yes, verified in `upstream_repos/fontc_crater_cache/Omnibus-Type/Ballet/`
- **Commit date**: 2020-09-24 13:24:35 -0300
- **Commit message**: "Adding files to origin master"
- **Source files at commit**:
  - `sources/Ballet.glyphs` (primary source)
  - `sources/Ballet-variable.designspace`
  - `sources/Ballet-static.designspace`
  - `sources/build.sh` (custom build script)
  - `sources/build-statics.sh`
  - `sources/gen_stat.py`
  - `fonts/variable/Ballet[opsz].ttf` (pre-built variable font)

## Confidence

**HIGH**: The PR #2696 explicitly references the upstream commit. The commit date (2020-09-24) predates the google/fonts merge (2020-09-30) by a reasonable margin. The upstream repo URL matches both the METADATA.pb and the font copyright. The only issue is the missing config.yaml, which is expected for a pre-gftools-builder era font.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Ballet.glyphs
axisOrder:
  - opsz
buildStatic: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. The METADATA.pb `source` block is missing the `commit` field. It should be set to `bd239d606894c2139ad997b60d2141bee7856817`.
2. A `config.yaml` needs to be created for this family (either upstream or as an override in google/fonts) to enable modern build tooling. The source is a `.glyphs` file with a `.designspace` for the optical size axis.

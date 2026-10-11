# Dangrek

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Danh Hong
**METADATA.pb path**: `ofl/dangrek/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/danhhong/Dangrek |
| Commit | `a8da8cf02ec7e96f45716b0052a027007bb042c2` |
| Config YAML | `Source/builder.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/danhhong/Dangrek` is documented in the METADATA.pb `source { repository_url }` field. It matches the copyright string in the font ("Copyright 2020 The Dangrek Project Authors (https://github.com/danhhong/Dangrek)"). The gftools-packager commit `f587dcbf8` in google/fonts (PR #3507) also references this URL: "Dangrek Version 8.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/danhhong/Dangrek.git".

## How the Commit Hash Was Identified

The commit hash `a8da8cf02ec7e96f45716b0052a027007bb042c2` is recorded in METADATA.pb and confirmed by the gftools-packager commit `f587dcbf8` (PR #3507, authored by Yanone): "Dangrek Version 8.000; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/danhhong/Dangrek.git at commit https://github.com/danhhong/Dangrek/commit/a8da8cf02ec7e96f45716b0052a027007bb042c2."

This commit is the HEAD of the `master` branch in the upstream repository. It is a merge commit: "Merge pull request #1 from yanone/master". No additional commits have been made since.

Note: After the initial onboarding (PR #3507), there was a subsequent batch update in commit `4f5dbdb58` ("Bumped to 8.002 (urgent glyph definition issues)" PR #4152) that modified `Dangrek-Regular.ttf`. This was a batch fix for Khmer fonts addressing "urgent glyph definition issues" and did not come from a new upstream commit -- the binary was likely rebuilt from the same source.

## How Config YAML Was Resolved

The upstream repository contains `Source/builder.yaml` at the recorded commit. The builder config references `Dangrek.glyphs` as the source with `outputDir: "../Release"`, `buildStatic: true`, `buildVariable: false`. This path is correctly recorded in the METADATA.pb `config_yaml` field as `Source/builder.yaml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit is HEAD of master: Yes
- Commit message: "Merge pull request #1 from yanone/master"
- Source files at commit: `Source/Dangrek.glyphs`, `Source/builder.yaml`
- Config YAML at commit: `Source/builder.yaml` (valid gftools-builder config)
- METADATA.pb files mapping: `Release/ttf/Dangrek-Regular.ttf` -> `Dangrek-Regular.ttf`
- Font was originally added in early google/fonts history (2011-03-02), then updated to V8 via PR #3507

## Confidence

**High**: The repository URL and commit hash are both confirmed by the gftools-packager commit message (PR #3507). The commit exists and is the HEAD of the master branch. The builder.yaml is present at the correct path in the upstream repo.

## Open Questions

None. All data is consistent and well-documented.

# Blaka

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Mohamed Gaber
**METADATA.pb path**: `ofl/blaka/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Gue3bara/Blaka |
| Commit | `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` |
| Config YAML | `sources/blakaregular.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/Gue3bara/Blaka` was already present in the METADATA.pb `source { repository_url }` field. It is confirmed by the copyright string ("Copyright 2019 The Blaka Project Authors (https://github.com/Gue3bara/Blaka)") and by multiple gftools-packager commits in google/fonts. The initial onboarding commit `0a949b872` (PR #4555, 2022-04-27, by Yanone) references this URL, as does the latest update commit `bc779ce70` (2023-09-29, also by Yanone).

## How the Commit Hash Was Identified

The commit hash `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is recorded in METADATA.pb. It matches the gftools-packager commit `bc779ce70` in google/fonts, which states: "Blaka Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Gue3bara/Blaka at commit https://github.com/Gue3bara/Blaka/commit/7f264eee862d3e94c2cb6a728c6429c2f3b9adc3."

This is the latest update (v1.003), superseding the initial onboarding commit `c3cbce1cfcc77b06bdf2b68a2ed098ed10c7cf75` (v1.001, from PR #4555). The commit exists in the upstream repo with message "Bumped version to 1.003 across all fonts" and is the HEAD of the repository.

## How Config YAML Was Resolved

The config file `sources/blakaregular.yaml` exists in the upstream repository at the recorded commit. It contains:

```yaml
sources:
  - temp/Blaka-Regular.glyphs
outputDir: "../fonts/regular"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The `config_yaml` field in METADATA.pb correctly points to `sources/blakaregular.yaml`. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: Latest commit (HEAD) in the Blaka repo
- Commit message: "Bumped version to 1.003 across all fonts"
- Config YAML at commit: `sources/blakaregular.yaml` exists
- Source file referenced: `temp/Blaka-Regular.glyphs` (in sources/temp/)
- Binary file in METADATA.pb: `fonts/regular/ttf/Blaka-Regular.ttf`

## Confidence

**High**: The repository URL and commit hash are consistently referenced across METADATA.pb, the gftools-packager commit in google/fonts, and the upstream repo. The commit exists and is the HEAD of the repo. The config YAML file exists at the recorded commit and contains valid gftools-builder configuration.

## Open Questions

None. All data is verified and consistent. Note that this is the same upstream repo shared by Blaka, Blaka Hollow, and Blaka Ink, all at the same commit hash.

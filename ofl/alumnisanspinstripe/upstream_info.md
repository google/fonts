# Alumni Sans Pinstripe

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Robert Leuschke
**METADATA.pb path**: `ofl/alumnisanspinstripe/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/alumni-sans-pinstripe |
| Commit | `26cf834f2eca219b017478be9ea1387c78756e78` |
| Config YAML | `sources/config.yml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/alumni-sans-pinstripe` was already present in the METADATA.pb `source {}` block. It matches the copyright notice in the font files ("Copyright 2014 The Alumni Sans Pinstripe Project Authors (https://github.com/googlefonts/alumni-sans-pinstripe)") and the remote URL of the cached upstream repo. The repository exists and is accessible.

## How the Commit Hash Was Identified

The commit hash `26cf834f2eca219b017478be9ea1387c78756e78` was already recorded in METADATA.pb and is confirmed by multiple sources:

1. **google/fonts commit message**: The onboarding commit `9d68dcf8e` (PR #4759, merged 2022-06-17) explicitly states: "Alumni Sans Pinstripe Version 1.010; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/googlefonts/alumni-sans-pinstripe at commit https://github.com/googlefonts/alumni-sans-pinstripe/commit/26cf834f2eca219b017478be9ea1387c78756e78."
2. **Single-commit repo**: The upstream repository contains only one commit (`26cf834`), authored by Viviana Monsalve on 2022-06-09 with message "v1.010 fonts added". There are no subsequent commits that could cause ambiguity.
3. **Timeline**: The upstream commit (2022-06-09) predates the google/fonts merge (2022-06-17) by 8 days, consistent with the onboarding workflow.
4. **Binary file sizes match**: The TTF files at this commit are 110,624 bytes (Italic) and 104,716 bytes (Regular), matching the files in `ofl/alumnisanspinstripe/`.

## How Config YAML Was Resolved

The config file `sources/config.yml` exists in the upstream repository at the referenced commit. Its contents:

```yaml
sources:
  - AlumniSansPinstripe.glyphs
  - AlumniSansPinstripe-Italic.glyphs
familyName: "Alumni Sans Pinstripe"
buildVariable: false
```

The METADATA.pb correctly references this as `config_yaml: "sources/config.yml"`. The source files (`.glyphs`) are relative to the `sources/` directory and are present at the commit. No override config.yaml exists in the google/fonts family directory, and none is needed since the upstream config is complete.

## Conclusion

This family's source metadata is fully complete and verified. The repository URL, commit hash, branch, and config_yaml path are all correctly recorded in METADATA.pb. The upstream repository is a single-commit repo created by Viviana Monsalve, onboarded via gftools-packager in PR #4759, with the commit hash explicitly confirmed in the google/fonts commit message. No corrections are needed.

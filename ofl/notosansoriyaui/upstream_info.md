# Noto Sans Oriya UI - Upstream Source Report

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [https://github.com/googlefonts/noto-fonts](https://github.com/googlefonts/noto-fonts) |
| Commit | `bc27c394087c8f52ef27d7a3742dd441dd0c22a5` |
| Version | 2.000 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Description

Oriya (Odia) script UI variant with tighter vertical metrics designed for Android system UI and web interfaces. Noto Sans Oriya UI is a UI variant of the corresponding Noto Sans family. UI variants use tighter vertical metrics (smaller ascender/descender values) than the standard versions, designed for Android system UI and web interfaces where vertical space is constrained.

## Upstream Details

The source repository is `googlefonts/noto-fonts`, the pre-2022 Noto monorepo that contained
pre-built binary fonts for all Noto families. This monorepo has since been superseded by the
per-script repositories under the `notofonts/` GitHub organization, which contain sources and
build from source using modern tooling. However, the binaries currently served on Google Fonts
for this family were built from the old monorepo, not the newer per-script repos.

The commit `bc27c394087c...` was verified by blob-hash comparison: the font binary
blob hashes at this commit in the monorepo match the blobs added in the google/fonts
onboarding PR #2823.

## Notes

UI variant. Dec 25 2020 batch.

## Confidence

**HIGH** (blob-hash verified against onboarding PR)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans-oriya.yaml` in the `notofonts/oriya` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.

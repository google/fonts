# Noto Sans Display - Upstream Source Report

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [https://github.com/googlefonts/noto-fonts](https://github.com/googlefonts/noto-fonts) |
| Commit | `217e0ab67385bc728b088f565c2c9b76633c01c5` |
| Version | 2.003 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Description

Display variant of Noto Sans with tighter spacing optimized for headlines and large text settings, covering Latin, Cyrillic, and Greek scripts. Noto Sans Display is the display-optimized variant of Noto Sans. It uses tighter line spacing than standard Noto Sans, making it suitable for headlines, titles, and other large-text contexts where compact vertical metrics are preferred.

## Upstream Details

The source repository is `googlefonts/noto-fonts`, the pre-2022 Noto monorepo that contained
pre-built binary fonts for all Noto families. This monorepo has since been superseded by the
per-script repositories under the `notofonts/` GitHub organization, which contain sources and
build from source using modern tooling. However, the binaries currently served on Google Fonts
for this family were built from the old monorepo, not the newer per-script repos.

The commit `217e0ab67385...` was verified by blob-hash comparison: the font binary
blob hashes at this commit in the monorepo match the blobs added in the google/fonts
onboarding PR #2823.

## Notes

Display variant (tighter spacing for headlines). Dec 25 2020 batch. Both upright and italic VFs.

## Confidence

**HIGH** (blob-hash verified against onboarding PR)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans.yaml` in the `notofonts/latin-greek-cyrillic` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the `repository_url` pointed at the deprecated `googlefonts/noto-fonts` monorepo, which no longer contains the Glyphs/glyphspackage sources (only built binaries). The sources now live in the per-script repo.

Corrected the METADATA.pb source block:
- repository_url: `https://github.com/googlefonts/noto-fonts` → `https://github.com/notofonts/latin-greek-cyrillic`
- commit: `217e0ab67385bc728b088f565c2c9b76633c01c5` → `41644bc7a679a27da9b44d1875e6a5f651c80674` (2023-02-20)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The per-script Noto repos postdate the 2021-01-13 onboarding of the shipped binary, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.

Note: Noto Sans Display is built from the base `NotoSans.glyphspackage` in this repo (there is no separate Display source); the Display cut is produced by the build recipe.

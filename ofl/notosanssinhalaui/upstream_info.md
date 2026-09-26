# Noto Sans Sinhala UI - Upstream Source Report

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [https://github.com/googlefonts/noto-fonts](https://github.com/googlefonts/noto-fonts) |
| Commit | `da23fbffb845dc5e9bd6da24b3dbbbc7effe7dbc` |
| Version | 2.001 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Description

Sinhala script UI variant with tighter vertical metrics designed for Android system UI and web interfaces. Noto Sans Sinhala UI is a UI variant of the corresponding Noto Sans family. UI variants use tighter vertical metrics (smaller ascender/descender values) than the standard versions, designed for Android system UI and web interfaces where vertical space is constrained.

## Upstream Details

The source repository is `googlefonts/noto-fonts`, the pre-2022 Noto monorepo that contained
pre-built binary fonts for all Noto families. This monorepo has since been superseded by the
per-script repositories under the `notofonts/` GitHub organization, which contain sources and
build from source using modern tooling. However, the binaries currently served on Google Fonts
for this family were built from the old monorepo, not the newer per-script repos.

The commit `da23fbffb845...` was verified by blob-hash comparison: the font binary
blob hashes at this commit in the monorepo match the blobs added in the google/fonts
onboarding PR #2823.

## Notes

UI variant. Dec 25 2020 batch.

## Confidence

**HIGH** (blob-hash verified against onboarding PR)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans-sinhala.yaml` in the `notofonts/sinhala` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the `repository_url` pointed at the deprecated `googlefonts/noto-fonts` monorepo, which no longer contains the Glyphs/glyphspackage sources (only built binaries). The sources now live in the per-script repo.

Corrected the METADATA.pb source block:
- repository_url: `https://github.com/googlefonts/noto-fonts` → `https://github.com/notofonts/sinhala`
- commit: `da23fbffb845dc5e9bd6da24b3dbbbc7effe7dbc` → `032355e96de5bac83fd996535af3d13b1fbfeccf` (2025-10-14)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The per-script Noto repos postdate the 2021-01-13 onboarding of the shipped binary, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.

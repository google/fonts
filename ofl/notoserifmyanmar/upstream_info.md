# Noto Serif Myanmar — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | `3b258db81a8ece82231fdf267e547383b0564200` |
| Version | 2.001 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Serif Myanmar was onboarded as part of the December 25, 2020 Noto batch via PR #2823, sourced from the googlefonts/noto-fonts monorepo at commit `3b258db81a8ece82231fdf267e547383b0564200`.

After onboarding, the Bold and Light weights were modified in-place within the google/fonts repository on 2021-06-23 to fix OS/2 weight class values. As a result, those specific weight files no longer match the blob hashes from this upstream commit. The Regular and other weights remain unmodified.

**Note**: Dec 25 2020 batch. Bold and Light later modified in-place in google/fonts (OS2 weight fix, 2021-06-23) so those weights no longer match this commit.

**Confidence**: HIGH (blob-verified for Regular and other unmodified weights; Bold and Light were post-processed in google/fonts)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-serif-myanmar.yaml` in the `notofonts/myanmar` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.


## Source-metadata correction (2026-06-02) — ⚠ REFRESH REQUIRED

**Model**: Claude Opus 4.8

fontc_crater reported a `missing source` failure for this family because the `repository_url` pointed at the deprecated `googlefonts/noto-fonts` monorepo, which no longer contains the Glyphs/glyphspackage sources (only built binaries). The sources now live in the per-script repo.

Corrected the METADATA.pb source block:
- repository_url: `https://github.com/googlefonts/noto-fonts` → `https://github.com/notofonts/myanmar`
- commit: `3b258db81a8ece82231fdf267e547383b0564200` → `57be35a771cf5da0271db8521c48a1cfdc4d2126` (2022-07-13)

The declared source is confirmed present at the new commit.

**⚠ REFRESH REQUIRED — this does NOT reproduce the shipped binary.** The per-script Noto repos postdate the 2021-01-13 onboarding of the shipped binary, so the source now resolves and the family becomes buildable, but a rebuild produces an **updated** font, not the originally-shipped artifact. Before shipping any rebuild, a human must QA the output for reflow / vertical-metric / glyph-coverage / version differences. The original build provenance (the exact source + commit that produced the shipped binary) is not recoverable from the current upstream.

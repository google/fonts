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

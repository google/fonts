# Pacifico — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The upstream repository for Pacifico was identified at https://github.com/googlefonts/Pacifico, hosted under the `googlefonts` GitHub organization. The METADATA.pb file referenced commit `423e7cb2b036ead2624c05197e17a83ddf5c6068` on the default branch, with the build configuration at `sources/config.yaml`.

## Font Description

Pacifico is a fun brush script typeface originally created by Vernon Adams and later extended by Jacques Le Bailly, Botjo Nikoltchev, and Ani Petrova. The design draws on American surf culture from the 1950s and 60s. The font covers Latin, Cyrillic (including Cyrillic Extended), and Vietnamese scripts.

## Designer

Vernon Adams was the original designer. The font was later expanded by Jacques Le Bailly, Botjo Nikoltchev, and Ani Petrova as part of the Google Fonts revival effort under the `googlefonts` organization.

## Repository

- **URL**: https://github.com/googlefonts/Pacifico
- **Commit**: `aff5d08efd4883cd58a660b4b688a73edcea3d92`
- **Config**: `sources/config.yaml`
- **License**: OFL

## Font Details

| Property | Value |
|----------|-------|
| Category | HANDWRITING |
| Style | Regular (400) |
| Subsets | latin, latin-ext, cyrillic, cyrillic-ext, vietnamese |
| Variable | No |

## Confidence

**High** — The repository is hosted under the `googlefonts` organization, the commit is explicitly referenced in METADATA.pb, and the copyright notice matches the repository URL.

## Source pin corrected (checked 2026-11-11)

**Model**: Claude Opus 5.5

The pin moved from [`423e7cb2`](https://github.com/googlefonts/Pacifico/commit/423e7cb2) to [`aff5d08e`](https://github.com/googlefonts/Pacifico/commit/aff5d08e). `423e7cb2` (2024-02-22) merges the unshipped v3.010 expansion; it was copied from fontc_crater's targets list in [google/fonts `5fa1b4a6`](https://github.com/google/fonts/commit/5fa1b4a6).

Google Fonts still ships v3.001, added by [google/fonts#2127](https://github.com/google/fonts/pull/2127) ([google/fonts `34ce35e2`](https://github.com/google/fonts/commit/34ce35e2)). The shipped `Pacifico-Regular.ttf` (md5 `63d7fc2ef0f495c53190ca6c457c2b96`) is byte-identical to `fonts/Pacifico-Regular.ttf` as committed with `sources/Pacifico.glyphs` in `aff5d08e` ("Fix kerning for pair Ic", on `main`). The onboarding commit names PR #6's commit [`87509815`](https://github.com/googlefonts/Pacifico/commit/87509815), which is on no branch; `aff5d08e` is the commit PR #6 was merged as, with the same tree.

`aff5d08e` has no `sources/config.yaml`, so `config_yaml` was dropped from METADATA.pb and an override `config.yaml` names `sources/Pacifico.glyphs`.

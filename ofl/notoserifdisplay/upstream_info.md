# Noto Serif Display — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | `7dca4ca5ec66a517c081b6ab5ae6235644aa2cb3` |
| Version | 2.003 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Serif Display is a display variant of Noto Serif, onboarded as part of the December 25, 2020 Noto batch via PR #2823. The font binaries (both upright and italic variable fonts) were sourced from the googlefonts/noto-fonts monorepo at commit `7dca4ca5ec66a517c081b6ab5ae6235644aa2cb3`.

The commit was verified by blob-hash comparison: both the upright and italic VF binary blob hashes at this commit in the googlefonts/noto-fonts monorepo match the blobs added to google/fonts in PR #2823 (commit a559a6efc).

**Note**: Display variant. Dec 25 2020 batch. Both upright and italic VFs.

**Confidence**: HIGH (blob-verified)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-serif.yaml` in the `notofonts/latin-greek-cyrillic` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.

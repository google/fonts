# Noto Sans Thai UI — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | `282a3a827151188c0ee4bce392e89e6ef4c16323` |
| Version | 2.000 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Sans Thai UI is a UI variant of Noto Sans Thai, onboarded as part of the large December 25, 2020 Noto batch via PR #2823. The font binary was sourced from the googlefonts/noto-fonts monorepo at commit `282a3a827151188c0ee4bce392e89e6ef4c16323`.

The commit was verified by blob-hash comparison: the font binary blob hash at this commit in the googlefonts/noto-fonts monorepo matches the blob added to google/fonts in PR #2823 (commit a559a6efc).

**Note**: UI variant. Dec 25 2020 batch.

**Confidence**: HIGH (blob-verified)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans-thai-ui.yaml` in the `notofonts/thai` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.

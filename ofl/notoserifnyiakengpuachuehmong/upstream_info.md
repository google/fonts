# Noto Serif Nyiakeng Puachue Hmong — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | `9232f17974e5783a5dbd862f38225e0584e73add` |
| Version | 1.000 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Serif Nyiakeng Puachue Hmong was onboarded as part of the December 25, 2020 Noto batch via PR #2823. The font binary was sourced from the googlefonts/noto-fonts monorepo at commit `9232f17974e5783a5dbd862f38225e0584e73add`.

The commit was verified by blob-hash comparison: the font binary blob hash at this commit in the googlefonts/noto-fonts monorepo matches the blob added to google/fonts in PR #2823 (commit a559a6efc).

**Note**: Dec 25 2020 batch.

**Confidence**: HIGH (blob-verified)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-serif-nyiakeng-puachue-hmong.yaml` in the `notofonts/nyiakeng-puachue-hmong` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.

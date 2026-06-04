# Noto Sans N'Ko — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/googlefonts/noto-fonts |
| Commit | Not yet identified |
| Version | 2.001 |
| Onboarding PR | [google/fonts#2823](https://github.com/google/fonts/pull/2823) |
| Date | 2021-01-13 |

## Investigation Summary

Noto Sans N'Ko v2.001 was onboarded as part of the December 25, 2020 Noto batch via PR #2823. The binary originated from the old googlefonts/noto-fonts monorepo, which contained fonts for many scripts in a single repository. This predates the reorganization into per-script repos (e.g., notofonts/nko).

The exact commit within noto-fonts has not yet been identified, though the blob matches the PR #2823 batch. The family directory in google/fonts was later renamed via PR #5605, resulting in the current `notosansnko_todelist` directory slug.

**Note**: v2.001 from the old noto-fonts monorepo. Predates notofonts/nko repo. Directory later renamed in PR #5605. Exact commit in noto-fonts not yet identified (same blob as PR #2823 batch).

**Confidence**: MEDIUM (repository identified, blob matches PR #2823 batch, but exact commit within noto-fonts not yet pinpointed)

## Build Configuration (Override)

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-sans-nko-unjoined.yaml` in the `notofonts/nko` repository (the current per-script Noto repo). **Important caveat**: this config references the current notofonts/ per-script repo sources, which may produce a newer version than the binary currently shipped in google/fonts. The shipped binary was built from the older `googlefonts/noto-fonts` monorepo using a different build pipeline. This override config serves as a starting point for reproducible build attempts but is not expected to produce a byte-identical match.

## Commit Added (HIGH confidence)

Commit `20bc5918912503bc1537a407a694738c33c048aa` was determined by **tag_match**. Matched a version tag in the upstream repo whose date is on or before the binary modification date in google/fonts (2022-11-24). This is the most reliable method.

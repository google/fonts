# Amatic SC

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Vernon Adams, Ben Nathan, Thomas Jockin
**METADATA.pb path**: `ofl/amaticsc/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/AmaticSC |
| Commit | `308846136d2dcfb6aef2160d7e927698cdaf9c05` |
| Config YAML | `sources/config.yaml` |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/AmaticSC` was already present in METADATA.pb. It was added by Simon Cozens in commit `5f2b22f48` ("Update upstreams", 2023-12-14) as part of a bulk update of upstream source blocks. The URL is also referenced in the original google/fonts onboarding commit `81e5d4b23` (PR #1271, by Marc Foley, 2017-10-31): "Taken from the upstream repo, https://github.com/googlefonts/AmaticSC". The copyright string in the font files confirms this URL. The remote URL of the cached repo matches.

## How the Commit Hash Was Identified

The commit `308846136d2dcfb6aef2160d7e927698cdaf9c05` was ported from the fontc_crater targets list in the Batch 1/4 commit (`19cdcec59`, 2025-03-31) by @felipesanches.

This commit is the HEAD of the upstream repo's main branch. It is a merge commit for PR #18 ("add sources/config.yaml"), authored by @felipesanches on 2025-02-24. This is NOT the original onboarding commit -- the original onboarding into google/fonts was done in 2017 (PR #1271) without recording a specific upstream commit hash.

However, this commit is the correct reference for fontc_crater purposes because:
1. The binary font files (`fonts/ttf/AmaticSC-Bold.ttf` and `fonts/ttf/AmaticSC-Regular.ttf`) at this commit are byte-identical to the files currently in `ofl/amaticsc/` in google/fonts (both Bold at 156,180 bytes and Regular at 151,624 bytes).
2. The `sources/config.yaml` file (needed for gftools-builder / fontc_crater) was added in this commit.
3. The repo is a shallow clone with only this commit available, which is the latest state of the repo.

Since the repo had no commits between the original onboarding (2017) and the config.yaml addition (2025), this commit correctly represents the source state.

## How Config YAML Was Resolved

The `sources/config.yaml` file exists in the upstream repo at the referenced commit. It was added by @felipesanches in PR #18 (merged 2025-02-24). The config is minimal:

```yaml
sources:
  - AmaticSC.glyphs
```

This references the Glyphs source file at `sources/AmaticSC.glyphs`, which exists at the referenced commit. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`. No override config.yaml exists in the google/fonts family directory.

## Conclusion

The source metadata for Amatic SC is complete and correct. The repository URL is confirmed through multiple sources (copyright string, PR history, commit messages). The commit hash points to the latest state of the upstream repo, which includes both the original source files and the config.yaml needed for fontc_crater. The binary fonts at this commit match those in google/fonts byte-for-byte. Status: **complete**.

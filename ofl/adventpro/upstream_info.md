# Advent Pro

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: VivaRado
**METADATA.pb path**: `ofl/adventpro/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/Advent |
| Commit | `d206a139ee9045993fbd1e530b93f28f8bf4e3b1` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/googlefonts/Advent` was already present in the METADATA.pb source block. It was originally set via gftools-packager when PR #5522 onboarded Version 3.000 (commit `ce1042736` in google/fonts, authored by Yanone on 2022-12-01). The `config_yaml` field was later added in the "Batch 1/4" commit (`19cdcec59`, 2025-03-31), porting data from fontc_crater's targets.json.

The cached upstream repo at `googlefonts/Advent` confirms the remote URL matches.

## How the Commit Hash Was Identified

The commit `d206a139ee9045993fbd1e530b93f28f8bf4e3b1` is explicitly referenced in the google/fonts PR #5522 commit message:

> Advent Pro Version 3.000 taken from the upstream repo https://github.com/googlefonts/Advent at commit https://github.com/googlefonts/Advent/commit/d206a139ee9045993fbd1e530b93f28f8bf4e3b1.

This commit is the only commit in the upstream repo (the entire repository history is a single commit titled "Latest binaries", authored by Yanone on 2022-11-25). Therefore there is no ambiguity about which commit was used.

**Binary file verification**: The SHA256 hashes of both variable font files match exactly between the upstream repo at this commit and the google/fonts directory:
- `AdventPro[wdth,wght].ttf`: `b60ab2920b89bdc4b7dadfb282cadac6e03833e7a80844f9eac096359b2b9766`
- `AdventPro-Italic[wdth,wght].ttf`: `0917a5d65589025f2a752b1b0568f924dac49a065a25b4d60116b3c6d4d9ebae`

This confirms the fonts in google/fonts were taken directly from the upstream repo's pre-built binaries at `fonts/variable/split/`, not built from source.

## How Config YAML Was Resolved

The upstream repo contains `sources/config.yaml` at the referenced commit, confirmed via `git ls-tree`. The config uses a `.designspace` source file (`sources/AdventPro.designspace`) which references UFO masters in `sources/advent_pro/`. The config is set to build variable TTF only (no OTF, no static, no webfont).

The METADATA.pb correctly references this as `config_yaml: "sources/config.yaml"`. Note that the fonts currently in google/fonts were NOT built using this config -- they are pre-built binaries copied from the upstream repo's `fonts/variable/split/` directory. The config would be relevant for any future rebuild from source using fontc/gftools-builder.

No override `config.yaml` exists in the google/fonts family directory.

## Key Timeline

| Date | Event |
|------|-------|
| 2022-11-25 | Upstream commit `d206a13` ("Latest binaries") by Yanone |
| 2022-12-01 | google/fonts PR #5522 merged (Version 3.000 onboarded) |
| 2024-04-03 | upstream.yaml merged into METADATA.pb source block |
| 2025-03-31 | Batch 1/4 added `config_yaml` field to METADATA.pb |

## Conclusion

The source block for Advent Pro is **complete** and well-documented. The repository URL, commit hash, branch, and config_yaml are all correctly set in METADATA.pb. The commit hash is verified both by the explicit reference in PR #5522 and by identical SHA256 hashes of the binary font files. The upstream repo has only one commit, making verification trivial.

**Confidence**: HIGH

# Ancizar Sans

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Universidad Nacional de Colombia (UNAL), Cesar Puertas, Viviana Monsalve, Julian Moncada
**METADATA.pb path**: `ofl/ancizarsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/UNAL-OMD/UNAL-Ancizar |
| Commit | `54a5aa2153b4485ff2710612d47183c346e6b842` |
| Config YAML | `sources/config-sans.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL `https://github.com/UNAL-OMD/UNAL-Ancizar` was already recorded in the METADATA.pb source block. It is also referenced in the copyright string of the font files and in the google/fonts commit message (`544bd4e`) that initially added the family:

> Taken from the upstream repo https://github.com/UNAL-OMD/UNAL-Ancizar at commit https://github.com/UNAL-OMD/UNAL-Ancizar/commit/54a5aa2153b4485ff2710612d47183c346e6b842.

The repository is cached locally at `upstream_repos/fontc_crater_cache/UNAL-OMD/UNAL-Ancizar` and is accessible.

Note: This is a shared repository with the sibling family "Ancizar Serif", which uses a separate config (`sources/config-serif.yaml`).

## How the Commit Hash Was Identified

The commit `54a5aa2153b4485ff2710612d47183c346e6b842` was explicitly referenced in the google/fonts onboarding commit (`544bd4e`, authored by Yanone on 2025-04-16). This commit message states the fonts were taken from the upstream repo at that exact commit.

**Verification**: The git blob hashes of the binary files are identical between google/fonts and the upstream repo at this commit:

- `AncizarSans[wght].ttf`: blob `ddfd6550ee6f9980d4945384a03ed5fee68d02a7` (172,192 bytes)
- `AncizarSans-Italic[wght].ttf`: blob `d226c7a1fae1fe37d35c1a41975dc3f3bfbb56e7` (178,372 bytes)

The upstream commit message is "New Sans binaries" (2025-04-16) by Yanone, and the google/fonts commit was made the same day, confirming the onboarder (Yanone) updated the upstream binaries and then immediately onboarded them.

The upstream `main` branch has since progressed past this commit (current HEAD: `c4303cb`, "Added RFN"), but the subsequent commits are related to Serif fixes and an RFN addition, not Sans changes.

## How Config YAML Was Resolved

The file `sources/config-sans.yaml` exists in the upstream repository at the referenced commit. Its contents:

```yaml
sources:
  - AncizarSans.glyphs
  - AncizarSans-Italic.glyphs
buildVariable: true
buildStatic: true
buildTTF: false
buildOTF: false
buildWebfont: false
buildSmallCap: false
```

This is a valid gftools-builder configuration referencing the `.glyphs` source files for the Sans variant. The `config_yaml` field in METADATA.pb correctly points to this file. No local override config.yaml exists in the google/fonts family directory.

The `config_yaml: "sources/config-sans.yaml"` field was added in a subsequent commit (`6a0d06b`, 2025-05-22) by Felipe Sanches as part of PR #9350 to enrich source metadata.

## google/fonts Commit History

1. `544bd4e` (2025-04-16, Yanone): Initial onboarding - "Ancizar Sans: Version 8.100 added" (resolves #9095)
2. `cdcc68c`: Update OFL.txt
3. `6a0d06b` (2025-05-22, Felipe Sanches): Added `config_yaml` field to source block (PR #9350)
4. `264e439` (2025-05-22, Dave Crossland): Added `display_name: "UNAL Ancizar Sans"` to METADATA.pb

## Conclusion

The source metadata for Ancizar Sans is **complete**. The repository URL, commit hash, config YAML path, and branch are all correctly recorded in METADATA.pb. The commit hash has been verified by comparing binary blob hashes between google/fonts and the upstream repo at the referenced commit -- they are identical. The config file exists at the specified path and contains a valid gftools-builder configuration for the Sans sources. No action is required.

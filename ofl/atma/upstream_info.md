# Atma

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Black Foundry
**METADATA.pb path**: `ofl/atma/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/BlackFoundryCom/Atma |
| Commit | `f805a3068057f9422e57427b4538c7d168684c7a` |
| Config YAML | — |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL was not present in the current METADATA.pb on the main branch. The copyright string references "www.black-foundry.com" and the upstream repo at `BlackFoundryCom/Atma` was already identified in the tracking data (`gfonts_library_sources.json`). A pending PR branch (`sources_info_2026-02-25`, commit `9a14639f3`) adds the source block with this URL and commit hash, but it has not yet been merged to main.

The repo was verified in the upstream cache at `upstream_repos/fontc_crater_cache/BlackFoundryCom/Atma` with remote URL `https://github.com/BlackFoundryCom/Atma`.

## How the Commit Hash Was Identified

The upstream repository has only a single commit: `f805a3068057f9422e57427b4538c7d168684c7a` (2016-04-21, "Update README.md"). The font was added to google/fonts via PR #945 (`d248fd36`, "hotfix-atma: v1.102 added", 2017-05-11) by Marc Foley. Since the upstream repo has only one commit and it predates the google/fonts onboarding, this commit is the only possible reference point. The fonts in google/fonts were likely compiled from these sources (or received directly from Black Foundry).

## How Config YAML Was Resolved

No `config.yaml` or `builder.yaml` exists in the upstream repository. No override `config.yaml` exists in `google/fonts/ofl/atma/`. The repo has UFO source files but lacks a designspace file and a gftools-builder configuration, so it cannot currently be built with gftools-builder without creating an override config.yaml.

## Verification

- Commit exists in upstream repo: Yes
- Commit date: 2016-04-21 18:48:49 +0200
- Commit message: "Update README.md"
- Source files at commit:
  - `Sources/Design/Atma.ufo` (base master)
  - `Sources/Design/Atma-Light.ufo`
  - `Sources/Design/Atma-ExtraBold.ufo`
  - `Sources/Design/AtmaInstanceTest.ufo`
  - `Sources/DesignBengali/Atma-Bold.ufo`
  - `Sources/DesignBengali/Atma-Light.ufo`
  - `Sources/Mastering/` (interpolation data, PS/TT mastering scripts)
  - Pre-compiled fonts in `Fonts/OTF/` and `Fonts/TTF/`

## Confidence

**Medium**: The repository URL and commit are correct (only one commit exists). However, there is no config.yaml and no designspace file in the repo, which means building with gftools-builder would require creating a designspace and a config.yaml override. The original fonts were likely built using the mastering scripts in `Sources/Mastering/` rather than gftools-builder. The UFO sources exist but the build process is non-standard.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - Sources/Mastering/TT/Atma-Light.ufo
  - Sources/Mastering/TT/Atma-Regular.ufo
  - Sources/Mastering/TT/Atma-Medium.ufo
  - Sources/Mastering/TT/Atma-SemiBold.ufo
  - Sources/Mastering/TT/Atma-Bold.ufo
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

- Would an override config.yaml with a new designspace be appropriate for this family, or should it be rebuilt from scratch with a proper gftools-builder setup?
- The repo has both Latin and Bengali UFO sources in separate directories. A designspace would need to incorporate both script sources correctly.

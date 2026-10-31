# Cabin - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Cabin |
| **Designer** | Impallari Type, Rodrigo Fuenzalida |
| **License** | OFL |
| **Date Added** | 2020-07-22 |
| **Repository URL** | https://github.com/impallari/Cabin |
| **Commit Hash** | `70efa8c3179359cc50b01ca184fec8a694156140` |
| **Branch** | N/A (defaults to master) |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Was Found

The repository URL `https://github.com/impallari/Cabin` was added in commit `cd5db6b6e` ("Update upstreams"), which added a `source { repository_url: "..." }` block to the METADATA.pb. The URL is also embedded in the font copyright string: "Copyright 2018 The Cabin Project Authors (https://github.com/impallari/Cabin)".

## How Commit Was Determined

The commit hash `70efa8c3179359cc50b01ca184fec8a694156140` is directly cited in the google/fonts onboarding commit for Cabin v3.001:

- **google/fonts commit**: `e0e68be37` ("cabin: v3.001 added (#2571)")
- **Commit message**: "Taken from the upstream repo https://github.com/impallari/Cabin/commit/70efa8c3179359cc50b01ca184fec8a694156140"
- **PR #2571**: Created by vv-monsalve, merged 2020-07-24. PR body also explicitly cites the same upstream commit URL.

This commit is also HEAD of the upstream repository's master branch (the latest and final commit). It is a merge commit dated 2020-07-22: "Merge pull request #24 from vv-monsalve/master" with parent commit "copyright fixed".

The v3.001 update was a major overhaul that converted Cabin from static fonts to a variable font with `wdth` (75-100) and `wght` (400-700) axes.

### Previous versions

- **v2.220** (PR #679, m4rc1e, merged 2017-05-01): Took fonts from upstream commit `9476ee6f5459ee37cf8462452f3e4640c3a48519`
- **v2.001** (PR #503, 2016)
- **v1.007** (earlier update)

## Config YAML Status

**No config.yaml exists** in the upstream repository at any commit, and no override config.yaml exists in the google/fonts family directory.

At the recorded commit, the source files are:
- `sources/CabinRegular.designspace`
- `sources/CabinItalic.designspace`
- `sources/CabinRegular_statics.designspace`
- `sources/CabinItalic_statics.designspace`
- `sources/CabinRegular_v3001.glyphs`
- `sources/CabinItalic_v3001.glyphs`
- `sources/build.sh` (custom build script)
- `sources/Cabin_stat_table.py`

The sources are in gftools-compatible formats (designspace + glyphs), but the original build used a custom `build.sh` script rather than gftools-builder. A config.yaml would need to be created to use gftools-builder with these sources.

## Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/impallari/Cabin/`
- **Commit hash**: Verified -- exists in the repo, is HEAD of master; explicitly cited in both the google/fonts commit message and PR #2571
- **Source files**: Designspace and Glyphs sources present at the recorded commit (gftools-compatible formats)
- **Font binary history**: VF fonts added in google/fonts via PR #2571 (vv-monsalve, 2020-07-24)

## Confidence Level

**HIGH** -- The repository URL and commit hash are thoroughly verified through multiple independent sources (commit message, PR body, copyright string). The missing_config status is accurate because no config.yaml exists in the upstream repo.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/CabinRegular.designspace
  - sources/CabinItalic.designspace
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Could a config.yaml override be created for the google/fonts family directory to enable gftools-builder builds from the existing designspace sources?
2. The upstream repo uses a custom `build.sh` with specialized steps (STAT table via Python script). Would a gftools-builder config.yaml be able to replicate this build process, or would additional tooling be needed?

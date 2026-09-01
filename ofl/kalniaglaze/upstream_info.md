# Kalnia Glaze — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kalniaglaze`
**Status**: complete

## Initial State

The METADATA.pb at `ofl/kalniaglaze/METADATA.pb` already contained a complete source block:

```
source {
  repository_url: "https://github.com/fridamedrano/Kalnia-Glaze"
  commit: "3338853e096724f548386c608d7c42c63c6c33bd"
  archive_url: "https://github.com/fridamedrano/Kalnia-Glaze/releases/download/v1.110/Kalnia-Glaze-v1.110.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "KalniaGlaze[wdth,wght].ttf"
    dest_file: "KalniaGlaze[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

No override `config.yaml` existed in the google/fonts family directory.

## Investigation

### Onboarding History

Kalnia Glaze was first onboarded to Google Fonts as Version 1.107 in commit `51543cfeb` (2024-04-10), merged via PR #7539. The gftools-packager commit message referenced upstream commit `65e7c785d950985a8936a35c8c525db44fb63965` ("v1.107 with reported fixes added", 2024-04-10).

The font was then updated to Version 1.110 in commit `d4c19446e` (2024-06-13), merged via PR #7864. The gftools-packager commit message referenced upstream commit `1da962604705abc74467d29d5ca74e0f371f7dd5` ("Article small fix", 2024-06-13).

### Commit Hash Analysis

The METADATA.pb currently contains commit `3338853e096724f548386c608d7c42c63c6c33bd`, which was set by the fontc_crater batch port commit `4ad8ac680` on 2025-03-31 ("[Batch 2/4] port info from fontc_crater targets list"). This commit also added `config_yaml: "sources/config.yaml"` to the source block.

The commit `3338853` ("Merge pull request #21 from fridamedrano/image-license", 2024-06-23) is the HEAD of the upstream repo's main branch. It is the latest commit, made 10 days after the v1.110 onboarding. The changes between the gftools-packager commit `1da9626` and `3338853` were purely documentation — social media images and an image license file. No source files (`sources/`) or font binaries (`fonts/`) were modified.

The original gftools-packager commit `1da9626` ("Article small fix") was itself a documentation-only commit, 2 commits after the actual version bump at `ba10a45` ("version number increased to 1.110"). The v1.110 tag points to `ba10a45`.

### Source Files and Config

The upstream repo at `sources/` contains:
- `KalniaGlaze.glyphs` — the Glyphs source file
- `config.yaml` — gftools-builder configuration
- `paints.py` — paint compiler script used in the build recipe

The `config.yaml` at `sources/config.yaml` is identical at all relevant commits (`ba10a45`, `1da9626`, `3338853`). It includes a custom recipe with `paintcompiler` step using `paints.py`, which is essential for building this color font.

### Upstream Repository State

The cached repo at `upstream_repos/fontc_crater_cache/fridamedrano/Kalnia-Glaze` was verified:
- Clean working tree, no local modifications
- Remote: `https://github.com/fridamedrano/Kalnia-Glaze`
- Branch: main, up to date with origin
- Tags: v1.105, v1.106, v1.107, v1.110
- Total commits: 126 (full history now available after unshallowing)

### Assessment of Current Commit Hash

The current commit `3338853` in METADATA.pb differs from the gftools-packager commit `1da9626` used during onboarding. However, since:
1. No source files or font binaries changed between `1da9626` and `3338853`
2. The `config.yaml` is identical at both commits
3. `3338853` is the HEAD of main, making it a natural reference point

The current hash is acceptable, though `1da9626` would have been the more precise onboarding commit. Both are functionally equivalent for build purposes.

## Actions Taken

- Verified the upstream repository URL is valid and accessible
- Unshallowed the cached repo to access full commit history (was previously depth-1)
- Verified config.yaml exists at `sources/config.yaml` in the upstream repo at both the onboarding commit and HEAD
- Confirmed the config.yaml content is identical across relevant commits
- Traced the complete onboarding history through google/fonts git log
- Verified no source or binary changes between gftools-packager commit and current METADATA.pb commit
- Confirmed the upstream repo is clean and synced

## Final State

The source block in METADATA.pb is complete and correct. All required fields are present:
- `repository_url` points to a valid upstream repo
- `commit` references a valid commit with identical sources/fonts to the onboarding commit
- `config_yaml` correctly points to `sources/config.yaml`
- `archive_url` points to the v1.110 release
- `branch` is set to "main"

No changes needed. Status: **complete**.

## Source Block

```
source {
  repository_url: "https://github.com/fridamedrano/Kalnia-Glaze"
  commit: "3338853e096724f548386c608d7c42c63c6c33bd"
  archive_url: "https://github.com/fridamedrano/Kalnia-Glaze/releases/download/v1.110/Kalnia-Glaze-v1.110.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "KalniaGlaze[wdth,wght].ttf"
    dest_file: "KalniaGlaze[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

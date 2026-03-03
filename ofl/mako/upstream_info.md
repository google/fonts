# Mako — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/MakoFont"
  commit: "f1365c6fd308090395e543858ce9c8520061c913"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Mako-Regular.ttf"
    dest_file: "Mako-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

**Repository**: https://github.com/googlefonts/MakoFont
**Created**: 2023-07-12
**Last pushed**: 2025-02-25
**Default branch**: master

The repository contains a single font family (Mako) with sources in both `.glyphs` and `.ufo` format:

- `sources/Mako.glyphs` — Glyphs source file
- `sources/Mako-Regular.ufo/` — UFO source directory
- `sources/config.yaml` — gftools-builder configuration (added in the force-push)
- `fonts/ttf/Mako-Regular.ttf` — Pre-built binary
- `fonts/otf/Mako-Regular.otf` — Pre-built OTF binary
- `fonts/webfonts/Mako-Regular.woff2` — Pre-built webfont

The `config.yaml` contains:
```yaml
sources:
  - Mako.glyphs
```

### Repository History Issue

The repository currently has only **one commit**: `f1365c6` ("Add sources/config.yaml") dated 2025-02-25, authored by Felipe Sanches. This is the result of a **force-push** that replaced the original commit history.

The original commit chain (still accessible as dangling objects on GitHub) consisted of multiple commits by Emma Marichal on 2023-07-27:

1. `52b0604` — "added missing glyphs" (2023-07-27T15:03:17Z)
2. `c1e9eb3` — "math spacing / small fixes" (2023-07-27T15:25:27Z)
3. `de7bec3` — "updated features / font infos / small fixes" (2023-07-27T15:41:16Z)
4. `493c853` — "Fonts exported and tested" (2023-07-27T15:41:52Z) — **original onboarding commit**

The original onboarding commit `493c853` had the same directory structure as `f1365c6`, except it did **not** include `sources/config.yaml`. The force-push in February 2025 squashed the history and added the config file.

## Onboarding History

1. **Initial addition**: The font was initially added to google/fonts on 2011-05-11 (commit `90abd17b4`).

2. **gftools-packager update (PR #6565)**: On 2023-07-27, Emma Marichal submitted PR #6565, which updated the font using gftools-packager. The commit message stated: "Mako Version 1.100; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.33] taken from the upstream repo https://github.com/googlefonts/MakoFont at commit https://github.com/googlefonts/MakoFont/commit/493c8535e2ae836eea478f167b7c05755818360f." PR was merged on 2023-08-01 by Rosalie Wagner.

3. **upstream.yaml merge** (commit `66f91f1`): On 2024-04-03, Simon Cozens merged upstream.yaml data into METADATA.pb, adding the `files` and `branch` fields to the source block.

4. **Batch 2/4 update** (commit `4ad8ac6`): On 2025-03-31, Felipe Sanches updated the source block as part of a batch import from fontc_crater targets. This changed the commit hash from `493c853` to `f1365c6` and added `config_yaml: "sources/config.yaml"`.

## Build Configuration

The `sources/config.yaml` file exists at the current commit `f1365c6` in the upstream repo:
```yaml
sources:
  - Mako.glyphs
```

This config was added as part of the force-push on 2025-02-25. The original onboarding commit (`493c853`) did **not** have a `config.yaml` file.

## Findings

1. **Commit hash discrepancy**: The METADATA.pb currently points to `f1365c6`, which is a force-pushed commit from February 2025 that replaced the entire repository history. The **actual onboarding commit** was `493c853` (Emma Marichal, "Fonts exported and tested", 2023-07-27), which is now a dangling commit on GitHub.

2. **Binary match confirmed**: The `fonts/ttf/Mako-Regular.ttf` file in the upstream repo at `f1365c6` is byte-identical to the one in google/fonts (SHA-256: `660904f61bb44671dd8f5029bf179f82c7f78daa1c250c7dadb5927f1f1ef816`). Since the force-push preserved the binary, this is consistent.

3. **Force-push rationale**: The force-push appears to have been done specifically to add `sources/config.yaml` to the repo. However, this destroyed the original commit history, making the original onboarding hash `493c853` unreachable through normal git operations (though it remains accessible via the GitHub API as a dangling object).

4. **Current commit is valid but misleading**: While `f1365c6` does contain the correct font binaries and now includes `config.yaml`, it was not the commit used for onboarding. The correct onboarding commit was `493c853`, which the Batch 2/4 update overwrote.

5. **The config_yaml field is correct**: Since the `config.yaml` exists at `sources/config.yaml` in the current commit (`f1365c6`), and this is the commit referenced in METADATA.pb, the `config_yaml` field is internally consistent — but it only works because the commit hash was changed to the force-pushed version.

6. **Recommendation**: Since the repo was force-pushed to include `config.yaml` and the binaries match, the current METADATA.pb is functionally correct for the `f1365c6` commit. However, the original onboarding commit `493c853` should be documented for historical accuracy. The current state is a pragmatic choice — using the newer commit that includes `config.yaml` rather than the original commit that did not have it.

## Recommended Source Block

The current source block is functionally correct for the force-pushed state of the repo. No changes are needed:

```
source {
  repository_url: "https://github.com/googlefonts/MakoFont"
  commit: "f1365c6fd308090395e543858ce9c8520061c913"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Mako-Regular.ttf"
    dest_file: "Mako-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

**Note**: If the goal is to restore historical accuracy, the commit should revert to `493c8535e2ae836eea478f167b7c05755818360f` (the true onboarding commit), and either an override `config.yaml` should be placed in the google/fonts family directory, or the `config_yaml` field should be removed (since it did not exist at that commit). However, the current approach of using the force-pushed commit is a workable alternative, as the binary output is identical and `config.yaml` is available.

# Labrada — Investigation Report

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete
**Confidence**: HIGH

## Summary

Labrada is a serif typeface family designed by Mercedes Jáuregui (Omnibus-Type). It was onboarded to Google Fonts via PR #5799 on 2023-01-20 by Emma Marichal, using gftools-packager. The METADATA.pb source block was already fully populated with the correct repository URL, commit hash, and config_yaml path. All data was verified and found to be accurate.

## METADATA.pb Source Block (Pre-existing)

The source block in METADATA.pb contained the following fields:

```
source {
  repository_url: "https://github.com/Omnibus-Type/Labrada"
  commit: "b15424f8840bda81f5dfa88f97bb634598faeadc"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Labrada-Italic[wght].ttf"
    dest_file: "Labrada-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Labrada[wght].ttf"
    dest_file: "Labrada[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository URL

**URL**: https://github.com/Omnibus-Type/Labrada
**Status**: Valid. The upstream repository was found cached at `upstream_repos/fontc_crater_cache/Omnibus-Type/Labrada/` and the remote URL matched.

The copyright string in METADATA.pb also confirmed the repository URL: `"Copyright 2022 The Labrada Project Authors (https://github.com/Omnibus-Type/Labrada)"`.

## Commit Hash Verification

**Commit**: `b15424f8840bda81f5dfa88f97bb634598faeadc`
**Commit date**: 2023-01-18
**Commit message**: "Merge pull request #2 from emmamarichal/main"

This commit was the HEAD of the `main` branch at the time of onboarding. The upstream repository had only this single commit on the main branch, meaning there were no additional commits after the referenced hash.

### Binary file verification

Both font binaries in google/fonts matched their counterparts in the upstream repo at the referenced commit (identical MD5 checksums):

- `Labrada[wght].ttf`: `365f3ea51d857848b45c46ed7e3d1706` (match)
- `Labrada-Italic[wght].ttf`: `f8bacf6322f662b06e14ce9a0690fb87` (match)

This confirmed that the fonts in google/fonts were taken directly from the upstream repo's `fonts/variable/` directory at commit `b15424f`, not rebuilt from sources.

### Timeline

- **2023-01-18**: Upstream commit `b15424f` merged (PR #2 by emmamarichal)
- **2023-01-19**: Emma Marichal created the onboarding commit in google/fonts via gftools-packager
- **2023-01-20**: PR #5799 merged by Marc Foley into google/fonts

The commit hash was explicitly referenced in the gftools-packager commit message: "Labrada Version 1.000 taken from the upstream repo https://github.com/Omnibus-Type/Labrada at commit [...]/commit/b15424f8840bda81f5dfa88f97bb634598faeadc".

## Config YAML

**Path**: `sources/config.yaml` (in the upstream repo)
**Location**: `upstream_repos/fontc_crater_cache/Omnibus-Type/Labrada/sources/config.yaml`

The config.yaml was a valid gftools-builder configuration referencing two Glyphs source files:

```yaml
sources:
  - Labrada.glyphs
  - Labrada-Italic.glyphs
axisOrder:
  - wght
familyName: "Labrada"
```

The full config also included STAT table definitions for weight axis values (Thin through Black) for both the Roman and Italic variable fonts.

No override `config.yaml` existed in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly pointed to the upstream file at `sources/config.yaml`.

## Source Block History

The source block was assembled across multiple commits in google/fonts:

1. **Commit `5ecbfea`** (2023-01-19): Original onboarding via gftools-packager. Created the initial METADATA.pb with `repository_url` and `commit` fields inside a basic `source {}` block (via the accompanying `upstream.yaml`).
2. **Commit `66f91f1`** (2024-04-03): Simon Cozens' automated "Merge upstream.yaml into METADATA.pb" added the `files {}` mappings and `branch: "main"` to the source block.
3. **Commit `4ad8ac6`** (2025-03-31): Felipe Sanches' "[Batch 2/4] port info from fontc_crater targets list" added the `config_yaml: "sources/config.yaml"` field.

## Conclusion

The Labrada source block in METADATA.pb was already complete and accurate. All three key fields — `repository_url`, `commit`, and `config_yaml` — were present and verified:

- The repository URL pointed to a valid upstream repo
- The commit hash matched the exact commit used for onboarding (confirmed by binary file comparison and gftools-packager message)
- The config_yaml path pointed to a valid gftools-builder config in the upstream repo
- No additional upstream commits existed after the referenced hash

No changes were needed.

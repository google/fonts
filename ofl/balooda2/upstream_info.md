# Baloo Da 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Ek Type

## Source Data

| Field            | Value |
|------------------|-------|
| Repository URL   | https://github.com/yanone/Baloo2-Variable |
| Commit           | `ffd6308743a5829fe6980ce86f5629ba0250df98` |
| Config YAML      | `builder/BalooDa2.yaml` |
| Branch           | `master` |

## Repository URL

The METADATA.pb `repository_url` field pointed to `https://github.com/yanone/Baloo2-Variable`. This was confirmed as the correct upstream repository. The copyright line in METADATA.pb referenced `https://github.com/EkType/Baloo2`, which was the original source by Ek Type, but the fonts were rebuilt from the Yanone fork for the variable font version. The remote URL of the cached repository matched the METADATA.pb value.

## Commit Verification

The commit `ffd6308743a5829fe6980ce86f5629ba0250df98` was recorded in METADATA.pb and was explicitly referenced in the gftools-packager message in google/fonts commit `9104fa8b6` (PR #3980, merged 2021-11-25):

> Baloo Da 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/ffd6308743a5829fe6980ce86f5629ba0250df98.

The commit itself (`ffd6308`, authored 2021-11-19 by Yanone) was titled "Update BalooChettan2[wght].ttf" and only modified the BalooChettan2 binary. However, this was the HEAD of the repository at the time of onboarding, and the BalooDa2 binary had been updated one commit earlier (`ad6a1b1`, same date, same author). The gftools-packager tool used the repository HEAD rather than the specific BalooDa2 commit, which was standard practice.

Binary blob verification confirmed an exact match: the `BalooDa2[wght].ttf` blob hash at commit `ffd6308` in the upstream repo (`2a4e952b1c9d98dd814f22b919f36742df446ce8`) was identical to the blob hash in google/fonts HEAD. This confirmed the commit was correct.

Three commits existed after `ffd6308` on master (a merge, a copyright file addition, and a 2022-09-09 regeneration of fonts as v1.701), but all postdated the google/fonts merge and were not relevant to this onboarding.

## Config YAML

The config file `builder/BalooDa2.yaml` existed at the referenced commit. Its contents were:

```yaml
sources:
  - ../sources/BalooDa2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

The source file `sources/BalooDa2.glyphs` was confirmed to exist at the referenced commit. The config was a valid gftools-builder configuration for building the variable font. No override config.yaml was present in the google/fonts family directory, and none was needed since the upstream repo already contained the config.

## Conclusion

All source metadata was complete and verified. The repository URL, commit hash, and config_yaml path were all correct in METADATA.pb. The binary blob hash matched exactly between the upstream commit and google/fonts, confirming the commit was the correct onboarding reference. The source block (added by Felipe Sanches in commit `3524a1dc7` on 2025-09-24) accurately captured the original onboarding data from PR #3980.

**Confidence: HIGH**

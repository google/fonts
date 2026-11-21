# Baloo Bhai 2

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: COMPLETE
- **Designer**: Ek Type

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/yanone/Baloo2-Variable |
| commit           | da523dfa21aa0e376253d61c21e39146dc55702a |
| config_yaml      | builder/BalooBhai2.yaml |
| branch           | master |

## Repository URL

The METADATA.pb `repository_url` points to `https://github.com/yanone/Baloo2-Variable`. This is a dedicated repository maintained primarily by Yanone (post@yanone.de) with contributions from Girish Dalvi (girish.dalvi@iitb.ac.in). The copyright notice references `https://github.com/EkType/Baloo2`, which is the original Baloo project, but the Variable font update was done in the yanone fork. The repo contains all ten Baloo 2 Variable families (Baloo 2, Baloo Bhai 2, Baloo Bhaijaan 2, Baloo Bhaina 2, Baloo Chettan 2, Baloo Da 2, Baloo Paaji 2, Baloo Tamma 2, Baloo Tammudu 2, Baloo Thambi 2).

The cached clone at `upstream_repos/fontc_crater_cache/yanone/Baloo2-Variable` is clean and the remote matches the METADATA.pb URL.

## Commit Verification

The referenced commit `da523dfa` (2021-10-28, "Update BalooTammudu2[wght].ttf") is the tip of a batch of font binary updates pushed on the same day. While this specific commit only modifies BalooTammudu2, the BalooBhai2 binary was updated in commit `27837c9` ("Update BalooBhai2[wght].ttf", 2021-10-28), which is an ancestor of `da523df`.

**Binary verification**: The BalooBhai2[wght].ttf file at commit `da523df` in the upstream repo has MD5 hash `47fa2bd8c8c1cc56f919e63fb0b38bd7`, which matches exactly the file in `ofl/baloobhai2/BalooBhai2[wght].ttf` in google/fonts. This confirms that `da523df` is the correct commit reference.

The google/fonts commit `29d0f91` ("Baloo Bhai 2: Version 1.700 added (#3982)", 2021-11-03) explicitly references this commit via gftools-packager:

> Baloo Bhai 2 Version 1.700 taken from the upstream repo https://github.com/yanone/Baloo2-Variable at commit https://github.com/yanone/Baloo2-Variable/commit/da523dfa21aa0e376253d61c21e39146dc55702a.

Note: There are later commits in the upstream repo after `da523df` (including kerning fixes in PR #3 and a 1.701 regeneration in 2022-09-09), but these have NOT been incorporated into google/fonts. The binary in google/fonts matches exactly the state at `da523df`.

## Config Verification

The config file `builder/BalooBhai2.yaml` exists at the referenced commit and contains:

```yaml
sources:
  - ../sources/BalooBhai2.glyphs
outputDir: "../fonts"
buildTTF: false
buildOTF: false
buildWebfont: false
buildVariable: true
```

This is a valid gftools-builder configuration. The referenced source file `sources/BalooBhai2.glyphs` also exists at the commit. No override config.yaml exists in the google/fonts family directory.

## Conclusion

All source metadata is correct and verified:

- **Repository URL**: Confirmed valid, matches cached clone remote.
- **Commit hash**: Confirmed correct. Binary hash matches between upstream at `da523df` and google/fonts. The gftools-packager message explicitly references this commit.
- **Config path**: `builder/BalooBhai2.yaml` exists at the referenced commit with valid gftools-builder configuration.
- **Branch**: `master` (confirmed as the only branch in the repo).

**Status**: COMPLETE -- no changes needed to METADATA.pb.

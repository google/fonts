# Noto Serif NP Hmong — Upstream Source Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | https://github.com/notofonts/nyiakeng-puachue-hmong |
| Commit | `2c945bb9c314d607d45c3120fcb35701349d9c87` |
| Version | 1.001 |
| Onboarding PR | [google/fonts#5609](https://github.com/google/fonts/pull/5609) |
| Date | 2022-11-25 |

## Investigation Summary

Noto Serif NP Hmong v1.001 was onboarded via PR #5609. The binary was taken from a GitHub release attachment associated with the `NotoSerifNPHmong-v1.001` tag at commit `2c945bb9c314d607d45c3120fcb35701349d9c87` in the notofonts/nyiakeng-puachue-hmong repository. This is a tag-based release where the font binary is distributed as a release asset rather than being committed directly to the repository tree.

This commit corresponds to the NotoSerifNPHmong-v1.001 release tag in the notofonts/nyiakeng-puachue-hmong repository. The binary was taken from the GitHub release attachment for this tag, as confirmed by PR #5257.

**Note**: NotoSerifNPHmong-v1.001 tag. Binary from GitHub release attachment.

**Confidence**: HIGH (tag-verified)

## Build Configuration

An override `config.yaml` has been created in the google/fonts family directory, copied from `sources/config-serif-nyiakeng-puachue-hmong.yaml` in the `notofonts/nyiakeng-puachue-hmong` repository. This config references the same repo and commit as the METADATA.pb source block, and the `config_yaml` field has been set accordingly. This is the correct build configuration for reproducing the shipped binary.

# Are You Serious

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: Complete
- **Designer**: Robert Leuschke
- **Date added to Google Fonts**: 2021-08-27

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| repository_url   | https://github.com/googlefonts/are-you-serious                    |
| commit           | 2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8                          |
| config_yaml      | sources/config.yml                                                 |
| branch           | master                                                             |
| Status           | Complete                                                           |
| Confidence       | HIGH                                                               |

## How URL Found

The repository URL `https://github.com/googlefonts/are-you-serious` was already present in METADATA.pb, originally added by Simon Cozens in commit `f7455d788` (2023-08-15, "Populate source.repository_url"), and later expanded with file mappings in commit `66f91f10f` (2024-04-03, "Merge upstream.yaml into METADATA.pb").

The URL is also confirmed by the onboarding commit messages in google/fonts (PRs #3776 and #3853), both of which explicitly reference this upstream repo.

## How Commit Identified

The commit `2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8` was added to METADATA.pb in commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"), sourced from fontc_crater's target.json.

### Verification

The upstream repo has only a single commit (`2975e6b`, "Name fixed", 2021-09-16 by Viviana Monsalve). This is the initial (and only) commit in the repository, which contains all source files, built fonts, and configuration.

The font was onboarded to google/fonts in two PRs:

1. **PR #3776** (commit `b6f5c2bd7`, 2021-08-31): Initial onboarding. Referenced upstream commit `21eb86d2baf500684d3b8600bc53f6ce27721495`, which no longer exists in the upstream repo. This added the .ttf file and all metadata files.

2. **PR #3853** (commit `d586f4d8e`, 2021-09-17): Follow-up that only modified `DESCRIPTION.en_us.html`. This referenced commit `2975e6bae2dba4fa1e30e9cd0b210e3a47b478d8` (the current and only commit in the repo).

The fact that PR #3776 referenced a commit (`21eb86d`) that no longer exists, and that the repo now has only a single commit (`2975e6b`) dated 2021-09-16, strongly indicates the upstream repo was force-pushed/rebased between the two PRs. The commit `2975e6b` ("Name fixed") likely squashed or replaced the earlier history.

**Binary verification**: The SHA-256 hash of `AreYouSerious-Regular.ttf` in google/fonts matches the file at commit `2975e6b` in the upstream repo exactly (`e2f61a166f382d7031ce750fe31d9a6d009a7dc8b63aafe4feff65e5cb4b3874`). File size is 150,788 bytes in both locations.

Since the repo has only one commit and the binaries match, `2975e6b` is confirmed as the correct reference commit.

## How Config Resolved

The upstream repo contains `sources/config.yml` at commit `2975e6b`:

```yaml
sources:
  - AreYouSerious.glyphs
familyName: "Are You Serious"
buildVariable: false
autohintTTF: false
```

This is a valid gftools-builder configuration pointing to the Glyphs source file. The `config_yaml` field in METADATA.pb is correctly set to `sources/config.yml`. Note the `.yml` extension (not `.yaml`).

No override config.yaml is needed in the google/fonts family directory since the upstream repo already has one.

## Conclusion

All source metadata for Are You Serious is complete and verified:

- **Repository URL**: Correct, points to `googlefonts/are-you-serious`
- **Commit hash**: `2975e6b` is the only commit in the repo and the binary matches exactly
- **Config**: `sources/config.yml` exists in the upstream repo with valid gftools-builder configuration
- **No action needed**: METADATA.pb is fully populated with correct data

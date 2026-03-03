# AR One Sans

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: Niteesh Yadav
- **Date Added**: 2023-09-06

## Source Data

| Field            | Value |
|------------------|-------|
| repository_url   | https://github.com/niteeshy/ar-one-sans |
| commit           | 6dc5e6850f2ced9f28e733c9a7860c54246e17a8 |
| branch           | main |
| config_yaml      | sources/config.yaml |

## How URL Found

The repository URL `https://github.com/niteeshy/ar-one-sans` was already present in METADATA.pb from the original onboarding commit (`29abece3f`, 2023-09-06) by Viviana Monsalve using gftools-packager. The commit message explicitly states: "taken from the upstream repo https://github.com/niteeshy/ar-one-sans". The URL is also embedded in the font copyright string. The remote URL in the cached repo confirms it is valid and accessible.

## How Commit Identified

The original onboarding commit message (google/fonts `29abece3f`) referenced upstream commit `a463b112ca9393f1904765e0f32891b849eb9cf1`. However, this commit no longer exists in the upstream repository. The repo has only a single commit (`6dc5e68`, dated 2024-04-14), indicating the repository was force-pushed/rebased at some point after onboarding, squashing all history into one commit.

The current METADATA.pb commit hash `6dc5e6850f2ced9f28e733c9a7860c54246e17a8` was set by the "Batch 1/4" commit (`19cdcec5`, 2025-03-31) which ported data from fontc_crater's target.json. This replaced the original (now-orphaned) hash with the current HEAD of the repo.

Binary verification confirms the font file at the current commit matches google/fonts exactly:
- `fonts/variable/AROneSans[ARRR,wght].ttf` SHA-256: `235b1352c58fb6d9763d74711d7c2e1d726d805fc04cad8fde2f56a469566b5f` (identical in both repos)

Since the repo was force-pushed to a single commit and the binary matches, the current commit hash `6dc5e68` is the correct reference for the current state of the upstream repo.

## How Config Resolved

The upstream repo contains `sources/config.yaml` with gftools-builder configuration:
- Source: `AROneSans.glyphs`
- Axis order: ARRR, wght
- Family name: AR One Sans
- STAT table entries defined for both axes

The `config_yaml` field was added by the "Batch 1/4" commit, sourced from fontc_crater's target.json. The config file exists at the referenced commit. No local override config.yaml is needed.

## Google Fonts Commit History

| Date | Hash | Description |
|------|------|-------------|
| 2023-09-06 | `29abece3f` | Initial onboarding via gftools-packager (Viviana Monsalve), PR #6662 |
| 2023-09-06 | `12523465a` | Removed primary_script "Zinh" field |
| 2023-09-07 | `e8dbd6924` | Removed target_blank |
| 2023-10-20 | `2c8a9578c` | Updated DESCRIPTION.en_us.html |
| 2024-04-03 | `66f91f10f` | Merged upstream.yaml into METADATA.pb (added files/branch) |
| 2025-03-31 | `19cdcec59` | Batch 1/4: updated commit hash and added config_yaml |

## Conclusion

All source metadata fields are complete and verified:
- **repository_url**: Correct, matches onboarding records and copyright string
- **commit**: `6dc5e68` is the only commit in the repo (force-pushed); binary file matches google/fonts exactly
- **config_yaml**: `sources/config.yaml` exists in upstream with valid gftools-builder configuration
- **Note**: The original onboarding commit `a463b112` no longer exists due to a force-push of the upstream repo. The current commit `6dc5e68` contains identical font binaries and is the correct reference.

No action needed. Source block is complete.

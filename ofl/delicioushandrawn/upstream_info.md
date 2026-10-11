# Delicious Handrawn - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Delicious Handrawn |
| Designer | Agung Rohmat |
| License | OFL |
| Repository URL | https://github.com/alphArtype/Delicious-Handrawn |
| Commit Hash (in METADATA.pb) | 454896185708d68530577800804c032756040370 |
| Correct Onboarding Commit | 0a9b42f98d6f2ee40563a406b1cdd9bb5a58fe57 |
| Branch | main |
| Config YAML | sources/config.yaml |
| Status | complete (but commit hash is incorrect) |
| Date Added | 2023-01-06 |

## How URL Found

The repository URL `https://github.com/alphArtype/Delicious-Handrawn` is documented in the METADATA.pb source block, the copyright string, and all three gftools-packager PRs.

## How Commit Determined

### Onboarding History

Three versions were onboarded via gftools-packager:

1. **v1.000** - Initial add (commit 8c3135f0b, 2023-01-06)
   - Upstream commit: `b4bc06828c04da4ef07518386cc77bbdfdba1e20`

2. **v1.001** - Update (commit 46f8f535f, 2023-02-15)
   - Upstream commit: `d32722cd629ea4d6f48c63d5f4387a9441db3c6c`

3. **v1.002** - Latest update, PR #6068 by emmamarichal (commit 0f70b3d62, 2023-03-23)
   - Upstream commit: `0a9b42f98d6f2ee40563a406b1cdd9bb5a58fe57`
   - This is the commit from which the current fonts in google/fonts were built

### Commit Hash Discrepancy

The METADATA.pb currently contains commit `454896185708d68530577800804c032756040370`, which is the HEAD of the upstream repo (a merge commit "Merge pull request #5 from sursly/main" from 2024-04-21). This is **newer** than the actual onboarding commit.

This incorrect commit was introduced in commit `19cdcec59` ("Batch 1/4: port info from fontc_crater targets list", 2025-03-31), which replaced the correct commit `0a9b42f` with `4548961` based on fontc_crater's target.json data. The fontc_crater target list appears to track the latest upstream state rather than the exact onboarding commit.

The correct onboarding commit should be `0a9b42f98d6f2ee40563a406b1cdd9bb5a58fe57` as documented in PR #6068.

## Config YAML Status

- `sources/config.yaml` exists in the upstream repository:
  ```yaml
  sources:
    - Delicious-Handrawn.glyphs
  familyName: Delicious Handrawn
  buildVariable: false
  ```
- The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml`
- No override config.yaml in google/fonts (not needed)

## Verification

- Repository URL is valid and accessible
- Upstream repo cloned at `upstream_repos/fontc_crater_cache/alphArtype/Delicious-Handrawn/` (shallow clone)
- Current HEAD (`4548961`) is newer than the onboarding commit (`0a9b42f`)
- The config.yaml exists at `sources/config.yaml` in the upstream repo
- Source file `Delicious-Handrawn.glyphs` referenced in config exists in `sources/` directory

## Confidence Level

**High** for repository URL and config_yaml. **High** that the correct onboarding commit should be `0a9b42f` (clearly documented in PR #6068), and that `4548961` in METADATA.pb is incorrect (introduced by batch fontc_crater port).

## Open Questions

- The commit hash in METADATA.pb should be corrected from `454896185708d68530577800804c032756040370` to `0a9b42f98d6f2ee40563a406b1cdd9bb5a58fe57` to reflect the actual onboarding commit used in PR #6068.
- The newer commit `4548961` (2024-04-21) may contain source changes that haven't been reviewed for Google Fonts yet.

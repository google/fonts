# Investigation: Edu AU VIC WA NT Pre

## Family Overview

- **Family name**: Edu AU VIC WA NT Pre
- **Display name**: Edu Australia VIC WA NT Hand Precursive
- **Designer**: Tina Anderson, Corey Anderson
- **License**: OFL
- **Category**: HANDWRITING
- **Date added**: 2024-08-12
- **Variable axes**: wght (400-700)

## Source Block Status

**Already has source block**: Yes (complete with repository_url, commit, archive_url, files, branch, config_yaml)

## Upstream Repository

- **Repository URL**: https://github.com/SorkinType/VICWANTSchoolhandAustralia
- **Cached at**: upstream_repos/fontc_crater_cache/SorkinType/VICWANTSchoolhandAustralia
- **Repository status**: Clean, up to date with origin
- **Source files**: `sources/AuVICWANT.glyphs` (single Glyphs source)
- **Config**: `sources/config.yaml` using `fontprimer` recipe provider
- **Shared repo**: This upstream repo serves ALL five Edu AU VIC WA NT family variants (Hand, Arrows, Dots, Guides, Pre). A single `.glyphs` source is built into multiple font families using the `variants` system in config.yaml.

## Config.yaml Analysis

The config.yaml uses `recipeProvider: fontprimer` with a `variants` system. The Pre (Precursive) variant is defined as:

```yaml
- name: Precursive
  alias: Pre
  steps:
    - operation: remapLayout
      args: "'ss01=>ccmp'"
```

The Precursive variant remaps stylistic set 1 (ss01) to the `ccmp` (Glyph Composition/Decomposition) feature, effectively making the precursive letterforms the default.

## Commit Hash Analysis

### Current METADATA.pb commit
- **Commit**: `6529c525fceb9ec15e51dfa6d87244ef053c2d8a`
- **Date**: 2024-12-04
- **Author**: Eben Sorkin
- **Message**: "corrected positions for lcaron, dcaron, tcaron and Lcaron in the various styles required for cursive and other stylistic varients"

### Important: Repo history was squashed
The upstream repo currently has only ONE commit (`6529c52`), dated 2024-12-04. All previous history was squashed into this single commit. The old commit hashes still exist as GitHub tags but are no longer reachable from any branch:

- **v1.000** tag -> `abab94d19985f24132e45db4c4822b042eb63302` (initial release, 2024-03-19)
- **v1.001** tag -> `88099a2e2d47e222cb62441730a2bc1c082754e1` (2024-04-30)
- **v1.002** tag -> `4d4efe710065410b34b66fa9d588498351642f41` (2024-10-11)

### Onboarding History in google/fonts

The Pre variant had the most revisions in its PR before merge:

1. **Initial onboarding**: Commit `598c0e2b` (2024-08-13, Simon Cozens) "Edu VIC WA NT Pre: Version 1.001 added". This commit added the font with commit hash `abab94d1` (v1.000 tag) and archive_url pointing to the v1.000 release. No explicit upstream commit reference in the commit message body.

2. **Update quote spacing and kerning**: Commit `ac132fec` (2024-09-11, Simon Cozens) -- font binary update.

3. **Update anchor positions**: Commit `8f0e4df5` (2024-09-27, Simon Cozens) -- font binary update.

4. **PR merge**: PR #8022, merged 2024-10-02 by Emma Marichal. The final binary (1,298,364 bytes) differs from the initial onboarding (1,286,528 bytes), indicating the font was rebuilt with corrections between August and September 2024.

5. **Batch update**: Commit `19cdcec5` (2025-03-31, Felipe Sanches) as part of "[Batch 1/4] port info from fontc_crater targets list" changed the commit hash from `abab94d1` (v1.000) to `6529c52` (current HEAD) and added `config_yaml: "sources/config.yaml"`.

### Archive URL inconsistency

The METADATA.pb currently references commit `6529c52` (post-squash HEAD) but the `archive_url` still points to the v1.000 release. However, the binary that was actually merged into google/fonts went through multiple rebuild iterations (quote spacing, anchor positions) in the PR, so it may not match the v1.000 release binary exactly. The final merged binary was likely built from a newer upstream state.

### Commit hash accuracy concern

The original METADATA.pb at onboarding used commit `abab94d1` (tag v1.000), but the font binary was updated twice within the PR (likely from newer upstream commits). The batch update changed the hash to `6529c52` (post-squash HEAD). Since the repo was force-pushed to squash history, `6529c52` is the only reachable commit.

## Verification Summary

| Field | Value | Status |
|-------|-------|--------|
| repository_url | https://github.com/SorkinType/VICWANTSchoolhandAustralia | Correct |
| commit | 6529c525fceb9ec15e51dfa6d87244ef053c2d8a | Acceptable (post-squash HEAD; original was abab94d1 / v1.000) |
| config_yaml | sources/config.yaml | Correct (exists in repo) |
| archive_url | v1.000 release | May not match final merged binary (binary was updated in PR) |
| branch | main | Correct |

## Status

- **Status**: complete
- **Confidence**: HIGH
- **Notes**: Source block is fully populated. The commit hash `6529c52` is the only commit in the (squashed) repo. The font binary went through multiple updates in PR #8022 (quote spacing, anchor positions) before merging. The archive_url still points to v1.000 which may not match the final binary. The config.yaml uses `fontprimer` recipe provider. No action needed.

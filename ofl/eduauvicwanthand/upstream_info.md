# Investigation: Edu AU VIC WA NT Hand

## Family Overview

- **Family name**: Edu AU VIC WA NT Hand
- **Display name**: Edu Australia VIC WA NT Hand
- **Designer**: Tina Anderson, Corey Anderson
- **License**: OFL
- **Category**: HANDWRITING
- **Date added**: 2024-05-02
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

The config.yaml uses `recipeProvider: fontprimer` with `familyName: Edu AU VIC WA NT Hand` and `shortFamilyName: Edu AU VIC WA NT`. The Hand variant is the base/default variant -- all other variants (Pre, Arrows, Dots, Guides) are derived from it through the `variants` list using stylistic set freezing and subsetting operations.

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

The Hand variant was the FIRST of the five to be onboarded, and has the most complex history:

1. **Initial onboarding**: Commit `4191cb9e` (2024-05-02, Simon Cozens) "Edu AU VIC WA NT Hand: Version 1.001 added". The commit body explicitly states: "Taken from the upstream repo https://github.com/SorkinType/VICWANTSchoolhandAustralia at commit https://github.com/SorkinType/VICWANTSchoolhandAustralia/commit/88099a2e2d47e222cb62441730a2bc1c082754e1." This matches the v1.001 tag.

2. **Update**: Commit `f391c677` (2024-05-03, Simon Cozens) "Update" -- updated DESCRIPTION, font binary, METADATA.pb, and OFL.txt.

3. **Fixes**: Commit `bf2234b6` (2024-05-09, Simon Cozens) "Fixes" -- font binary update only.

4. **Latest build (x3)**: Commits `a4d81d6c`, `cf4ce712`, `685295e6` (May-June 2024, Simon Cozens) -- incremental font binary updates.

5. **PR merge**: PR #7628, merged 2024-06-06 by Emma Marichal.

6. **Batch update**: Commit `19cdcec5` (2025-03-31, Felipe Sanches) as part of "[Batch 1/4] port info from fontc_crater targets list" changed the commit hash from `88099a2e` (v1.001) to `6529c52` (current HEAD) and added `config_yaml: "sources/config.yaml"`.

### Commit hash accuracy

The original onboarding explicitly referenced commit `88099a2e` (v1.001 tag). The font went through several iterations in the PR before merging. The batch update later changed the hash to `6529c52` (post-squash HEAD). The METADATA.pb `archive_url` correctly points to the v1.001 release, which aligns with the original onboarding commit.

## Verification Summary

| Field | Value | Status |
|-------|-------|--------|
| repository_url | https://github.com/SorkinType/VICWANTSchoolhandAustralia | Correct |
| commit | 6529c525fceb9ec15e51dfa6d87244ef053c2d8a | Acceptable (post-squash HEAD; original was 88099a2e / v1.001) |
| config_yaml | sources/config.yaml | Correct (exists in repo) |
| archive_url | v1.001 release | Correct for the original onboarding |
| branch | main | Correct |

## Status

- **Status**: complete
- **Confidence**: HIGH
- **Notes**: Source block is fully populated. This was the first of the five Edu AU VIC WA NT variants to be onboarded (2024-05-02 vs 2024-08-12 for the others). The commit hash `6529c52` is the only commit in the (squashed) repo. The archive_url points to v1.001 which matches the binary from the original onboarding by Simon Cozens. The config.yaml uses `fontprimer` recipe provider. No action needed.

# Investigation: Edu AU VIC WA NT Arrows

## Family Overview

- **Family name**: Edu AU VIC WA NT Arrows
- **Display name**: Edu Australia VIC WA NT Hand Arrows
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

The config.yaml uses `recipeProvider: fontprimer` with a `variants` system that produces different font families from a single source (`AuVICWANT.glyphs`). The Arrows variant is defined as:

```yaml
- name: Outline Arrows
  alias: Arrows
  steps:
    - operation: featureFreeze
      args: -f ss05
    - operation: exec
      args: --output-file=$out --unicodes=A0,20,30-39,61-7A,41-5A --notdef-outline --name-IDs=* --layout-features=* $in
      exe: hb-subset
```

The Arrows variant freezes stylistic set 5 (ss05) and subsets to a limited character set.

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

The Arrows variant went through several stages:

1. **First onboarding (as "Edu VIC WA NT Arrows")**: Initially onboarded under the directory `ofl/eduvicwantarrows/` with commit `abab94d1` (v1.000 tag). Merged via PR #7447 on 2024-08-15 by Viviana Monsalve.

2. **Rename and update**: Commit `69cc6cf7` (2024-08-13, Simon Cozens) renamed from `ofl/eduvicwantarrows/` to `ofl/eduauvicwantarrows/` and updated the font binary. The old METADATA.pb referenced `VICWANTSchoolHandAustralia` (uppercase H) which was corrected to `VICWANTSchoolhandAustralia`.

3. **Display name fix**: PR #8070, merged 2024-08-20 by Viviana Monsalve, fixed the `display_name` field.

4. **v1.001 update**: PR #8319, merged 2024-11-08 by Viviana Monsalve. Simon Cozens's commit (`22484892c`, 2024-10-11) updated the font binary and changed the commit hash from `abab94d1` (v1.000) to `4d4efe71` (v1.002) and archive_url to the v1.002 release. The commit message explicitly stated: "Taken from the upstream repo https://github.com/SorkinType/VICWANTSchoolhandAustralia at commit https://github.com/SorkinType/VICWANTSchoolhandAustralia/commit/4d4efe710065410b34b66fa9d588498351642f41."

5. **Batch update**: Commit `19cdcec5` (2025-03-31, Felipe Sanches) as part of "[Batch 1/4] port info from fontc_crater targets list" changed the commit hash from `4d4efe71` to `6529c52` and added `config_yaml: "sources/config.yaml"`.

### Commit hash accuracy concern

The current commit `6529c52` in METADATA.pb was set by the batch update on 2025-03-31. This is a post-onboarding squash commit from 2024-12-04 that consolidates all previous history. The original onboarding used commit `4d4efe71` (tag v1.002, from 2024-10-11) as referenced by Simon Cozens's explicit commit message. Since the upstream repo was force-pushed to squash history, the original commit is no longer reachable from any branch (though tags still reference it on GitHub). Using the current HEAD `6529c52` is reasonable since the repo has only one commit now, but the original commit was `4d4efe71`.

## Verification Summary

| Field | Value | Status |
|-------|-------|--------|
| repository_url | https://github.com/SorkinType/VICWANTSchoolhandAustralia | Correct |
| commit | 6529c525fceb9ec15e51dfa6d87244ef053c2d8a | Acceptable (post-squash HEAD; original was 4d4efe71) |
| config_yaml | sources/config.yaml | Correct (exists in repo) |
| archive_url | v1.002 release | Correct |
| branch | main | Correct |

## Status

- **Status**: complete
- **Confidence**: HIGH
- **Notes**: Source block is fully populated. The commit hash `6529c52` is the only commit in the (squashed) repo, so it is the most sensible value to reference. The config.yaml uses `fontprimer` recipe provider, which is not the standard `gftools-builder` but is the correct configuration for this font family. No action needed.

# Kumbh Sans — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kumbhsans`
**Status**: complete

## Initial State

METADATA.pb already contained a complete source block with:
- `repository_url`: `https://github.com/xconsau/KumbhSans`
- `commit`: `b1c41a8ff0916a5421bd3976c361f1980c0e7cfc`
- `branch`: `master`
- `config_yaml`: `sources/config.yaml`
- `files` mappings for the variable font and OFL.txt

No override `config.yaml` existed in the google/fonts family directory.

## Investigation

### Upstream Repository

The upstream repository at `https://github.com/xconsau/KumbhSans` was verified as accessible (HTTP 200). The cached clone at `upstream_repos/fontc_crater_cache/xconsau/KumbhSans` was clean and up-to-date with origin.

### Commit Hash Verification

The referenced commit `b1c41a8ff0916a5421bd3976c361f1980c0e7cfc` is the HEAD of the `master` branch. It is a merge commit: "Merge pull request #16 from RosaWagner/master", dated 2023-11-28.

This commit was introduced by the gftools-packager commit `4bd526bcb` in google/fonts ("Kumbh Sans: Version 1.005 added"), authored by Rosalie Wagner on 2023-11-29. The commit message explicitly states: "Kumbh Sans Version 1.005 taken from the upstream repo https://github.com/xconsau/KumbhSans at commit b1c41a8ff0916a5421bd3976c361f1980c0e7cfc."

The timeline is consistent: the upstream merge happened on 2023-11-28, and the google/fonts packager commit followed on 2023-11-29. Rosalie Wagner authored both the upstream PR and the google/fonts commit, providing strong provenance evidence.

### Source Block History

The source block was built incrementally across multiple commits:

1. **`30b43cbad`** (2022-12-07, PR #5667): Version 1.004 introduced the initial source block with `repository_url` and commit `07b9138758d865763846adab4ee02a3c45a30daa`. Also added the YOPQ axis.
2. **`4bd526bcb`** (2023-11-29, PR #7028): Version 1.005 updated the commit hash to `b1c41a8ff0916a5421bd3976c361f1980c0e7cfc`.
3. **`66f91f10f`** (2024-04-03): Upstream.yaml merge added `files` mappings and `branch: "master"`.
4. **`4ad8ac680`** (2025-03-31): Batch port from fontc_crater targets added `config_yaml: "sources/config.yaml"`.

### Config Verification

The upstream repository has `sources/config.yaml` at the referenced commit. It contains a valid gftools-builder configuration referencing `KumbhSans.designspace` with `buildOTF: false` and axis order `[YOPQ, wght]`, plus STAT table definitions.

Source files in the `sources/` directory include:
- `KumbhSans.designspace`
- Multiple `.ufo` directories (Regular, Thin, Black, and Display variants)
- `config.yaml`

### File Mappings Verification

The source block maps:
- `fonts/variable/KumbhSans[YOPQ,wght].ttf` → `KumbhSans[YOPQ,wght].ttf` (verified present at commit)
- `OFL.txt` → `OFL.txt` (verified present at commit)

## Actions Taken

No changes were needed. The source block is complete and all data was verified as correct.

## Final State

The source metadata for Kumbh Sans is fully complete with verified data:
- Repository URL: valid and accessible
- Commit hash: verified as correct (matches gftools-packager provenance, timeline consistent)
- Config: `sources/config.yaml` exists in upstream at referenced commit
- Files: all mappings verified
- Branch: `master` confirmed as default branch

**Confidence**: HIGH

## Source Block

```
source {
  repository_url: "https://github.com/xconsau/KumbhSans"
  commit: "b1c41a8ff0916a5421bd3976c361f1980c0e7cfc"
  files {
    source_file: "fonts/variable/KumbhSans[YOPQ,wght].ttf"
    dest_file: "KumbhSans[YOPQ,wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

# Freehand - Investigation Report

## Family Details

- **Family name**: Freehand
- **Designer**: Danh Hong
- **License**: OFL
- **Category**: DISPLAY
- **Primary script**: Khmr (Khmer)
- **Date added**: 2011-03-02
- **Path in google/fonts**: `ofl/freehand/`

## Source Metadata (Current METADATA.pb)

```
source {
  repository_url: "https://github.com/danhhong/Freehand"
  commit: "43c90b514cfa24587b118a4819d975459e1d7d6d"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Freehand-Regular.ttf"
    dest_file: "Freehand-Regular.ttf"
  }
  branch: "master"
}
```

## Upstream Repository

- **URL**: https://github.com/danhhong/Freehand
- **Status**: Valid and accessible
- **Default branch**: master
- **Cached at**: `upstream_repos/fontc_crater_cache/danhhong/Freehand`
- **Repo clean**: Yes (clean, up to date with origin)

### Upstream Commit History (all 7 commits)

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `43c90b5` | 2021-11-01 | Danh Hong | Merge pull request #3 from yanone/master |
| `d181650` | 2021-10-28 | Yanone | New binary |
| `cb68ecd` | 2021-10-28 | Yanone | Bumped version |
| `b855708` | 2021-10-28 | Yanone | Updated sidebearings |
| `99c5905` | 2021-06-07 | Danh Hong | Merge pull request #2 from yanone/master |
| `05ae11a` | 2021-04-16 | Yanone | Freehand ready for GF |
| `1275f91` | 2020-08-24 | khmertool | update |

### Repository Structure (at HEAD = `43c90b5`)

```
AUTHORS.txt
CONTRIBUTORS.txt
DESCRIPTION.en_us.html
OFL.txt
Release/ttf/Freehand-Regular.ttf
Source/builder.yaml
Source/Freehand.glyphs
```

### Build Configuration

`Source/builder.yaml` exists in the upstream repo:

```yaml
sources:
  - Freehand.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder config pointing to `Source/Freehand.glyphs`.

## google/fonts Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `aa120dd` | 2025-09-18 | Sources info: added commit hash and config_yaml to METADATA.pb |
| `4f5dbdb` | 2021-12-07 | PR #4152: Bumped to 8.002 (urgent glyph definition issues) |
| `3017cf8` | 2021-11-10 | PR #4021: Freehand v8.001 added (from upstream commit `43c90b5`) |
| `22560a2` | 2021-09-08 | PR #3510: Freehand v8.000 added (from upstream commit `99c5905`) |

## Commit Hash Verification

### PR #3510 (v8.000) -- Initial onboarding of new binary

- **gftools-packager hash**: `99c5905ced30852fb8b442b38355828de11bb5dd`
- Upstream binary at `99c5905`: 235,584 bytes
- google/fonts binary at `22560a2`: 235,584 bytes
- **Match**: Yes -- binary sizes are identical

### PR #4021 (v8.001) -- Update

- **gftools-packager hash**: `43c90b514cfa24587b118a4819d975459e1d7d6d`
- Upstream binary at `43c90b5`: 235,560 bytes
- google/fonts binary at `3017cf8`: 235,560 bytes
- SHA256 of upstream binary at `43c90b5`: `033e81fa370449e9b45644510162cfe099865aa1934dee468c79075e7703d2cf`
- SHA256 of google/fonts binary at `3017cf8`: `033e81fa370449e9b45644510162cfe099865aa1934dee468c79075e7703d2cf`
- **Match**: Yes -- SHA256 hashes match exactly

### PR #4152 (v8.002) -- Urgent glyph definition fix

- This was a batch update of 14 Khmer fonts by Yanone
- google/fonts binary at `4f5dbdb`: 235,540 bytes
- No corresponding upstream commit exists -- `43c90b5` is the latest upstream commit
- The fix addressed glyph definition issues where GSUB-substituted glyphs were not recognized as letters by Microsoft Edge
- The changes were made to the Glyphs sources locally and never pushed to the upstream repo

### Current State Mismatch

The current binary in google/fonts (235,540 bytes, SHA256: `3f2f1155d862304cf29cc4252aa5df4d47468d127c3c12cbf16894b0dda6c833`) does NOT match the binary at the METADATA.pb commit hash `43c90b5` (235,560 bytes, SHA256: `033e81fa370449e9b45644510162cfe099865aa1934dee468c79075e7703d2cf`).

The METADATA.pb commit hash `43c90b5` corresponds to the v8.001 update (PR #4021), but the current binary is from the v8.002 batch fix (PR #4152, merged 2021-12-07) which has no corresponding upstream commit. The v8.002 changes were made by Yanone locally and not pushed back to the `danhhong/Freehand` repository.

## Assessment

### Status: **complete** (with caveat)

The source metadata is as complete as it can be:

- **Repository URL**: Correct (`https://github.com/danhhong/Freehand`)
- **Commit hash**: `43c90b5` -- this is the latest commit in the upstream repo and was the commit used for PR #4021 (v8.001). However, the current binary in google/fonts is from a later batch fix (PR #4152, v8.002) that was never pushed upstream.
- **Config YAML**: `Source/builder.yaml` -- correct, exists in upstream at the referenced commit
- **Branch**: `master` -- correct

### Caveat: Post-onboarding binary modification

The current binary in google/fonts was produced by PR #4152 (2021-12-07), a batch fix for urgent Khmer glyph definition issues by Yanone. This PR modified the binary without a corresponding upstream commit. The upstream repo's latest commit (`43c90b5`, 2021-11-01) predates PR #4152, and there is no commit in the upstream repo that matches the current google/fonts binary.

This means the METADATA.pb `commit` field (`43c90b5`) is the best available reference -- it is the latest upstream commit -- but it does not correspond to the exact binary currently served. Rebuilding from `43c90b5` would produce v8.001, not the current v8.002.

### Confidence: **HIGH**

The commit hash `43c90b5` was explicitly referenced in PR #4021's gftools-packager message and verified via SHA256 hash comparison. The discrepancy with the current binary is well-documented through PR #4152's commit history.

### Key People

- **Danh Hong** (danhhong): Original designer, repository owner
- **Yanone** (yanone): Font engineer who performed all onboarding and updates (PRs #3510, #4021, #4152)
- **Rosalie Wagner** (RosaWagner): Merged all three PRs

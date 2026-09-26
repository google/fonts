# Investigation Report: Farro

## Family Details
- **Family name**: Farro
- **Designer**: Grayscale (Aceler Chua)
- **Category**: Sans-Serif
- **Date added**: 2019-07-17
- **Weights**: Light (300), Regular (400), Medium (500), Bold (700)
- **License**: OFL
- **Subsets**: latin, latin-ext, menu

## Upstream Repository
- **URL**: https://github.com/grayscaleltd/farro
- **Status**: Active, public
- **Owner**: Grayscale Limited (grayscaleltd)
- **Primary contributor**: Aceler Chua <hi@aclr.co>
- **Source files**: `sources/farro.glyphs` (Glyphs format)
- **Pre-compiled binaries**: `fonts/ttf/` (4 TTF files)

## Commit Hash Verification
- **Commit in METADATA.pb**: `fa80aadd0c61b6e76d95870579d0650f9d91df76`
- **Commit message**: "updated copyright notices according to #2, added AUTHOR and CONTRIBUTORS"
- **Commit date**: 2019-07-17 10:07:35 +0800
- **Commit author**: Aceler Chua
- **Is HEAD of master**: Yes (this is the latest commit on the only branch)

### Verification Evidence

1. **PR #2069** in google/fonts titled "farro: v1.101 added" by Marc Foley explicitly states:
   > Taken from the upstream https://github.com/grayscaleltd/farro at commit https://github.com/grayscaleltd/farro/commit/fa80aadd0c61b6e76d95870579d0650f9d91df76

2. **PR merged**: 2019-07-17 at 08:34 UTC, the same day the upstream commit was made (02:07 UTC).

3. **File size match**: All four TTF files in google/fonts have identical sizes to those in the upstream repo at this commit:
   - Farro-Bold.ttf: 68,004 bytes
   - Farro-Light.ttf: 68,252 bytes
   - Farro-Medium.ttf: 68,928 bytes
   - Farro-Regular.ttf: 68,588 bytes

4. **Version strings match**: Both google/fonts and upstream binaries report "Version 1.101".

5. **No subsequent upstream commits**: `fa80aad` is the HEAD of the master branch. No additional work has been done in the upstream repo since onboarding.

**Confidence**: HIGH -- The commit hash is explicitly documented in the onboarding PR body, file sizes match perfectly, and the commit is the latest in the repo.

## Build Configuration
- **config.yaml in upstream**: No
- **config.yaml in google/fonts**: Yes (override)
  ```yaml
  buildVariable: false
  sources:
    - sources/farro.glyphs
  ```
- **config_yaml in METADATA.pb**: Not set (correctly omitted since local override exists)

The override config.yaml was added in commit `e997cf9` (2025-10-30) by Felipe Sanches as part of the source metadata enrichment project. It references `sources/farro.glyphs`, the only source file in the upstream repo at the referenced commit.

## History in google/fonts

| Date | Commit | Author | Description |
|------|--------|--------|-------------|
| 2019-07-17 | `57a48fbb` | Marc Foley | Initial onboarding: "farro: v1.101 added" (PR #2069) |
| 2021-04-26 | `d0623a23` | Bruno Arueira | Fix incorrect file permissions |
| 2023-08-15 | `f7455d78` | Simon Cozens | Added `source.repository_url` to METADATA.pb |
| 2023-12-14 | `2423d2ae` | Simon Cozens | Same change re-applied in "Update upstreams" |
| 2025-10-30 | `e997cf9f` | Felipe Sanches | Added commit hash and override config.yaml |

## Request History
- **Issue #1533**: "Add Farro" opened by Dave Crossland, linking to the upstream repo and cc'ing @chakler (Aceler Chua's GitHub handle).

## Current METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/grayscaleltd/farro"
  commit: "fa80aadd0c61b6e76d95870579d0650f9d91df76"
}
```

## Status
- **Status**: complete
- **Repository URL**: Verified correct
- **Commit hash**: Verified correct (HEAD of master, explicitly referenced in PR #2069)
- **Config**: Override config.yaml present in google/fonts family directory
- **Confidence**: HIGH

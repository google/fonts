# Corben

## Source Data

| Field | Value |
|---|---|
| Family Name | Corben |
| Repository URL | https://github.com/librefonts/corben |
| Commit Hash | `94d5b00e6b64f85258d17e766a1e8e6d85554adc` |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/corben` is part of the librefonts GitHub organization, which hosts archival copies of early Google Fonts projects. The URL was already documented in the tracking data and matches the git remote of the cached upstream repo at `upstream_repos/fontc_crater_cache/librefonts/corben`.

## How Commit Determined

The upstream repository contains exactly **one commit**: `94d5b00e6b64f85258d17e766a1e8e6d85554adc` ("update .travis.yml"). Since this is the only commit in the repository, it is trivially the correct reference. The librefonts repos were created as archival snapshots of the font projects' state when they were onboarded to Google Fonts.

Note that unlike the other librefonts repos in this batch, Corben has had multiple font file modifications in google/fonts:
1. `90abd17b4` (2015-03-07) - Initial commit (added both Regular and Bold)
2. `bacec3651` - Fix fsType for 54 font files
3. `5b1755d5a` (2015-09-21) - "corben: Update to correct internal metadata" (modified both Bold and Regular)
4. `ee1e172ab` (2017-08-29) - "ofl/corben/Corben-Bold.ttf ttfautohinted" (PR #1180, modified Bold only)

The most recent font modification was the ttfautohint application in 2017, which was a post-processing step applied directly to the binary in google/fonts (not from the upstream source). The upstream librefonts repo is an archival snapshot and was not modified for these updates.

## Config YAML Status

**No config.yaml exists** in the upstream repository. The source files are:
- `src/Corben-Regular.sfd` (FontForge SFD format)
- `src/Corben-Regular-TTF.sfd` (FontForge SFD format)
- `src/Corben-Bold.sfd` (FontForge SFD format)
- `src/Corben-Bold-TTF.sfd` (FontForge SFD format)
- `src/Corben-Bold.vfb` (FontLab VFB format)

These are legacy font formats that are **not compatible with gftools-builder**. No override `config.yaml` exists in the google/fonts family directory either.

## Verification

- **Repository accessible**: Yes (verified via git remote URL)
- **Commit hash valid**: Yes - matches the only commit in the repo
- **Font files modified post-onboarding**: Yes - internal metadata fix and ttfautohint were applied directly in google/fonts
- **Source block in METADATA.pb**: Pending (exists on feature branch `sources_info_2026-02-25`, not yet merged to main)

## Confidence Level

**High** - Single-commit librefonts archival repository. The commit hash is unambiguous. The post-onboarding modifications (metadata fix and ttfautohint) were applied directly to binaries in google/fonts, not from the upstream source.

## Open Questions

None. The family has SFD-only sources and cannot be rebuilt with gftools-builder without a source format conversion.

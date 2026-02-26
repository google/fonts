# Contrail One - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Contrail One |
| Designer | Riccardo De Franceschi |
| Repository URL | https://github.com/librefonts/contrailone |
| Commit | 21ed60440130b6afcdd5e7555e9fe7c8c4344146 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/contrailone` was identified from the librefonts organization. The source block was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files") on the pending PR branch `sources_info_2026-02-25` (PR #10270). This PR has not yet been merged into main.

The current METADATA.pb on main does not have a source block. The copyright mentions Sorkin Type Co (Eben Sorkin) as the foundry.

## How Commit Determined

The commit `21ed60440130b6afcdd5e7555e9fe7c8c4344146` is the HEAD (and only commit in the shallow clone) of the `librefonts/contrailone` repository. The commit message is "update .travis.yml". This follows the standard librefonts repo pattern.

## Config YAML Status

No config.yaml exists in the upstream repository. The source files are:
- `src/ContrailOne-Regular-TTF.sfd` (FontForge SFD format)
- `src/ContrailOne-Regular.vfb` (FontLab VFB format)

These formats are not compatible with gftools-builder. No override config.yaml exists in the google/fonts family directory.

## Verification

- Repository URL returns HTTP 200 (inferred from successful git clone in cache)
- Commit hash matches the HEAD of the cached repo
- The font binary has never been updated since the initial commit and the deploy commit
- Added to Google Fonts on 2011-10-26
- No source block exists in the main branch METADATA.pb (pending PR #10270)

## Confidence Level

**High** for repository URL and commit hash.

**N/A** for config.yaml - the sources are in legacy formats (SFD/VFB) not supported by gftools-builder.

## Open Questions

None. This is a straightforward legacy font with SFD/VFB sources in a standard librefonts archive repository.

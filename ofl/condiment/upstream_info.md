# Condiment - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Condiment |
| Designer | Sudtipos (Angel Koziupa, Alejandro Paul) |
| Repository URL | https://github.com/librefonts/condiment |
| Commit | 0a1933e09c9008136f997c47c75ddf6b00a8d884 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/condiment` was identified from the librefonts organization. The source block was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files") on the pending PR branch `sources_info_2026-02-25` (PR #10270). This PR has not yet been merged into main.

The current METADATA.pb on main does not have a source block.

## How Commit Determined

The commit `0a1933e09c9008136f997c47c75ddf6b00a8d884` is the HEAD (and only commit in the shallow clone) of the `librefonts/condiment` repository. The commit message is "update .travis.yml". This follows the standard librefonts repo pattern.

## Config YAML Status

No config.yaml exists in the upstream repository. The source files are:
- `src/Condiment-Regular-TTF.sfd` (FontForge SFD format)
- `src/Condiment-Regular-OTF.vfb` (FontLab VFB format)

These formats are not compatible with gftools-builder. No override config.yaml exists in the google/fonts family directory.

## Verification

- Repository URL returns HTTP 200
- Commit hash matches the HEAD of the cached repo
- The font binary has never been updated since the initial commit and the deploy commit
- Added to Google Fonts on 2012-01-25
- No source block exists in the main branch METADATA.pb (pending PR #10270)

## Confidence Level

**High** for repository URL and commit hash.

**N/A** for config.yaml - the sources are in legacy formats (SFD/VFB) not supported by gftools-builder.

## Open Questions

None. This is a straightforward legacy font with SFD-only sources in a standard librefonts archive repository.

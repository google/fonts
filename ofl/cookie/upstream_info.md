# Cookie

## Source Data

| Field | Value |
|---|---|
| Family Name | Cookie |
| Repository URL | https://github.com/librefonts/cookie |
| Commit Hash | `15549218a2cb9d78b590471e0fe76644b33c986d` |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/cookie` is part of the librefonts GitHub organization, which hosts archival copies of early Google Fonts projects. The URL was already documented in the tracking data and matches the git remote of the cached upstream repo at `upstream_repos/fontc_crater_cache/librefonts/cookie`.

## How Commit Determined

The upstream repository contains exactly **one commit**: `15549218a2cb9d78b590471e0fe76644b33c986d` ("update .travis.yml"). Since this is the only commit in the repository, it is trivially the correct reference. The librefonts repos were created as archival snapshots of the font projects' state when they were onboarded to Google Fonts.

The font file in google/fonts (`Cookie-Regular.ttf`) was added only in the initial commit (`90abd17b4`, 2015-03-07) and has never been modified since on the main branch.

## Config YAML Status

**No config.yaml exists** in the upstream repository. The source files are:
- `src/Cookie-Regular-TTF.sfd` (FontForge SFD format)
- `src/Cookie-Regular.vfb` (FontLab VFB format)

These are legacy font formats that are **not compatible with gftools-builder**. No override `config.yaml` exists in the google/fonts family directory either.

## Verification

- **Repository accessible**: Yes (verified via git remote URL)
- **Commit hash valid**: Yes - matches the only commit in the repo
- **Font file unchanged since onboarding**: Yes - only modified in initial commit on main
- **Source block in METADATA.pb**: Pending (exists on feature branch `sources_info_2026-02-25`, not yet merged to main)

## Confidence Level

**High** - Single-commit librefonts archival repository. The commit hash is unambiguous.

## Open Questions

None. The family has SFD-only sources and cannot be rebuilt with gftools-builder without a source format conversion.

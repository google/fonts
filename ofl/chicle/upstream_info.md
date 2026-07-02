# Chicle - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Chicle |
| Designer | Sudtipos (Angel Koziupa, Alejandro Paul) |
| License | OFL |
| Date Added | 2011-11-30 |
| Repository URL | https://github.com/librefonts/chicle |
| Commit | `4ee3e89dbbdcfc0d56f7e1e3cc3d2de009219502` |
| Branch | master |
| Config YAML | N/A |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/chicle` was already documented in the tracking data. This is a librefonts mirror repository containing the font sources. The repo contains SFD (FontForge) and VFB source files along with TTX decompositions.

## How Commit Determined

The upstream repository has only a single commit:
- `4ee3e89dbbdcfc0d56f7e1e3cc3d2de009219502` (2014-10-17) - "update .travis.yml"

This is the one and only commit in the repository, so it is trivially the correct commit reference. The source block was added to METADATA.pb in commit `9a14639f3` as part of a batch update adding source blocks to 602 families.

## Config YAML Status

**No config.yaml exists** - neither in the upstream repository nor as an override in the google/fonts family directory.

The upstream repo contains only legacy source formats:
- `src/Chicle-Regular-TTF.sfd` (FontForge SFD)
- `src/Chicle-Regular-OTF.vfb` (FontLab VFB)

These formats are not compatible with gftools-builder, which requires `.glyphs`, `.glyphx`, `.ufo`, or `.designspace` sources. No config.yaml can be created without first converting the sources to a modern format.

## Verification

- Repository URL verified: accessible at https://github.com/librefonts/chicle
- Commit hash verified: matches the only commit in the repository
- Font files last modified in google/fonts: `b736f39c3` (2015-04-27) - "nbspace and fsType fixes"
- No source block exists in the current METADATA.pb on main (the batch update `9a14639f3` is in a pending PR branch)

## Confidence Level

**HIGH** - Repository URL and commit hash are definitively correct. The repo has only one commit, making verification trivial. The missing_config status is accurate since only SFD/VFB sources exist.

## Open Questions

None. This family cannot have a config.yaml without source format conversion.

# Croissant One - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Croissant One |
| Repository URL | https://github.com/librefonts/croissantone |
| Commit Hash | ebcefa6161a0558f994a038105f90f304fe91ff7 |
| Branch | master |
| Config YAML | N/A (SFD/VFB-only sources) |
| Designer | Eduardo Tunni |
| License | OFL |
| Date Added | 2012-11-12 |

## How URL Found

The repository URL `https://github.com/librefonts/croissantone` was identified from the librefonts organization on GitHub, which hosts many legacy Google Fonts source repositories. The source block was added in commit 9a14639f3 ("Add source blocks to 602 more METADATA.pb files", 2026-02-25).

## How Commit Determined

The commit `ebcefa6161a0558f994a038105f90f304fe91ff7` is the HEAD (latest) commit of the upstream repository. The commit message is "update .travis.yml". The upstream repository has 12 commits total, mostly CI configuration updates and initial file organization.

The font binary in google/fonts was part of the initial repository commit (90abd17b4, 2015-03-07) and has never been updated since. HEAD is used as the reference point since the repo represents the canonical state of the project.

## Config YAML Status

**No config.yaml exists** in the upstream repository, and no override config exists in the google/fonts family directory.

The upstream repository contains only legacy source formats:
- `src/CroissantOne-Regular-TTF.sfd` (FontForge SFD format)
- `src/CroissantOne-Regular-OTF.vfb` (FontLab VFB format)

These are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources.

## Verification

- **Repository accessible**: Yes - cloned at `upstream_repos/fontc_crater_cache/librefonts/croissantone/`
- **Commit exists**: Yes - `ebcefa6` is HEAD of the upstream repo
- **Config exists at commit**: No - no config.yaml anywhere in the repo
- **Source files present**: Only SFD/VFB legacy formats
- **Font binary history**: Only modified in the initial google/fonts commit (2015-03-07)

## Confidence Level

**HIGH** for repository URL and commit hash. The librefonts/croissantone repo is the canonical upstream source. The status of "missing_config" is correct since only legacy SFD/VFB sources exist.

## Open Questions

None. This is a legacy font with SFD/VFB-only sources that cannot be rebuilt with modern tooling without a source conversion effort.

# Courgette - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Courgette |
| Repository URL | https://github.com/librefonts/courgette |
| Commit Hash | e9638c8874f097c75ff3206c5dfe15b6ef4c67b1 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Designer | Karolina Lach |
| License | OFL |
| Date Added | 2012-07-10 |

## How URL Found

The repository URL `https://github.com/librefonts/courgette` was identified from the librefonts organization on GitHub, which hosts many legacy Google Fonts source repositories. The source block was added in commit 9a14639f3 ("Add source blocks to 602 more METADATA.pb files", 2026-02-25).

## How Commit Determined

The commit `e9638c8874f097c75ff3206c5dfe15b6ef4c67b1` is the HEAD (latest) commit of the upstream repository. The commit message is "update .travis.yml". Since the font binary files in google/fonts have never been updated since the initial commit (90abd17b4, 2015-03-07), and the upstream repo only contains legacy SFD/VFB sources with CI configuration updates, HEAD is used as the reference point for the repository state.

The font binary was part of the initial google/fonts repository commit and has never been updated since.

## Config YAML Status

**No config.yaml exists** in the upstream repository, and no override config exists in the google/fonts family directory.

The upstream repository contains only legacy source formats:
- `src/Courgette-Regular-OTF.sfd` (FontForge SFD format)
- `src/Courgette-Regular-TTF.sfd` (FontForge SFD format)
- `src/Courgette-Regular.vfb` (FontLab VFB format)

These are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources.

## Verification

- **Repository accessible**: Yes - cloned at `upstream_repos/fontc_crater_cache/librefonts/courgette/`
- **Commit exists**: Yes - `e9638c8` is HEAD of the upstream repo
- **Config exists at commit**: No - no config.yaml anywhere in the repo
- **Source files present**: Only SFD/VFB legacy formats
- **Font binary history**: Only modified in the initial google/fonts commit (2015-03-07)

## Confidence Level

**HIGH** for repository URL and commit hash. The librefonts/courgette repo is the canonical upstream source. The status of "missing_config" is correct since only legacy SFD/VFB sources exist.

## Open Questions

None. This is a legacy font with SFD-only sources that cannot be rebuilt with modern tooling without a source conversion effort.

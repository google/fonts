# Erica One

**Date investigated**: 2026-02-27
**Status**: missing_config (SFD-only sources)
**Designer**: Miguel Hernandez (LatinoType)
**METADATA.pb path**: `ofl/ericaone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/ericaone |
| Commit | `bde7cb1ee528f936a9bae89a746742983531d9f8` |
| Config YAML | None (SFD-only sources, not gftools-builder compatible) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/ericaone` was identified from the fontc_crater_cache at `librefonts/ericaone`. The repo was created on 2014-07-16 by Mikhail Kashkin (hash3g) with the initial commit message "Move ericaone font files to separate repository", indicating it was split out from a larger googlefontdirectory collection into its own repository. This is a librefonts mirror, not the original designer's repository.

No other upstream repository exists for this font. A GitHub search found only the librefonts mirror and a google-fonts-bower package (which is just a bower distribution, not a source repo).

## How the Commit Hash Was Identified

The upstream repository has 11 commits, all by Mikhail Kashkin (hash3g):

1. `b8d3a3e` (2014-07-16) - Initial commit: "Move ericaone font files to separate repository" -- adds all font source files, TTX decomposed files, METADATA.json, license, and description
2. `19e03a5` through `bde7cb1` (2014-08-19 to 2014-10-17) - 10 subsequent commits all exclusively modifying `.travis.yml` for CI configuration

Since the font sources were only ever present in the initial commit, and all later commits only touched CI configuration, the latest commit `bde7cb1` is used as the reference because it represents the final state of the repository with no source file changes.

The font binary in google/fonts (`ofl/ericaone/EricaOne-Regular.ttf`) has never been modified since the initial bulk import commit `90abd17b4` (2015-03-07, by Dave Crossland). The font's head table shows creation and modification dates of 2012-01-24, consistent with the `date_added` of 2012-01-18 in METADATA.pb. This was a very early Google Fonts addition, predating the librefonts mirror by over two years.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files available are:

- `src/EricaOne-Regular-TTF.sfd` -- FontForge Spline Font Database (version 3.0)
- `src/EricaOne-Regular-OTF.vfb` -- FontLab binary source

Neither SFD nor VFB formats are supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. An override config.yaml cannot be created because there are no compatible source files to reference.

The root directory also contains TTX-decomposed files (`.ttx` table dumps of the compiled fonts), but these are not editable font sources.

## Verification

- **Repository URL**: Verified accessible via `gh repo view` -- created 2014-07-16, not archived
- **Commit hash**: `bde7cb1` confirmed as HEAD of master branch with `git rev-parse HEAD`
- **Source files**: Confirmed SFD (FontForge) and VFB (FontLab) only -- no `.glyphs`, `.ufo`, or `.designspace` files present
- **Font binary unchanged**: The TTF in google/fonts has only one entry in git log (the initial commit `90abd17b4`), confirming it was never updated
- **Font version**: Version 1.003 per `src/VERSIONS.txt`; font head table creation date 2012-01-24

## Confidence

**HIGH** -- The repository URL is confirmed as the only available upstream. The commit hash is the latest in a repo with only CI-related changes after the initial file import. The SFD-only source limitation is clearly verified. No config.yaml can be created for this font family.

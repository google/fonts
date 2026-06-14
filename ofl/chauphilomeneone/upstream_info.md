# Investigation: Chau Philomene One

## Source Data

| Field | Value |
|---|---|
| Family Name | Chau Philomene One |
| Designer | Vicente Lamonaca |
| License | OFL |
| Date Added | 2012-04-04 |
| Repository URL | https://github.com/librefonts/chauphilomeneone |
| Commit | `ac51123e5c7a33cd48b4fdf686b91922ea68c422` |
| Branch | master |
| Config YAML | None (not applicable) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/chauphilomeneone` was added to the METADATA.pb source block by commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The `librefonts` organization on GitHub hosts many open-source font projects that were associated with early Google Fonts onboarding.

## How Commit Determined

The commit `ac51123e5c7a33cd48b4fdf686b91922ea68c422` is the only commit (HEAD) in the upstream repository, dated 2014-10-17. Its message is "update .travis.yml".

The font was originally added to google/fonts in the initial commit (`90abd17b4`), and later updated via PR #876 ("hotfix-chauphilomeneone: v1.002 added") by Marc Foley (m4rc1e) on 2017-05-08. Since the upstream repo has only one commit and it predates all google/fonts updates, this commit is unambiguously the correct reference.

## Config YAML Status

**Not applicable.** The upstream repository contains source files in legacy formats:

- `src/ChauPhilomeneOne-Regular-TTF.sfd` and `src/ChauPhilomeneOne-Italic-TTF.sfd` (FontForge SFD format)
- `src/ChauPhilomeneOne-Regular-OTF.vfb` and `src/ChauPhilomeneOne-Italic-OTF.vfb` (FontLab VFB format)
- TTX decomposed font tables

There are no `.glyphs`, `.ufo`, or `.designspace` files that would be compatible with gftools-builder. No `config.yaml` exists in the upstream repo or as an override in the google/fonts family directory.

## Verification

- **Repository URL**: Verified -- the upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/chauphilomeneone`.
- **Commit**: Verified as HEAD (and only commit) of the upstream repo. Predates all google/fonts updates.
- **Source type**: SFD and VFB sources -- neither compatible with gftools-builder.
- **No config.yaml**: Correctly absent given the source formats.

## Confidence Level

**Very High** -- The repository has only one commit, making the commit reference unambiguous. The source formats (SFD, VFB) are well-documented as legacy formats.

## Open Questions

None. The status is correctly `missing_config` because the source formats (SFD, VFB) are not compatible with gftools-builder. No action needed unless the font is eventually migrated to a modern source format.

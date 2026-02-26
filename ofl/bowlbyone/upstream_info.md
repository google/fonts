# Investigation Report: Bowlby One

## Source Data

| Field | Value |
|---|---|
| Family Name | Bowlby One |
| Designer | Vernon Adams |
| License | OFL |
| Date Added | 2011-07-13 |
| Repository URL | https://github.com/librefonts/bowlbyone |
| Commit Hash | `3aca9b57cf9c7b9688b635d5dcfb6d53948e26a2` |
| Branch | master |
| Config YAML | None |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/bowlbyone` was previously recorded in the tracking data. The librefonts organization hosts archival copies of many early Google Fonts projects. The repository is accessible and contains the original source files.

## How Commit Determined

The repository has only 11 commits total, all from 2014. The recorded commit `3aca9b5` is the tip of master (the latest commit, from 2014-10-17: "update .travis.yml"). This is the only meaningful commit to use as a reference since the repo has not been updated since 2014.

The font binary in google/fonts was last updated in two key commits:
1. `efb2eb034` (2015-04-27) - nbspace and fsType fixes by Dave Crossland
2. `5df13fc14` (2017-08-07) - "hotfix-bowlbyone: v1.001 added" by Marc Foley via PR #864

The 2017 hotfix updated the font binary to v1.001. This update was made by Marc Foley (m4rc1e), likely regenerating or modifying the binary outside the upstream repo. The upstream repo was never updated to reflect this change.

## Config YAML Status

**No config.yaml exists** in either the upstream repository or as an override in google/fonts.

The upstream repository only contains SFD (FontForge) and VFB (FontLab) source files:
- `src/BowlbyOne-Regular-TTF.sfd`
- `src/BowlbyOne-Regular.vfb`

These formats are not compatible with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files.

## Verification

- **Repository accessible**: Yes, `librefonts/bowlbyone` is accessible on GitHub
- **Commit exists**: Yes, `3aca9b5` verified on GitHub (2014-10-17)
- **Local cache**: Repo cached at `upstream_repos/fontc_crater_cache/librefonts/bowlbyone/`
- **Commit matches tip**: Yes, the recorded commit is the latest commit in the repo
- **Source files**: SFD and VFB only (not gftools-builder compatible)

## Confidence Level

**HIGH** - The repository URL and commit hash are correct. The commit is the tip of an archival repo that has not been updated since 2014. The font binary in google/fonts was later modified independently (2015, 2017) without corresponding upstream changes.

## Open Questions

1. The 2017 hotfix (v1.001, PR #864) was done by Marc Foley. It is unclear where the updated source for v1.001 resides, if anywhere.
2. Since only SFD/VFB sources exist, a config.yaml cannot be created for gftools-builder. This family may need to remain in "missing_config" status permanently, or an alternative build approach would need to be developed.

# Butcherman - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Butcherman |
| **Designer** | Typomondo |
| **License** | OFL |
| **Date Added** | 2011-12-19 |
| **Repository URL** | https://github.com/librefonts/butcherman |
| **Commit Hash** | `92a34525b5032c76484c49e652f649e52d1465e5` |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

## How URL Was Found

The repository URL `https://github.com/librefonts/butcherman` was added as part of a batch source block addition in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The librefonts GitHub organization hosts mirrors/archives of many Google Fonts source repos. The URL is consistent with the standard librefonts naming convention for this family.

## How Commit Was Determined

The recorded commit `92a34525b5032c76484c49e652f649e52d1465e5` is the **only commit** in the entire repository. The repo was initialized by hash3g on 2014-10-17 with the message "update .travis.yml". Since there is only one commit, it is trivially the correct reference point -- it represents the only state the repo has ever been in.

The font binaries in google/fonts were last updated via PR #870 ("hotfix-butcherman: v1.004 added"), authored by m4rc1e and merged on 2017-08-07. This was a hotfix to the font file (66148 -> 66100 bytes), likely addressing minor issues.

## Config YAML Status

**No config.yaml exists** in the upstream repository and no override config.yaml exists in the google/fonts family directory.

The repository contains only SFD (FontForge) source files at `src/Butcherman-Regular.sfd` and `src/Butcherman-Regular-TTF.sfd`. These are FontForge-format sources that are **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources.

No config.yaml can be created for this family without first converting the sources to a gftools-compatible format.

## Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/butcherman/`
- **Commit hash**: Verified -- it is the only commit in the repo (HEAD of master)
- **Source files**: Only SFD files present (`src/Butcherman-Regular.sfd`, `src/Butcherman-Regular-TTF.sfd`)
- **Font binary history**: Last updated in google/fonts via PR #870 (m4rc1e, 2017-08-07)

## Confidence Level

**HIGH** -- The repository URL is correct and the commit hash is trivially verified as the sole commit. The missing_config status is accurate because only SFD sources exist, which cannot be built with gftools-builder.

## Open Questions

None. The data is complete and verified. The family will remain in `missing_config` status unless the sources are converted to a gftools-compatible format.

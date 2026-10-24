# Butterfly Kids - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Butterfly Kids |
| **Designer** | Tart Workshop |
| **License** | OFL |
| **Date Added** | 2012-02-15 |
| **Repository URL** | https://github.com/librefonts/butterflykids |
| **Commit Hash** | `0c553b23416ad40db0b241d1d0b9165d890933b7` |
| **Branch** | master |
| **Config YAML** | N/A |
| **Status** | missing_config |

## How URL Was Found

The repository URL `https://github.com/librefonts/butterflykids` was added as part of a batch source block addition in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The librefonts GitHub organization hosts mirrors/archives of many Google Fonts source repos.

## How Commit Was Determined

The recorded commit `0c553b23416ad40db0b241d1d0b9165d890933b7` is the **only commit** in the entire repository. The repo was initialized by hash3g on 2014-10-17 with the message "update .travis.yml". Since there is only one commit, it is trivially the correct reference -- there is no other state the repo has ever been in.

The font binaries in google/fonts were last updated via PR #871 ("hotfix-butterflykids: v1.001 added"), authored by m4rc1e and merged on 2017-08-07. This was a hotfix to the font file.

## Config YAML Status

**No config.yaml exists** in the upstream repository and no override config.yaml exists in the google/fonts family directory.

The repository contains only a VFB (FontLab 5) source file at `src/ButterflyKids-Regular-TTF.vfb`. VFB is a proprietary binary format from FontLab 5 that is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` sources.

No config.yaml can be created for this family without first converting the sources to a gftools-compatible format.

## Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/librefonts/butterflykids/`
- **Commit hash**: Verified -- it is the only commit in the repo (HEAD of master)
- **Source files**: Only VFB file present (`src/ButterflyKids-Regular-TTF.vfb`)
- **Font binary history**: Last updated in google/fonts via PR #871 (m4rc1e, 2017-08-07)

## Confidence Level

**HIGH** -- The repository URL is correct and the commit hash is trivially verified as the sole commit. The missing_config status is accurate because only a VFB source file exists, which cannot be built with gftools-builder.

## Open Questions

None. The data is complete and verified. The family will remain in `missing_config` status unless the sources are converted to a gftools-compatible format (e.g., .glyphs or .ufo).

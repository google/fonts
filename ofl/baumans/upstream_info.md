# Baumans - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Baumans |
| Repository URL | https://github.com/librefonts/baumans |
| Commit Hash | 00e0253a48feaa474db9cd5145ec21891f1d7214 |
| Config YAML | (none) |
| Status | missing_config |
| Category | DISPLAY |
| Designer | Cyreal |
| Date Added | 2011-12-07 |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/baumans` was identified from the fontc_crater cache and added to METADATA.pb as part of a bulk source block addition (commit `9a14639f3` in google/fonts). The `librefonts` GitHub organization hosts mirrors of many Google Fonts projects, and this repository contains the Baumans source files.

## How the Commit Hash Was Determined

The commit hash `00e0253a48feaa474db9cd5145ec21891f1d7214` is the latest (and only visible) commit in the upstream repository, titled "update .travis.yml". The repository appears to have been cloned as a shallow clone with only 1 commit visible. Since this is the only commit available, and the repository only has this single grafted commit, it was used as the reference commit.

The font binary in google/fonts was last modified in commit `75a425850` ("hotfix-baumans: v1.002 added", PR #849, August 2017, by Marc Foley). The PR body was empty, so no upstream commit was referenced.

## Config YAML Status

**No config.yaml exists** in the upstream repository at the recorded commit. The repository contains only legacy source formats:
- `.vfb` files (FontLab Studio format) in the `src/` directory
- `.ttx` files (XML font table dumps) at the root level
- No `.glyphs`, `.ufo`, or `.designspace` source files

There is also no override `config.yaml` in the google/fonts family directory (`ofl/baumans/`).

This font predates the gftools-builder workflow. The source files are in VFB format, which is not directly buildable by gftools-builder. This is why the status is `missing_config` - there are no buildable source files to configure.

## Verification

- **Repository exists**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/baumans/`
- **Commit exists**: Yes, `00e0253` is confirmed in the repo ("update .travis.yml")
- **Repo structure**: Contains `.ttx` dumps, `.vfb` source files in `src/`, `OFL.txt`, `FONTLOG.txt`, `DESCRIPTION.en_us.html`
- **METADATA.pb has source block**: Yes (added in bulk, no config_yaml field)

## Confidence Level

**Medium** - The repository URL is correct (it contains Baumans font files), but the commit hash is simply the latest commit in the repo rather than a verified onboarding commit. The `librefonts` organization hosts many Google Fonts, and the repo predates modern tracking practices. There is no way to precisely trace which commit was used for the 2017 hotfix since the PR body was empty and the repo only has one visible commit (shallow clone).

## Open Questions

1. Should this family be considered "complete" despite having no buildable sources? The VFB format requires FontLab to convert, which is outside the gftools-builder workflow.
2. The upstream repo appears to be a shallow clone - fetching full history might reveal additional commits that could help identify the exact onboarding commit.

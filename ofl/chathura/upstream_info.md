# Investigation: Chathura

## Source Data

| Field | Value |
|---|---|
| Family Name | Chathura |
| Designer | Appaji Ambarisha Darbha |
| License | OFL |
| Date Added | 2017-05-09 |
| Repository URL | https://github.com/appajid/Chathura |
| Commit | `f6944e361db05f2cb3a33356e54615f4cf754de8` |
| Branch | master |
| Config YAML | None (not applicable) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/appajid/Chathura` was added to the METADATA.pb source block by commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The URL matches the repository where the font source files are hosted.

## How Commit Determined

The commit `f6944e361db05f2cb3a33356e54615f4cf754de8` is the only commit (HEAD) in the upstream repository, dated 2016-05-31. It is a "Merge pull request #5 from davelab6/davelab6-ttf-fix".

The font was added to google/fonts via PR #944 ("hotfix-chathura: v1.002 added") by Marc Foley (m4rc1e) on 2017-05-11. Since the upstream repo has only one commit (the HEAD), and it predates the google/fonts onboarding by about a year, this commit is unambiguously the correct reference.

## Config YAML Status

**Not applicable.** The upstream repository contains only SFD (FontForge) source files and pre-built TTF binaries. There are no `.glyphs`, `.ufo`, or `.designspace` files that would be compatible with gftools-builder. The repository structure:

- `Chathura-Bold.sfd`, `Chathura-ExtraBold.sfd`, `Chathura-Light.sfd`, `Chathura-Regular.sfd`, `Chathura-Thin.sfd`
- Pre-built TTF files for all 5 weights
- No `config.yaml` in the upstream repo
- No override `config.yaml` in the google/fonts family directory

Since SFD sources cannot be used with gftools-builder, a config.yaml is not applicable for this family.

## Verification

- **Repository URL**: Verified -- the upstream repo is cached at `upstream_repos/fontc_crater_cache/appajid/Chathura`.
- **Commit**: Verified as HEAD (and only commit) of the upstream repo. Predates the google/fonts onboarding.
- **Source type**: SFD-only sources -- not compatible with gftools-builder.
- **No config.yaml**: Correctly absent given the source format.

## Confidence Level

**Very High** -- The repository has only one commit, making the commit reference unambiguous. The source format (SFD) is well-documented.

## Open Questions

None. The status is correctly `missing_config` because the SFD source format is not compatible with gftools-builder. No action needed unless the font is eventually migrated to a modern source format.

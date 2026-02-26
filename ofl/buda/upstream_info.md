# Buda

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Adele Antignac
**METADATA.pb path**: `ofl/buda/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/buda |
| Commit | `c632d6ba92f1c89f40f704c2cd873d5a9ede22a6` |
| Config YAML | N/A (SFD-only sources) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/buda` was identified from the librefonts organization on GitHub, which hosts many early Google Fonts source repositories. The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/buda/` and contains the SFD source files and TTX dumps for the Buda font. The URL was added to the tracking data and a pending source block exists on branch `sources_info_2026-02-25` (commit `9a14639f3`) but has not yet been merged to the main branch of google/fonts.

## How the Commit Hash Was Identified

The upstream repository has only a single commit: `c632d6ba92f1c89f40f704c2cd873d5a9ede22a6` (message: "update .travis.yml"). This is both the initial and only commit in the repository, making it the only possible reference. The font binary in google/fonts was last updated in PR #868 ("hotfix-buda: v1.003 added", 2017-08-07) by Marc Foley, which predates the source block tracking effort. Since the upstream repo has only one commit, the hash is unambiguously correct.

## How Config YAML Was Resolved

There is no config.yaml in the upstream repository. The only source file is `src/Buda-Light-TTF.sfd`, which is a FontForge SFD format file. SFD files are not compatible with the gftools-builder pipeline, so no config.yaml can be created for this family. No override config.yaml exists in the google/fonts family directory either.

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: Not available (single commit, likely very old)
- Commit message: "update .travis.yml"
- Source files at commit: `src/Buda-Light-TTF.sfd` (FontForge SFD format)
- Font binary in google/fonts last updated: 2017-08-07 (PR #868)
- Original addition to Google Fonts: 2010-12-20

## Confidence

**High**: The repository URL and commit hash are straightforward to verify. The upstream repo has only one commit, so the hash is unambiguous. The font uses SFD sources which cannot be built with gftools-builder, making this family permanently `missing_config` in the modern build system.

## Open Questions

1. The source block has been prepared on branch `sources_info_2026-02-25` but has not yet been merged into the main google/fonts repository. Once merged, METADATA.pb will document the upstream source.
2. Since the font uses SFD sources only, it would need to be converted to a modern source format (UFO or Glyphs) before a config.yaml could be created. This is unlikely to happen unless the font receives a major redesign/update.

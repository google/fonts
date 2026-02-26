# Chango

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Fontstage
**METADATA.pb path**: `ofl/chango/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/chango |
| Commit | `ca58222d6319223db35d6e76052ef9a78cca43f7` |
| Config YAML | N/A (SFD-only sources) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/chango` was already documented in the tracking data. It was added to METADATA.pb in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25). The repository is part of the `librefonts` GitHub organization which hosts many Google Fonts upstream sources.

## How the Commit Hash Was Identified

The commit `ca58222d6319223db35d6e76052ef9a78cca43f7` is the **only commit** in the upstream repository (2014-10-17, "update .travis.yml"). This is a single-commit repository, making the hash unambiguous.

The font files in google/fonts have never been updated since the initial commit `90abd17b4`. The font was added to Google Fonts on 2011-12-13 (date_added field).

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory (`ofl/chango/`).

The upstream repository contains only legacy source formats:
- `src/Chango-Regular-TTF.sfd` (FontForge SFD format)
- `src/Chango-Regular-OTF.vfb` (FontLab VFB format)
- Various TTX decomposition files

Neither SFD nor VFB formats are compatible with gftools-builder. A `config.yaml` cannot be created without first converting the sources to a modern format (`.glyphs` or `.ufo`).

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2014-10-17 13:32:32 +0300
- Commit message: "update .travis.yml"
- Source files at commit: `src/Chango-Regular-TTF.sfd`, `src/Chango-Regular-OTF.vfb`

## Confidence

**High**: The repository URL and commit hash are straightforward -- the repo has only one commit. The URL is confirmed by its presence in the librefonts organization. The lack of config.yaml is expected given the legacy source formats (SFD/VFB only).

## Open Questions

1. The sources are in legacy formats (SFD and VFB). To enable gftools-builder builds, these would need to be converted to `.glyphs` or `.ufo` format. This is not a trivial conversion and may require manual review by a type designer.
2. The family was added to Google Fonts in 2011 (date_added: 2011-12-13). The upstream repository appears to be a post-hoc archive created in 2014, rather than the original development location.
3. The designer "Fontstage" does not appear to have an active online presence. Any source conversion work would likely need to be done by the Google Fonts team.

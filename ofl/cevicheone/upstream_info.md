# Ceviche One

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: Miguel Hernandez
**METADATA.pb path**: `ofl/cevicheone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/cevicheone |
| Commit | `afec42c6e7445edd88c3f45b7a51b5da6b43b027` |
| Config YAML | N/A (SFD-only sources) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/cevicheone` was already documented in the tracking data. It was added to METADATA.pb in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25). The repository is part of the `librefonts` GitHub organization which hosts many Google Fonts upstream sources. Note that the METADATA.pb currently has no `source { }` block in the live version -- the source block was added as part of a batch enrichment.

## How the Commit Hash Was Identified

The commit `afec42c6e7445edd88c3f45b7a51b5da6b43b027` is the **only commit** in the upstream repository (message: "update .travis.yml"). This is a single-commit repository, making the hash unambiguous. The font files in google/fonts were last updated in commit `08e091b33` (2015-04-27, "Updating ofl/cevicheone/*ttf with nbspace and fsType fixes") by Dave Crossland, which was a minor binary fix. The original font was added in the initial commit `90abd17b4`.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and no override `config.yaml` exists in the google/fonts family directory (`ofl/cevicheone/`).

The upstream repository contains only legacy source formats:
- `src/CevicheOne-Regular-TTF.sfd` (FontForge SFD format)
- `src/CevicheOne-Regular-OTF.vfb` (FontLab VFB format)
- Various TTX decomposition files

Neither SFD nor VFB formats are compatible with gftools-builder. A `config.yaml` cannot be created without first converting the sources to a modern format (`.glyphs` or `.ufo`).

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: Not explicitly dated in log, but the repo has only this one commit
- Commit message: "update .travis.yml"
- Source files at commit: `src/CevicheOne-Regular-TTF.sfd`, `src/CevicheOne-Regular-OTF.vfb`

## Confidence

**High**: The repository URL and commit hash are straightforward -- the repo has only one commit. The URL is confirmed by its presence in the librefonts organization. The lack of config.yaml is expected given the legacy source formats (SFD/VFB only).

## Open Questions

1. The sources are in legacy formats (SFD and VFB). To enable gftools-builder builds, these would need to be converted to `.glyphs` or `.ufo` format. This is not a trivial conversion and may require manual review by a type designer.
2. The family was added to Google Fonts in 2011 (date_added: 2011-12-07). The upstream repository appears to be a post-hoc archive rather than the original development location.

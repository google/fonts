# Investigation: Carrois Gothic SC

## Source Data

| Field | Value |
|---|---|
| Family Name | Carrois Gothic SC |
| Designer | Carrois Apostrophe |
| License | OFL |
| Date Added | 2012-09-30 |
| Repository URL | https://github.com/librefonts/carroisgothicsc |
| Commit Hash | `cd21c85aa57e4b1fc55eca2e31692cbd749e4e46` |
| Branch | master |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/carroisgothicsc` was recorded in the tracking data and added to the METADATA.pb source block in commit `9a14639f3` on branch `sources_info_2026-02-25` (not yet merged to main). This is a librefonts mirror repository, separate from the Carrois Gothic (non-SC) repo.

## How Commit Determined

The commit hash `cd21c85aa57e4b1fc55eca2e31692cbd749e4e46` is the HEAD (and only) commit of the upstream repository, with the message "update .travis.yml". The repository has only a single commit, so there is no ambiguity.

The font was originally part of the initial google/fonts commit (`90abd17b4`). A hotfix was later applied in commit `e57e3eea9` (PR #875) by Marc Foley on 2017-05-08, updating the TTF from its original version to v1.002. This hotfix modified the binary and metadata but the upstream librefonts repo was not updated to reflect this.

## Verification

- **Commit exists in upstream repo**: Yes. `cd21c85` is the HEAD and sole commit.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/carroisgothicsc/`.
- **Source files present**: The `src/` directory contains VFB files (FontLab Studio binary format): `CarroisGothicSC-Regular.vfb`, `CarroisGothicSC-Regular-OTF.vfb`, `CarroisGothicSC-Regular-TTF.vfb`. No open-format sources (.glyphs, .ufo, .designspace, .sfd) are available.
- **TTX decomposed files**: The root directory and `orig/` directory contain TTX-decomposed font data, but these are not standard buildable sources for gftools-builder.

## Config YAML Status

**No config.yaml possible.** The upstream repository only contains VFB files (FontLab Studio proprietary binary format), which are not supported by gftools-builder. There are no SFD, Glyphs, UFO, or Designspace files that could be used as build sources.

No override config.yaml exists in the google/fonts family directory either.

## Relationship to Carrois Gothic

Carrois Gothic SC is the small-caps variant of Carrois Gothic. Both were designed by Ralph du Carrois (Carrois Apostrophe) and share the same history:
- Added in the initial google/fonts commit
- Hotfixed by Marc Foley in May 2017 (PR #875 for SC, PR #874 for regular)
- Upstream librefonts repos each have a single commit and contain VFB-only sources
- Neither has gftools-builder-compatible sources

## Confidence Level

**HIGH** -- The commit hash is the only commit in the single-commit repository. The repository URL is a standard librefonts mirror. The situation is identical to Carrois Gothic (non-SC).

## Open Questions

- Same as Carrois Gothic: VFB sources would need conversion to an open format before any config.yaml could be created.
- The hotfix PR #875 (2017) updated the binary in google/fonts but the upstream was never synced.
- The status should remain `missing_config` as there are no gftools-builder-compatible sources.

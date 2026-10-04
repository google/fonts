# Investigation: Carrois Gothic

## Source Data

| Field | Value |
|---|---|
| Family Name | Carrois Gothic |
| Designer | Carrois Apostrophe |
| License | OFL |
| Date Added | 2012-09-30 |
| Repository URL | https://github.com/librefonts/carroisgothic |
| Commit Hash | `09bb67138894e329544a6a1e1ebf0ff516f82a0e` |
| Branch | master |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/carroisgothic` was recorded in the tracking data and added to the METADATA.pb source block in commit `9a14639f3` on branch `sources_info_2026-02-25` (not yet merged to main). This is a librefonts mirror repository.

## How Commit Determined

The commit hash `09bb67138894e329544a6a1e1ebf0ff516f82a0e` is the HEAD (and only) commit of the upstream repository, with the message "update .travis.yml". The repository has only a single commit, so there is no ambiguity about which commit to reference.

The font was originally part of the initial google/fonts commit (`90abd17b4`). A hotfix was later applied in commit `29cf1c494` (PR #874) by Marc Foley on 2017-05-08, updating the TTF from v1.001 to v1.002. This hotfix modified the binary and metadata but the upstream librefonts repo was not updated to reflect this change.

## Verification

- **Commit exists in upstream repo**: Yes. `09bb671` is the HEAD and sole commit.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/carroisgothic/`.
- **Source files present**: The `src/` directory contains VFB files (FontLab Studio binary format): `CarroisGothic-Regular.vfb`, `CarroisGothic-Regular-OTF.vfb`, `CarroisGothic-Regular-TTF.vfb`. No open-format sources (.glyphs, .ufo, .designspace, .sfd) are available.
- **TTX decomposed files**: The root directory and `orig/` directory contain TTX-decomposed font data, but these are not standard buildable sources for gftools-builder.

## Config YAML Status

**No config.yaml possible.** The upstream repository only contains VFB files (FontLab Studio proprietary binary format), which are not supported by gftools-builder. There are no SFD, Glyphs, UFO, or Designspace files that could be used as build sources. VFB files cannot be processed by open-source font build tools.

No override config.yaml exists in the google/fonts family directory either.

## Confidence Level

**HIGH** -- The commit hash is the only commit in the single-commit repository. The repository URL is a standard librefonts mirror. The font's history in google/fonts is clear: initial commit, then a hotfix by Marc Foley.

## Open Questions

- The hotfix PR #874 (2017) updated the binary TTF in google/fonts but the upstream librefonts repo was never updated. The current binary in google/fonts may not match what can be built from the upstream sources.
- VFB sources would need to be converted to an open format (e.g., UFO) before a config.yaml could be created. This is unlikely to happen unless someone undertakes a conversion project.
- The status should remain `missing_config` as there are no gftools-builder-compatible sources.

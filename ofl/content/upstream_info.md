# Content - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Content |
| Designer | Danh Hong |
| Repository URL | https://github.com/librefonts/content |
| Commit | 15b7178f9b93d01ba29f9a6cca770578cc7275e5 |
| Branch | master |
| Config YAML | N/A (no editable source files) |
| Status | no_upstream_repo (should be updated to missing_config) |

## How URL Found

The tracking data had this family listed as `no_upstream_repo`, but a librefonts archive repository exists at `https://github.com/librefonts/content`. This repo was found in the local cache at `upstream_repos/fontc_crater_cache/librefonts/content/`. The URL was verified to return HTTP 200.

The METADATA.pb on main has no source block. The font was added to Google Fonts on 2011-03-02 as part of the initial commit.

## How Commit Determined

The commit `15b7178` is the HEAD (and only commit in the shallow clone) of the `librefonts/content` repository. The full hash needs to be verified from the remote. The commit message is "update .travis.yml", following the standard librefonts pattern.

## Config YAML Status

No config.yaml exists in the upstream repository. Unlike other librefonts repos, this one has **no editable source files at all**:
- `src/` directory contains only `VERSIONS.txt` (no SFD, VFB, Glyphs, UFO, or designspace files)
- The repo contains only TTX dumps of the compiled TTF files

This is a Khmer script font (primary_script: "Khmr") created by Danh Hong as part of the KhmerOS project. The original source files may have been created in a tool that predates modern font editing formats used by Google Fonts.

## Verification

- Repository URL returns HTTP 200
- Commit hash matches the HEAD of the cached repo
- The font binaries have never been updated since the initial commit and the deploy commit
- Copyright references "Khmer OS Content" and "khmertype.blogspot.com"
- No source block exists in any branch of the google/fonts METADATA.pb

## Confidence Level

**Medium** for repository URL - the librefonts repo exists and is accessible, but it contains only TTX dumps rather than editable sources. It is still the best known upstream reference.

**N/A** for config.yaml - no editable sources exist in any known format.

## Open Questions

1. The tracking data should be updated from `no_upstream_repo` to reflect that `librefonts/content` exists as an upstream reference, even though it lacks editable sources.
2. Are original source files available elsewhere (e.g., the KhmerOS project at khmertype.blogspot.com)?
3. Should a source block be added to METADATA.pb pointing to librefonts/content, even without editable sources?

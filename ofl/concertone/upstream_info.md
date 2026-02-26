# Concert One - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Concert One |
| Designer | Johan Kallas, Mihkel Virkus |
| Repository URL | https://github.com/librefonts/concertone |
| Commit | c2160f498dbb0ebf8394fbd117c21d2160cdef01 |
| Branch | master |
| Config YAML | N/A (SFD-only sources) |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/concertone` was identified from the librefonts organization, which hosts mirrored source repositories for many early Google Fonts families. The source block was added in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files") on the pending PR branch `sources_info_2026-02-25` (PR #10270). This PR has not yet been merged into main.

The current METADATA.pb on main does not have a source block.

## How Commit Determined

The commit `c2160f498dbb0ebf8394fbd117c21d2160cdef01` is the HEAD (and only commit in the shallow clone) of the `librefonts/concertone` repository. The commit message is "update .travis.yml". This is a standard librefonts repo pattern where the single visible commit represents the latest state of the source archive.

## Config YAML Status

No config.yaml exists in the upstream repository. The source files are:
- `src/ConcertOne-Regular-TTF.sfd` (FontForge SFD format)
- `src/ConcertOne-Regular-OTF.vfb` (FontLab VFB format)

These formats are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No override config.yaml exists in the google/fonts family directory either.

## Verification

- Repository URL returns HTTP 200
- Commit hash matches the HEAD of the cached repo
- The font binary in google/fonts was last modified by a v-metrics hotfix (commit `dc96bd2ff`, May 2024, by Emma Marichal) applied directly to the binary - no upstream source changes
- No source block exists in the main branch METADATA.pb (pending PR #10270)

## Confidence Level

**High** for repository URL and commit hash. The librefonts repo is the canonical source archive.

**N/A** for config.yaml - the sources are in legacy formats (SFD/VFB) not supported by gftools-builder.

## Open Questions

1. The v-metrics hotfix was applied directly to the binary in google/fonts without corresponding upstream changes. Should this be documented more formally?
2. Would it be worthwhile to convert the SFD sources to a gftools-builder compatible format?

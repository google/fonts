# Cabin Condensed - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Cabin Condensed |
| **Designer** | Impallari Type |
| **License** | OFL |
| **Date Added** | 2011-11-30 |
| **Repository URL** | https://github.com/impallari/Cabin |
| **Commit Hash** | `9476ee6f5459ee37cf8462452f3e4640c3a48519` |
| **Branch** | N/A (defaults to master) |
| **Config YAML** | Override in google/fonts |
| **Status** | complete |

## How URL Was Found

The repository URL `https://github.com/impallari/Cabin` was added in commit `c8f729cbd` ("Add more upstreams (c,d)"). Both Cabin and Cabin Condensed share the same upstream repository, as they are generated from the same Glyphs source files. The copyright string in the fonts confirms the connection: "Copyright 2016 The Cabin Project Authors (impallari@gmail.com)".

## How Commit Was Determined

The commit hash `9476ee6f5459ee37cf8462452f3e4640c3a48519` was added in the batch source block update `9a14639f3` ("Add source blocks to 602 more METADATA.pb files").

This commit corresponds to the upstream merge that produced the v2.200 fonts used in the last binary update for Cabin Condensed:

- **Upstream commit**: `9476ee6f` is a merge commit from 2017-02-23: "Merge pull request #12 from m4rc1e/master" with message "sources | fonts: v2.200 update"
- **google/fonts commit**: `eef4029d7` ("cabincondened: v2.200 added (#680)"), merged 2017-05-01
- **PR #680** (m4rc1e): "Same as #679, both families are generated from the same .glyphs file" -- referring to the Cabin v2.220 update in PR #679

Note that while Cabin was later updated to v3.001 as a variable font (upstream commit `70efa8c3`), **Cabin Condensed was not updated**. The Cabin Condensed static fonts still correspond to the v2.200 era. The v3.001 Cabin variable font includes a `wdth` axis (75-100) that covers condensed widths, but Cabin Condensed remains a separate family entry with static binaries from the older commit.

## Config YAML Status

**No config.yaml exists** in the upstream repository at any commit, and no override config.yaml exists in the google/fonts family directory.

At the recorded commit (`9476ee6f`), the source files are:
- `sources/Cabin.glyphs` (contains both regular and condensed masters)
- `sources/Cabin-Italic.glyphs`

These are Glyphs format sources that are potentially compatible with gftools-builder, but a config.yaml would need to be created. The Cabin Condensed static fonts were originally extracted from these sources.

At the later Cabin v3.001 commit (`70efa8c3`), the sources were restructured to:
- `sources/CabinRegular_v3001.glyphs`
- `sources/CabinItalic_v3001.glyphs`
- `sources/CabinRegular.designspace`
- `sources/CabinItalic.designspace`
- `sources/build.sh` (custom build script)

## Verification

- **Repository URL**: Confirmed valid; repo is cloned at `upstream_repos/fontc_crater_cache/impallari/Cabin/`
- **Commit hash**: Verified -- exists in the repo; the merge commit message ("sources | fonts: v2.200 update") directly aligns with google/fonts PR #680 ("cabincondened: v2.200 added")
- **Source files**: Glyphs sources present at the recorded commit (gftools-compatible format)
- **Font binary history**: Last binary update was PR #680 (m4rc1e, merged 2017-05-01)

## Confidence Level

**HIGH** -- The commit hash is well-supported by cross-referencing:
1. The upstream commit is a merge of m4rc1e's v2.200 update (PR #12 in the upstream repo)
2. The google/fonts PR #680 was also authored by m4rc1e and titled "cabincondened: v2.200 added"
3. PR #680 body explicitly states "Same as #679, both families are generated from the same .glyphs file"
4. The TTF files in the upstream commit's `fonts/TTF/CabinCondensed-*.ttf` correspond to the binaries added in google/fonts


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - sources/Cabin.glyphs
familyName: Cabin Condensed
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. Should Cabin Condensed be updated to use the v3.001 sources and the newer commit hash (`70efa8c3`), or is it intentionally kept at the v2.200 static fonts? The newer Cabin variable font already includes condensed width via the `wdth` axis.
2. Could a config.yaml override be created for Cabin Condensed to enable gftools-builder builds from the `.glyphs` sources at commit `9476ee6f`?

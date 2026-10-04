# Fredericka the Great

**Date investigated**: 2026-02-27
**Status**: no_buildable_source
**Designer**: Tart Workshop (Crystal Kluge, Font Diner, Inc)
**METADATA.pb path**: `ofl/frederickathegreat/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/frederickathegreat |
| Commit | `937ffb6bea2b78bf3d064cce27b3b0c1d7ca10d8` |
| Config YAML | N/A (VFB-only sources, not buildable with gftools-builder) |
| Branch | `master` |

## Upstream Repository

The upstream repo at `librefonts/frederickathegreat` was created on 2014-07-16 as part of the `librefonts` organization's effort to host Google Fonts sources on GitHub. The repo has not been updated since 2014-10-17 (last push).

### Repository Contents (all commits)

Root directory:
- `.travis.yml` - CI configuration (the only file modified after initial commit)
- `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `OFL.txt`, `METADATA.json`
- `FrederickatheGreat-Regular.ttf.*.ttx` - Decomposed TTX (XML) representations of the binary font
- `src/` directory containing:
  - `FrederickatheGreat-Regular-Regular-TTF.vfb` - FontLab VFB binary source
  - `METADATA_comments.txt` - Build/subset scripts
  - `VERSIONS.txt` - Records "Version 1.000"

The only source file is a `.vfb` (FontLab binary format), which is **not buildable** with gftools-builder. There are no `.glyphs`, `.ufo`, or `.designspace` files.

### Commit History

The repo has exactly 10 commits, all from 2014:
1. `937ffb6b` (2014-07-16) - "Move frederickathegreat font files to separate repository" (initial commit with all font content)
2. `1ac054b0` through `6968170d` (2014-08-19 to 2014-10-17) - All subsequent commits only modify `.travis.yml` (CI configuration)

The `src/` directory tree SHA (`89a2bf5b`) is identical across all commits, confirming no source files were ever changed after the initial commit.

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/frederickathegreat` is documented in a pending source block that was prepared in google/fonts commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25). The `librefonts` organization is a known collection of Google Fonts upstream sources, created by the Google Fonts team (vitalyvolkov, xen are listed as contributors).

## How the Commit Hash Was Identified

### Previously Referenced Commit

The batch source block commit `9a14639f3` references `6968170d91ffd9daea400fb4d12bf0173f7d6302` (the HEAD/latest commit in the upstream repo). However, this commit only modifies `.travis.yml` and has no bearing on the font sources.

### Correct Commit

The correct commit to reference is `937ffb6bea2b78bf3d064cce27b3b0c1d7ca10d8` (the initial commit, 2014-07-16), which is the only commit that contains the actual font sources and VFB file. All 9 subsequent commits only modify `.travis.yml`.

Since the `src/` directory is unchanged across all commits, either commit hash is technically valid for referencing the source state. However, the initial commit `937ffb6b` is more precise because it is the commit that actually introduced the font content.

## Font Binary History in google/fonts

The font binary `FrederickatheGreat-Regular.ttf` has been modified twice:

1. **Initial commit** `90abd17b4` (2015-03-07, Dave Crossland): Added original v1.000 (486,216 bytes)
2. **PR #1361** `66934bdd4` (authored 2017-11-28 by Micah Stupak/laerm0, committed by Marc Foley, merged 2019-07-09): Updated to v1.01 with name table fix (486,016 bytes) - Solves issue #1305 (macOS Font Book validation warnings)

The current binary in google/fonts (v1.01, 486,016 bytes) was produced by the PR #1361 name table fix. This fix was applied directly to the binary font (using font editing tools) and was **never pushed back** to the upstream `librefonts/frederickathegreat` repo. The upstream repo still only has the original v1.000 TTX decomposition and VFB source.

## Build Configuration

No `config.yaml` exists in the upstream repo, and none can be created because:
- The only source is a `.vfb` file (proprietary FontLab binary format)
- There are no `.glyphs`, `.ufo`, or `.designspace` files
- The TTX files are decomposed representations of the binary, not editable design sources
- gftools-builder cannot build from VFB sources

No override `config.yaml` is present in the google/fonts family directory.

## Source Block Status

The METADATA.pb currently has **no source block** on the main branch. A pending source block was prepared in commit `9a14639f3` (not yet merged to main) with:
```
source {
  repository_url: "https://github.com/librefonts/frederickathegreat"
  commit: "6968170d91ffd9daea400fb4d12bf0173f7d6302"
}
```

The commit hash should ideally be corrected to `937ffb6bea2b78bf3d064cce27b3b0c1d7ca10d8` (the initial commit that actually contains font sources), though the source state is identical at either commit.

## Verification

- Upstream repo exists and is accessible: Yes
- Upstream repo is not archived or forked: Correct
- Source files at referenced commit: `src/FrederickatheGreat-Regular-Regular-TTF.vfb` (VFB only)
- No `.glyphs`, `.ufo`, or `.designspace` files: Confirmed
- No `config.yaml` in upstream repo: Confirmed
- No override `config.yaml` in google/fonts: Confirmed
- Current binary (v1.01) was NOT built from upstream sources: It was a direct binary edit (name table fix by laerm0/Micah Stupak in PR #1361)

## Confidence

**Medium**: The repository URL is correct (librefonts organization, matches the font). The commit hash `937ffb6b` correctly references the initial source content. However, the current binary in google/fonts (v1.01) was produced by a direct binary modification (PR #1361), not by building from the VFB source. The upstream repo was never updated with the v1.01 changes. This family cannot be rebuilt from source using gftools-builder.

## Open Questions

1. Is there a more authoritative source repository for this font? The `librefonts` organization repo only has TTX decompositions and a VFB file. The original designer (Crystal Kluge / Font Diner / Tart Workshop) may have the original design files in a modern format.
2. Should the commit hash reference `937ffb6b` (initial content commit) or `6968170d` (HEAD, only CI changes)?

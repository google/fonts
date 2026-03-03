# Loved by the King — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete

## METADATA.pb Source Block (current)

No source block exists. The current METADATA.pb contains only basic font metadata (name, designer, license, category, fonts, subsets, classifications) with no `source { }` block.

## Repository Analysis

The only upstream repository found is **librefonts/lovedbytheking** on GitHub (`https://github.com/librefonts/lovedbytheking`).

- **Organization**: `librefonts` is an automated mirror organization that decomposed early Google Fonts binaries into TTX (XML) format for version control. It is not a design-source repository.
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Commits**: Single commit (`d22be35`) by `hash3g` dated 2014-10-17, titled "update .travis.yml"
- **Branches**: Only `master`
- **Status**: Clean, synced with origin

### Repository Contents

The repo contains:
- **Root**: Decomposed TTX files of `LovedbytheKing.ttf` (each table in a separate `.ttx` file), `METADATA.json`, `OFL.txt`, `DESCRIPTION.en_us.html`, `.travis.yml`
- **`src/`**: `LovedbytheKing-TTF.sfd` (FontForge Spline Font Database v3.0), `LovedbytheKing.vfb` (FontLab binary), decomposed OTF TTX files, `METADATA_comments.txt`, `VERSIONS.txt`

### Source File Analysis

- **SFD file**: FontForge Spline Font Database format (legacy). Not compatible with gftools-builder.
- **VFB file**: FontLab Studio binary format (legacy, proprietary). Not compatible with gftools-builder.
- **No `.glyphs`, `.glyphx`, `.ufo`, or `.designspace` files** exist in the repo.
- **No `config.yaml`** exists in the repo.
- The TTX files are decomposed binary font tables, not editable design sources.

### Build Configuration (Travis CI)

The `.travis.yml` used the legacy `fontbakery-build.py` tool (circa 2014), which predated the modern gftools-builder pipeline. This build system is no longer supported.

## Onboarding History

- **Added to Google Fonts**: 2011-07-06 (per `date_added` in METADATA.pb)
- **Git history**: The font binary was added in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the bulk import of all existing Google Fonts into the new Git-based repository.
- **No subsequent modifications**: The TTF file has never been updated since the initial commit.
- **No associated PRs**: The font was part of the initial bulk import, so there are no individual onboarding PRs to trace.

## Font Metadata (from TTX)

- **Version**: 1.002 (2006)
- **Copyright**: Copyright (c) 2006 by Kimberly Geswein. All rights reserved.
- **Designer**: Kimberly Geswein
- **Designer URL**: http://kimberlygeswein.com (site is live, returns HTTP 200)
- **Head table created/modified**: 2011-07-01

## Designer Context

Kimberly Geswein is a prolific handwriting font designer with 22 font families in Google Fonts. She does not appear to have a GitHub account. Her fonts were typically created in FontLab or FontForge (VFB/SFD formats), predating the modern .glyphs/.ufo workflow. No designer-maintained upstream repository was found for this font.

## Build Configuration

- **config.yaml**: Does not exist in the upstream repo
- **gftools-builder compatible sources**: None. The repo contains only SFD (FontForge) and VFB (FontLab) files, which are legacy formats not supported by gftools-builder.
- **Override config.yaml feasibility**: Not feasible. There are no `.glyphs`, `.ufo`, or `.designspace` sources from which gftools-builder could compile fonts.

## Findings

1. **No proper design sources exist**: The librefonts/lovedbytheking repo is an automated mirror containing decomposed TTX files and legacy SFD/VFB sources. These cannot be used with the modern gftools-builder pipeline.

2. **The librefonts repo is the only known upstream**: No other repository (e.g., a designer-maintained repo) was found. The designer (Kimberly Geswein) does not have a GitHub presence.

3. **Font has never been updated**: The binary in google/fonts dates from the initial bulk import (2015) and the font version is from 2006. It has never gone through the modern onboarding pipeline.

4. **SFD-only sources**: The only usable source format is the FontForge SFD file. This is a legacy format that cannot be compiled via gftools-builder. A `config.yaml` override is not applicable here.

5. **Pattern match**: Other Kimberly Geswein fonts (e.g., `architectsdaughter`) already reference `librefonts` repos in their source blocks with SFD-only sources, establishing a precedent for documenting these legacy repos.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lovedbytheking"
  commit: "d22be35555328ba7c5a7255b875f08dd420e6cdd"
}
```

**Notes on the recommended block**:
- The `repository_url` points to the librefonts mirror, which is the only known upstream repository.
- The `commit` is `d22be35` — the single commit in the repository, which contains all the source files.
- No `config_yaml` field is included because there is no config.yaml in the repo and no gftools-builder compatible sources exist to create an override for.
- This follows the same pattern as `architectsdaughter` (another Kimberly Geswein font with a `librefonts` source block).
- **Status**: incomplete — the font lacks modern design sources (.glyphs/.ufo/.designspace) needed for gftools-builder compilation. The source block documents what exists (SFD-only legacy sources) but the font cannot be rebuilt from these sources using the current toolchain.

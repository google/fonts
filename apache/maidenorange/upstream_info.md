# Maiden Orange -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `maidenorange/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `MaidenOrange.vfb` | FontLab binary | No |
| `METADATA_comments.txt` | Metadata | N/A |

The only design source is a FontLab VFB binary (`MaidenOrange.vfb`). VFB is a proprietary format not supported by gftools-builder or fontc. No `.glyphs`, `.ufo`, or `.designspace` files exist. A gftools-builder config.yaml cannot be created for this family.

## Designer

Brian J. Bonislawsky, operating as Astigmatic (AOETI). Licensed under Apache 2.0.

## Onboarding History

### Initial Addition

Maiden Orange was part of the initial commit (`90abd17`) to the google/fonts repository on 2015-03-07 by Dave Crossland. The font file was named `MaidenOrange.ttf` (version 1.000). The `date_added` field in METADATA.pb is "2010-12-20", indicating the font was part of Google Fonts well before the current repository structure.

### Hotfix Update (PR #781)

On 2017-08-07, Marc Foley submitted PR #781 ("hotfix-maidenorange: v1.001 added") which:
- Renamed the font file from `MaidenOrange.ttf` to `MaidenOrange-Regular.ttf`
- Updated the font binary to version 1.001 (from 1.000)
- Updated DESCRIPTION.en_us.html formatting
- Updated METADATA.pb (filename, full_name, copyright, subsets order)

The PR body was empty, providing no information about where the v1.001 binary came from.

## Version Discrepancy

- The googlefontdirectory-hg sources correspond to **Version 1.000**
- The font currently in google/fonts is **Version 1.001** (updated via PR #781)
- The v1.001 binary was produced by Marc Foley in the hotfix but its build process is undocumented

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/maidenorange` (created 2014-07-16 by Mikhail Kashkin). The librefonts organization systematically split out font families from the old google/fonts monorepo into individual repositories. It contains the same VFB source and TTX-decomposed font tables, with 12 commits (all from 2014) related to Travis CI setup. This is not an original designer repository and adds no additional sources beyond googlefontdirectory-hg.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- The upstream sources are **VFB-only**, which is not compatible with gftools-builder
- Creating an override config.yaml is not feasible because gftools-builder cannot process VFB files
- This is a legacy font (added 2010) with proprietary-format sources and no active upstream development

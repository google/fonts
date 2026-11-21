# Luckiest Guy -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `luckiestguy/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `LuckiestGuy.vfb` | FontLab binary | No |
| `METADATA_comments.txt` | Metadata | N/A |

The only design source is a FontLab VFB binary (`LuckiestGuy.vfb`). VFB is a proprietary format not supported by gftools-builder or fontc. No `.glyphs`, `.ufo`, or `.designspace` files exist. A gftools-builder config.yaml cannot be created for this family.

## Designer

Brian J. Bonislawsky, operating as Astigmatic (AOETI). Copyright: "(c) 2010 by Brian J. Bonislawsky DBA Astigmatic (AOETI)."

## Onboarding History

### Initial Addition

The font was part of the initial commit to the google/fonts repository:
- **Commit**: `90abd17b` (2015-03-07) by Dave Crossland -- "Initial commit"
- **Date added**: 2011-01-06 (per METADATA.pb; the 2015 commit was when the repo was migrated to GitHub)
- The original font file was named `LuckiestGuy.ttf`

### Hotfix Update (PR #780)

The font was updated in PR #780:
- **Commit**: `9a93667` (2017-08-07)
- **Author**: Marc Foley (m4rc1e)
- **Merged by**: Dave Crossland (davelab6)
- **Title**: "hotfix-luckiestguy: v1.001 added"
- **PR body**: Empty (no description provided)
- **Changes**:
  1. Renamed `LuckiestGuy.ttf` to `LuckiestGuy-Regular.ttf`
  2. Updated the binary from Version 1.000 to Version 1.001
  3. Updated METADATA.pb to reflect the new filename
  4. Rewrote DESCRIPTION.en_us.html

The v1.001 binary was likely produced by Marc Foley as part of the hotfix process, but the upstream sources were never updated to reflect this version. The PR body was empty, so there is no record of how the v1.001 binary was produced.

## Version Discrepancy

- The googlefontdirectory-hg sources correspond to **Version 1.000** of the font
- The font binary currently in google/fonts is **Version 1.001**
- The v1.001 binary was produced in PR #780 by Marc Foley, but how it was built is undocumented

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/luckiestguy` (created 2014-07-16, last pushed 2014-10-17, 1 commit by hash3g). It contains the same VFB source and TTX-decomposed font tables. The repo has been dormant since October 2014 and adds no additional source files beyond what is in googlefontdirectory-hg.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- The upstream sources are **VFB-only**, which is not compatible with gftools-builder
- Creating an override config.yaml is not feasible because gftools-builder cannot process VFB files

## Open Questions

- Where did the Version 1.001 binary come from? Marc Foley (m4rc1e) may know, as he authored PR #780 in August 2017. The VFB source may have been compiled locally with FontLab and post-processed.

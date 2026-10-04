# Della Respira -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `dellarespira/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `METADATA_comments.txt` | Metadata | N/A |

The `src/` directory contains only `METADATA_comments.txt` -- no original design sources. No `.glyphs`, `.ufo`, `.designspace`, `.sfd`, or `.vfb` files are present.

## Designer

Nathan Willis. Della Respira is a serif display typeface, a revival of the Della Robbia typeface by American Type Founders (ATF). Date added to Google Fonts: 2012-04-04.

## Original Source

The actual font source was maintained on Launchpad at `lp:revivalism-fonts` (https://launchpad.net/revivalism-fonts/) using Bazaar (bzr) version control. The Launchpad project page is still accessible. Bazaar VCS is not compatible with the Google Fonts toolchain.

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/dellarespira` (created 2014-07-16 by Mikhail Kashkin). It contains only TTX-decomposed font table files (the binary .ttf decompiled into XML), not actual editable font sources. The repo has 11 commits, all related to CI/Travis setup and TTX file organization.

## google/fonts History

The font binary has not been updated since the initial commit (`90abd17b4`) of the google/fonts repository on 2015-03-07. No gftools-packager updates or font refreshes have occurred.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- No buildable design sources are available in googlefontdirectory-hg or the librefonts mirror
- The original Launchpad/Bazaar source is the true upstream but uses a VCS not compatible with the Google Fonts toolchain
- A config.yaml cannot be created for this family

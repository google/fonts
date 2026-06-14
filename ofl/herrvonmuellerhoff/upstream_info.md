# Herr Von Muellerhoff -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `herrvonmuellerhoff/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `HerrVonMuellerhoff-Regular-TTF.sfd` | FontForge SFD | No (not supported by gftools-builder) |
| `Herr Von Muellerhoff-Regular-OTF.vfb` | FontLab binary | No |
| `HerrVonMuellerhoff-Regular.otf` | Compiled binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata | N/A |

The source directory contains an SFD file (FontForge Spline Font Database) and a VFB file (FontLab proprietary binary). While FontForge can compile fonts from SFD, gftools-builder and fontmake do not support SFD as an input format. Neither format is compatible with the gftools-builder toolchain (which requires `.glyphs`, `.ufo`, or `.designspace`). The `.otf` file is a compiled binary, not a design source.

## Designer

Alejandro Paul of Sudtipos. Copyright: "(c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name \"Herr Von Mullerhoff\"" (note the misspelling "Mullerhoff" vs "Muellerhoff" in the reserved font name). This is a handwriting/display font.

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/herrvonmuellerhoff` with a single commit:
- `f49091c` (2014-10-17) by hash3g

The repo contains the same SFD/VFB sources, TTX table dumps, and metadata files. It adds no additional design sources beyond what is in googlefontdirectory-hg.

## google/fonts History

The font binary was added in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HerrVonMuellerhoff-Regular.ttf`, 46624 bytes) has never been modified since. The `VERSIONS.txt` records "Version 1.000".

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- The SFD and VFB source formats are not supported by gftools-builder
- A config.yaml cannot be created for this family with the current source formats

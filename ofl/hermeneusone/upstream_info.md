# Hermeneus One -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `hermeneusone/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `HermeneusOne-Regular.vfb` | FontLab binary | No |
| `HermeneusOne-Regular-OTF.vfb` | FontLab binary | No |
| `HermeneusOne-Regular-TTF.vfb` | FontLab binary | No |
| `HermeneusOne-Regular.otf` | Compiled binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata | N/A |

The source directory contains three VFB files (FontLab proprietary binary format) and a compiled OTF binary. VFB files cannot be processed by gftools-builder, fontmake, or fontc. No `.glyphs`, `.ufo`, or `.designspace` files exist.

## Designer

Pablo Impallari and Rodrigo Fuenzalida. Hinting by Igino Marini (v1.2, November 2011). Copyright: "(c) 2012, Pablo Impallari (www.impallari.com|impallari@gmail.com) and Rodrigo Fuenzalida (www.rfuenzalida.com), with Reserved Font Name Hermeneus."

Hermeneus One is a Grecian-style serif display font. The FONTLOG.txt references the project page at `http://www.impallari.com/projects/overview/hermeneus`.

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/hermeneusone` with a single commit:
- `20a3262` (2014-10-17) by hash3g: "update .travis.yml"

The repo contains the same VFB sources, TTX table dumps, and metadata files. It adds no additional design sources beyond what is in googlefontdirectory-hg.

## google/fonts History

The font binary was added in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HermeneusOne-Regular.ttf`, 132940 bytes) has never been modified since.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- All source files are VFB format (FontLab proprietary binary), not supported by gftools-builder
- To build from these sources, VFB would need conversion to UFO or .glyphs format first
- A config.yaml cannot be created for this family with the current source formats

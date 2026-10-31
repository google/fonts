# Averia Libre -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `averialibre/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `METADATA_comments.txt` | Metadata | N/A |

The `src/` directory contains only `METADATA_comments.txt` -- no original design sources. The font was created algorithmically (see below), so no traditional editable sources exist.

## Designer

Dan Sayers -- http://iotic.com/averia/

The Averia font family was created by algorithmically averaging the outlines of all 725 OFL fonts from Google Fonts (as of November 2011). There are no traditional editable design sources -- the font outlines were generated programmatically using FontForge.

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/averialibre` with a single commit:
- `091de18` (2014-10-17) by hash3g: "update .travis.yml"

The repo contains TTX-decomposed font data (6 styles: Regular, Bold, Italic, BoldItalic, Light, LightItalic) and metadata files. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist. The TTX files represent v1.001 of the font.

## google/fonts History

1. `90abd17` (2015-03-07) -- Initial commit of the google/fonts repo (bulk import, v1.001)
2. `fc10731` (2017-08-07) -- "hotfix-averialibre: v1.002 added" (PR #837 by Marc Foley). Updated all 6 TTF files and DESCRIPTION/METADATA.
3. Several metadata-only commits thereafter (METADATA.pb format changes, language support updates)

The googlefontdirectory-hg and librefonts sources correspond to v1.001, while google/fonts serves v1.002. The v1.002 hotfix (PR #837) had an empty PR body, providing no upstream reference. The updated binaries were likely produced by Marc Foley directly.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- No gftools-builder compatible sources exist (TTX files are not a supported input format)
- An override config.yaml cannot be created because there are no `.glyphs`, `.ufo`, or `.designspace` sources
- This is inherent to the font's nature -- it was created through algorithmic averaging, not traditional font design

# Averia Sans Libre -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `averiasanslibre/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `METADATA_comments.txt` | Metadata | N/A |

The `src/` directory contains only `METADATA_comments.txt` -- no original design sources. The font was created algorithmically (see below), so no traditional editable sources exist.

## Designer

Dan Sayers -- http://iotic.com/averia/

The Averia font family was created by algorithmically averaging the outlines of all 725 OFL fonts from Google Fonts (as of November 2011). The original was built with FontForge (per nameID 3: "FontForge : AveriaSansLibre-Regular : 13-11-2011"). No SFD or other editable sources are available in any known repository.

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/averiasanslibre` with a single commit:
- `280f9a5` (2014-10-17) by hash3g: "update .travis.yml"

The repo contains decomposed TTX files for all 6 styles, plus metadata files (FONTLOG.txt, OFL.txt, METADATA.json). No `.glyphs`, `.ufo`, `.designspace`, `.sfd`, or `.vfb` files exist. The TTX files represent v1.001 of the font.

## google/fonts History

1. `90abd17` (2015-03-07) -- Initial commit (v1.001 TTFs)
2. `0f81bc9` (2017-08-07) -- "hotfix-averiasanslibre: v1.002 added (#838)" by Marc Foley. Updated all 6 TTFs with minor size changes.

The googlefontdirectory-hg and librefonts sources correspond to v1.001, while google/fonts serves v1.002. The upstream repo was never updated to reflect v1.002.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- No gftools-builder compatible sources exist (TTX files are not a supported input format)
- An override config.yaml cannot be created because there are no `.glyphs`, `.ufo`, or `.designspace` sources
- This is inherent to the font's nature -- it was created through algorithmic averaging, not traditional font design

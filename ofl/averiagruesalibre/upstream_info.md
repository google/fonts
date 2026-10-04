# Averia Gruesa Libre -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

## Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `averiagruesalibre/src/`

### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `METADATA_comments.txt` | Metadata | N/A |

The `src/` directory contains only `METADATA_comments.txt` -- no original design sources. The font was created algorithmically (see below), so no traditional editable sources exist.

## Designer

Dan Sayers (i@iotic.com) -- http://iotic.com/averia/

The Averia font family is unique in that it was created algorithmically by averaging the outlines of all 725 Google Web Fonts (as of November 2011). The "source" is essentially the averaging algorithm output, not a traditional font editor project. The original was built with FontForge (per nameID 3: "FontForge : AveriaGruesaLibre-Regular : 13-11-2011").

## librefonts Mirror

A mirror exists at `https://github.com/librefonts/averiagruesalibre` with a single visible commit:
- `507ebb4` (2014-10-17) -- "update .travis.yml" by hash3g

The repo contains TTX files (decomposed TTF tables using fontTools 2.4) and metadata files (FONTLOG.txt, DESCRIPTION.en_us.html, METADATA.json, OFL.txt). No `.glyphs`, `.ufo`, `.designspace`, `.sfd`, or `.vfb` files exist. The TTX files represent v1.001 of the font.

## google/fonts History

- **Initial addition**: Part of the initial commit (`90abd17b`) to google/fonts on 2015-03-07 (v1.001 TTFs)
- **Last font update**: PR #836 ("hotfix-averiagruesalibre: v1.002 added", merged 2017-05-08, by Marc Foley) -- updated the binary from v1.001 to v1.002

The googlefontdirectory-hg and librefonts sources correspond to v1.001, while google/fonts serves v1.002. The v1.002 update was a hotfix applied directly and never reflected in any upstream repo.

## Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- No gftools-builder compatible sources exist (TTX files are not a supported input format)
- An override config.yaml cannot be created because there are no `.glyphs`, `.ufo`, or `.designspace` sources to reference
- This is inherent to the font's nature -- it was created through an algorithmic averaging process rather than traditional font design

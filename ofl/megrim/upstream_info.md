# Megrim — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Megrim are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `megrim/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Megrim-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Megrim.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Megrim.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The SFD file was created 2010-05-05 and last modified 2011-04-28.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/megrim, created on 2014-07-16 under the `librefonts` organization (a third-party archive). The repo contains a single commit:
- `274ef53` (2014-10-17, author: hash3g) — "update .travis.yml"

**Contributors**: vitalyvolkov, xen — neither is the original font designer (Daniel Johnson).

The repository contains TTX-decomposed tables of the TrueType binary at root level, the SFD/VFB sources in `src/`, a `.travis.yml` for fontbakery CI (outdated), and metadata files.

## Original Designer

**Daniel Johnson** (il.basso.buffo@gmail.com). His personal page was listed as `http://io.debian.net/~danielj/` in the FONTLOG. No personal GitHub repository was found for Daniel Johnson under this font name. The librefonts/megrim archive appears to be the only GitHub repository containing the source files.

### FONTLOG Changelog
- 2010-05-11: Initial release
- 2010-07-02: Improved lowercase Icelandic glyphs; added more glyphs with diacritics
- 2010-08-31: Added stylistic alternate set (ss01); added Turkish glyphs

The SFD file's modification timestamp (2011-04-28) aligns with the font binary version string (20110427).

## Onboarding History

Megrim was added to Google Fonts on 2011-05-04 (per `date_added`). The font was part of the initial bulk import into the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary has never been updated since the initial import.

**Font version**: 20110427

The font predated the current GitHub-based workflow — no PRs were associated with its onboarding.

## Build Configuration

No `config.yaml` exists and none can be created. The only editable design source is a FontForge SFD file, plus a FontLab VFB file. Neither format is supported by gftools-builder, which requires .glyphs, .ufo, or .designspace sources. The legacy `.travis.yml` used the old `fontbakery-build.py` pipeline (circa 2014).

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/megrim"
  commit: "274ef534110a60534a520038400a8db0b3abd976"
}
```

No `config_yaml` field is included because the sources are in SFD/VFB formats not compatible with gftools-builder.

**Confidence**: HIGH — The librefonts/megrim repo is the only known GitHub repository for this font, and it contains the correct SFD source matching the compiled binary. The single commit (`274ef53`) is the only possible reference.

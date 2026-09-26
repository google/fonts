# Lustria — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Lustria are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lustria/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Lustria-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Lustria-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Lustria-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge) and VFB (FontLab) formats, which are not supported by gftools-builder.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/lustria, created on 2014-07-16 under the `librefonts` GitHub organization. It contains a single commit (`a796e0e874e34d163ac3aceb3f6014af1ef66d3c`) dated 2014-10-17, authored by `hash3g <hash3g@gmail.com>` with the message "update .travis.yml". The repo is not archived and not a fork.

**Contributors**: vitalyvolkov, xen

The repository contains TTX decomposed tables of the TTF binary at root level, plus the SFD/VFB sources in `src/`, a `.travis.yml` for CI using the legacy `fontbakery-build.py` pipeline, and metadata files (FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html).

The METADATA_comments.txt file references `~/googlefontdirectory/` paths, indicating this font was processed using the original Google Fonts directory tooling (font-optimizer, subset.py) before the current repository structure was established.

## Onboarding History

Lustria was added to Google Fonts on 2012-01-18 (per `date_added` in METADATA.pb). The font was included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland), which migrated the entire collection into the current structure.

The font binary (`Lustria-Regular.ttf`, 37,400 bytes) has never been updated since the initial commit. Its SHA-256 hash is `8b50753779d151674dcc74bdf9cdde1e788d8fb2b9ace8fb183a0def0f7361ce`.

**Designer**: MADType (Matthew Desmond, mattdesmond@gmail.com, www.madtype.com)

## Build Configuration

No `config.yaml` exists and none can be created. The only available sources are SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder. The legacy `.travis.yml` used the `fontbakery-build.py` pipeline with FontForge and fontcrunch, which is no longer the standard build system.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lustria"
  commit: "a796e0e874e34d163ac3aceb3f6014af1ef66d3c"
}
```

No `config_yaml` field is needed because the sources are SFD-only and cannot be built with gftools-builder.

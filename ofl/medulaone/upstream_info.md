# Medula One — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Medula One are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `medulaone/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `MedulaOne-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `MedulaOne-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `MedulaOne-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge, 269 KB) and VFB (FontLab, 102 KB) formats, which are not supported by gftools-builder.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/medulaone, created on 2014-07-16 by Mikhail Kashkin (@xen) as part of the `librefonts` organization's effort to create per-family repositories from the earlier googlefontdirectory collection.

The repo has 12 commits total (all from 2014):

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `71bda1c` | 2014-07-16 | Mikhail Kashkin (@xen) | Move medulaone font files to separate repository |
| `9559bbd` | 2014-10-17 | hash3g | update .travis.yml (HEAD) |

All commits after the initial one were Travis CI configuration updates. The source files (SFD, VFB) were never modified after the initial commit.

**Contributors**: Mikhail Kashkin (@xen), hash3g

The `src/VERSIONS.txt` indicates "Version 1.002".

## Onboarding History

Medula One was added to Google Fonts on 2011-12-19 (per `date_added` in METADATA.pb). The font file was included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07). The font binary was never modified after the initial commit.

The `librefonts/medulaone` repository was created on 2014-07-16, approximately 2.5 years after the font was added to Google Fonts, confirming the librefonts repo is a post-hoc archive.

**Designer**: LatinoType (Luciano Vergara, luciano@latinotype.com)
**Copyright**: Copyright (c) 2011

## Build Configuration

No `config.yaml` exists and none can be created. The only source files are SFD (FontForge) and VFB (FontLab) formats, neither of which is supported by gftools-builder. The `.travis.yml` used the legacy `fontbakery-build.py` tool.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/medulaone"
  commit: "9559bbd73be136d236851c03e0050708315aef2e"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder. The commit `9559bbd` is HEAD of master and the source files are identical to the initial commit.

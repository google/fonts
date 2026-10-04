# Love Ya Like A Sister - Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Confidence**: LOW

## Source Repository

The original design sources for Love Ya Like A Sister are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `loveyalikeasister/src/`.

### Source Files in googlefontdirectory-hg

- `LoveYaLikeASister-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `LoveYaLikeASister.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `LoveYaLikeASister.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are in SFD and VFB legacy formats only. No `.glyphs`, `.ufo`, or `.designspace` files are present. These formats are not compatible with gftools-builder.

## METADATA.pb Analysis

No source block exists in METADATA.pb. The current file contains only basic metadata (name, designer, license, category, fonts, subsets, classifications).

## Upstream Repository (librefonts archive)

**Repository URL**: https://github.com/librefonts/loveyalikeasister
**Repository type**: Archive/mirror (librefonts organization -- an archival project that extracted font files from the old `googlefontdirectory` into individual GitHub repositories)

The repository contains TTX decompositions of the font binary and the same SFD/VFB source files found in the googlefontdirectory-hg monorepo. No `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` files exist.

### Git history

The repository was created on 2014-07-16 by Mikhail Kashkin (xen/m@xen.ru) with commit message "Move loveyalikeasister font files to separate repository". All subsequent commits (11 total, last on 2014-10-17) were by Vitaly Volkov (hash3g) updating the Travis CI configuration.

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| `41b8b1e` | 2014-10-17 | hash3g | update .travis.yml |
| `0ebd3a1` | 2014-10-06 | hash3g | Rename fontbakery |
| `ae687bd` | 2014-09-19 | hash3g | Update .travis.yml |
| ... (8 more Travis CI updates) | | | |
| `b02575c` | 2014-07-16 | Mikhail Kashkin | Move loveyalikeasister font files to separate repository |

Neither contributor is the original designer (Kimberly Geswein).

### Version mismatch

The SFD source file in the repo declares version 1.003, while the compiled TTF binary in google/fonts reports version 1.002. This indicates the SFD was modified after the binary was originally compiled, making the SFD a newer (and different) version than what was used to produce the google/fonts binary.

## Onboarding History

- **date_added**: 2011-07-06 -- the font was added to Google Fonts
- The google/fonts repository initial commit was on 2015-03-07, which was a bulk import of all existing fonts
- The font binary (`LoveYaLikeASister.ttf`) has only been touched in two commits:
  1. `90abd17` (2015-03-07) -- Initial commit (bulk import)
  2. `76adaf1` (2021-11-01) -- Deploy commit by m4rc1e (repository restructuring, binary hash unchanged)
- SHA-256 of the binary: `4fbe2c1fa647de5a415acac7b2b6491542fe9767b6199719a3bd77a7cf35eb0d` (identical across both commits)

### Font binary metadata (from TTF name table)

- Version: 1.002 2007
- Copyright: "Copyright (c) 2011 by Kimberly Geswein. All rights reserved."
- Unique ID: "FontForge 2.0 : Love Ya Like A Sister Regular : 18-10-2011"
- Designer: Kimberly Geswein
- Vendor URL: http://www.kimberlygeswein.com
- Designer URL: http://www.kimberlygeswein.com
- License: SIL Open Font License 1.1

The font was compiled using FontForge on 2011-10-18.

## Designer Context

Kimberly Geswein is a prolific handwriting font designer with 22 font families in Google Fonts. She does not appear to have a GitHub account. Her fonts were typically created in FontLab or FontForge (VFB/SFD formats), predating the modern .glyphs/.ufo workflow. No designer-maintained upstream repository was found for this font.

## Build Configuration

The source files are SFD (FontForge) and VFB (FontLab) formats only. These are not compatible with gftools-builder. Creating an override `config.yaml` is not feasible because:
1. SFD files are not supported as source inputs by gftools-builder/fontmake
2. VFB files are proprietary FontLab format and not supported either
3. The SFD version (1.003) does not match the binary version (1.002), so even if conversion were possible, it would produce a different font

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/loveyalikeasister"
  commit: "41b8b1e41883c6ef530bece6c906ab917a90387e"
}
```

No `config_yaml` field is included because the sources are SFD-only and not gftools-builder compatible.

## Conclusion

The librefonts/loveyalikeasister repository is an archival mirror, not a true upstream. The font lacks modern design sources needed for gftools-builder compilation. The SFD version (1.003) does not match the binary version (1.002), indicating the sources were modified after the binary was originally compiled. Confidence is LOW because the librefonts repo is an archival mirror with a version mismatch.

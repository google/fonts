# McLaren — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

## Source Repository

The source files for McLaren are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `mclaren/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `McLaren-Regular.vfb` | FontLab VFB | Original source (proprietary, not buildable with gftools) |
| `McLaren-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF |
| `McLaren-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting |
| `McLaren-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable sources are three VFB files (FontLab Studio format), which are proprietary binary files not supported by gftools-builder or fontc.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/mclaren, created on 2014-07-16 under the `librefonts` organization. The repo contains a single commit:
- `7031b7b` (2014-10-17) — "update .travis.yml"

The librefonts/mclaren repository was created after the font was already in Google Fonts. This is a common pattern for the "librefonts" organization, which hosted TTX-decompiled sources for Google Fonts families — not the original upstream source but rather a decomposed archive.

The repo also contains TTX dumps of the TTF and OTF versions, a `.travis.yml` using `fontbakery-build.py` (legacy), and `src/VERSIONS.txt` recording version 1.000.

## Onboarding History

McLaren was added to Google Fonts on 2012-08-13 (per `date_added`). The font file appeared in the google/fonts repository's initial commit (`90abd17b4`, 2015-03-07), which was the mass import of the entire library. The font binary has never been updated since.

**Designer**: Brian J. Bonislawsky (Astigmatic/AOETI, astigma@astigmatic.com)
**GitHub**: https://github.com/astigmatic (exists but has only 2 generic repos, no font sources)
**Font version**: 1.000 (per VERSIONS.txt) / 1.001 (per copyright string)

## Build Configuration

No `config.yaml` exists and none can be created. The source files are exclusively in VFB format (FontLab Studio proprietary format). There is no way to create a config.yaml for gftools-builder without first converting the sources to an open format (.glyphs, .ufo, or .designspace).

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/mclaren"
  commit: "7031b7bdfd833221535738903fe1ea50f1772436"
  branch: "master"
}
```

No `config_yaml` field is included because the repository contains only VFB (FontLab) source files not compatible with gftools-builder.

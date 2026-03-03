# McLaren — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (VFB-only sources, no gftools-builder compatibility)

## METADATA.pb Source Block (current)

No source block exists in METADATA.pb. The current file only contains basic metadata:

```
name: "McLaren"
designer: "Astigmatic"
license: "OFL"
category: "DISPLAY"
date_added: "2012-08-13"
fonts {
  name: "McLaren"
  style: "normal"
  weight: 400
  filename: "McLaren-Regular.ttf"
  post_script_name: "McLaren-Regular"
  full_name: "McLaren"
  copyright: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"McLaren\""
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
```

## Repository Analysis

**Repository**: [librefonts/mclaren](https://github.com/librefonts/mclaren)
**Default branch**: master
**Created**: 2014-07-16
**Last pushed**: 2014-10-17
**Archived**: No

The repository contains a single commit:
- `7031b7b` (2014-10-17): "update .travis.yml"

### Repository structure:

```
├── DESCRIPTION.en_us.html
├── FONTLOG.txt
├── METADATA.json
├── OFL.txt
├── .travis.yml
├── McLaren-Regular.ttf.*.ttx (TTX table dumps of the TTF)
└── src/
    ├── McLaren-Regular.vfb         (original source)
    ├── McLaren-Regular-OTF.vfb     (merged contours for OTF)
    ├── McLaren-Regular-TTF.vfb     (TrueType outlines with hinting)
    ├── McLaren-Regular.otf.*.ttx   (TTX table dumps of the OTF)
    ├── METADATA_comments.txt       (subsetting/processing commands)
    └── VERSIONS.txt                (version info: v1.000)
```

### Source files

The only source files are three `.vfb` files (FontLab Studio format). These are proprietary binary files that cannot be processed by gftools-builder or fontc. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files were found.

The repository also contained TTX dumps (XML representations of compiled font tables) for both the TTF and OTF versions, but these are not buildable sources — they are decompiled representations of the binary fonts.

The `.travis.yml` was configured to use `fontbakery-build.py`, an older build system, not gftools-builder.

## Onboarding History

McLaren was added to Google Fonts on 2012-08-13 according to the `date_added` field. The font file appeared in the google/fonts repository's initial commit (`90abd17b4`, dated 2015-03-07), which was a mass import of the entire Google Fonts library.

The font binary (`McLaren-Regular.ttf`) has never been updated since the initial commit — no subsequent commits in google/fonts modified the font file.

The librefonts/mclaren repository was created on 2014-07-16, after the font was already in Google Fonts. This is a common pattern for the "librefonts" organization, which hosted TTX-decompiled sources for Google Fonts families. These repositories were not the original upstream source but rather a decomposed archive of the shipped fonts.

## Build Configuration

**Config status**: None (no config.yaml exists)
**Build compatibility**: Not gftools-builder compatible

The source files are exclusively in VFB format (FontLab Studio proprietary format). There is no way to create a config.yaml for gftools-builder without first converting the sources to an open format (.glyphs, .ufo, or .designspace).

An override config.yaml cannot be created because there are no source files in a format that gftools-builder can process.

## Findings

1. **VFB-only sources**: The upstream repository only contains `.vfb` files (FontLab Studio format), which are not compatible with gftools-builder or fontc. The sources would need to be converted to an open format before a build pipeline could be established.

2. **Single commit repository**: The librefonts/mclaren repo has exactly one commit (`7031b7b`), which is simply a Travis CI configuration update. The repo was likely auto-generated from the Google Fonts library rather than being a true upstream source.

3. **No designer GitHub presence**: Brian J. Bonislawsky (Astigmatic) has a GitHub account (`astigmatic`) but it has only 2 generic repositories, neither of which contains font sources. The original design sources likely remain with the designer in FontLab format.

4. **Font never updated**: The binary font file has not been modified since the initial google/fonts commit. The font remains at version 1.001 (per the copyright string) or 1.000 (per VERSIONS.txt).

5. **Source block can be added but status remains incomplete**: A source block pointing to librefonts/mclaren with the single commit hash can be added, but no config_yaml can be provided due to the VFB-only source format.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/mclaren"
  commit: "7031b7bdfd833221535738903fe1ea50f1772436"
  branch: "master"
}
```

Note: The `config_yaml` field is intentionally omitted because the repository contains only VFB (FontLab) source files, which are not compatible with gftools-builder. No override config.yaml can be created for the same reason. The source block documents the repository and commit for reference purposes, but a functional build pipeline cannot be established without source format conversion.

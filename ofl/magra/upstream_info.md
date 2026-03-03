# Magra -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD-only sources)

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic metadata (name, designer, license, category, date_added, fonts, subsets) with no `source { }` block.

## Repository Analysis

**Repository**: https://github.com/librefonts/magra
**Organization**: librefonts (created 2013-10-20)
**Repo created**: 2014-07-16
**Last push**: 2014-10-17

The repository was created under the `librefonts` GitHub organization, which served as a historical home for Google Fonts source files before the `googlefonts` organization became the standard location. No `googlefonts/magra` or `fontfuror/magra` repository exists. The designer's GitHub account (`fontfuror`) only has one repository: `fontfuror/Enriqueta`.

### Commit History (12 commits total)

| Commit | Date | Message |
|--------|------|---------|
| dc47090 | 2014-10-17 | update .travis.yml |
| f27f5a3 | 2014-10-06 | Rename fontbakery |
| 345872b | 2014-09-19 | Update .travis.yml |
| c7ce334 | 2014-09-15 | Update .travis.yml |
| fe0ae28 | 2014-09-14 | Installing ttfautohint from ppa |
| cfb6c52 | 2014-09-12 | Added raw=True to VDMX and FFTM |
| a84d38e | 2014-09-11 | update .travis.yml |
| c1fa02b | 2014-08-22 | Travis.yml update |
| fc59995 | 2014-08-22 | Travis.yml update |
| 6a5ad24 | 2014-08-21 | Travis.yml update |
| f3d052a | 2014-08-19 | Added .travis.yml |
| 905fba1 | 2014-07-16 | Move magra font files to separate repository |

The initial commit (905fba1) moved the font files from a prior location into this separate repository. All subsequent commits (11 of 12) only modified Travis CI configuration files -- no source file changes were ever made in this repository.

### Source Files

The repository contains source files in legacy formats only:

- `src/Magra-Regular.vfb` -- Original FontLab source with contour overlaps
- `src/Magra-Regular-OTF.vfb` -- Merged contours for OTF output
- `src/Magra-Bold-OTF.vfb` -- Merged contours for Bold OTF output
- `src/Magra-Regular-TTF.sfd` -- FontForge TrueType outlines with hinting
- `src/Magra-Bold-TTF.sfd` -- FontForge TrueType outlines with hinting

There are **no** `.glyphs`, `.ufo`, or `.designspace` source files. The sources are exclusively VFB (FontLab, proprietary binary format) and SFD (FontForge format).

### Other Files

The repository also contains TTX-decomposed font tables (`.ttx` files) for both Regular and Bold weights in TrueType and OpenType formats, a METADATA.json file, FONTLOG.txt, OFL.txt, and a DESCRIPTION.en_us.html file.

## Onboarding History

Magra was added to Google Fonts on 2012-01-11 (per `date_added` in METADATA.pb). The font files were included in the initial commit of the google/fonts repository (90abd17b4, dated 2015-03-07 by Dave Crossland), which migrated the entire Google Fonts collection into the current repository structure. The font binary files have never been updated since that initial commit.

No pull requests were associated with the addition of Magra to Google Fonts -- it predated the current PR-based workflow.

### Font Details

- **Designer**: Viviana Monsalve / FontFuror (www.fontfuror.com)
- **Copyright**: Copyright (c) 2011, FontFuror (info@fontfuror.com)
- **Version**: 1.001
- **Weights**: Regular (400) and Bold (700)
- **File sizes**: Regular: 45,536 bytes, Bold: 44,500 bytes

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the sources are in VFB and SFD formats, which are not compatible with gftools-builder.

The FONTLOG.txt indicates the font was originally built from FontLab VFB files. The TrueType TTF files were likely generated from the SFD files (FontForge format), with hinting adjustments applied. The Travis CI configuration used `fontbakery-build.py` (an older build tool, now superseded by gftools-builder).

An override config.yaml cannot be created for this font because:
1. The sources are VFB (proprietary FontLab format) and SFD (FontForge format)
2. gftools-builder requires .glyphs, .ufo, or .designspace sources
3. The VFB files would need to be converted to a modern format first

## Findings

1. **No source block in METADATA.pb**: The current METADATA.pb has no `source { }` block at all.
2. **Repository identified**: The upstream repository is `librefonts/magra` (accessible and not archived).
3. **SFD-only sources**: The repository contains only VFB and SFD source files. These are legacy formats not supported by gftools-builder.
4. **No config.yaml possible**: An override config.yaml cannot be created without first converting the sources to a modern format (.glyphs, .ufo, or .designspace).
5. **Commit hash**: The latest commit `dc47090` is appropriate for referencing, as no source files were modified after the initial commit -- all subsequent commits only updated Travis CI configuration.
6. **Static font**: The font has not been updated since its initial addition to Google Fonts in 2012.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/magra"
  commit: "dc47090320b21439c1a97594548890ccd86a42e3"
  branch: "master"
}
```

Note: The `config_yaml` field is omitted because no config.yaml exists and one cannot be created from the available SFD/VFB sources. The source block documents the upstream repository and its latest commit for reference purposes, even though the sources cannot currently be rebuilt with gftools-builder.

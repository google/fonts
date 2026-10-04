# Magra — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Magra are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `magra/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Magra-Regular.vfb` | FontLab VFB | Original source with contour overlaps (proprietary, not buildable) |
| `Magra-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Magra-Bold-OTF.vfb` | FontLab VFB | Merged contours for Bold OTF output |
| `Magra-Regular-TTF.sfd` | FontForge SFD | TrueType outlines with hinting (not gftools-builder compatible) |
| `Magra-Bold-TTF.sfd` | FontForge SFD | TrueType outlines with hinting |
| `Magra-Regular.otf` | Compiled OTF binary | Not a design source |
| `Magra-Bold.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The sources are exclusively VFB (FontLab, proprietary binary format) and SFD (FontForge format).

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/magra, created on 2014-07-16 under the `librefonts` GitHub organization. The repo has 12 commits total, all from 2014. The initial commit (`905fba1`, 2014-07-16) moved the font files from a prior location, and all 11 subsequent commits only modified Travis CI configuration — no source file changes were ever made.

The designer's GitHub account (`fontfuror`) only has one repository: `fontfuror/Enriqueta`. No `googlefonts/magra` repository exists.

### Commit History Highlights

| Commit | Date | Message |
|--------|------|---------|
| `905fba1` | 2014-07-16 | Move magra font files to separate repository |
| `dc47090` | 2014-10-17 | update .travis.yml (HEAD) |

## Onboarding History

Magra was added to Google Fonts on 2012-01-11 (per `date_added` in METADATA.pb). The font files were included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary files have never been updated since that initial commit.

**Designer**: Viviana Monsalve / FontFuror (www.fontfuror.com)
**Copyright**: Copyright (c) 2011, FontFuror (info@fontfuror.com)
**Version**: 1.001
**Weights**: Regular (400) and Bold (700)
**File sizes**: Regular: 45,536 bytes, Bold: 44,500 bytes

No pull requests were associated with the addition of Magra to Google Fonts — it predated the current PR-based workflow.

## Build Configuration

No `config.yaml` exists and none can be created. The sources are in VFB (proprietary FontLab format) and SFD (FontForge format), which are not compatible with gftools-builder. The FONTLOG.txt indicates the font was originally built from FontLab VFB files. The `.travis.yml` used the legacy `fontbakery-build.py` pipeline.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/magra"
  commit: "dc47090320b21439c1a97594548890ccd86a42e3"
  branch: "master"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder. The latest commit `dc47090` is appropriate for referencing, as no source files were modified after the initial commit.

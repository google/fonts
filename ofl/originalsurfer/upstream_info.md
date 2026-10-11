# Original Surfer — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The original design sources for Original Surfer were found in the `googlefontdirectory-hg` monorepo. The sources are FontLab VFB files (proprietary format, not buildable with gftools-builder). No canonical designer-owned GitHub repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `originalsurfer/src/`
- **Buildable**: No — legacy formats only (.vfb)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OriginalSurfer-Regular.vfb` | FontLab VFB | Original source with contour overlaps |
| `OriginalSurfer-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `OriginalSurfer-Regular-TTF.vfb` | FontLab VFB | TrueType hinting adjustments |
| `OriginalSurfer-Regular.otf` | Compiled binary | Not a design source |

All design sources are in FontLab VFB format (proprietary binary). No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2011-12-07
- **Copyright**: "Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Original Surfer\""

## Investigation Details

### GitHub Search

GitHub was searched for "OriginalSurfer", "original-surfer font", and "astigmatic font". Two repositories were found: `librefonts/originalsurfer` and `google-fonts-bower/originalsurfer-bower`. Neither is a canonical designer-owned repository. No Astigmatic-owned GitHub account was found.

### Designer Profile

No GitHub user account was found for "astigmatic", "AOETI", or "Bonislawsky". The Astigmatic website (`www.astigmatic.com`) was unreachable due to an expired SSL certificate. Brian J. Bonislawsky appears to have published multiple fonts through Google Fonts (including Sacramento, Oregano) but does not maintain a public source code repository for them.

### Librefonts Mirror

The `librefonts/originalsurfer` repository contains the same VFB source files as the googlefontdirectory-hg monorepo. This is a librefonts mirror, not a canonical designer-owned repository. The FONTLOG listed the 3 VFB source files as the original source files.

## Conclusion

The original design sources for Original Surfer are preserved in the `googlefontdirectory-hg` monorepo as FontLab VFB files. These are proprietary binary files not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

# Oregano — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The original design sources for Oregano were found in the `googlefontdirectory-hg` monorepo. The sources are FontLab VFB files (proprietary format, not buildable with gftools-builder). No canonical designer-owned GitHub repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oregano/src/`
- **Buildable**: No — legacy formats only (.vfb)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Oregano-Regular.vfb` | FontLab VFB | Original source with contour overlaps |
| `Oregano-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Oregano-Regular-TTF.vfb` | FontLab VFB | TrueType hinting adjustments |
| `Oregano-Italic.vfb` | FontLab VFB | Original source with contour overlaps |
| `Oregano-Italic-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Oregano-Italic-TTF.vfb` | FontLab VFB | TrueType hinting adjustments |
| `Oregano-Regular.otf` | Compiled binary | Not a design source |
| `Oregano-Italic.otf` | Compiled binary | Not a design source |

All design sources are in FontLab VFB format (proprietary binary). No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-08-13
- **Copyright**: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Oregano\""

## Investigation Details

### GitHub Search

GitHub was searched for "Oregano font Astigmatic", "Oregano font Brian Bonislawsky", and "astigmatic font". The only result for "astigmatic font" was `googlefonts/SacramentoFont`, which is a separate Astigmatic font. No Oregano-specific repository was found under any Astigmatic-related account.

### Designer Profile

No GitHub user account was found for "astigmatic", "AOETI", or "Bonislawsky". The Astigmatic website (`www.astigmatic.com`) was unreachable due to an expired SSL certificate.

### Librefonts Mirror

The `librefonts/oregano` repository contains the same VFB source files as the googlefontdirectory-hg monorepo. This is a librefonts mirror, not a canonical designer-owned repository. The FONTLOG listed the 6 VFB source files as the original source files.

## Conclusion

The original design sources for Oregano are preserved in the `googlefontdirectory-hg` monorepo as FontLab VFB files. These are proprietary binary files not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

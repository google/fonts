# Parisienne — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The original design sources for Parisienne were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `parisienne/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Parisienne-Regular.vfb` | FontLab VFB | Original source with contour overlaps |
| `Parisienne-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Parisienne-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting adjustments |
| `Parisienne-Regular-TTF.sfd` | FontForge SFD | TrueType variant |
| `Parisienne-Regular.otf` | Compiled binary | Not a design source |

All primary design sources are in FontLab VFB format. The SFD file is a FontForge variant for TrueType output. No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Google Fonts date added**: 2012
- **Copyright**: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI)"

## Investigation Details

The FONTLOG.txt described three VFB source files matching those found in the monorepo: the original source with overlaps, an OTF variant with merged contours, and a TTF variant with hinting adjustments.

Web searches were conducted for a GitHub repository under Astigmatic, googlefonts/ParisienneFont, and related variations. The only Astigmatic-attributed font found on GitHub under googlefonts was `googlefonts/SacramentoFont`. No dedicated Parisienne repository was found.

The DESCRIPTION.en_us.html contained no upstream repository link.

## Conclusion

The original design sources for Parisienne are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

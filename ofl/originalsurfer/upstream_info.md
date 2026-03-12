# Original Surfer — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/originalsurfer`, which is a librefonts mirror containing VFB (FontLab) source files. No designer-owned GitHub repository was found for Astigmatic (Brian J. Bonislawsky). No METADATA.pb changes were made.

## Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2011-12-07
- **Copyright**: "Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Original Surfer\""

## Search Results

### GitHub Search

GitHub was searched for "OriginalSurfer", "original-surfer font", and "astigmatic font". Two repositories were found: `librefonts/originalsurfer` and `google-fonts-bower/originalsurfer-bower`. Neither is a canonical designer-owned repository. No Astigmatic-owned GitHub account or Oregano/OriginalSurfer-specific repository was found.

### Designer Profile

No GitHub user account was found for "astigmatic", "AOETI", or "Bonislawsky". The Astigmatic website (`www.astigmatic.com`) was unreachable due to an expired SSL certificate. Brian J. Bonislawsky appears to have published multiple fonts through Google Fonts (including Sacramento, Oregano) but does not maintain a public source code repository for them.

### Librefonts Mirror

The `librefonts/originalsurfer` repository was found on GitHub. Its `src/` directory contains:
- `OriginalSurfer-Regular.vfb` — original FontLab VFB source
- `OriginalSurfer-Regular-OTF.vfb` — FontLab VFB with merged contours for OTF
- `OriginalSurfer-Regular-TTF.vfb` — FontLab VFB with TrueType hinting adjustments
- Various TTX decompiled OTF and TTF binary files

This is a librefonts mirror, not a canonical designer-owned repository. The FONTLOG listed these exact 3 VFB source files as the original source files.

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository with Glyphs or UFO sources exists for Original Surfer. The original sources were FontLab VFB files, preserved only in the librefonts mirror. No METADATA.pb changes were made.

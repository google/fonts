# Oregano — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/oregano`, which is a librefonts mirror containing VFB (FontLab) source files. No designer-owned GitHub repository was found for Astigmatic (Brian J. Bonislawsky). No METADATA.pb changes were made.

## Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-08-13
- **Copyright**: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Oregano\""

## Search Results

### GitHub Search

GitHub was searched for "Oregano font Astigmatic", "Oregano font Brian Bonislawsky", and "astigmatic font". The only result for "astigmatic font" was `googlefonts/SacramentoFont`, which is a separate Astigmatic font. No Oregano-specific repository was found under any Astigmatic-related account.

### Designer Profile

No GitHub user account was found for "astigmatic", "AOETI", or "Bonislawsky". The Astigmatic website (`www.astigmatic.com`) was unreachable due to an expired SSL certificate.

### Librefonts Mirror

The `librefonts/oregano` repository was found on GitHub. Its `src/` directory contains:
- `Oregano-Regular.vfb` — original FontLab VFB source
- `Oregano-Regular-OTF.vfb` — FontLab VFB with merged contours for OTF
- `Oregano-Regular-TTF.vfb` — FontLab VFB with TrueType hinting adjustments
- `Oregano-Italic.vfb` — original FontLab VFB source
- `Oregano-Italic-OTF.vfb` — FontLab VFB with merged contours for OTF
- `Oregano-Italic-TTF.vfb` — FontLab VFB with TrueType hinting adjustments
- Various TTX decompiled OTF binary files

This is a librefonts mirror, not a canonical designer-owned repository. The FONTLOG listed these exact 6 VFB source files as the original source files.

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository with Glyphs or UFO sources exists for Oregano. The original sources were FontLab VFB files, preserved only in the librefonts mirror. No METADATA.pb changes were made.

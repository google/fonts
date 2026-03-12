# Oldenburg — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/oldenburg`, which is a librefonts mirror containing VFB (FontLab) and SFD (FontForge) source files derived from the original. No designer-owned GitHub repository was found. No METADATA.pb changes were made.

## Family Details

- **Designer**: Nicole Fally (typeface design); Eben Sorkin (spacing and mastering)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2011-12-19
- **Copyright**: "Copyright (c) 2010 by Sorkin Type Co (eben@eyebytes.com) with Reserved Font Name Oldenburgh."

## Search Results

### GitHub Search

GitHub was searched for "Oldenburg font", "Oldenburg font Nicole Fally", and "SorkinType Oldenburg". No matching repositories were found under a designer-owned account. The SorkinType GitHub organization (`github.com/SorkinType`) was inspected directly — Oldenburg was not among its repositories.

### Librefonts Mirror

The `librefonts/oldenburg` repository was found on GitHub. Its `src/` directory contains:
- `Oldenburg-Regular.vfb` — FontLab VFB source (legacy, proprietary format)
- `Oldenburg-Regular-TTF.sfd` — FontForge SFD source
- Various TTX decompiled binary files
- `Oldenburgh-test.html` — a test file

This is a librefonts mirror, not a canonical designer-owned repository. The VFB and SFD formats are legacy source formats, not the preferred UFO or Glyphs formats.

### Description Reference

The DESCRIPTION.en_us.html referred to `http://code.google.com/p/googlefontdirectory/` (the original Google Code repository for Google Fonts, now defunct) as the source location, and listed Eben Sorkin (`sorkineben@gmail.com`) as the contact for contributions.

### FONTLOG

The FONTLOG recorded:
- Nicole Fally completed the design in FontLab VBF (sic) format (9 Dec 2011)
- Eben Sorkin mastered VBF to TTF (13 Dec 2011)

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository with Glyphs or UFO sources exists for Oldenburg. The sources originated as a FontLab VFB file which was then converted to TTF by Eben Sorkin. The original source is preserved only in the librefonts mirror. No METADATA.pb changes were made.

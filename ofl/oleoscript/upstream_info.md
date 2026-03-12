# Oleo Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/oleoscript`, which is a librefonts mirror containing VFB (FontLab) and SFD (FontForge) source files. No designer-owned GitHub repository was found for Soytutype. No METADATA.pb changes were made.

## Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-03-29
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

## Search Results

### GitHub Search

GitHub was searched for "OleoScript font" and "soytutype". No results were returned for either query. GitHub API search for "OleoScript" returned only four repositories: two librefonts mirrors (`librefonts/oleoscript`, `librefonts/oleoscriptswashcaps`) and two Google Fonts bower packaging repositories.

### Soytutype Website

The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused). No active web presence or GitHub profile was found for Soytutype.

### Librefonts Mirror

The `librefonts/oleoscript` repository was found on GitHub. Its `src/` directory contains:
- `OleoScript-Regular-OTF.vfb` — FontLab VFB source
- `OleoScript-Regular-TTF.sfd` — FontForge SFD source
- `OleoScript-Bold-OTF.vfb` — FontLab VFB source
- `OleoScript-Bold-TTF.sfd` — FontForge SFD source
- Various TTX decompiled binary files

This is a librefonts mirror, not a canonical designer-owned repository.

### FONTLOG

The FONTLOG confirmed source files exist in VFB and SFD formats, with an initial release date of 27 March 2012.

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository with Glyphs or UFO sources exists for Oleo Script. The original sources were in FontLab VFB format (with a FontForge SFD variant for TrueType hinting). Both source formats are legacy formats not suitable for modern font development workflows. No METADATA.pb changes were made.

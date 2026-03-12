# Oleo Script Swash Caps — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with Glyphs or UFO sources was found. The only GitHub repository identified was `librefonts/oleoscriptswashcaps`, which is a librefonts mirror containing VFB (FontLab) and SFD (FontForge) source files. Oleo Script Swash Caps is a companion family to Oleo Script, both by Soytutype. No designer-owned GitHub repository was found. No METADATA.pb changes were made.

## Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-11-12
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

## Search Results

### GitHub Search

GitHub was searched for "OleoScript", "soytutype", and related terms. No designer-owned repositories were found. GitHub API search for "OleoScript" returned only four repositories, all mirrors or packaging repos.

### Soytutype Website

The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused). No active GitHub profile was found for Soytutype.

### Librefonts Mirror

The `librefonts/oleoscriptswashcaps` repository was found on GitHub. Its `src/` directory contains:
- `OleoScriptSwashCaps-Regular-OTF.vfb` — FontLab VFB source
- `OleoScriptSwashCaps-Regular-TTF.sfd` — FontForge SFD source
- `OleoScriptSwashCaps-Bold-OTF.vfb` — FontLab VFB source
- `OleoScriptSwashCaps-Bold-TTF.sfd` — FontForge SFD source
- Various TTX decompiled binary files

This is a librefonts mirror, not a canonical designer-owned repository.

### Relationship to Oleo Script

Oleo Script Swash Caps is explicitly described as a "sister family" to Oleo Script, both produced by Soytutype in 2012. The FONTLOG for this family references the same source file structure as Oleo Script. The source investigation for both families reached the same conclusion.

## Cached Upstream Repos

No cached clone was found in `/mnt/shared/upstream_repos/fontc_crater_cache/` for this family.

## Conclusion

No canonical upstream repository with Glyphs or UFO sources exists for Oleo Script Swash Caps. The original sources were in FontLab VFB format. No METADATA.pb changes were made.

# Oleo Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The original design sources for Oleo Script were found in the `googlefontdirectory-hg` monorepo. The sources are in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oleoscript/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OleoScript-Regular-OTF.vfb` | FontLab VFB | Proprietary binary, not buildable with gftools |
| `OleoScript-Regular-TTF.sfd` | FontForge SFD | Not buildable with gftools-builder |
| `OleoScript-Bold-OTF.vfb` | FontLab VFB | Proprietary binary, not buildable with gftools |
| `OleoScript-Bold-TTF.sfd` | FontForge SFD | Not buildable with gftools-builder |
| `OleoScript-Regular.otf` | Compiled binary | Not a design source |
| `OleoScript-Bold.otf` | Compiled binary | Not a design source |

No UFO or Glyphs sources are available. The VFB files are the primary design sources, with SFD files serving as TrueType-hinting variants.

## Family Details

- **Designer**: soytutype fonts
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-03-29
- **Copyright**: "Copyright (c) 2012, Soytutype (contact@soytutype.com.ar|soytutype@gmail.com), with reserved fontname 'Oleo'"

## Investigation Details

### GitHub Search

GitHub was searched for "OleoScript font" and "soytutype". No results were returned for either query. GitHub API search for "OleoScript" returned only four repositories: two librefonts mirrors (`librefonts/oleoscript`, `librefonts/oleoscriptswashcaps`) and two Google Fonts bower packaging repositories.

### Soytutype Website

The Soytutype website (`www.soytutype.com.ar`) was unreachable (connection refused). No active web presence or GitHub profile was found for Soytutype.

### Librefonts Mirror

The `librefonts/oleoscript` repository contains the same VFB and SFD source files as the googlefontdirectory-hg monorepo. This is a librefonts mirror, not a canonical designer-owned repository.

### FONTLOG

The FONTLOG confirmed source files exist in VFB and SFD formats, with an initial release date of 27 March 2012.

## Conclusion

The original design sources for Oleo Script are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern (UFO/Glyphs) sources exist, and no canonical designer-owned repository was found.

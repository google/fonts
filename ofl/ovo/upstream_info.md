# Ovo — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Ovo is a medium-contrast serif font designed by Nicole Fally, mastered by Eben Sorkin of SorkinType. The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found, and the SorkinType GitHub organization does not contain an Ovo repository.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ovo/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Ovo-Regular.vfb` | FontLab VFB | Original source, proprietary binary |
| `Ovo-Regular-TFF.sfd` | FontForge SFD | TrueType variant (note: filename has "TFF" typo) |
| `Ovo-Regular.otf` | Compiled binary | Not a design source |

The VFB file is the primary design source. No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Nicole Fally (original design), Eben Sorkin (spacing and mastering)
- **License**: OFL
- **Google Fonts date added**: 2011-07-20
- **Copyright**: Sorkin Type Co (www.sorkintype.com)

Nicole Fally created the initial version (v1.000, July 2010) in FontLab VFB format. Eben Sorkin completed the mastering and TTF conversion (v1.002, July 2011). The FONTLOG credits Nicole Fally (nf@t-g-d.at, www.t-g-d.at) as the original designer.

## Investigation Details

### Designer Profiles

- GitHub user search for "nicolefally": no account found
- GitHub repository search for "ovo font": no relevant font repository found
- SorkinType GitHub organization (https://github.com/SorkinType): reviewed all 70+ repositories — no Ovo repository exists

### Librefonts Mirror

The `librefonts/ovo` repository (https://github.com/librefonts/ovo) contains the same VFB and SFD source files as the googlefontdirectory-hg monorepo. The FONTLOG confirms the original design was created in FontLab (VFB format).

## Conclusion

The original design sources for Ovo are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. Neither Nicole Fally nor Eben Sorkin maintain a public GitHub repository for this font.

## References

- librefonts mirror: https://github.com/librefonts/ovo
- SorkinType GitHub: https://github.com/SorkinType
- Google Fonts: https://fonts.google.com/specimen/Ovo

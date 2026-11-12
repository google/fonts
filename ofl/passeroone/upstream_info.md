# Passero One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

The original design sources for Passero One were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found, and the SorkinType GitHub organization does not contain a Passero One repository.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `passeroone/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `PasseroOne-Regular.vfb` | FontLab VFB | Original source, proprietary binary |
| `PasseroOne-Regular-TTF.sfd` | FontForge SFD | TrueType variant |
| `PasseroOne-Regular.otf` | Compiled binary | Not a design source |

The VFB file is the primary design source. No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Viktoriya Grabowska (design), Eben Sorkin (mastering, Sorkin Type Co)
- **License**: OFL
- **Google Fonts date added**: 2011
- **Copyright**: Sorkin Type Co, 2011

## Investigation Details

The FONTLOG.txt described the font history: original design by Viktoriya Grabowska in FontLab VFB format, mastered and spaced by Eben Sorkin (Sorkin Type Co).

The DESCRIPTION.en_us.html pointed to `code.google.com/p/googlefontdirectory/` as the source location, which is the old Google Code project hosting (now defunct, available only as an archive).

Sorkin Type has 67+ repositories on GitHub, but none named PasseroOne, Passero, or Passero-One were found. The font was contributed in August-December 2011, predating GitHub becoming the standard for font source hosting.

## Conclusion

The original design sources for Passero One are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. The font predates GitHub-era source hosting, and no modern repository was ever created.

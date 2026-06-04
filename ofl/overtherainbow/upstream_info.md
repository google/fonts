# Over the Rainbow — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Over the Rainbow is a handwriting font designed by Kimberly Geswein. The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `overtherainbow/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OvertheRainbow.vfb` | FontLab VFB | Original source, proprietary binary |
| `OvertheRainbow-TTF.sfd` | FontForge SFD | TrueType hinting variant |

No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Kimberly Geswein (KG Fonts)
- **License**: OFL
- **Google Fonts date added**: 2011-04-27

## Investigation Details

### Designer Profile

Kimberly Geswein runs KG Fonts (kimberlygeswein.com), where she has produced over 350 fonts since 2006. Her website focuses on commercial font sales and does not link to any GitHub or open-source repositories. No GitHub account was found for "kimberlygeswein".

### GitHub Search

GitHub repository search for "kimberly geswein" found only `googlefonts/indieflower` (a different font by the same designer) and an AUR archive package. Search for "OvertheRainbow" found only `librefonts/overtherainbow` (a librefonts mirror).

### Librefonts Mirror

The `librefonts/overtherainbow` repository (https://github.com/librefonts/overtherainbow) contains the same VFB and SFD source files as the googlefontdirectory-hg monorepo. It is a librefonts mirror, not the designer's canonical repository.

## Conclusion

The original design sources for Over the Rainbow are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

## References

- librefonts mirror: https://github.com/librefonts/overtherainbow
- Designer website: https://kimberlygeswein.com
- Google Fonts: https://fonts.google.com/specimen/Over+the+Rainbow

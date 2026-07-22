# Overlock SC — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Overlock SC is the small-caps companion family to Overlock, designed by Dario Manuel Muhafara of TIPO digital typefoundry (Buenos Aires, Argentina). The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `overlocksc/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

| File | Format | Notes |
|------|--------|-------|
| `OverlockSC-Regular.vfb` | FontLab VFB | Original source, proprietary binary |
| `OverlockSC-Regular-OTF.vfb` | FontLab VFB | OTF variant |
| `OverlockSC-Regular-TTF.sfd` | FontForge SFD | TrueType hinting variant |
| `OverlockSC-Regular.otf` | Compiled binary | Not a design source |

The primary design sources are VFB files. The SFD file is a FontForge variant for TrueType output. No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Dario Manuel Muhafara (TIPO digital typefoundry)
- **License**: OFL
- **Google Fonts date added**: 2011-12-19
- **Related family**: Overlock (shares upstream source and designer)

## Investigation Details

Overlock SC shares its upstream with Overlock. No GitHub account for Dario Manuel Muhafara was found. The TIPO foundry website (tipo.net.ar) does not link to any source repositories.

The `librefonts/overlock` repository (https://github.com/librefonts/overlock) is a librefonts organization mirror containing VFB and SFD sources for both Overlock and Overlock SC. It is not the designer's own repository.

## Conclusion

The original design sources for Overlock SC are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

## References

- librefonts mirror (shared with Overlock): https://github.com/librefonts/overlock
- TIPO foundry: https://www.tipo.net.ar
- Google Fonts: https://fonts.google.com/specimen/Overlock+SC

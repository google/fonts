# Overlock — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Overlock is a display sans-serif designed by Dario Manuel Muhafara of TIPO digital typefoundry (Buenos Aires, Argentina). The original design sources were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned repository was found.

## Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `overlock/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

### Source Files

The family has 6 styles (Regular, Italic, Bold, Bold Italic, Black, Black Italic). Each style has a primary VFB source, an OTF-specific VFB, and an SFD for TrueType output.

**Design sources (VFB — FontLab, proprietary binary):**
- `Overlock-Regular.vfb`, `Overlock-Regular-OTF.vfb`
- `Overlock-Italic.vfb`, `Overlock-Italic-OTF.vfb`
- `Overlock-Bold.vfb`, `Overlock-Bold-OTF.vfb`
- `Overlock-BoldItalic.vfb`, `Overlock-BoldItalic-OTF.vfb`
- `Overlock-Black.vfb`, `Overlock-Black-OTF.vfb`
- `Overlock-BlackItalic.vfb`, `Overlock-BlackItalic-OTF.vfb`

**TrueType hinting variants (SFD — FontForge):**
- `Overlock-Regular-TTF.sfd`, `Overlock-Italic-TTF.sfd`, `Overlock-Bold-TTF.sfd`
- `Overlock-BoldItalic-TTF.sfd`, `Overlock-Black-TTF.sfd`, `Overlock-BlackItalic-TTF.sfd`

**Compiled binaries (not design sources):**
- `Overlock-Regular-OTF.otf`, `Overlock-Italic-OTF.otf`, `Overlock-Bold-OTF.otf`
- `Overlock-BoldItalic-OTF.otf`, `Overlock-Black-OTF.otf`, `Overlock-BlackItalic-OTF.otf`

No UFO or Glyphs sources are available.

## Family Details

- **Designer**: Dario Manuel Muhafara (TIPO digital typefoundry)
- **License**: OFL
- **Google Fonts date added**: 2011-12-19

## Investigation Details

### Designer Profile

Dario Manuel Muhafara operates the TIPO digital typefoundry at tipo.net.ar. The foundry primarily offers proprietary commercial typefaces. No personal GitHub account for Muhafara was found. The TIPO foundry website does not link to any source repositories.

### Librefonts Mirror

The `librefonts/overlock` repository (https://github.com/librefonts/overlock) is a librefonts organization mirror containing the same VFB and SFD source files. It is not the designer's own repository.

## Conclusion

The original design sources for Overlock are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

## References

- librefonts mirror: https://github.com/librefonts/overlock
- TIPO foundry: https://www.tipo.net.ar
- Google Fonts: https://fonts.google.com/specimen/Overlock

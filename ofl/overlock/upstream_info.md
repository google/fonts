# Overlock — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Overlock is a display sans-serif designed by Dario Manuel Muhafara of TIPO digital typefoundry (Buenos Aires, Argentina). It was added to Google Fonts on 2011-12-19.

## Designer

Dario Manuel Muhafara operates the TIPO digital typefoundry at tipo.net.ar. The foundry primarily offers proprietary commercial typefaces. No personal GitHub account for Muhafara was found.

## Upstream Repository Search

The following repositories were identified during the investigation:

- **librefonts/overlock** (https://github.com/librefonts/overlock) — This repository belongs to the `librefonts` GitHub organization, which functions as a mirror/archive for open-source fonts. It is NOT a designer-owned canonical repo. The `src/` folder contains `.vfb` (FontLab VFB) and `.sfd` (FontForge SFD) files along with TTX dumps. No UFO or Glyphs sources were found.

No GitHub account for Dario Manuel Muhafara was found. The TIPO foundry website (tipo.net.ar) does not link to any source repositories and presents its fonts as proprietary commercial work.

## Source File Analysis (librefonts/overlock)

The `src/` folder contains:
- `Overlock-*.vfb` — FontLab VFB source files (proprietary binary format)
- `Overlock-*-TTF.sfd` — FontForge SFD source files
- `Overlock-*-OTF.vfb` / `.otf.*.ttx` — OTF build artifacts

No UFO or Glyphs source files were found. The highest-quality open source format present is SFD.

## Conclusion

No canonical designer-owned upstream repository was found for Overlock. The only GitHub source is the `librefonts/overlock` mirror, which contains VFB and SFD files (no UFO or Glyphs sources). No METADATA.pb source block was added.

## References

- librefonts mirror: https://github.com/librefonts/overlock
- TIPO foundry: https://www.tipo.net.ar
- Google Fonts: https://fonts.google.com/specimen/Overlock

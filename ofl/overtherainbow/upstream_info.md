# Over the Rainbow — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Over the Rainbow is a handwriting font designed by Kimberly Geswein. It was added to Google Fonts on 2011-04-27. The copyright notice references kimberlygeswein.com.

## Designer

Kimberly Geswein runs KG Fonts (kimberlygeswein.com), where she has produced over 350 fonts since 2006. Her website focuses on commercial font sales and does not link to any GitHub or open-source repositories.

## Upstream Repository Search

The following searches were conducted:

- GitHub user search for "kimberlygeswein": no GitHub account was found
- GitHub repository search for "kimberly geswein": only `googlefonts/indieflower` (a different font by the same designer) and an AUR archive package were found
- GitHub search for "over rainbow font": no designer-owned repository was found
- GitHub search for "OvertheRainbow": only `librefonts/overtherainbow` (a librefonts mirror) was found

## librefonts/overtherainbow Analysis

The repository https://github.com/librefonts/overtherainbow is a librefonts organization mirror. Its `src/` folder contains:
- `OvertheRainbow.vfb` — FontLab VFB source file (proprietary binary format)
- `OvertheRainbow-TTF.sfd` — FontForge SFD source file

No UFO or Glyphs source files were found. This is a librefonts mirror, not the designer's canonical repository.

## Conclusion

No canonical designer-owned upstream repository was found for Over the Rainbow. Kimberly Geswein does not appear to maintain a public GitHub account, and the only source-code repository found is the `librefonts/overtherainbow` mirror, which contains VFB and SFD files only. No METADATA.pb source block was added.

## References

- librefonts mirror: https://github.com/librefonts/overtherainbow
- Designer website: https://kimberlygeswein.com
- Google Fonts: https://fonts.google.com/specimen/Over+the+Rainbow

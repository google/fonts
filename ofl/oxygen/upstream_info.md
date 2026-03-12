# Oxygen — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

Oxygen is a sans-serif font family originally designed for use with the KDE desktop environment, created by Vernon Adams (GitHub: vernnobile). It was added to Google Fonts on 2012-03-29.

## Designer

Vernon Adams (vern@newtypography.co.uk) is an active open-source font designer with a GitHub account at https://github.com/vernnobile (368 followers, 71 repositories). He designed many well-known Google Fonts including Oswald, Muli, Nunito, and Pacifico.

## Canonical Upstream Repository

The canonical upstream repository is **vernnobile/oxygenFont**: https://github.com/vernnobile/oxygenFont

This is the designer's own repository. The README describes the Oxygen Font as "originally aimed as a desktop/gui font for integrated use with the KDE desktop." The repository contains:

- `Oxygen-GoogleWebFont/src/` — SFD source files for the Google Fonts (web font) version:
  - `Oxygen-Regular.sfd`, `Oxygen-Light.sfd`, `Oxygen-Bold.sfd`
- `Oxygen-Monospace/src/` — SFD and UFO sources for the monospace variant (see OxygenMono report)
- `OxygenSans-version-0.2/` and `OxygenSans-version-0.4/` — older milestone versions

Latest commit: `62db0ebe3488c936406685485071a54e3d18473b`

## Source File Analysis

The Oxygen Sans sources in this repository use FontForge SFD format only. No UFO or Glyphs source files exist for the Oxygen Sans weights. The designer subsequently renamed the Oxygen font family to "Comme" (https://github.com/vernnobile/commeFont), which contains full UFO sources, but that is a separate evolution of the design.

## Conclusion

The canonical designer-owned upstream repository is `vernnobile/oxygenFont` at https://github.com/vernnobile/oxygenFont. However, since the Oxygen Sans sources exist only in SFD format (no UFO or Glyphs), no source block was added to METADATA.pb. The newer "Comme" continuation of this design (https://github.com/vernnobile/commeFont) contains UFO sources but represents a different, expanded family.

## References

- Canonical upstream: https://github.com/vernnobile/oxygenFont
- Designer continuation (Comme): https://github.com/vernnobile/commeFont
- Designer GitHub profile: https://github.com/vernnobile
- Google Fonts: https://fonts.google.com/specimen/Oxygen

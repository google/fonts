# Rufina — Upstream Source Investigation

**Designer**: Martin Sommaruga
**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Summary

No canonical upstream repository with UFO or Glyphs source files was found for Rufina. The FONTLOG indicates that sources exist only in VFB and SFD format from the old Google Code repository, which does not qualify as a usable upstream per policy.

## Investigation

The FONTLOG.txt describes two source files:
1. `Rufina-Regular-OTF.vfb` — FontLab VFB format
2. `Rufina-Regular-TTF.sfd` — FontForge SFD format

These sources were described as available from `http://code.google.com/p/googlefontdirectory/`, the old Google Fonts code repository, which is no longer accessible.

Searches were conducted for:
- `Rufina font` by name
- `estudiotrama font`
- `sommaruga typeface`
- `Rufina sommaruga typeface`
- `estudiotrama` GitHub organization/user

No GitHub user or organization named `estudiotrama` was found. The only repositories matching "Rufina" were unrelated (Discord bots, random repos) or the `librefonts/rufina` mirror (skipped per policy).

## Conclusion

No canonical upstream repository with editable UFO or Glyphs sources was found for Rufina. The original sources are in VFB/SFD format only (skip per policy). No source block was added to METADATA.pb.

# Devonshire

## Summary

Devonshire is a handwriting/display typeface designed by Brian J. Bonislawsky (Astigmatic). The only known upstream repo is a librefonts mirror containing TTX-decomposed files and legacy source formats (SFD/VFB). No gftools-compatible sources exist.

## Key Findings

- **Designer**: Astigmatic (Brian J. Bonislawsky)
- **Date added to Google Fonts**: 2011-11-16
- **Repository URL**: https://github.com/librefonts/devonshire
- **Commit**: `7d88bb81c76ccd1b7d48a15ae97a00c45f9ffb01` (single commit "update .travis.yml")
- **Source formats available**: SFD (FontForge), VFB (FontLab), TTX decomposed files
- **config_yaml**: None (not applicable - no gftools-buildable sources)
- **Override config.yaml**: None in google/fonts

## Repository Analysis

The librefonts/devonshire repo is a mirror repository created by Mikhail Kashkin. It contains:
- TTX-decomposed font tables (the binary .ttf decompiled into XML)
- `src/Devonshire-Regular-TTF.sfd` - FontForge source
- `src/Devonshire-Regular-OTF.vfb` - FontLab Studio source (binary, proprietary format)
- Standard metadata files (FONTLOG.txt, METADATA.json, OFL.txt)

The repo has a single commit in its history (after unshallowing): `7d88bb8 update .travis.yml`.

The FONTLOG.txt in google/fonts mentions two VFB source files as the canonical sources, indicating the font was originally designed in FontLab Studio.

## google/fonts History

The font binary has not been updated since the initial commit (90abd17b4) of the google/fonts repository. The source block was added in commit 9a14639f3 (2026-02-25) as part of a batch update.

## Status

- **repository_url**: Correct (https://github.com/librefonts/devonshire)
- **commit**: `7d88bb8` is the only/latest commit in the repo
- **config_yaml**: N/A - SFD/VFB sources are not gftools-builder compatible
- **Overall**: missing_config (SFD-only sources, not gftools-builder compatible)

## Recommendation

Status should remain `missing_config` with the note that sources are SFD/VFB format only. The font would need to be converted to .glyphs or .ufo format and a config.yaml created before it could be built with gftools-builder.

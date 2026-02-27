# Investigation: Germania One

## Summary

Germania One is a display typeface designed by John Vargas Beltran, blending German fraktur and Bauhaus sans-serif forms. It was added to Google Fonts on 2012-01-18 and was part of the initial bulk import of the google/fonts repository. The upstream repository is https://github.com/librefonts/germaniaone, a single-commit archive containing TTX decompositions and legacy VFB/SFD source files. No gftools-builder compatible sources exist, so no config.yaml is possible. The METADATA.pb currently has no source block.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Germania One |
| **Designer**      | John Vargas Beltran |
| **Repository URL**| https://github.com/librefonts/germaniaone |
| **Commit Hash**   | `73d401d495adf37b1af75a5dca9cb5cdb046b05d` |
| **Config YAML**   | none (SFD/VFB-only sources) |
| **Branch**        | master |
| **Status**        | no_config_possible |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Current State

No source block exists. The METADATA.pb contains only basic metadata:
- Name: "Germania One"
- Designer: "John Vargas Beltran"
- License: OFL
- Category: DISPLAY
- Date added: 2012-01-18
- Single font file: `GermaniaOne-Regular.ttf`
- Subsets: menu, latin, latin-ext

### Onboarding History in google/fonts

The font was added in commit `90abd17b4` ("Initial commit", 2015-03-07 by Dave Crossland). This was a bulk import of the entire Google Fonts library into the repository. The font was originally added to the Google Fonts catalog on 2012-01-18, before this repository existed. There have been no font file updates since the initial commit -- only metadata changes (METADATA.json to .pb conversions, language support, stroke/classification updates).

### Upstream Repository

The repo at https://github.com/librefonts/germaniaone (cached at `upstream_repos/fontc_crater_cache/librefonts/germaniaone`) contains:
- Single commit: `73d401d` ("update .travis.yml")
- This is a librefonts archive repo with squashed history

### Source Files

The repo contains only legacy format sources:
- `src/GermaniaOne-Regular-TTF.sfd` -- FontForge SFD file
- `src/GermaniaOne-Regular-OTF.vfb` -- FontLab VFB file
- TTX decompositions of the TrueType and OpenType binaries
- No `.glyphs`, `.ufo`, or `.designspace` files

The FONTLOG.txt in google/fonts mentions three original source files:
1. `GermaniaOne-Regular-OTF.vfb` -- Merged contours for OTF
2. `GermaniaOne-Regular-TTF.vfb` -- TrueType outlines with hinting
3. `GermaniaOne-Regular.vfb` -- Original source with components

Note: The TTF VFB was converted to SFD in the librefonts archive, and only the OTF VFB was preserved in VFB format.

Since the sources are SFD and VFB only, gftools-builder cannot process them. No config.yaml is possible.

### Designer Information

- **John Vargas Beltran** (john.vargasbeltran@gmail.com)
- Website: www.johnvargasbeltran.com
- The font was designed as a hybrid between historical fraktur and Bauhaus geometric sans-serif forms

### Copyright Information

"Copyright (c) 2011 by John Vargas Beltran (john.vargasbeltran@gmail.com), with Reserved Font Name 'Germania One'"

## Conclusion

Germania One has an identifiable upstream repository (librefonts/germaniaone), but it only contains legacy SFD/VFB source files. A source block can be added to METADATA.pb with the repository URL and commit hash, but no config.yaml can be provided since gftools-builder does not support SFD or VFB sources.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/germaniaone"
  commit: "73d401d495adf37b1af75a5dca9cb5cdb046b05d"
}
```

**Status**: no_config_possible
**Confidence**: HIGH

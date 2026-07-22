# Investigation: Geostar

## Summary

Geostar is a display serif font designed by Joe Prince (Admix Designs), added to Google Fonts on 2011-08-10. The font was part of the initial bulk import of the google/fonts repository. The upstream repository is https://github.com/librefonts/geostar, a single-commit archive containing TTX decompositions and legacy source files (SFD, VFB). No gftools-builder compatible sources exist, so no config.yaml is possible. The METADATA.pb currently has no source block.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Geostar |
| **Designer**      | Joe Prince |
| **Repository URL**| https://github.com/librefonts/geostar |
| **Commit Hash**   | `ca481fdb49204442916697e3d7b1cf6fda792b77` |
| **Config YAML**   | none (SFD/VFB-only sources) |
| **Branch**        | master |
| **Status**        | no_config_possible |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Current State

No source block exists. The METADATA.pb contains only basic metadata:
- Name: "Geostar"
- Designer: "Joe Prince"
- License: OFL
- Category: DISPLAY
- Date added: 2011-08-10
- Single font file: `Geostar-Regular.ttf`

### Onboarding History in google/fonts

The font was added in commit `90abd17b4` ("Initial commit", 2015-03-07 by Dave Crossland). This was a bulk import of the entire Google Fonts library into the repository. The font was originally added to the Google Fonts catalog on 2011-08-10, before this repository existed. There have been no font file updates since the initial commit -- only metadata changes (METADATA.json to .pb conversions, language support, stroke/classification updates).

### Upstream Repository

The repo at https://github.com/librefonts/geostar (cached at `upstream_repos/fontc_crater_cache/librefonts/geostar`) contains:
- Single commit: `ca481fd` ("update .travis.yml")
- This is a librefonts archive repo with squashed history

### Source Files

The repo contains only legacy format sources:
- `src/Geostar-Regular-TTF.sfd` -- FontForge SFD file
- `src/Geostar-Regular.vfb` -- FontLab VFB file
- TTX decompositions of the TrueType and OpenType binaries
- No `.glyphs`, `.ufo`, or `.designspace` files

Since the sources are SFD and VFB only, gftools-builder cannot process them. No config.yaml is possible.

### Copyright Information

The font copyright states: "Copyright (c) 2011, Admix Designs (http://www.admixdesigns.com joe@admixdesigns.com) with Reserved Font Name Geostar."

## Conclusion

Geostar has an identifiable upstream repository (librefonts/geostar), but it only contains legacy SFD/VFB source files. A source block can be added to METADATA.pb with the repository URL and commit hash, but no config.yaml can be provided since gftools-builder does not support SFD or VFB sources.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/geostar"
  commit: "ca481fdb49204442916697e3d7b1cf6fda792b77"
}
```

**Status**: no_config_possible
**Confidence**: HIGH

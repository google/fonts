# Investigation Report: Fresca

## Summary

Fresca is a sans-serif display font designed by Ivan Moreno of Fontstage, added to Google Fonts on 2011-12-07. The font has never been updated since its initial inclusion in the google/fonts repository. The only known upstream repository is `librefonts/fresca`, which is a mirror containing TTX decompositions and legacy source files (VFB and SFD formats). There are no gftools-builder compatible sources (.glyphs, .ufo, .designspace), so no config.yaml can be created.

## Key Findings

| Field             | Value                                              |
|-------------------|----------------------------------------------------|
| Family Name       | Fresca                                             |
| Designer          | Fontstage (Ivan Moreno)                            |
| Repository URL    | https://github.com/librefonts/fresca               |
| Commit Hash       | ca8ad60bad380c425ebe357ee8a3a71770a849b4           |
| Branch            | master                                             |
| Config YAML       | None (no gftools-builder compatible sources)       |
| Status            | no_config_possible                                 |
| Confidence        | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no source block. The font was added on 2011-12-07, predating the source metadata system.

### google/fonts Commit History

The font binary `Fresca-Regular.ttf` was added in the initial commit (`90abd17b4`) on 2015-03-07 (when the repo was created on GitHub) and has never been modified since. The only other commits touching the fresca directory are metadata updates (METADATA.json removal, METADATA.pb updates for language support, stroke/classifications).

### Upstream Repository

The only upstream repository found is `librefonts/fresca` (https://github.com/librefonts/fresca). This is a librefonts mirror with a single commit (`ca8ad60`, dated 2014-10-17, by hash3g, message: "update .travis.yml").

The repository contains:
- **Source files**: `src/Fresca-Regular-OTF.vfb` (FontLab format) and `src/Fresca-Regular-TTF.sfd` (FontForge format)
- **TTX decompositions**: Multiple `.ttx` files decomposed from the binary
- **Standard metadata**: FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html, METADATA.json

The source files are in legacy formats (VFB, SFD) that are not compatible with gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` files exist.

### Designer Information

The FONTLOG identifies Ivan Moreno (info@fontstage.com, www.fontstage.com) as the type designer. No other GitHub repositories from Fontstage were found.

### Search for Alternative Upstream Repos

- No repository found under googlefonts organization
- No repository found under any other GitHub organization
- GitHub search for "fresca font" returned no relevant results
- The librefonts mirror is the only known repository

## Conclusion

Fresca has a known upstream repository (`librefonts/fresca`) but it only contains legacy VFB/SFD sources, not gftools-builder compatible formats. No config.yaml can be created. The source block should document the repository URL and commit for reference purposes, noting the absence of buildable sources.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/fresca"
  commit: "ca8ad60bad380c425ebe357ee8a3a71770a849b4"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

**Note**: No `config_yaml` field because the repository only contains VFB/SFD sources, which are not gftools-builder compatible. The font binary in google/fonts predates the librefonts mirror and was likely compiled manually from the VFB source.

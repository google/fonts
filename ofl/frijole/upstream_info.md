# Investigation Report: Frijole

## Summary

Frijole is a display font designed by Dave "Squid" Cohen of Sideshow (a DBA of Font Diner, Inc), added to Google Fonts on 2011-12-19. The font has never been updated since its initial inclusion. The only known upstream repository is `librefonts/frijole`, which is a mirror containing a VFB source file (FontLab format). There are no gftools-builder compatible sources, so no config.yaml can be created.

## Key Findings

| Field             | Value                                              |
|-------------------|----------------------------------------------------|
| Family Name       | Frijole                                            |
| Designer          | Sideshow (Dave "Squid" Cohen / Font Diner)         |
| Repository URL    | https://github.com/librefonts/frijole              |
| Commit Hash       | 0e6ba6cfcc631a3db6c6d6e64e523377176e8eec           |
| Branch            | master                                             |
| Config YAML       | None (no gftools-builder compatible sources)       |
| Status            | no_config_possible                                 |
| Confidence        | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no source block. The font was added on 2011-12-19, predating the source metadata system.

### google/fonts Commit History

The font binary `Frijole-Regular.ttf` was added in the initial commit (`90abd17b4`) on 2015-03-07 (when the repo was created on GitHub) and has never been modified since. The only other commits touching the frijole directory are metadata updates (METADATA.json removal, METADATA.pb updates for language support).

### Upstream Repository

The only upstream repository found is `librefonts/frijole` (https://github.com/librefonts/frijole). This is a librefonts mirror with a single commit (`0e6ba6c`, dated 2014-10-17, by hash3g, message: "update .travis.yml").

The repository contains:
- **Source file**: `src/Frijole-Regular-TTF.vfb` (FontLab format)
- **TTX decompositions**: Multiple `.ttx` files decomposed from the binary
- **Standard metadata**: FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html, METADATA.json

The only source file is a VFB (FontLab) binary, which is not compatible with gftools-builder. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist.

### Designer Information

The FONTLOG identifies Font Diner (support@fontdiner.com, www.fontdiner.com) as the designer and masterer. The designer is Dave "Squid" Cohen, working under the Sideshow brand (a DBA of Font Diner, Inc). No dedicated GitHub repositories from Font Diner or Sideshow were found for this font.

### Search for Alternative Upstream Repos

- No repository found under googlefonts organization
- No repository found under fontdiner organization on GitHub
- GitHub search for "frijole font" returned no relevant results
- The librefonts mirror is the only known repository

## Conclusion

Frijole has a known upstream repository (`librefonts/frijole`) but it only contains a legacy VFB source, not a gftools-builder compatible format. No config.yaml can be created. The source block should document the repository URL and commit for reference purposes.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/frijole"
  commit: "0e6ba6cfcc631a3db6c6d6e64e523377176e8eec"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

**Note**: No `config_yaml` field because the repository only contains a VFB source file, which is not gftools-builder compatible. The font binary in google/fonts predates the librefonts mirror and was likely compiled manually from the VFB source.

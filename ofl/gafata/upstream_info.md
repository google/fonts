# Investigation Report: Gafata

## Summary

Gafata is a Latin sans-serif font designed by Lautaro Hourcade, present in Google Fonts since the initial commit (2015-03-07). The upstream repository is `https://github.com/librefonts/gafata`, which contains only legacy source formats: FontForge SFD (`.sfd`) and FontLab VFB (`.vfb`). There is no `config.yaml` and no gftools-builder-compatible sources (.glyphs, .ufo, .designspace). The repository has only a single commit and was likely created as a mirror of the original Google Code hosting.

## Key Findings

| Field              | Value                                                      |
|--------------------|------------------------------------------------------------|
| Family Name        | Gafata                                                     |
| Designer           | Lautaro Hourcade                                           |
| License            | OFL                                                        |
| Date Added         | 2012-10-31                                                 |
| Repository URL     | https://github.com/librefonts/gafata                       |
| Commit Hash        | dcd42b72333486b9704c2d3736e3c26b0346cb67                   |
| Config YAML        | None (SFD-only sources)                                    |
| Source Type         | FontForge SFD, FontLab VFB                                |
| Status             | no_config_possible                                         |
| Confidence         | HIGH                                                       |

## Investigation Details

### Onboarding History

Gafata was present in the google/fonts repository since the initial commit `90abd17b4` (2015-03-07) by Dave Crossland. The font itself was originally released on 2012-10-31. Subsequent commits only modified metadata (METADATA.pb, languages, stroke/classification).

### Upstream Repository

The upstream repository at `https://github.com/librefonts/gafata` is accessible and verified. It was created under the `librefonts` organization, which hosts mirrors of fonts originally from Google Code.

The repository contains a single commit:
- `dcd42b7` (2014-10-17) by hash3g: "update .travis.yml"

This commit is the initial (and only) commit in the repository, adding all files at once including the Travis CI configuration.

### Repository Contents

The repository has the following structure:
- Root level: TTX decomposed font tables (`.ttx` files for various tables like `_c_m_a_p`, `_g_l_y_f`, etc.)
- `src/Gafata-Regular-OTF.vfb` - FontLab VFB source (117 KB)
- `src/Gafata-Regular-TTF.sfd` - FontForge SFD source (221 KB)
- `src/Gafata-Regular-before_ttfautohint.ttf.*` - Pre-autohint TTX decompositions
- `src/Gafata-Regular.otf.*` - OTF TTX decompositions
- `FONTLOG.txt` - Font changelog and history
- `METADATA.json` - Legacy metadata format
- `.travis.yml` - CI configuration

### Source File Assessment

The only editable source files are:
1. **Gafata-Regular-TTF.sfd** (FontForge format) - TrueType outlines with hinting
2. **Gafata-Regular-OTF.vfb** (FontLab format) - Merged contours for OTF

Neither format is compatible with gftools-builder. The VFB format is proprietary (FontLab 5) and the SFD format is FontForge-specific. There are no `.glyphs`, `.ufo`, or `.designspace` files.

The FONTLOG confirms: "There are 2 Source files: 1. Gafata-Regular-OTF.vfb... 2. Gafata-Regular-TTF.sfd..."

### Config.yaml Assessment

No `config.yaml` exists in the upstream repository. Creating an override config.yaml is not possible because gftools-builder cannot process SFD or VFB source files. The sources would need to be converted to a modern format (.glyphs, .ufo, or .designspace) before a config.yaml could be useful.

### Branch Information

The repository has only one branch: `master` (default).

### Historical Context

The FONTLOG documents:
- Initial release: October 30, 2012 (v4.001) by Lautaro Hourcade
- Last update: March 1, 2013 (v4.002) - updated metrics, fixed Z metrics bug
- Original source was hosted on Google Code (now defunct): `http://code.google.com/p/googlefontdirectory/`

## Conclusion

Gafata has a known upstream repository at `librefonts/gafata` with a single commit (`dcd42b7`). However, the sources are in legacy formats (SFD/VFB) that are not compatible with gftools-builder. No config.yaml can be created without first converting the sources to a modern format. The status is `no_config_possible`.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gafata"
  commit: "dcd42b72333486b9704c2d3736e3c26b0346cb67"
  branch: "master"
}
```

Note: No `config_yaml` field is included because the upstream repo only has SFD/VFB sources that are incompatible with gftools-builder.

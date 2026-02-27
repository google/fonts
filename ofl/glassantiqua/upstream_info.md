# Investigation Report: Glass Antiqua

## Summary

**Glass Antiqua** is a display/handwriting serif font designed by Denis Masharov, added to Google Fonts on 2012-02-22. It is a revival of the 1913 typeface "Glass Antiqua" by Genzsch & Heyse. The upstream repository is `librefonts/glassantiqua` on GitHub, a mirror repo created by hash3g in October 2014. The repo contains decomposed TTX files alongside legacy source formats (SFD and VFB). There are no gftools-builder-compatible sources and no config.yaml. The font binary in google/fonts has not been modified since the initial commit.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Glass Antiqua                                                      |
| Designer           | Denis Masharov                                                     |
| Repository URL     | https://github.com/librefonts/glassantiqua                        |
| Commit Hash        | ccc1839b05e9827b7f3a1439d089952908cd0334                           |
| Config YAML        | None (SFD-only sources)                                            |
| Status             | no_config_possible                                                 |
| Confidence         | HIGH                                                               |
| License            | OFL                                                                |
| Date Added         | 2012-02-22                                                         |
| Category           | DISPLAY                                                            |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/glassantiqua/METADATA.pb` contains basic metadata plus stroke/classifications fields. Originally it had no source block. A source block was added in commit `9a14639f3c` (2026-02-25) with the repository URL and commit hash.

### Google Fonts Git History

The font file `GlassAntiqua-Regular.ttf` was added in the initial commit of the google/fonts repository:

- **Commit**: `90abd17b4f97671435798b6147b698aa9087612f` (2015-03-07, Dave Crossland, "Initial commit")
- The font binary has not been modified since then.
- Subsequent commits touched METADATA files only: METADATA.json to METADATA.pb conversion, language support metadata, stroke and classifications additions, HTML formatting.
- **Commit `47a6c224b3`** (2023-08-08, Evan Adams): Added `stroke: "SERIF"` and `classifications: "HANDWRITING"` to METADATA.pb.

A deploy commit (`76adaf1d2`, 2021-11-01, m4rc1e) deleted the files, but this commit is not on the main branch -- it was part of an orphan/dead branch. The main branch retains the original font file from the initial commit.

### Upstream Repository Analysis

**Repository**: https://github.com/librefonts/glassantiqua
**Cached at**: `upstream_repos/fontc_crater_cache/librefonts/glassantiqua`
**GitHub status**: Accessible (HTTP 200)

The repository is a shallow clone containing a single visible commit:
- **Commit**: `ccc1839b05e9827b7f3a1439d089952908cd0334` (2014-10-17, hash3g, "update .travis.yml")

This is a `librefonts` organization mirror -- these repos were created by hash3g as part of a systematic effort to create GitHub mirrors of Google Fonts families with decomposed TTX data and CI configuration.

### Source Files

The repository contains:
- **`src/GlassAntiqua-Regular-TTF.sfd`** -- FontForge SFD source (TTF outlines)
- **`src/GlassAntiqua-Regular-OTF.vfb`** -- FontLab VFB source (binary, proprietary format)
- **`src/GlassAntiqua-Regular.otf.*.ttx`** -- Decomposed OTF TTX tables (including kern table)
- **Root-level `GlassAntiqua-Regular.ttf.*.ttx`** -- Decomposed TTF TTX tables (including GPOS, GDEF, GSUB, DSIG)
- **`src/GlassAntiqua-A.jpg`**, **`src/GlassAntiqua-B.jpg`** -- Reference images (likely scans of original 1913 typeface)
- **`.travis.yml`** -- Travis CI config using fontbakery-build.py
- **`src/VERSIONS.txt`** -- "GlassAntiqua-Regular.ttf: 1.001"

**No gftools-builder-compatible sources** (.glyphs, .ufo, .designspace) exist. The only editable sources are SFD (FontForge) and VFB (FontLab), neither of which is supported by gftools-builder/fontc.

### Config YAML Assessment

No config.yaml exists and none can be created because:
1. There are no .glyphs, .ufo, or .designspace source files
2. SFD and VFB formats are not supported by gftools-builder
3. The TTX files are decomposed table dumps, not proper build sources

### Notable Details

- The font is a revival of a historical typeface ("Glass Antiqua" by Genzsch & Heyse, 1913), found in the Taschen book "Type: A Visual History of Typefaces and Graphic Styles, 1901-1938."
- The src/ directory contains two JPG reference images, likely scans from the original specimen.
- The font has both SERIF stroke and HANDWRITING classification, reflecting its hybrid nature (slab serif + antiqua + cursive calligraphy elements).

## Conclusion

The source block in METADATA.pb is correct. The librefonts mirror is the only known upstream repository. The font sources are SFD/VFB only, making a gftools-builder config.yaml impossible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/glassantiqua"
  commit: "ccc1839b05e9827b7f3a1439d089952908cd0334"
}
```

**Status**: `no_config_possible` -- SFD/VFB-only sources are not compatible with gftools-builder.

# Investigation Report: Give You Glory

## Summary

**Give You Glory** is a handwriting font designed by Kimberly Geswein, added to Google Fonts on 2011-07-13. The upstream repository is `librefonts/giveyouglory` on GitHub, a mirror repo created by hash3g in October 2014. The repo contains decomposed TTX files alongside legacy source formats (SFD and VFB). There are no gftools-builder-compatible sources (.glyphs, .ufo, .designspace) and no config.yaml. The font binary in google/fonts has not been modified since the initial commit.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Give You Glory                                                     |
| Designer           | Kimberly Geswein                                                   |
| Repository URL     | https://github.com/librefonts/giveyouglory                        |
| Commit Hash        | 2787317ad77bac728fea1ca0c4ce7f0d3ba273d5                           |
| Config YAML        | None (SFD-only sources)                                            |
| Status             | no_config_possible                                                 |
| Confidence         | HIGH                                                               |
| License            | OFL                                                                |
| Date Added         | 2011-07-13                                                         |
| Category           | HANDWRITING                                                        |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/giveyouglory/METADATA.pb` contains basic metadata (family name, designer, license, fonts block) but originally had no source block. A source block was added in commit `9a14639f3c` (2026-02-25) with the repository URL and commit hash.

### Google Fonts Git History

The font file `GiveYouGlory.ttf` was added in the initial commit of the google/fonts repository:

- **Commit**: `90abd17b4f97671435798b6147b698aa9087612f` (2015-03-07, Dave Crossland, "Initial commit")
- The font binary has not been modified since then.
- Subsequent commits only touched METADATA files (METADATA.json to METADATA.pb conversion, language support, HTML formatting).

A deploy commit (`76adaf1d2`, 2021-11-01, m4rc1e) appears to have deleted the files, but this commit is not on the main branch -- it was part of an orphan/dead branch. The main branch retains the original font file from the initial commit.

### Upstream Repository Analysis

**Repository**: https://github.com/librefonts/giveyouglory
**Cached at**: `upstream_repos/fontc_crater_cache/librefonts/giveyouglory`
**GitHub status**: Accessible (HTTP 200)

The repository is a shallow clone containing a single visible commit:
- **Commit**: `2787317ad77bac728fea1ca0c4ce7f0d3ba273d5` (2014-10-17, hash3g, "update .travis.yml")

This is a `librefonts` organization mirror -- these repos were created by hash3g as part of a systematic effort to create GitHub mirrors of Google Fonts families with decomposed TTX data and CI configuration.

### Source Files

The repository contains:
- **`src/GiveYouGlory-TTF.sfd`** -- FontForge SFD source (TTF outlines)
- **`src/GiveYouGlory.vfb`** -- FontLab VFB source (binary, proprietary format)
- **`src/GiveYouGlory.otf.*.ttx`** -- Decomposed OTF TTX tables
- **Root-level `GiveYouGlory.ttf.*.ttx`** -- Decomposed TTF TTX tables
- **`.travis.yml`** -- Travis CI config using fontbakery-build.py
- **`src/VERSIONS.txt`** -- "GiveYouGlory.ttf: Version 1.002"

**No gftools-builder-compatible sources** (.glyphs, .ufo, .designspace) exist. The only editable sources are SFD (FontForge) and VFB (FontLab), neither of which is supported by gftools-builder/fontc.

### Config YAML Assessment

No config.yaml exists and none can be created because:
1. There are no .glyphs, .ufo, or .designspace source files
2. SFD and VFB formats are not supported by gftools-builder
3. The TTX files are decomposed table dumps, not proper build sources

## Conclusion

The source block in METADATA.pb is correct. The librefonts mirror is the only known upstream repository. The font sources are SFD/VFB only, making a gftools-builder config.yaml impossible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/giveyouglory"
  commit: "2787317ad77bac728fea1ca0c4ce7f0d3ba273d5"
}
```

**Status**: `no_config_possible` -- SFD/VFB-only sources are not compatible with gftools-builder.

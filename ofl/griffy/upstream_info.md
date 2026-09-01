# Investigation Report: Griffy

## Summary

Griffy is a static display font designed by Dave "Squid" Cohen of Neapolitan (Font Diner, Inc), added to Google Fonts in September 2012. The upstream repository at `librefonts/griffy` contains only VFB (FontLab) sources and TTX decompositions -- there are no gftools-buildable source files (.glyphs, .ufo, .designspace). The only source file is `src/Griffy-Regular-TTF.vfb`. Without buildable sources, no config.yaml is possible. The font has never been updated since its initial commit in the google/fonts repository. The METADATA.pb currently has no source block on the main branch.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Griffy                                                             |
| Repository URL    | https://github.com/librefonts/griffy                               |
| Commit            | `eed85949102ab5baa1a8ca8d6b24239709a76bab`                         |
| Config YAML       | None (VFB-only sources, not buildable with gftools)                |
| Source File       | `src/Griffy-Regular-TTF.vfb`                                       |
| Status            | no_config_possible                                                 |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb on the main branch of google/fonts has no source block:
```
name: "Griffy"
designer: "Neapolitan"
license: "OFL"
category: "DISPLAY"
date_added: "2012-09-06"
fonts {
  name: "Griffy"
  style: "normal"
  weight: 400
  filename: "Griffy-Regular.ttf"
  post_script_name: "Griffy-Regular"
  full_name: "Griffy"
  copyright: "Copyright (c) 2012 by Font Diner, Inc DBA Neapolitan ..."
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
```

Note: A batch commit (`9a14639`, 2026-02-25) on a separate branch added a source block with repository_url and commit hash, but this has not been merged to main.

### Onboarding History in google/fonts

1. **Initial commit** (`90abd17b4`, 2015-03-07): The google/fonts repository was initialized by Dave Crossland with all existing fonts. Griffy was part of this initial import. The font was originally added to Google Fonts on 2012-09-06 per METADATA.pb's `date_added` field.

2. **No subsequent font file updates**: The Griffy-Regular.ttf file has never been updated since the initial import. Only metadata changes have been made (METADATA.pb format updates, language metadata, HTML formatting).

### Upstream Repository Verification

The cached repo at `fontc_crater_cache/librefonts/griffy` is a shallow clone with a single commit:
- **Commit `eed8594`** (2014-10-17): "update .travis.yml" by hash3g

The repository structure:
```
./DESCRIPTION.en_us.html
./FONTLOG.txt
./OFL.txt
./METADATA.json
./Griffy-Regular.ttf.*.ttx    (multiple TTX table decompositions)
./Griffy-Regular.ttf.ttx      (main TTX file)
./src/
  Griffy-Regular-TTF.vfb      (FontLab VFB source, 240 KB)
  METADATA_comments.txt
  VERSIONS.txt                ("Griffy-Regular.ttf: Version 1.000")
```

### Source File Analysis

The repository only contains:
- **VFB file** (`src/Griffy-Regular-TTF.vfb`): FontLab Studio binary format. Not supported by gftools-builder or fontc.
- **TTX files** (root directory): XML decompositions of the TTF, used as an archival format by the librefonts project. Not buildable sources.
- **No .glyphs, .ufo, or .designspace files**: The font cannot be rebuilt with modern tooling without first converting the VFB sources.

### Commit Hash Verification

The commit `eed85949` is the only commit in the upstream repository (shallow clone). The `librefonts/griffy` repo is an archival repository that contains the VFB source and TTX decompositions, set up by hash3g in October 2014. The font itself was created by Font Diner in September 2012.

Since the font was never updated in google/fonts after the initial import, and the upstream repo is purely archival (no buildable sources), this commit correctly represents the state of the upstream repository.

## Conclusion

Griffy has an identifiable upstream repository (`librefonts/griffy`) with a known commit hash, but no gftools-buildable sources. The repository contains only VFB (FontLab) sources, which cannot be used with gftools-builder or fontc. A config.yaml cannot be created without first converting the VFB to a supported format (.glyphs or .ufo).

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/griffy"
  commit: "eed85949102ab5baa1a8ca8d6b24239709a76bab"
}
```

No `config_yaml` field should be added since the upstream repo has no gftools-buildable sources.

**Status**: no_config_possible
**Confidence**: HIGH

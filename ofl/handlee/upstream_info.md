# Investigation Report: Handlee

## Summary

Handlee is a handwriting font designed by Joe Prince (Admix Designs), added to Google Fonts on 2011-12-13. The font was included in the initial commit of the google/fonts repository and has never been updated. The upstream repository is `librefonts/handlee` on GitHub, which contains an SFD (FontForge) source file and a VFB (FontLab) source file. Neither format is compatible with gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` sources exist, making it impossible to create a config.yaml for building.

## Key Findings

| Field | Value |
|---|---|
| **Family Name** | Handlee |
| **Designer** | Joe Prince |
| **Date Added** | 2011-12-13 |
| **Repository URL** | https://github.com/librefonts/handlee |
| **Commit Hash** | d937cfc17b0389d9847b8a865060b7241af7c654 |
| **Config YAML** | None (SFD/VFB-only sources) |
| **Status** | no_config_possible |
| **Confidence** | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has no `source { }` block. The font has a single weight (Regular) with filename `Handlee-Regular.ttf`. Classifications include HANDWRITING and stroke SANS_SERIF.

### Git History in google/fonts

The font binary was added in the initial commit:
- `90abd17b4` (2015-03-07) - "Initial commit" by Dave Crossland

The font file has only been touched once more:
- `76adaf1d2` (2021-11-01) - "deploy: c7e2740188205a85323c7385547f6f59b4f2245a" - gh-pages deployment, not a font update.

The binary has never been updated since the initial commit.

### Upstream Repository

The upstream repository at `https://github.com/librefonts/handlee` (cached at `librefonts/handlee`) has only a single commit:
- `d937cfc17b0389d9847b8a865060b7241af7c654` (2014-10-17) - "update .travis.yml"

The repository contains:
- **Font files**: TTX decompositions of the TTF file (various table-level files)
- **Source files** in `src/`:
  - `Handlee-Regular-TTF.sfd` - FontForge SFD source
  - `Handlee-Regular-OTF.vfb` - FontLab VFB source
  - Various OTF TTX decompositions
- **No gftools-builder compatible sources**: No `.glyphs`, `.ufo`, or `.designspace` files exist
- **No config.yaml**

### Source Compatibility

The source files are SFD (FontForge) and VFB (FontLab) formats. Neither is compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` files. Creating an override config.yaml is not feasible without compatible source files.

### Commit Hash Rationale

The upstream repository has only one commit (`d937cfc`), so this is the only possible commit to reference. The repository predates the google/fonts initial commit.

### librefonts Organization Context

The `librefonts` organization on GitHub hosts decomposed (TTX) versions of many Google Fonts with their original source files. These repos typically have a single commit with Travis CI configuration for automated font building/testing. They serve as archival repositories rather than active development repos.

## Conclusion

Handlee has an identifiable upstream repository at `librefonts/handlee`, but it only contains SFD and VFB sources, making gftools-builder incompatible. The source block should reference the repository and commit, but no config.yaml is possible.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/handlee"
  commit: "d937cfc17b0389d9847b8a865060b7241af7c654"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
}
```

Note: The font binary in google/fonts was compiled from the original SFD/VFB sources. Since these formats are not supported by gftools-builder, no `config_yaml` field should be included.

**Status**: no_config_possible (SFD/VFB-only sources, no gftools-builder compatible files)

# Investigation Report: Homenaje

## Summary

Homenaje is a sans-serif font designed by Constanza Artigas Preller and Agustina Mingote, licensed under OFL. The upstream repository at `https://github.com/googlefonts/Homenaje` contains a single commit (d371ad8, 2025-02-24) by Felipe Sanches that set up the entire repo including a converted .glyphs source and config.yaml. The METADATA.pb source block is complete with repository_url, commit hash, and config_yaml path. The original v1.002 sources (VFB/SFD format) are preserved in the repo's `old/` directory.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Homenaje                                           |
| Designer           | Constanza Artigas Preller, Agustina Mingote        |
| License            | OFL                                                |
| Directory          | ofl/homenaje                                       |
| Repository URL     | https://github.com/googlefonts/Homenaje            |
| Commit Hash        | d371ad8e2f096db1f866c8fdfb9804f90dc39453           |
| Config YAML        | sources/config.yaml                                |
| Status             | **complete**                                       |
| Confidence         | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/homenaje/METADATA.pb` has a complete source block:

```
source {
  repository_url: "https://github.com/googlefonts/Homenaje"
  commit: "d371ad8e2f096db1f866c8fdfb9804f90dc39453"
  config_yaml: "sources/config.yaml"
}
```

The font was added on 2012-01-18 and the copyright references the Homenaje Project Authors with RFN.

### Git History in google/fonts

Key commits affecting the font binary:

1. **90abd17b4** (2015-03-07) by Dave Crossland: "Initial commit" -- original addition
2. **fbcc9a513** (2016-12-02) by Marc Foley: "homenaje: v1.100 added (#458)" -- updated the .ttf from 22,192 to 36,436 bytes, updated copyright, inherited vertical metrics

Source block history:
1. **2423d2aef** (2023-12-14) by Simon Cozens: "Update upstreams" -- added initial `source { repository_url }` block
2. **19cdcec59** (2025-03-31) by Felipe Sanches: "[Batch 1/4] port info from fontc_crater targets list" -- added commit hash and config_yaml path

### Upstream Repository Analysis

The cached repository at `googlefonts/Homenaje` (remote: `https://github.com/googlefonts/Homenaje`) contains:

- **1 commit total**: `d371ad8` (2025-02-24) by Felipe Sanches: "Add sources/config.yaml"
- This single commit created the entire repository contents including:
  - `sources/Homenaje.glyphs` (19,150 lines) -- converted .glyphs source file
  - `sources/config.yaml` -- gftools-builder configuration
  - `old/version-1.002/` -- archive of original v1.002 sources (VFB, SFD, OTF formats)
  - Standard metadata files (OFL.txt, FONTLOG.txt, AUTHORS.txt, etc.)
  - Pre-built `fonts/Homenaje-Regular.ttf`

### Config.yaml Contents

```yaml
sources:
  - Homenaje.glyphs
```

Simple configuration pointing to the single .glyphs source file.

### Source Files

The repository contains both legacy and modern sources:
- **Modern**: `sources/Homenaje.glyphs` -- Glyphs format, compatible with gftools-builder
- **Legacy (old/version-1.002/src/)**: `Homenaje-Regular-OTF.vfb`, `Homenaje-Regular.vfb`, `Homenaje-Regular-TTF.sfd`, `Homenaje-Regular.otf`

### Note on Commit Hash

The commit hash `d371ad8` in METADATA.pb points to the repo setup commit from 2025-02-24, which is the only commit in the repository. This commit was made well after the font was originally onboarded in 2016 (PR #458). The .glyphs file appears to be a conversion from the original VFB sources. Since this is the only commit in the repo and it contains the config.yaml and source files needed for building, the reference is technically correct for build purposes.

## Conclusion

**Status: complete**

The source metadata for Homenaje is complete. The METADATA.pb has a valid repository_url, commit hash, and config_yaml path. The upstream repository contains a .glyphs source file and a properly configured config.yaml. The commit hash references the only commit in the repository, which set up the entire repo including converted sources. All data is consistent and the font can be rebuilt from the referenced sources.

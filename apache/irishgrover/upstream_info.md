# Investigation Report: Irish Grover

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `irishgrover/src/` |
| **Buildable** | No — VFB is proprietary, not compatible with gftools-builder |

The googlefontdirectory-hg monorepo (a git mirror of the original Google Code Mercurial repository) contains the following source files under `irishgrover/src/`:

- `IrishGrover.vfb` — FontLab VFB format (proprietary, not buildable with gftools-builder)
- `METADATA_comments.txt` — metadata only, not a source file

The VFB file is the original design source, but FontLab's .vfb format is proprietary and cannot be used with gftools-builder. Converting to a modern format (.glyphs or .ufo) would require FontLab or a conversion tool, and the result would need verification.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Irish Grover |
| Designer           | Sideshow (Font Diner, Inc) |
| License            | Apache 2.0 |
| Category           | DISPLAY |
| Date Added         | 2011-01-06 |
| Source Types        | VFB (FontLab, proprietary format) |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/irishgrover/`
- **No source block** in METADATA.pb
- **Copyright**: "Copyright (c) 2010 by Font Diner, Inc DBA Sideshow. All rights reserved."

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 90abd17b4 | 2015-03-07 | Dave Crossland | Initial commit |
| daa6505c6 | 2017 | Marc Foley | hotfix-irishgrover: v1.001 added (#777) |

The hotfix renamed `IrishGrover.ttf` to `IrishGrover-Regular.ttf`.

### Designer Context

Font Diner (DBA Sideshow) is a commercial type foundry. The DESCRIPTION.en_us.html describes Irish Grover as "a fun, flamboyant, new display font by Squid." The font was donated to Google Fonts under the Apache license.

### Search for Upstream Repository

No cached upstream repository was found in `upstream_repos/fontc_crater_cache/` for this family. No googlefonts/irishgrover or fontdiner repository with source files exists. The font was contributed directly to Google Fonts without a tracked upstream repository.

## Conclusion

While the googlefontdirectory-hg monorepo preserves the original VFB design source, this proprietary format is not compatible with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) exist, so no config.yaml can be created without first converting the VFB to a supported format.

### Status: no_config_possible
### Confidence: HIGH

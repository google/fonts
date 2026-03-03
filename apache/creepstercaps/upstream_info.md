# Investigation Report: Creepster Caps

## Summary

Creepster Caps is a display font designed by Font Diner, Inc (DBA Sideshow), featuring a horror/Halloween-themed aesthetic. It was added to Google Fonts on 2011-10-24 via the initial commit and has never been updated since. The only cached repository is the `librefonts/creepstercaps` mirror, which contains TTX dumps and a FontForge SFD source file. No dedicated upstream repository with gftools-builder compatible sources exists. There is a related but distinct font "Creepster" (without "Caps") in the OFL directory, which has its own librefonts mirror.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Creepster Caps |
| Designer           | Sideshow (Font Diner, Inc) |
| License            | Apache 2.0 |
| Category           | DISPLAY |
| Date Added         | 2011-10-24 |
| Repository URL     | None (no proper upstream repo) |
| Commit Hash        | N/A |
| Config YAML        | None |
| Source Types        | SFD (FontForge format, in librefonts mirror) |
| Font Version        | 1.000 |
| Status             | no_upstream_repo |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/creepstercaps/`
- **Files**: CreepsterCaps-Regular.ttf, DESCRIPTION.en_us.html, LICENSE.txt, METADATA.pb
- **No source block** in METADATA.pb
- **Font version**: Version 1.000 (from name table)
- **Copyright**: "Copyright (c) 2011 by Font Diner, Inc. All rights reserved."
- **Vendor**: Font Diner, Inc
- **Note**: The copyright says 2011, and the font was added with the initial commit in March 2015

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

Creepster Caps has never been updated since the initial commit. All subsequent commits touching this directory were metadata-only changes (METADATA.pb language data, etc.).

### Relationship to "Creepster" (OFL)

There is a separate font called "Creepster" (without "Caps") in `ofl/creepster/`. That font is also by Font Diner/Sideshow and has a similar horror theme. The OFL version has its own librefonts mirror at `librefonts/creepster` with SFD sources. These are two distinct fonts:
- **Creepster Caps** (Apache 2.0, in `apache/creepstercaps/`) - this investigation
- **Creepster** (OFL, in `ofl/creepster/`) - separate font, already investigated

### Cached Mirror: librefonts/creepstercaps

- **Path**: upstream_repos/fontc_crater_cache/librefonts/creepstercaps
- **URL**: https://github.com/librefonts/creepstercaps
- **Content**: TTX dumps of the binary font, plus SFD source in src/
- **Source files**:
  - `src/CreepsterCaps-Regular-TTF.sfd` - FontForge SFD format
  - TTX table dumps at root level
- **Single commit** by hash3g: "update .travis.yml"
- **Versions file**: Lists Version 1.000

The SFD file header confirms:
- FontName: CreepsterCaps-Regular
- Version: 1.001 (slightly newer than the binary's 1.000)
- Copyright: "Copyright (c) 2011 by Font Diner, Inc. All rights reserved."
- CreationTime: 1319137200 (approx Oct 20, 2011)
- ModificationTime: 1319464871 (approx Oct 24, 2011)

### Search for Upstream Repository

- **No googlefonts/creepstercaps** or similar repository exists
- **No googlefonts/creepster-caps** repository exists
- **fontdiner/fonts** exists but is empty (LICENSE and README.md only)
- The librefonts mirror is the only repository, and it is an automated dump, not a proper upstream

### Config.yaml Assessment

No config.yaml exists. The only source format available is SFD (FontForge), which is not compatible with gftools-builder. The SFD file contains the "-TTF" suffix in its filename, suggesting it was reverse-engineered from the TTF binary rather than being the original design source.

The original design sources were likely in a proprietary format (FontLab .vfb or similar) used by Font Diner and never published.

## Conclusion

Creepster Caps has no proper upstream repository. The librefonts/creepstercaps mirror contains TTX dumps and a FontForge SFD file (likely reverse-engineered), but these are not suitable as a proper upstream. The font was produced by Font Diner and delivered as a compiled binary. No gftools-builder compatible sources or build configuration exist.

### Recommended METADATA.pb Source Block

No source block can be added. There is no upstream repository containing original design sources.

### Status: no_upstream_repo
### Confidence: HIGH

There is no proper upstream repository for this font. The font was created by Font Diner (a commercial foundry) and the original design files were never published to a public repository. The librefonts mirror contains only decompiled/reverse-engineered files.

# Investigation Report: Creepster Caps

## Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `creepstercaps/src/` |
| **Buildable** | No — SFD is not compatible with gftools-builder |

The googlefontdirectory-hg monorepo (a git mirror of the original Google Code Mercurial repository) contains the following source files under `creepstercaps/src/`:

- `CreepsterCaps-Regular-TTF.sfd` — FontForge SFD format (not buildable with gftools-builder)
- `METADATA_comments.txt` — metadata only, not a source file

The SFD file has a `-TTF` suffix in its filename, suggesting it was derived from the compiled TTF binary rather than being the original design source. The SFD header confirms FontName: CreepsterCaps-Regular, Version: 1.001 (slightly newer than the binary's 1.000), Copyright: "Copyright (c) 2011 by Font Diner, Inc. All rights reserved.", with creation/modification dates in October 2011.

No gftools-builder compatible sources (.glyphs, .ufo, .designspace) are present. The original design sources were likely in a proprietary format (FontLab .vfb or similar) used by Font Diner and never published.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Creepster Caps |
| Designer           | Sideshow (Font Diner, Inc) |
| License            | Apache 2.0 |
| Category           | DISPLAY |
| Date Added         | 2011-10-24 |
| Font Version       | 1.000 |
| Status             | no_config_possible |
| Confidence         | HIGH |

## Investigation Details

### Current State in google/fonts

- **Directory**: `apache/creepstercaps/`
- **Files**: CreepsterCaps-Regular.ttf, DESCRIPTION.en_us.html, LICENSE.txt, METADATA.pb
- **No source block** in METADATA.pb
- **Font version**: Version 1.000 (from name table)
- **Copyright**: "Copyright (c) 2011 by Font Diner, Inc. All rights reserved."
- **Vendor**: Font Diner, Inc

### Git History in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| 90abd17 | 2015-03-07 | Dave Crossland | Initial commit |

Creepster Caps has never been updated since the initial commit. All subsequent commits touching this directory were metadata-only changes (METADATA.pb language data, etc.).

### Relationship to "Creepster" (OFL)

There is a separate font called "Creepster" (without "Caps") in `ofl/creepster/`. That font is also by Font Diner/Sideshow and has a similar horror theme. These are two distinct fonts:
- **Creepster Caps** (Apache 2.0, in `apache/creepstercaps/`) — this investigation
- **Creepster** (OFL, in `ofl/creepster/`) — separate font

### Cached Mirror: librefonts/creepstercaps

The librefonts mirror at `https://github.com/librefonts/creepstercaps` contains TTX dumps and the same SFD source file found in googlefontdirectory-hg. Single commit by hash3g: "update .travis.yml". This is an automated dump, not a proper upstream repository.

### Search for Upstream Repository

- No googlefonts/creepstercaps or similar repository exists
- fontdiner/fonts exists but is empty (LICENSE and README.md only)
- Font Diner is a commercial foundry; the original design sources were never made publicly available

### Config.yaml Assessment

No config.yaml can be created. The only source format available is SFD (FontForge), which is not compatible with gftools-builder.

## Conclusion

Creepster Caps has no buildable upstream sources. The googlefontdirectory-hg monorepo and the librefonts mirror both contain only an SFD file (likely reverse-engineered from the TTF) and metadata. The font was produced by Font Diner and delivered as a compiled binary. No gftools-builder compatible sources or build configuration exist.

### Status: no_config_possible
### Confidence: HIGH

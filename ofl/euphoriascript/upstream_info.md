# Investigation Report: Euphoria Script

## Family Metadata
- **Family Name**: Euphoria Script
- **Designer**: Sabrina Mariela Lopez
- **License**: OFL
- **Category**: HANDWRITING
- **Date Added**: 2012-02-08
- **Path in google/fonts**: `ofl/euphoriascript`

## Source Repository
- **Repository URL**: https://github.com/librefonts/euphoriascript
- **Commit**: `c7606fae5a17e051d983269f008dba6e8f4c0c77`
- **Branch**: master
- **Status**: missing_config
- **Confidence**: HIGH

## Investigation Details

### METADATA.pb Analysis
The current METADATA.pb on the google/fonts main branch has no `source {}` block. A source block was prepared in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files") pointing to the librefonts repository.

### Font File History in google/fonts
The TTF file (`EuphoriaScript-Regular.ttf`, 38,424 bytes) was added in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the bulk import that brought all existing Google Fonts into the current repository structure. The font itself dates from 2012 (version 1.002), as indicated by the font's name table and FONTLOG.

The TTF file has never been modified since the initial commit.

### Upstream Repository Analysis
The repository at `https://github.com/librefonts/euphoriascript` is part of the **librefonts** organization, which is an archival/mirror project that decomposed Google Fonts families into TTX (XML) representations alongside their original source files. The repo was created by **hash3g** (hash.3g@gmail.com) on 2014-10-17 and contains exactly one commit (`c7606fa`).

The repository is verified as accessible (HTTP 200).

### Repository Contents
The repo contains:
- **Root level**: TTX decomposition of `EuphoriaScript-Regular.ttf` (glyf, cmap, head, name, etc.)
- **`src/` directory**:
  - `EuphoriaScript-Regular.vfb` - original FontLab source with overlaps
  - `EuphoriaScript-Regular-OTF.vfb` - FontLab source for OTF generation (without overlaps)
  - `EuphoriaScript-Regular-TTF.sfd` - FontForge source used to generate final TTF
  - TTX decompositions of the OTF
  - `METADATA_comments.txt` - subsetting/build comments from the original Google Font Directory
  - `VERSIONS.txt` - records "EuphoriaScript-Regular.ttf: Version 1.002"
- `METADATA.json`, `FONTLOG.txt`, `OFL.txt`, `DESCRIPTION.en_us.html`
- `.travis.yml` - CI config using fontbakery-build.py

### Source File Formats
The original sources are:
- **VFB** (FontLab format) - proprietary binary, not compatible with gftools-builder
- **SFD** (FontForge format) - open format, but not compatible with gftools-builder

There are no `.glyphs`, `.ufo`, or `.designspace` files. The sources are entirely legacy formats.

### Build Configuration
- **No `config.yaml`** exists in the upstream repo
- **No `config.yaml` override** exists in the google/fonts family directory
- The `.travis.yml` references `fontbakery-build.py`, an older build system from 2014
- The `METADATA_comments.txt` shows the original Google Font Directory subsetting workflow using `subset.py`

### Designer Information
- **Sabrina Mariela Lopez** (TypeSenses)
- Contact: typesenses@live.com.ar
- Website: www.typesenses.com (referenced in font metadata)
- No known personal GitHub repository for this font

### About the librefonts Organization
The librefonts GitHub organization is **not** the original designer's repository. It is an archival project that extracted Google Fonts families into individual repos with TTX decompositions. The single commit by hash3g (a Google Fonts infrastructure contributor) confirms this is an automated extraction, not an active development repository.

### Font Details
- **Version**: 1.002
- **Created**: Mon Feb 6 13:07:54 2012 (per head table)
- **Units per Em**: 1250
- **Copyright**: Copyright (c) 2012 Sabrina Mariela Lopez (typesenses@live.com.ar), with Reserved Font Name "Euphoria Script"

## Conclusion

Euphoria Script has a known upstream repository at `https://github.com/librefonts/euphoriascript` with a single commit (`c7606fa`). This is an archival repo, not the original designer's repository. The sources are legacy formats (VFB and SFD) that are not compatible with gftools-builder, so no `config.yaml` can be created. The font has not been updated since its original onboarding in 2012.

### Recommended METADATA.pb Source Block
```
source {
  repository_url: "https://github.com/librefonts/euphoriascript"
  commit: "c7606fae5a17e051d983269f008dba6e8f4c0c77"
}
```

No `config_yaml` field is applicable since the sources are SFD/VFB only.

### Status Summary
- **Repository URL**: Verified (HTTP 200)
- **Commit Hash**: `c7606fae5a17e051d983269f008dba6e8f4c0c77` (only commit in repo)
- **Config**: None (SFD-only sources, not gftools-builder compatible)
- **Overall Status**: missing_config (inherent limitation - legacy sources only)

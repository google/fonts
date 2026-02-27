# Investigation Report: Felipa

## Family Details
- **Family name**: Felipa
- **Designer**: Fontstage (Javier Alcaraz)
- **License**: OFL
- **Category**: Handwriting / Display
- **Date added to Google Fonts**: 2012-02-08
- **Google Fonts path**: `ofl/felipa`

## Source of Truth in google/fonts
- **Binary file**: `Felipa-Regular.ttf` (40,000 bytes)
- **Font version**: Version 1.001
- **Font created date**: 2012-02-03
- **SHA-256**: `d3f07e2669e046acc1030139a4b08046d7eca87c0b477a8cc99ac1c46af84edc`
- **Initial commit in google/fonts**: `90abd17b4f97671435798b6147b698aa9087612f` (2015-03-07, by Dave Crossland) -- this was the initial import of the entire library into the current google/fonts repo structure
- **Binary never modified**: The TTF has not been updated since the initial commit

## Upstream Repository
- **Repository URL**: https://github.com/librefonts/felipa
- **Status**: Accessible (HTTP 200)
- **Commit**: `3489dd2445fc633f3b32485420d9c56998fad093` (only commit in the repo)
- **Commit date**: 2014-10-17
- **Commit author**: hash3g (hash.3g@gmail.com)
- **Commit message**: "update .travis.yml"
- **Branch**: `master`

### Repository Nature
This is a typical **librefonts archive repository**, created by hash3g in October 2014 to preserve sources from the Google Font Directory. The repository has a single commit and contains:

- **Root directory**: TTX files (XML decomposition of the compiled TrueType font tables), plus DESCRIPTION, FONTLOG, OFL.txt, METADATA.json
- **src/ directory**: Original source files
  - `Felipa-Regular-TTF.sfd` (FontForge SFD format, 276 KB)
  - `Felipa-Regular.vfb` (FontLab VFB format, 143 KB -- binary, proprietary)
  - OTF TTX decompositions
  - `METADATA_comments.txt` (subsetting commands from the old Google Font Directory workflow)
  - `VERSIONS.txt` (records "Version 1.001")
- **No compiled font binaries** (.ttf or .otf) in the repo -- only TTX decompositions
- **`.travis.yml`**: Old CI configuration using fontbakery-build.py (now defunct)

### Source File Assessment
- **SFD file** (`Felipa-Regular-TTF.sfd`): FontForge SplineFont Database format. This is a TTF-mastered SFD, not directly usable with gftools-builder.
- **VFB file** (`Felipa-Regular.vfb`): FontLab Studio binary format. Proprietary and not usable with modern open-source toolchains.
- **No `.glyphs`, `.ufo`, or `.designspace` sources**: The font predates modern open-source font development workflows.
- **No `config.yaml`**: Not present and not applicable -- there are no gftools-builder compatible sources.

## FONTLOG Evidence
The FONTLOG in the repository lists:
- Source files: `Felipa-Regular-OTF.vfb` (Mastered OTF source) and `Felipa-Regular-TTF.sfd` (Mastered TTF source)
- Designer: Javier Alcaraz (info@fontstage.com, www.fontstage.com)
- Initial release: 3 February 2012, v1.001

## Commit Hash Verification
Since the upstream repo has only a single commit (`3489dd2`), this is the only possible reference. The commit is dated 2014-10-17, which is after the font was added to Google Fonts (2012-02-08), consistent with librefonts repos being created as post-hoc archives. The font sources in the repo match the font metadata (same version, same copyright, same designer info).

## Current METADATA.pb State
The current METADATA.pb on the `main` branch of google/fonts does **not** have a source block. A source block was added on branch `sources_info_2026-02-25` (commit `9a14639f3`) with:
```
source {
  repository_url: "https://github.com/librefonts/felipa"
  commit: "3489dd2445fc633f3b32485420d9c56998fad093"
}
```

## Recommendation

### Source Block
```
source {
  repository_url: "https://github.com/librefonts/felipa"
  commit: "3489dd2445fc633f3b32485420d9c56998fad093"
}
```

- **No `config_yaml` field** is needed -- the sources are SFD/VFB only, not compatible with gftools-builder.
- **No override `config.yaml`** is needed -- there are no buildable sources (.glyphs/.ufo/.designspace) to configure.

### Status
- **Status**: `complete` (SFD-only sources)
- **Confidence**: HIGH
- **Rationale**: Single-commit archive repo with only SFD/VFB sources. The repo URL is valid, the commit hash is the only commit, and the source files match the font metadata. No config.yaml is possible or needed.

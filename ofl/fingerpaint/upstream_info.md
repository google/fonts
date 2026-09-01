# Investigation Report: Finger Paint

## Family Overview

- **Family name**: Finger Paint
- **Designer**: Ralph du Carrois (Carrois Apostrophe)
- **License**: OFL
- **Category**: Display
- **Date added to Google Fonts**: 2012-09-30
- **Styles**: Regular (1 style, weight 400)
- **Current version in google/fonts**: 1.002

## Upstream Repository

- **URL**: https://github.com/librefonts/fingerpaint
- **Status**: Active (not archived), but dormant since October 2014
- **Default branch**: master
- **Total commits**: 1

### Repository Contents

The repository was created as a single commit on 2014-10-17 by user "hash3g" (hash.3g@gmail.com). It is part of the `librefonts` organization, which hosts TTX decompositions and VFB source files for many Google Fonts families (861 public repos).

The repository contains:
- **Source files**: `src/FingerPaint-Regular.vfb`, `src/FingerPaint-Regular-OTF.vfb`, `src/FingerPaint-Regular-TTF.vfb` (FontLab VFB format)
- **TTX decompositions**: Multiple `.ttx` table files for both TrueType and OpenType versions in both root and `orig/` directories
- **Metadata**: `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- **CI config**: `.travis.yml` (uses fontbakery-build.py, targeting Python 2.7)
- **No gftools-builder compatible sources**: No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files
- **No config.yaml**

### Source File Types

The only editable sources are VFB files (FontLab Studio proprietary format). These are not compatible with gftools-builder and cannot be used for automated rebuilds.

## Commit History in google/fonts

### Initial commit (2015-03-07)
- **Commit**: `90abd17b4` by Dave Crossland
- **Message**: "Initial commit"
- **Font version**: 1.001 (107,404 bytes)
- This was part of a mass initial commit that added many font families to the repository.

### Hotfix v1.002 (2017-05-08)
- **Commit**: `3a2f5cae3` by Marc Foley
- **PR**: [#886](https://github.com/google/fonts/pull/886) - "hotfix-fingerpaint: v1.002 added"
- **Committer**: Dave Crossland
- **Font version**: 1.002 (107,440 bytes)
- Changes: Updated binary font to v1.002, reformatted `DESCRIPTION.en_us.html`, updated `METADATA.pb` (copyright string cleanup, full_name correction)
- The PR body was empty, providing no details about the source of the v1.002 binary

### Key observation

The upstream librefonts repo contains v1.001 sources and was last updated on 2014-10-17. The v1.002 hotfix was applied to google/fonts on 2017-05-08 by Marc Foley, but the upstream repo was never updated. The source of the v1.002 binary is unclear -- it was likely compiled by Marc Foley directly from modified VFB files that were not pushed to the upstream repository.

## Commit Hash Verification

- **Recorded commit**: `cb21d1208d6f0a641a348584627dc058a2f2998a`
- **Commit date**: 2014-10-17
- **This is the only commit in the repository**, so it is trivially the correct reference
- **However**, the binary currently in google/fonts (v1.002) was NOT built from this commit's sources (v1.001). The v1.002 binary was produced externally and submitted via PR #886

## Source Block Assessment

### Current METADATA.pb

The current METADATA.pb in google/fonts does **not** have a source block. A pending source block addition exists in commit `9a14639f3` (not yet merged to main) with:
```
source {
  repository_url: "https://github.com/librefonts/fingerpaint"
  commit: "cb21d1208d6f0a641a348584627dc058a2f2998a"
}
```

### Proposed source block

```
source {
  repository_url: "https://github.com/librefonts/fingerpaint"
  commit: "cb21d1208d6f0a641a348584627dc058a2f2998a"
}
```

No `config_yaml` field is appropriate because:
1. The upstream repo has no `config.yaml`
2. The sources are VFB-only (not compatible with gftools-builder)
3. An override config.yaml is not feasible since there are no `.glyphs`, `.ufo`, or `.designspace` sources to reference

## Status

- **Status**: missing_config
- **Confidence**: HIGH
- **Repository URL**: Verified (https://github.com/librefonts/fingerpaint is accessible)
- **Commit hash**: Verified (only commit in repo)
- **Config**: None possible -- VFB-only sources are not gftools-builder compatible

## Notes

- The font was designed by Ralph du Carrois and mastered by Andreas Eigendorf in 2012
- The upstream repo is a librefonts archive containing TTX decompositions and VFB sources, typical of the early Google Fonts era
- The v1.002 hotfix binary in google/fonts has no corresponding upstream source update
- The designer's website is [carrois.com](http://www.carrois.com)
- To enable automated rebuilds, the VFB sources would need to be converted to `.glyphs` or `.ufo` format, which would require designer involvement

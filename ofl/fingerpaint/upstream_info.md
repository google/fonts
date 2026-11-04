# Finger Paint

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Finger Paint (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/fingerpaint.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  FingerPaint-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/fingerpaint at `39a0edc95f87`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/fingerpaint.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`39a0edc95f87` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/fingerpaint at cb21d1208d6f0a641a348584627dc058a2f2998a:
  src/FingerPaint-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/fingerpaint"
      commit: "cb21d1208d6f0a641a348584627dc058a2f2998a"
    }

## Previous investigation

## Investigation Report: Finger Paint

### Family Overview

- **Family name**: Finger Paint
- **Designer**: Ralph du Carrois (Carrois Apostrophe)
- **License**: OFL
- **Category**: Display
- **Date added to Google Fonts**: 2012-09-30
- **Styles**: Regular (1 style, weight 400)
- **Current version in google/fonts**: 1.002

### Upstream Repository

- **URL**: https://github.com/librefonts/fingerpaint
- **Status**: Active (not archived), but dormant since October 2014
- **Default branch**: master
- **Total commits**: 1

#### Repository Contents

The repository was created as a single commit on 2014-10-17 by user "hash3g" (hash.3g@gmail.com). It is part of the `librefonts` organization, which hosts TTX decompositions and VFB source files for many Google Fonts families (861 public repos).

The repository contains:
- **Source files**: `src/FingerPaint-Regular.vfb`, `src/FingerPaint-Regular-OTF.vfb`, `src/FingerPaint-Regular-TTF.vfb` (FontLab VFB format)
- **TTX decompositions**: Multiple `.ttx` table files for both TrueType and OpenType versions in both root and `orig/` directories
- **Metadata**: `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt`
- **CI config**: `.travis.yml` (uses fontbakery-build.py, targeting Python 2.7)
- **No gftools-builder compatible sources**: No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files
- **No config.yaml**

#### Source File Types

The only editable sources are VFB files (FontLab Studio proprietary format). These are not compatible with gftools-builder and cannot be used for automated rebuilds.

### Commit History in google/fonts

#### Initial commit (2015-03-07)
- **Commit**: `90abd17b4` by Dave Crossland
- **Message**: "Initial commit"
- **Font version**: 1.001 (107,404 bytes)
- This was part of a mass initial commit that added many font families to the repository.

#### Hotfix v1.002 (2017-05-08)
- **Commit**: `3a2f5cae3` by Marc Foley
- **PR**: [#886](https://github.com/google/fonts/pull/886) - "hotfix-fingerpaint: v1.002 added"
- **Committer**: Dave Crossland
- **Font version**: 1.002 (107,440 bytes)
- Changes: Updated binary font to v1.002, reformatted `DESCRIPTION.en_us.html`, updated `METADATA.pb` (copyright string cleanup, full_name correction)
- The PR body was empty, providing no details about the source of the v1.002 binary

#### Key observation

The upstream librefonts repo contains v1.001 sources and was last updated on 2014-10-17. The v1.002 hotfix was applied to google/fonts on 2017-05-08 by Marc Foley, but the upstream repo was never updated. The source of the v1.002 binary is unclear -- it was likely compiled by Marc Foley directly from modified VFB files that were not pushed to the upstream repository.

### Commit Hash Verification

- **Recorded commit**: `cb21d1208d6f0a641a348584627dc058a2f2998a`
- **Commit date**: 2014-10-17
- **This is the only commit in the repository**, so it is trivially the correct reference
- **However**, the binary currently in google/fonts (v1.002) was NOT built from this commit's sources (v1.001). The v1.002 binary was produced externally and submitted via PR #886

### Source Block Assessment

#### Current METADATA.pb

The current METADATA.pb in google/fonts does **not** have a source block. A pending source block addition exists in commit `9a14639f3` (not yet merged to main) with:
```
source {
  repository_url: "https://github.com/librefonts/fingerpaint"
  commit: "cb21d1208d6f0a641a348584627dc058a2f2998a"
}
```

#### Proposed source block

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

### Status

- **Status**: missing_config
- **Confidence**: HIGH
- **Repository URL**: Verified (https://github.com/librefonts/fingerpaint is accessible)
- **Commit hash**: Verified (only commit in repo)
- **Config**: None possible -- VFB-only sources are not gftools-builder compatible

### Notes

- The font was designed by Ralph du Carrois and mastered by Andreas Eigendorf in 2012
- The upstream repo is a librefonts archive containing TTX decompositions and VFB sources, typical of the early Google Fonts era
- The v1.002 hotfix binary in google/fonts has no corresponding upstream source update
- The designer's website is [carrois.com](http://www.carrois.com)
- To enable automated rebuilds, the VFB sources would need to be converted to `.glyphs` or `.ufo` format, which would require designer involvement

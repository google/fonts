# Libre Caslon Display

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Libre Caslon Display (google/fonts at commit `2fe1e8c6b137`). Its
only published source is a FontLab import of the shipped fonts, not a design source
(listed under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the
binary files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/librecaslondisplay.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  LibreCaslonDisplay-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/librecaslondisplay at `2f19dc143214`.
Builds with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/librecaslondisplay.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`2f19dc143214` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/impallari/Libre-Caslon-Display at
  3491f6a9cfde2bc15e736463b0bc7d93054d5da1: source/LibreCaslonDisplay-Regular-TTF.vfb, a
  FontLab import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      commit: "3491f6a9cfde2bc15e736463b0bc7d93054d5da1"
      repository_url: "https://github.com/impallari/Libre-Caslon-Display"
    }

## Previous investigation

## Investigation Report: Libre Caslon Display

**Family name**: Libre Caslon Display
**Directory**: `ofl/librecaslondisplay`
**Date added**: 2017-11-30
**Designer**: Impallari Type (Pablo Impallari, Rodrigo Fuenzalida)
**License**: OFL
**Model**: Claude Opus 4.6

### Summary

Libre Caslon Display is a display-weight serif font designed by Pablo Impallari and Rodrigo Fuenzalida, intended as the headline companion to Libre Caslon Text. The upstream repository uses exclusively FontLab `.vfb` source files, which are not compatible with gftools-builder. No config.yaml can be created since there are no buildable source formats (`.glyphs`, `.ufo`, `.designspace`).

### Upstream Repository

- **URL**: https://github.com/impallari/Libre-Caslon-Display
- **Status**: Active (accessible, unchanged since 2016)
- **Local cache**: `upstream_repos/fontc_crater_cache/impallari/Libre-Caslon-Display`
- **Default branch**: master
- **Repository clean**: Yes (verified)

### Commit History (Upstream)

The upstream repository has only 6 commits, all by Pablo Impallari:

| Hash | Date | Message |
|------|------|---------|
| `3491f6a` | 2016-07-25 | v1.002 |
| `b3d497e` | 2015-07-24 | cosmetics |
| `830fb56` | 2015-07-24 | Improving Description |
| `fa77c97` | 2015-07-24 | Removed RFN |
| `e8f1926` | 2014-12-01 | Uploading v1 |
| `23d1bee` | 2014-12-01 | readme |

The repository has had no new commits since `3491f6a` (v1.002, 2016-07-25). This is the HEAD of master.

### Onboarding to Google Fonts

- **Onboarding commit**: `95b0ecc63` on 2017-11-30 by Marc Foley (m4rc1e)
- **Commit message**: "librecaslondisplay: v1.100 added / Taken from the upstream repo https://github.com/impallari/Libre-Caslon-Display"
- **PR**: #1372, created 2017-11-30, merged 2019-07-10 by Marc Foley
- **PR body**: Contains FontBakery report results and rendering screenshots; confirms the upstream repo URL

The version number in the google/fonts commit message ("v1.100") does not match the upstream version ("v1.002"). According to the FONTLOG, v1.002 was a version number bump "to keep it the same as the text version." The "v1.100" label likely reflects a version assigned during the onboarding/processing workflow rather than a version tag in the upstream repo.

### Binary File Comparison

The binary font file in google/fonts does NOT match any binary in the upstream repository:

| Location | File size |
|----------|-----------|
| google/fonts (onboarded) | 101,384 bytes |
| Upstream at `3491f6a` (v1.002) | 124,204 bytes |
| Upstream at `b3d497e` (cosmetics) | 123,812 bytes |
| Upstream at `e8f1926` (v1) | 124,400 bytes |

The file in google/fonts is significantly smaller (101 KB vs 124 KB), indicating it was processed/rebuilt from the upstream sources before onboarding, likely using Google Fonts tools to strip unnecessary tables or apply font modifications for web serving.

### Commit Hash Verification

The commit hash `3491f6a9cfde2bc15e736463b0bc7d93054d5da1` was recorded in the METADATA.pb source block (added by commit `9a14639f3` on 2026-02-25). This is the latest (and last) commit on the upstream repository. Since the onboarding occurred on 2017-11-30, after this commit (2016-07-25), and there have been no subsequent commits, `3491f6a` is the correct reference commit -- it was the HEAD at the time of onboarding and remains the HEAD today.

### Source Files

At the referenced commit (`3491f6a`), the repository contains:

**Source files (FontLab only)**:
- `source/LibreCaslonDisplay-Regular.vfb`
- `source/LibreCaslonDisplay-Regular-OTF.vfb`
- `source/LibreCaslonDisplay-Regular-TTF.vfb`

**Pre-compiled binaries**:
- `fonts/TTF/LibreCaslonDisplay-Regular.ttf`
- `fonts/OTF/LibreCaslonDisplay-Regular.otf`

There are no `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files. The `.vfb` format is proprietary FontLab format and is not supported by gftools-builder or fontc.

### Config.yaml Assessment

**No config.yaml can be created.** The upstream sources are exclusively in `.vfb` format, which is not compatible with gftools-builder. An override config.yaml would serve no purpose since there are no buildable source files.

### METADATA.pb Source Block

Current state:
```
source {
  repository_url: "https://github.com/impallari/Libre-Caslon-Display"
  commit: "3491f6a9cfde2bc15e736463b0bc7d93054d5da1"
}
```

This is correct and complete for a VFB-only repository. The `config_yaml` field is correctly absent since there are no buildable sources.

### Status

- **Repository URL**: Verified correct
- **Commit hash**: Verified correct (`3491f6a`, HEAD of master, last commit before onboarding)
- **Config.yaml**: Not applicable (VFB-only sources)
- **Overall status**: `missing_config` (VFB-only sources; no path to gftools-builder compatibility without source conversion)
- **Confidence**: HIGH

### Notes

- The font was rebuilt/processed during onboarding (binary sizes differ from upstream), which is expected Google Fonts behavior
- The upstream repo has been completely dormant since July 2016 (no activity in nearly 10 years)
- The version discrepancy ("v1.100" in google/fonts vs "v1.002" in upstream) is a labeling artifact from the onboarding process
- The repository is part of a pair: Libre Caslon Display and [Libre Caslon Text](https://github.com/impallari/Libre-Caslon-Text) are companion families

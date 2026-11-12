# Combo

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Combo (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/combo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Combo-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/combo at `8921bc4f7647`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/combo.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`8921bc4f7647` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/combo at ae46147e06fad7d2d664c2738ae08a9262adbeb1:
  src/Combo-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/combo"
      commit: "ae46147e06fad7d2d664c2738ae08a9262adbeb1"
    }

## Previous investigation

## Combo - Investigation Report

### Source Data

| Field | Value |
|-------|-------|
| Family Name | Combo |
| Designer | Eduardo Tunni |
| Repository URL | https://github.com/librefonts/combo |
| Commit Hash | ae46147e06fad7d2d664c2738ae08a9262adbeb1 |
| Branch | master (default) |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

### How URL Was Found

The repository URL was not yet in the main branch of google/fonts. It was added in a pending PR branch (`sources_info_2026-02-25`) as part of commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files"). The librefonts organization hosts many font families originally contributed to Google Fonts, and this is the standard location for Eduardo Tunni's fonts.

### How Commit Was Determined

The commit `ae46147e06fad7d2d664c2738ae08a9262adbeb1` (dated October 17, 2014) is the **only commit** in the entire repository. The commit message is "update .travis.yml". Despite the message, this single commit contains all the font files, source files, and metadata.

Since there is only one commit, this is unambiguously the correct reference.

### Config YAML Status

**No config.yaml exists** in the upstream repository or as an override in google/fonts.

The upstream repository contains only:
- `src/Combo-Regular-OTF.vfb` - FontLab binary source
- `src/Combo-Regular-TTF.vfb` - FontLab binary source
- Various TTX decompositions of the compiled font
- `Combo-Regular.ttf.*` - TTX decompositions at the root

There are **no gftools-buildable source files** (no `.ufo`, `.glyphs`, or `.designspace` files). The only sources are `.vfb` (FontLab 5 binary format), which can be referenced in a config.yaml but are not directly buildable by modern gftools/fontc toolchains.

The tracking data notes "No buildable source files at recorded commit" which is accurate for modern build systems. However, a config.yaml could still reference the VFB files similarly to how other families handle this (e.g., Codystar).

### Verification

- **Repository accessible**: Yes, https://github.com/librefonts/combo is accessible
- **Commit exists**: Yes, `ae46147e` is the only commit and HEAD of master
- **Source block on main**: No -- the source block is only on the pending PR branch `sources_info_2026-02-25`
- **No config.yaml**: Correct, neither upstream nor override exists

### Confidence Level

**High** for repository URL and commit hash. There is only one commit in the repo, so the commit hash is unambiguous.

**Note**: The status of "missing_config" is accurate. An override config.yaml could potentially be created referencing the VFB sources, similar to what was done for Codystar:

```yaml
buildVariable: false
sources:
  - src/Combo-Regular-TTF.vfb
```

### Open Questions

1. Should an override config.yaml be created referencing the VFB source, similar to the Codystar approach?
2. The source block with repository_url and commit hash needs to be merged to main (currently only on pending PR branch).

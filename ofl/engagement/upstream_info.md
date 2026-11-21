# Engagement

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Engagement (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/engagement.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Engagement-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/engagement at `ac44547ef476`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Engagement-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/engagement.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`ac44547ef476` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/engagement at 4a28e79422bbd98791c29adff6630d14f620ffd3:
  src/Engagement-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/engagement"
      commit: "4a28e79422bbd98791c29adff6630d14f620ffd3"
    }

## Previous investigation

## Investigation Report: Engagement

**Date investigated:** 2026-02-27
**Status:** missing_config (VFB-only sources, not compatible with gftools-builder)
**Designer:** Brian J. Bonislawsky (Astigmatic)

### METADATA.pb Path

`ofl/engagement/METADATA.pb`

### Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | https://github.com/librefonts/engagement                 |
| commit           | 4a28e79422bbd98791c29adff6630d14f620ffd3                 |
| branch           | master                                                   |
| config_yaml      | N/A (no gftools-builder compatible sources)              |

### How URL Was Found

The repository URL `https://github.com/librefonts/engagement` was identified as the upstream source for this font. The `librefonts` organization on GitHub contains automated decompositions of Google Fonts font files, created by user hash3g. The repository contains TTX decompositions of the binary font along with the original VFB (FontLab Studio) source files.

The repository URL was verified as accessible (HTTP 200).

The font was added to Google Fonts on 2011-12-07 (per `date_added` in METADATA.pb). The librefonts/engagement repo was created on 2014-10-17, and the google/fonts repository initial commit was on 2015-03-07. The librefonts repo is not the original designer's repository -- it is a third-party archive containing decomposed font data and the VFB sources.

No alternative upstream repository from the original designer (Brian J. Bonislawsky / Astigmatic) was found on GitHub.

### How Commit Hash Was Identified

The repository contains only a single commit:

- `4a28e79` (hash3g, 2014-10-17): "update .travis.yml" -- initial and only commit creating all files

Since there is only one commit in the entire repository, this is trivially the correct (and only possible) commit hash.

### How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are exclusively in VFB (FontLab Studio) format:

- `src/Engagement-Regular.vfb` -- original source with contour overlaps
- `src/Engagement-Regular-OTF.vfb` -- merged contours for OTF
- `src/Engagement-Regular-TTF.vfb` -- TrueType outlines with hinting

VFB files are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No `.glyphs`, `.ufo`, or `.designspace` files exist anywhere in the repository. The remaining files are TTX decompositions of the compiled fonts, not editable source files.

An override config.yaml cannot be created because there are no gftools-builder compatible source files to reference.

The `.travis.yml` in the repo references `fontbakery-build.py` for building from TTX files, which is an obsolete workflow unrelated to gftools-builder.

### Verification

- **Repository accessible:** Yes (HTTP 200)
- **Repository clean:** Yes (no local modifications)
- **Font binary unchanged since initial google/fonts commit:** The TTF file `ofl/engagement/Engagement-Regular.ttf` (76,408 bytes) was added in the google/fonts initial commit (90abd17b, 2015-03-07) and has never been modified on the main branch.
- **No source block in METADATA.pb on main:** Confirmed. The current METADATA.pb on the main branch of google/fonts does not contain a source block. A source block was added on the `sources_info_2026-02-25` branch (commit 9a14639f3) as part of a batch of 602 families, but this has not been merged yet.
- **Source file formats:** VFB only (FontLab Studio proprietary format)
- **No gftools-builder compatible sources:** Confirmed

### Confidence

**HIGH** -- The repository has only one commit, making the commit hash unambiguous. The URL is verified accessible. The limitation (VFB-only sources) is clearly documented in the FONTLOG.txt which describes all three VFB source files.

### Notes

- This font was designed by Brian J. Bonislawsky for Astigmatic in 2011
- The librefonts/engagement repo is a third-party archive, not the original designer's repository
- The font would need to be converted from VFB to a modern source format (.glyphs or .ufo) before a config.yaml could be created for gftools-builder
- The copyright notice references "Astigmatic (AOETI)" with the Reserved Font Name "Engagement"

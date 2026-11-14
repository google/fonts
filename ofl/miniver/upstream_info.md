# Miniver

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Miniver (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/miniver.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Miniver-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/miniver at `a8403b81abfb`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/miniver.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`a8403b81abfb` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Miniver-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Miniver — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Miniver are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/miniver/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Miniver-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontLab VFB file (63 KB) optimized for TTF output. No UFO, Glyphs, SFD, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and requires conversion before modern tooling can be used.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting the VFB source to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Dathan Boardman (Open Window)
- **Contact**: dathanboardman@gmail.com
- **FONTLOG**: Confirms "Designed by Dathan Boardman of Open Window", matching the copyright in METADATA.pb exactly.

No canonical repository by the designer was found on GitHub.

### Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/miniver
- **Latest commit**: `b301973d6822dc2661ce510355b4d7f9ed573926` (2014-10-17, "update .travis.yml")
- **Default branch**: `master`

The repo has been dormant since October 2014. It contains TTX decompositions of the built font in the root directory and uses an obsolete Travis CI configuration.

### Notes

- The VFB source format is proprietary and requires FontLab Studio or conversion to UFO for modern tooling.
- No evidence of an authoritative repository from the original designer (Open Window / Dathan Boardman) was found on GitHub.
- The `librefonts` organization archived this font as-is; it is unlikely to receive further upstream development.
- Confidence in source identification: High — FONTLOG text, designer name, email, and font name all match the METADATA.pb.

# Metal Mania

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Metal Mania (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/metalmania.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from MetalMania-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/metalmania at `7d22f34e7f4c`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/metalmania.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`7d22f34e7f4c` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/MetalMania-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Metal Mania — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Metal Mania are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/metalmania/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MetalMania-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontLab VFB file (300 KB) with TrueType outlines and hinting adjustments. No UFO, Glyphs, SFD, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 5) and requires conversion before modern tooling can be used.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting the VFB source to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Dathan Boardman (Open Window)
- **Contact**: dathanboardman@gmail.com
- **Date added to Google Fonts**: 2012-07-11
- **Font version**: 1.002 (August 2012, unchanged since initial release)
- **FONTLOG reference**: A Google+ profile (`https://profiles.google.com/openwindowfonts/about`) that no longer exists (404).

The designer has a GitHub account at https://github.com/dathanboardman but has 0 public repositories. No upstream source is maintained by the original designer; this family should be considered orphaned.

### Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/metalmania
- **Status**: Dormant — last commit 2014-10-17, no activity since
- **Latest commit**: `7f5e5a82` (2014-10-17) — "update .travis.yml"
- **First commit**: `10c6697f` (2014-07-16) — "Move metalmania font files to separate repository"
- **Total commits**: 11

The repo was created and maintained by Mikhail Kashkin (hash3g) as part of the `librefonts` infrastructure, not by the original designer. The root of the repository contains TTX-format table dumps generated from the binary. It uses an obsolete fontbakery-build pipeline and has no issues, PRs, or forks.

### Notes

- The only authoritative source is the VFB FontLab binary, which would need conversion to UFO or Glyphs for any future rebuild.
- The `librefonts` organization on GitHub was an early Google Fonts infrastructure project that is no longer active.
- Confidence in source identification is high — the VFB filename matches the FONTLOG description exactly ("MetalMania-Regular-TTF.vfb TrueType outlines with hinting adjustments corresponding to the TTF file"), and version 1.002 matches.

# Milonga

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Milonga (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/milonga.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Milonga-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/milonga at `46b17bd9ccc2`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/milonga.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`46b17bd9ccc2` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Milonga-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Milonga — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Milonga are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/milonga/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Milonga-Regular.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `Milonga-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Three VFB files are present: the main master (`Milonga-Regular.vfb`, 285 KB), one optimized for OTF output (`-OTF.vfb`, 192 KB), and one optimized for TTF output (`-TTF.vfb`, 259 KB). The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, SFD, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and requires conversion before modern tooling can be used.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Pablo Impallari (Impallari Type), with co-designers Brenda Gallo and Rodrigo Fuenzalida
- **Contact**: impallari@gmail.com
- **Font version**: 1.000 — initial release with no subsequent updates
- **Design notes**: A tribute to Rioplatense culture, inspired by the Argentine/Uruguayan "fileteado porteno" painting tradition. Designed for display/headline use.

No dedicated repository under the `impallari` GitHub account was found for Milonga (unlike Miltonian, which has `impallari/Miltonian`). A search for `impallari/Milonga` returns a 404.

### Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/milonga
- **Last commit**: `5cbad6e6871080ea3507db062760135a22522a5e` (2014-10-17, "update .travis.yml")

This is a legacy mirror from 2014 with an obsolete fontbakery-build pipeline. It has not been updated since October 2014.

### Notes

- The VFB source format requires FontLab Studio (proprietary) to edit. No open-source-friendly alternative source (UFO, Glyphs, SFD) is available.
- Consider reaching out via the Impallari Type GitHub account or `impallari@gmail.com` to determine if updated sources exist.
- The `librefonts` organization on GitHub was an early Google Fonts infrastructure project that is no longer active.

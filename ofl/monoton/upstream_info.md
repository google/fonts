# Monoton

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Monoton (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontForge import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/monoton.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from Monoton-Regular.ttf, the font Google Fonts
  ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/monoton at `db46b75aa0eb`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/monoton.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`db46b75aa0eb` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/monoton/src/Monoton-Regular-TTF.sfd, a
  FontForge import of the shipped font (quadratic outlines, its TrueType instructions;
  tools/probes/ttf_sfd_origin), not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Monoton — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Monoton are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/monoton/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `Monoton-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Only one design source is present: a FontForge SFD file for TTF production. The SFD format is not supported by gftools-builder. No UFO, Glyphs, VFB, or other sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The SFD format is not compatible with gftools-builder.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting the SFD source to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Vernon Adams
- **Date added to Google Fonts**: 2011

The font was added to Google Fonts in the early era before open source font hosting on GitHub was common practice.

### Notes

- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- The SFD source could potentially be converted to UFO using FontForge for future modernization.

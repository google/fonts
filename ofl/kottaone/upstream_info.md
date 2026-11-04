# Kotta One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Kotta One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/kottaone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from KottaOne-Regular.ttf, the font Google
  Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/kottaone at `dca071e73dc3`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/kottaone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`dca071e73dc3` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/kottaone/src/KottaOne-Regular-TTF.sfd, a
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

## Investigation: Kotta One

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/kottaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files (4)

| File | Format | Notes |
|------|--------|-------|
| `KottaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KottaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KottaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

### Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012 by Ania Kruk (hello@aniakruk.com), with Reserved Font Name 'Kotta'"

The DESCRIPTION.en_us.html describes Kotta One as "a new and unusual text typeface that mixes the characteristics of an italic with legibility of a roman."

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/kottaone` containing only TTX dumps of the binary font — no VFB or SFD sources. The googlefontdirectory-hg monorepo preserves the more complete VFB and SFD design sources that the librefonts mirror did not retain.

No upstream GitHub repository for Ania Kruk or Kotta One was found.

### Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. The librefonts mirror only preserved TTX dumps, making the googlefontdirectory-hg sources the more complete record. No upstream GitHub repository is known for this family.

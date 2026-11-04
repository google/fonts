# Sansita One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Sansita One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/sansitaone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from SansitaOne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/sansitaone at `057bf3d6779c`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/sansitaone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`057bf3d6779c` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/SansitaOne-TTF.vfb, a FontLab import of
  the shipped font, not a source: Simon on google/fonts#10490 ("batch-converted from the
  binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Sansita One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `sansitaone/src/`

### Source Files

The `sansitaone/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): SansitaOne-TTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): SansitaOne-TTF.sfd

### Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

### Designer

- **Designer**: Omnibus-Type (omnibus.type@gmail.com / www.omnibus-type.com)

### Investigation Details

The following searches and checks were performed:

- Checked `repos/Omnibus-Type/SansitaOne` — not found
- Checked `repos/googlefonts/SansitaOne` — not found
- Searched GitHub for `Sansita One font` — no relevant results
- Searched GitHub for `SansitaOne font OFL` — no relevant results
- Listed all `Omnibus-Type` user repositories — no SansitaOne repository present

The `Omnibus-Type` user repositories included a `Sansita` repo (for the 2016 family) and a `Sansita-Swashed` repo, but no dedicated Sansita One repository. Sansita One is an earlier, distinct display font from 2011.

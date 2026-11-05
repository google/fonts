# Racing Sans One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Racing Sans One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/racingsansone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  RacingSansOne-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/racingsansone at `4ca096913015`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/racingsansone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`4ca096913015` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/RacingSansOne-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Racing Sans One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `racingsansone/src/`

### Source Files

The `racingsansone/src/` directory contains design sources in proprietary VFB format only, which cannot be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): RacingSansOne-Regular-OT.vfb, RacingSansOne-Regular-TTF.vfb, RacingSansOne-Regular.vfb
- **OTF** (compiled binaries, not design sources): RacingSansOne-Regular.otf
- **Other**: RacingsSansOne-Preview.jpg

### Buildability

Not buildable with gftools-builder. The VFB sources are in FontLab's proprietary format. Conversion to UFO or Glyphs format would be required before a reproducible build pipeline could be established.

### Investigation Details

The following searches were performed:

- Searched GitHub for "racing sans one font" and "racingsansone" repositories.
- Checked the `impallari` GitHub account — Pablo Impallari has 26 public repositories, but none for Racing Sans One. The repositories present include other Impallari Type fonts (Cabin, Dosis, Dancing Script, etc.) but not Racing Sans One.
- Checked the `rfuenzalida` GitHub account (co-designer Rodrigo Fuenzalida) — found 5 repositories (`AntonFont`, `Freeman`, `Instrument_Serif`, `MondaFont`, `Outfit-Fonts`), none of which is Racing Sans One.
- Searched for repos with "RacingSansOne" in the name — found only `librefonts/racingsansone` (a librefonts mirror — skipped per policy) and `google-fonts-bower/racingsansone-bower` (a Bower packaging mirror).
- Reviewed the FONTLOG.txt, which referenced `www.impallari.com` and the impallari.com projects page, but no GitHub repository was listed.

No canonical upstream repository with font source files was found.

### Notes

- Designers: Pablo Impallari and Rodrigo Fuenzalida, with spacing/kerning by Igino Marini
- The font was developed in 2012; the FONTLOG references FontLab-era workflow
- Neither designer's GitHub account contains a Racing Sans One source repository

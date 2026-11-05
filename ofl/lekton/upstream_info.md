# Lekton

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Lekton (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontForge import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/lekton.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Lekton-{Bold,Italic,Regular}.ttf, the fonts Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/lekton at `904b0f52b1f6`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 3 styles. Those tools,
including this family's plan `plans/lekton.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`904b0f52b1f6` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/lekton/src/Lekton-Bold-TTF.sfd,
  src/Lekton-Italic-TTF.sfd, src/Lekton-Regular-TTF.sfd, a FontForge import of the
  shipped fonts (quadratic outlines, its TrueType instructions;
  tools/probes/ttf_sfd_origin), not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Investigation: Lekton

**Model**: Claude Opus 4.6
**Confidence**: MEDIUM

### Source Repository

The original design sources for Lekton are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lekton/src/`.

#### Source Files in googlefontdirectory-hg

- `Lekton-Regular-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton-Bold-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton-Italic-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `Lekton034.otf` -- compiled OTF binary, not a design source
- `LektonBold034.otf` -- compiled OTF binary, not a design source
- `LektonItalic004.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are SFD (FontForge) format only. No `.glyphs`, `.ufo`, or `.designspace` files are present. SFD files are not compatible with gftools-builder. The `.otf` files are compiled binaries, not design sources.

### METADATA.pb Analysis

The METADATA.pb for Lekton contains no `source { }` block -- no `repository_url`, no commit hash, no config path.

### Google Fonts History

The google/fonts git history for `ofl/lekton/Lekton-Regular.ttf` shows only:
- `90abd17b4` -- "Initial commit" (original onboarding, pre-dating gftools-packager)

### Designer Information

The designer is listed as "ISIA Urbino" (Istituto Superiore per le Industrie Artistiche, Urbino -- an Italian design school). The OFL copyright states: `Copyright (c) 2008, 2009, 2010, Accademia di Belle Arti di Urbino (luciano.perondi@isiaurbino.net)`. The font is attributed to the academic institution rather than an individual designer.

No upstream repository for this font was found in the upstream repo cache.

### Conclusion

The googlefontdirectory-hg monorepo preserves SFD sources for all three styles of Lekton (Regular, Bold, Italic), but SFD is a legacy format not compatible with gftools-builder. No config.yaml can be created without first converting sources to a supported format. Lekton was created by ISIA Urbino (an Italian design institution) and was part of the initial google/fonts batch before source tracking was in place. Finding a modern upstream repository would require contacting the institution.

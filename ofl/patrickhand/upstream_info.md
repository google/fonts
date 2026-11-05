# Patrick Hand

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Patrick Hand (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/patrickhand.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from PatrickHand-Regular.ttf, the font Google
  Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/patrickhand at `a70e13047552`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/patrickhand.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`a70e13047552` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6:
  ofl/patrickhand/src/PatrickHand-Regular-TTF.sfd, a FontForge import of the shipped
  font (quadratic outlines, its TrueType instructions; tools/probes/ttf_sfd_origin), not
  a source: Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Patrick Hand — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/patrickhand/src/` |
| **Buildable** | No — legacy format only (.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files

- **.sfd** (FontForge): PatrickHand-Regular-TTF.sfd, PatrickHand-Regular_prettfautohint.sfd
- **Compiled binaries** (not design sources): PatrickHand-Regular.otf, PatrickHand-Regular_prettfautohint.ttf
- **Metadata**: METADATA_comments.txt

The only design sources are SFD files (FontForge format), which are not buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

### Investigation

The METADATA.pb listed the designer as Patrick Wagesreiter with copyright dated 2010-2012.

The DESCRIPTION.en_us.html described the font as based on the designer's own handwriting, supporting Latin and Latin extended characters plus Vietnamese. No upstream repository link was present.

Web searches were conducted for Patrick Wagesreiter on GitHub, for a repository named PatrickHand, and for any organization or user matching the designer. The only Patrick Hand-related repository found was `m4rc1e/PatrickHandSC`, attributed to Marc Foley, a Google Fonts developer and font engineer — not the original designer. This covers the SC variant and is an engineering preparation repo, not a canonical designer-owned upstream.

No designer-owned repository was found for either Patrick Hand or Patrick Hand SC.

### Conclusion

No canonical designer-owned upstream repository was found. The `m4rc1e/PatrickHandSC` repo is a Google Fonts engineering repository for the SC variant only. The legacy googlefontdirectory-hg archive contains only SFD sources, which are not buildable with gftools-builder. No METADATA.pb changes were made.

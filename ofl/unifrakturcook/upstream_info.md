# UnifrakturCook

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped UnifrakturCook (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/unifrakturcook.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from UnifrakturCook-Bold.ttf, the font Google
  Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/unifrakturcook at `9e76e3479753`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/unifrakturcook.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`9e76e3479753` is the equivalence commit: its build is functionally equivalent to the
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
  ofl/unifrakturcook/src/UnifrakturCook-Bold-TTF.sfd, a FontForge import of the shipped
  font (quadratic outlines, its TrueType instructions; tools/probes/ttf_sfd_origin), not
  a source: Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## UnifrakturCook — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: j. 'mach' wust

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `unifrakturcook/src/`.

#### Source Files

- **SFD (FontForge)**: UnifrakturCook-Bold-TTF.sfd

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

### Investigation Details

UnifrakturCook was created by j. 'mach' wust as a modification of Peter Wiegel's font "Koch fette deutsche Schrift" (itself based on a 1910 typeface by Rudolf Koch). The font was originally published at http://unifraktur.sourceforge.net/cook.html.

The FONTLOG.txt confirmed that the source format is FontForge SFD:

> "The FontForge source file of Unifraktur Cook. FontForge is a free font editor. FontForge has been used to add OpenType features and to generate UnifrakturCook.ttf"

The following searches were conducted:

1. **SourceForge**: The project is hosted at https://unifraktur.sourceforge.net/ and distributes SFD (FontForge) source files. No GitHub repository is mentioned on the project page.
2. **GitHub search**: Searches for "unifrakturcook" and "unifraktur cook" on GitHub returned only `librefonts/unifrakturcook` (a downstream binary mirror, skipped per policy) and `google-fonts-bower/unifrakturcook-bower` (a CSS wrapper, not font sources).
3. **j. 'mach' wust GitHub**: No GitHub account was identified for the designer.
4. **Peter Wiegel**: Peter Wiegel (the original Koch Fraktur designer) maintains fonts at peter-wiegel.de but no GitHub presence was found.

UnifrakturCook is hosted on SourceForge and its sources exist in FontForge SFD format. SFD sources are not eligible per the source block policy (which requires UFO or Glyphs format). The font predates the adoption of modern open font source workflows.

# Titillium Web

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Titillium Web (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/titilliumweb.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  TitilliumWeb-{Black,Bold,BoldItalic,Italic,Light,LightItalic,Regular,SemiBold,SemiBoldItalic}.ttf,
  the fonts Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs
  branch 2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it
  (#117, typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/titilliumweb at `1ba6c9da5b42`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 9 styles. Those tools,
including this family's plan `plans/titilliumweb.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`1ba6c9da5b42` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6:
  ofl/titilliumweb/src/TitilliumWeb-Black-TTF.sfd, src/TitilliumWeb-Bold-TTF.sfd,
  src/TitilliumWeb-BoldItalic-TTF.sfd, src/TitilliumWeb-Italic-TTF.sfd,
  src/TitilliumWeb-Light-TTF.sfd, src/TitilliumWeb-LightItalic-TTF.sfd,
  src/TitilliumWeb-Regular-TTF.sfd, src/TitilliumWeb-SemiBold-TTF.sfd,
  src/TitilliumWeb-SemiBoldItalic-TTF.sfd, a FontForge import of the shipped fonts
  (quadratic outlines, its TrueType instructions; tools/probes/ttf_sfd_origin), not a
  source: Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Titillium Web — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Accademia di Belle Arti di Urbino

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `titilliumweb/src/`.

#### Source Files

- **SFD (FontForge)**: TitilliumWeb-Black-TTF.sfd, TitilliumWeb-Bold-TTF.sfd, TitilliumWeb-BoldItalic-TTF.sfd, TitilliumWeb-Italic-TTF.sfd, TitilliumWeb-Light-TTF.sfd, TitilliumWeb-LightItalic-TTF.sfd, TitilliumWeb-Regular-TTF.sfd, TitilliumWeb-SemiBold-TTF.sfd, TitilliumWeb-SemiBoldItalic-TTF.sfd, TitilliumWeb-Thin-TTF.sfd, TitilliumWeb-ThinItalic-TTF.sfd
- **OTF (compiled)**: TitilliumWeb-Black.otf, TitilliumWeb-Bold.otf, TitilliumWeb-BoldItalic.otf, TitilliumWeb-Italic.otf, TitilliumWeb-Light.otf, TitilliumWeb-LightItalic.otf, TitilliumWeb-Regular.otf, TitilliumWeb-SemiBold.otf, TitilliumWeb-SemiBoldItalic.otf, TitilliumWeb-Thin.otf, TitilliumWeb-ThinItalic.otf

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

### Investigation Details

Titillium Web was created as a collective academic project at the Accademia di Belle Arti di Urbino (Italy) within its Visual Design Master program (Campi Visivi course). The font was iteratively developed by successive student cohorts.

The following searches were conducted:

1. **GitHub organization search**: No GitHub organization or user account was found for the Accademia di Belle Arti di Urbino (`accademiadiurbino`).
2. **SFD sources**: A repository at `ecm4u/Titillium` was found containing SFD (FontForge) source files and compiled fonts, attributed to the Accademia. However, SFD sources are FontForge-specific format and do not meet the requirement for UFO or Glyphs sources.
3. **Derived works**: A repository `eliheuer/titillium-web-vf` was found containing Glyphs files for a variable font version, but this is a fork/derivative (based on Cairo by Mohamed Gaber), not the canonical upstream.
4. **Pro version**: `chialab/titillium_pro` was found with UFO sources, but this is a commercial extended variant ("Titillium Pro") — not the original Titillium Web distributed on Google Fonts.
5. **Mirror repositories**: `FontFaceKit/titilliumweb`, `librefonts/titilliumweb` were found but are downstream binary mirrors.

The original Titillium Web sources exist only in FontForge SFD format. The font predates the widespread adoption of UFO as a standard open font source format. No eligible upstream source repository was identified.

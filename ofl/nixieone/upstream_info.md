# Nixie One

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Nixie One (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontForge import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/nixieone.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from NixieOne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/nixieone at `96a6f91927c5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/nixieone.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`96a6f91927c5` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/nixieone/src/NixieOne-Regular-TTF.sfd, a
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

## Nixie One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nixieone/src/`
- **Buildable**: No — legacy formats only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source Files

| File | Type |
|------|------|
| `NixieOne-Regular-TTF.sfd` | FontForge SFD source (not buildable with gftools-builder) |
| `NixieOne-Regular.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The SFD file is the only editable source. It is a FontForge format file, not compatible with gftools-builder.

### Designer and Provenance

- **Designer**: Jovanny Lemonad (`lemonad@jovanny.ru`, jovanny.ru)
- The designer's website `jovanny.ru` is currently unreachable (ECONNREFUSED).
- No official repository maintained by the designer was found on GitHub. Jovanny Lemonad designed several other Google Fonts (e.g., Philosopher, Yeseva One); some have GitHub repos under `alexeiva/` but no Nixie One repo was found.

### Additional Mirror

A third-party mirror exists at https://github.com/librefonts/nixieone (latest commit `14c80bd` on 2014-10-17, "update .travis.yml"). It contains the same SFD source plus TTX decompilations. The `src/VERSIONS.txt` records version 1.004, matching the Google Fonts binary.

### Build System

Not applicable — the SFD source requires FontForge and is not compatible with the modern gftools-builder pipeline.

### config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

### Notes

- The font in Google Fonts is Version 1.004, matching `VERSIONS.txt` in the librefonts mirror.
- Nixie One is a single-weight family (Regular only); no italic or bold sources exist.
- **Confidence**: Medium-High. The librefonts mirror matches the shipped version exactly; however, it is not a designer-maintained repository.

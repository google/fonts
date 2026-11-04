# Frijole

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Frijole (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/frijole.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Frijole-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/frijole at `1dd0cd3ac838`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/frijole.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`1dd0cd3ac838` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/frijole at 0e6ba6cfcc631a3db6c6d6e64e523377176e8eec:
  src/Frijole-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/frijole"
      commit: "0e6ba6cfcc631a3db6c6d6e64e523377176e8eec"
    }

## Previous investigation

## Investigation Report: Frijole

### Summary

Frijole is a display font designed by Dave "Squid" Cohen of Sideshow (a DBA of Font Diner, Inc), added to Google Fonts on 2011-12-19. The font has never been updated since its initial inclusion. The only known upstream repository is `librefonts/frijole`, which is a mirror containing a VFB source file (FontLab format). There are no gftools-builder compatible sources, so no config.yaml can be created.

### Key Findings

| Field             | Value                                              |
|-------------------|----------------------------------------------------|
| Family Name       | Frijole                                            |
| Designer          | Sideshow (Dave "Squid" Cohen / Font Diner)         |
| Repository URL    | https://github.com/librefonts/frijole              |
| Commit Hash       | 0e6ba6cfcc631a3db6c6d6e64e523377176e8eec           |
| Branch            | master                                             |
| Config YAML       | None (no gftools-builder compatible sources)       |
| Status            | no_config_possible                                 |
| Confidence        | HIGH                                               |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb has no source block. The font was added on 2011-12-19, predating the source metadata system.

#### google/fonts Commit History

The font binary `Frijole-Regular.ttf` was added in the initial commit (`90abd17b4`) on 2015-03-07 (when the repo was created on GitHub) and has never been modified since. The only other commits touching the frijole directory are metadata updates (METADATA.json removal, METADATA.pb updates for language support).

#### Upstream Repository

The only upstream repository found is `librefonts/frijole` (https://github.com/librefonts/frijole). This is a librefonts mirror with a single commit (`0e6ba6c`, dated 2014-10-17, by hash3g, message: "update .travis.yml").

The repository contains:
- **Source file**: `src/Frijole-Regular-TTF.vfb` (FontLab format)
- **TTX decompositions**: Multiple `.ttx` files decomposed from the binary
- **Standard metadata**: FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html, METADATA.json

The only source file is a VFB (FontLab) binary, which is not compatible with gftools-builder. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist.

#### Designer Information

The FONTLOG identifies Font Diner (support@fontdiner.com, www.fontdiner.com) as the designer and masterer. The designer is Dave "Squid" Cohen, working under the Sideshow brand (a DBA of Font Diner, Inc). No dedicated GitHub repositories from Font Diner or Sideshow were found for this font.

#### Search for Alternative Upstream Repos

- No repository found under googlefonts organization
- No repository found under fontdiner organization on GitHub
- GitHub search for "frijole font" returned no relevant results
- The librefonts mirror is the only known repository

### Conclusion

Frijole has a known upstream repository (`librefonts/frijole`) but it only contains a legacy VFB source, not a gftools-builder compatible format. No config.yaml can be created. The source block should document the repository URL and commit for reference purposes.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/frijole"
  commit: "0e6ba6cfcc631a3db6c6d6e64e523377176e8eec"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "master"
}
```

**Note**: No `config_yaml` field because the repository only contains a VFB source file, which is not gftools-builder compatible. The font binary in google/fonts predates the librefonts mirror and was likely compiled manually from the VFB source.

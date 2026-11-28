# McLaren

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped McLaren (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/mclaren.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from McLaren-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/mclaren at `43b028c204c5`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: McLaren-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/mclaren.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`43b028c204c5` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The build's GSUB numbers or packs some lookups differently from the release's (fontc
  places a lookup that only a contextual lookup calls, and packs chained contextual
  rules, its own way: gfonts-ai-usage-report 22-fontc-problems, problems 12 and 13);
  every rule is the same and the text shapes identically (tools/functional_gate.py).
  Decided 2026-10-02: problems that need fontc are disclosed and fixed in fontc later.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/McLaren-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## McLaren — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

### Source Repository

The source files for McLaren are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `mclaren/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `McLaren-Regular.vfb` | FontLab VFB | Original source (proprietary, not buildable with gftools) |
| `McLaren-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF |
| `McLaren-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting |
| `McLaren-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable sources are three VFB files (FontLab Studio format), which are proprietary binary files not supported by gftools-builder or fontc.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/mclaren, created on 2014-07-16 under the `librefonts` organization. The repo contains a single commit:
- `7031b7b` (2014-10-17) — "update .travis.yml"

The librefonts/mclaren repository was created after the font was already in Google Fonts. This is a common pattern for the "librefonts" organization, which hosted TTX-decompiled sources for Google Fonts families — not the original upstream source but rather a decomposed archive.

The repo also contains TTX dumps of the TTF and OTF versions, a `.travis.yml` using `fontbakery-build.py` (legacy), and `src/VERSIONS.txt` recording version 1.000.

### Onboarding History

McLaren was added to Google Fonts on 2012-08-13 (per `date_added`). The font file appeared in the google/fonts repository's initial commit (`90abd17b4`, 2015-03-07), which was the mass import of the entire library. The font binary has never been updated since.

**Designer**: Brian J. Bonislawsky (Astigmatic/AOETI, astigma@astigmatic.com)
**GitHub**: https://github.com/astigmatic (exists but has only 2 generic repos, no font sources)
**Font version**: 1.000 (per VERSIONS.txt) / 1.001 (per copyright string)

### Build Configuration

No `config.yaml` exists and none can be created. The source files are exclusively in VFB format (FontLab Studio proprietary format). There is no way to create a config.yaml for gftools-builder without first converting the sources to an open format (.glyphs, .ufo, or .designspace).

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/mclaren"
  commit: "7031b7bdfd833221535738903fe1ea50f1772436"
  branch: "master"
}
```

No `config_yaml` field is included because the repository contains only VFB (FontLab) source files not compatible with gftools-builder.

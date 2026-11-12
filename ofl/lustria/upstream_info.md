# Lustria

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Lustria (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontForge import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/lustria.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from Lustria-Regular.ttf, the font Google Fonts
  ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/lustria at `0ceac6193151`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/lustria.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`0ceac6193151` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/lustria/src/Lustria-Regular-TTF.sfd, a
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

## Lustria — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Lustria are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lustria/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Lustria-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Lustria-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Lustria-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge) and VFB (FontLab) formats, which are not supported by gftools-builder.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/lustria, created on 2014-07-16 under the `librefonts` GitHub organization. It contains a single commit (`a796e0e874e34d163ac3aceb3f6014af1ef66d3c`) dated 2014-10-17, authored by `hash3g <hash3g@gmail.com>` with the message "update .travis.yml". The repo is not archived and not a fork.

**Contributors**: vitalyvolkov, xen

The repository contains TTX decomposed tables of the TTF binary at root level, plus the SFD/VFB sources in `src/`, a `.travis.yml` for CI using the legacy `fontbakery-build.py` pipeline, and metadata files (FONTLOG.txt, OFL.txt, DESCRIPTION.en_us.html).

The METADATA_comments.txt file references `~/googlefontdirectory/` paths, indicating this font was processed using the original Google Fonts directory tooling (font-optimizer, subset.py) before the current repository structure was established.

### Onboarding History

Lustria was added to Google Fonts on 2012-01-18 (per `date_added` in METADATA.pb). The font was included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland), which migrated the entire collection into the current structure.

The font binary (`Lustria-Regular.ttf`, 37,400 bytes) has never been updated since the initial commit. Its SHA-256 hash is `8b50753779d151674dcc74bdf9cdde1e788d8fb2b9ace8fb183a0def0f7361ce`.

**Designer**: MADType (Matthew Desmond, mattdesmond@gmail.com, www.madtype.com)

### Build Configuration

No `config.yaml` exists and none can be created. The only available sources are SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder. The legacy `.travis.yml` used the `fontbakery-build.py` pipeline with FontForge and fontcrunch, which is no longer the standard build system.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lustria"
  commit: "a796e0e874e34d163ac3aceb3f6014af1ef66d3c"
}
```

No `config_yaml` field is needed because the sources are SFD-only and cannot be built with gftools-builder.

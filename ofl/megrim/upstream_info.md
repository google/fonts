# Megrim

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Megrim (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontForge import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/megrim.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Megrim.ttf, the font
  Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/megrim at `a951854e1c45`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/megrim.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`a951854e1c45` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/megrim/src/Megrim-TTF.sfd, a FontForge
  import of the shipped font (quadratic outlines, its TrueType instructions;
  tools/probes/ttf_sfd_origin), not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Megrim — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Megrim are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `megrim/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Megrim-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Megrim.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Megrim.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The SFD file was created 2010-05-05 and last modified 2011-04-28.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/megrim, created on 2014-07-16 under the `librefonts` organization (a third-party archive). The repo contains a single commit:
- `274ef53` (2014-10-17, author: hash3g) — "update .travis.yml"

**Contributors**: vitalyvolkov, xen — neither is the original font designer (Daniel Johnson).

The repository contains TTX-decomposed tables of the TrueType binary at root level, the SFD/VFB sources in `src/`, a `.travis.yml` for fontbakery CI (outdated), and metadata files.

### Original Designer

**Daniel Johnson** (il.basso.buffo@gmail.com). His personal page was listed as `http://io.debian.net/~danielj/` in the FONTLOG. No personal GitHub repository was found for Daniel Johnson under this font name. The librefonts/megrim archive appears to be the only GitHub repository containing the source files.

#### FONTLOG Changelog
- 2010-05-11: Initial release
- 2010-07-02: Improved lowercase Icelandic glyphs; added more glyphs with diacritics
- 2010-08-31: Added stylistic alternate set (ss01); added Turkish glyphs

The SFD file's modification timestamp (2011-04-28) aligns with the font binary version string (20110427).

### Onboarding History

Megrim was added to Google Fonts on 2011-05-04 (per `date_added`). The font was part of the initial bulk import into the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary has never been updated since the initial import.

**Font version**: 20110427

The font predated the current GitHub-based workflow — no PRs were associated with its onboarding.

### Build Configuration

No `config.yaml` exists and none can be created. The only editable design source is a FontForge SFD file, plus a FontLab VFB file. Neither format is supported by gftools-builder, which requires .glyphs, .ufo, or .designspace sources. The legacy `.travis.yml` used the old `fontbakery-build.py` pipeline (circa 2014).

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/megrim"
  commit: "274ef534110a60534a520038400a8db0b3abd976"
}
```

No `config_yaml` field is included because the sources are in SFD/VFB formats not compatible with gftools-builder.

**Confidence**: HIGH — The librefonts/megrim repo is the only known GitHub repository for this font, and it contains the correct SFD source matching the compiled binary. The single commit (`274ef53`) is the only possible reference.

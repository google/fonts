# Averia Libre

**Model**: Claude Opus 5.5
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Averia Libre as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/averialibre.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  AveriaLibre-{Bold,BoldItalic,Italic,Light,LightItalic,Regular}.ttf, the fonts Google
  Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/averialibre at `62c6d4c1f4f2`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: AveriaLibre-Bold: 3 blocking
rows; functionally equivalent AveriaLibre-BoldItalic: 3 blocking rows; functionally
equivalent AveriaLibre-Italic: 3 blocking rows; functionally equivalent
AveriaLibre-Light: 3 blocking rows; functionally equivalent AveriaLibre-LightItalic: 3
blocking rows; functionally equivalent AveriaLibre-Regular: 3 blocking rows;
functionally equivalent. Those tools, including this family's plan
`plans/averialibre.json`: https://github.com/felipesanches/gf-source-modernization at
`4e08bb3`.

`62c6d4c1f4f2` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts kern with a legacy `kern` table; these sources kern through a GPOS
  kern feature, which is how fontc builds kerning. HarfBuzz shapes every kerned pair
  alike in both, except pairs with the soft hyphen (U+00AD), which it hides: there the
  release leaves half the pair's value on the following glyph and the build none (42 to
  102 pairs per style, tools/probes/binary_to_source/results/legacy-kern-pairs.txt in
  the evidence repository). Decided 2026-10-01: releases with an old kern table are
  accepted and disclosed.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Averia Libre -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

### Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `averialibre/src/`

#### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `METADATA_comments.txt` | Metadata | N/A |

The `src/` directory contains only `METADATA_comments.txt` -- no original design sources. The font was created algorithmically (see below), so no traditional editable sources exist.

### Designer

Dan Sayers -- http://iotic.com/averia/

The Averia font family was created by algorithmically averaging the outlines of all 725 OFL fonts from Google Fonts (as of November 2011). There are no traditional editable design sources -- the font outlines were generated programmatically using FontForge.

### librefonts Mirror

A mirror exists at `https://github.com/librefonts/averialibre` with a single commit:
- `091de18` (2014-10-17) by hash3g: "update .travis.yml"

The repo contains TTX-decomposed font data (6 styles: Regular, Bold, Italic, BoldItalic, Light, LightItalic) and metadata files. No `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files exist. The TTX files represent v1.001 of the font.

### google/fonts History

1. `90abd17` (2015-03-07) -- Initial commit of the google/fonts repo (bulk import, v1.001)
2. `fc10731` (2017-08-07) -- "hotfix-averialibre: v1.002 added" (PR #837 by Marc Foley). Updated all 6 TTF files and DESCRIPTION/METADATA.
3. Several metadata-only commits thereafter (METADATA.pb format changes, language support updates)

The googlefontdirectory-hg and librefonts sources correspond to v1.001, while google/fonts serves v1.002. The v1.002 hotfix (PR #837) had an empty PR body, providing no upstream reference. The updated binaries were likely produced by Marc Foley directly.

### Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- No gftools-builder compatible sources exist (TTX files are not a supported input format)
- An override config.yaml cannot be created because there are no `.glyphs`, `.ufo`, or `.designspace` sources
- This is inherent to the font's nature -- it was created through algorithmic averaging, not traditional font design

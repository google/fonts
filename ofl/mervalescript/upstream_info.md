# Mervale Script

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Mervale Script (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/mervalescript.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  MervaleScript-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/mervalescript at `d8bb7f3c3cb8`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
MervaleScript-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/mervalescript.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`d8bb7f3c3cb8` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/MervaleScript-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Mervale Script — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Mervale Script are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/mervalescript/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MervaleScript-Regular.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular-TTF.vfb` | FontLab VFB | No (proprietary) |
| `MervaleScript-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Three VFB files are present: the main master (`MervaleScript-Regular.vfb`), one with contour overlaps optimized for OTF output (`-OTF.vfb`), and one with hinting adjustments for TTF output (`-TTF.vfb`). No UFO, Glyphs, SFD, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio 4/5) and not editable with modern open-source tooling without conversion.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

### Designer & History

Mervale Script is a single-weight handwriting/script typeface designed by **Brian J. Bonislawsky** and **Jim Lyles** for Astigmatic (AOETI), released in 2012.

- **Contact**: astigma@astigmatic.com
- **Website**: www.astigmatic.com (SSL certificate expired — HTTPS unreachable as of investigation date)
- **Font version**: v1.000 (November 2012). No updates have been made in over 13 years.
- **Glyph coverage**: Latin-1, Latin-2, Turkish, Windows Baltic (per FONTLOG). Supports `latin` and `latin-ext` subsets.
- **Single weight**: Regular (400) only; no variable font or additional weights/styles.

No GitHub organization or user account for "Astigmatic" or "Brian J. Bonislawsky" was found that hosts original font sources. The GitHub user at https://github.com/astigmatic (id 34247703, created 2017-12-04) has only 2 unrelated repositories and is not affiliated with the type foundry.

### Additional Repository

A copy also exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/mervalescript
- **Type**: Third-party mirror, not an authoritative Astigmatic repository
- **Latest commit**: `31648e2a8d9b3f059379bb37aebb50f0e0b9d465` (2014-10-17)

The mirror contains TTX-exploded font tables and the same VFB source files. It uses an obsolete fontbakery-build pipeline via Travis CI and has been dormant since 2014.

### Notes

- The `.vfb` source files would need conversion via FontLab or `vfb2ufo` to produce UFO sources for modern tooling.
- Contacting Astigmatic directly (astigma@astigmatic.com) to confirm source availability would be the appropriate first step for modernization.
- The `librefonts` organization on GitHub is a community archive of free fonts, not maintained by Astigmatic.

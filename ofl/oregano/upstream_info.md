# Oregano

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Oregano (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/oregano.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Oregano-{Italic,Regular}.ttf, the fonts Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/oregano at `8acb85f087f2`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Oregano-Italic: 2 blocking rows;
functionally equivalent Oregano-Regular: 2 blocking rows; functionally equivalent. Those
tools, including this family's plan `plans/oregano.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`8acb85f087f2` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Oregano-Italic-TTF.vfb,
  src/Oregano-Regular-TTF.vfb, a FontLab import of the shipped fonts, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Oregano — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

The original design sources for Oregano were found in the `googlefontdirectory-hg` monorepo. The sources are FontLab VFB files (proprietary format, not buildable with gftools-builder). No canonical designer-owned GitHub repository was found.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `oregano/src/`
- **Buildable**: No — legacy formats only (.vfb)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Oregano-Regular.vfb` | FontLab VFB | Original source with contour overlaps |
| `Oregano-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Oregano-Regular-TTF.vfb` | FontLab VFB | TrueType hinting adjustments |
| `Oregano-Italic.vfb` | FontLab VFB | Original source with contour overlaps |
| `Oregano-Italic-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Oregano-Italic-TTF.vfb` | FontLab VFB | TrueType hinting adjustments |
| `Oregano-Regular.otf` | Compiled binary | Not a design source |
| `Oregano-Italic.otf` | Compiled binary | Not a design source |

All design sources are in FontLab VFB format (proprietary binary). No UFO or Glyphs sources are available.

### Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Category**: DISPLAY
- **Google Fonts date added**: 2012-08-13
- **Copyright**: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name \"Oregano\""

### Investigation Details

#### GitHub Search

GitHub was searched for "Oregano font Astigmatic", "Oregano font Brian Bonislawsky", and "astigmatic font". The only result for "astigmatic font" was `googlefonts/SacramentoFont`, which is a separate Astigmatic font. No Oregano-specific repository was found under any Astigmatic-related account.

#### Designer Profile

No GitHub user account was found for "astigmatic", "AOETI", or "Bonislawsky". The Astigmatic website (`www.astigmatic.com`) was unreachable due to an expired SSL certificate.

#### Librefonts Mirror

The `librefonts/oregano` repository contains the same VFB source files as the googlefontdirectory-hg monorepo. This is a librefonts mirror, not a canonical designer-owned repository. The FONTLOG listed the 6 VFB source files as the original source files.

### Conclusion

The original design sources for Oregano are preserved in the `googlefontdirectory-hg` monorepo as FontLab VFB files. These are proprietary binary files not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

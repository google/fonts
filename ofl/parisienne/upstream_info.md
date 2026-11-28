# Parisienne

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Parisienne (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/parisienne.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Parisienne-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/parisienne at `2eca5ed2015f`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Parisienne-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/parisienne.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`2eca5ed2015f` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Parisienne-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Parisienne — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Summary

The original design sources for Parisienne were found in the `googlefontdirectory-hg` monorepo in FontLab VFB and FontForge SFD formats, which are not buildable with gftools-builder. No canonical designer-owned GitHub repository was found.

### Source Repository

- **Repo**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (historical Google Font Directory Mercurial monorepo)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `parisienne/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

#### Source Files

| File | Format | Notes |
|------|--------|-------|
| `Parisienne-Regular.vfb` | FontLab VFB | Original source with contour overlaps |
| `Parisienne-Regular-OTF.vfb` | FontLab VFB | Merged contours for OTF output |
| `Parisienne-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting adjustments |
| `Parisienne-Regular-TTF.sfd` | FontForge SFD | TrueType variant |
| `Parisienne-Regular.otf` | Compiled binary | Not a design source |

All primary design sources are in FontLab VFB format. The SFD file is a FontForge variant for TrueType output. No UFO or Glyphs sources are available.

### Family Details

- **Designer**: Astigmatic (Brian J. Bonislawsky DBA Astigmatic AOETI)
- **License**: OFL
- **Google Fonts date added**: 2012
- **Copyright**: "Copyright (c) 2012 by Brian J. Bonislawsky DBA Astigmatic (AOETI)"

### Investigation Details

The FONTLOG.txt described three VFB source files matching those found in the monorepo: the original source with overlaps, an OTF variant with merged contours, and a TTF variant with hinting adjustments.

Web searches were conducted for a GitHub repository under Astigmatic, googlefonts/ParisienneFont, and related variations. The only Astigmatic-attributed font found on GitHub under googlefonts was `googlefonts/SacramentoFont`. No dedicated Parisienne repository was found.

The DESCRIPTION.en_us.html contained no upstream repository link.

### Conclusion

The original design sources for Parisienne are preserved in the `googlefontdirectory-hg` monorepo as VFB and SFD files. These are legacy formats not buildable with gftools-builder. No modern sources or canonical designer-owned repository exist.

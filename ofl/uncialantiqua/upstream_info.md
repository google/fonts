# Uncial Antiqua

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Uncial Antiqua (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/uncialantiqua.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  UncialAntiqua-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/uncialantiqua at `084af67347bc`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
UncialAntiqua-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/uncialantiqua.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`084af67347bc` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/UncialAntiqua-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Uncial Antiqua — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Astigmatic (Brian J. Bonislawsky)

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `uncialantiqua/src/`.

#### Source Files

- **VFB (FontLab)**: UncialAntiqua-Regular-OTF.vfb, UncialAntiqua-Regular-TTF.vfb, UncialAntiqua-Regular.vfb
- **OTF (compiled)**: UncialAntiqua-Regular.otf

Sources are in VFB format (FontLab, proprietary), which is not buildable with gftools-builder.

### Investigation Details

Uncial Antiqua was designed by Brian J. Bonislawsky under the studio name Astigmatic (AOETI). It combines Uncial and Half Uncial letterforms.

The following searches were conducted:

1. **GitHub user/org search**: The GitHub account `astigmatic` was found but contained only two repositories unrelated to fonts (`pro` — an Android app project, and `project1`). No font repositories were present.
2. **Repository name search**: Searches for "uncial antiqua", "uncialantiqua", and "astigmatic font" returned no canonical font source repositories on GitHub.
3. **Astigmatic website**: astigmatic.com was not investigated further as Astigmatic is a commercial foundry that releases fonts for free distribution but typically does not publish editable source files.

Uncial Antiqua was contributed to Google Fonts by Astigmatic, a commercial type foundry. While the font is released under OFL, the source files have not been made publicly available. This is consistent with Astigmatic's other Google Fonts contributions.

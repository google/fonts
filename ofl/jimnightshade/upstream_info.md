# Jim Nightshade

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Jim Nightshade (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/jimnightshade.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  JimNightshade-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/jimnightshade at `11a5210e11c6`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
JimNightshade-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/jimnightshade.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`11a5210e11c6` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/jimnightshade at
  a04375d8b6c564c11f00a67fa5df1d7bf446527f: src/JimNightshade-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/jimnightshade"
      commit: "a04375d8b6c564c11f00a67fa5df1d7bf446527f"
    }

## Previous investigation

## Investigation: Jim Nightshade

### Summary

| Field | Value |
|-------|-------|
| Family Name | Jim Nightshade |
| Slug | jim-nightshade |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/jimnightshade |
| Commit Hash | a04375d8b6c564c11f00a67fa5df1d7bf446527f |
| Config YAML | none |
| Status | missing_config |
| Confidence | HIGH |

### Source Data (METADATA.pb)

No source block

### Investigation

The `ofl/jimnightshade/` directory in google/fonts contains `DESCRIPTION.en_us.html`, `FONTLOG.txt`, `JimNightshade-Regular.ttf`, `METADATA.pb`, and `OFL.txt`. The METADATA.pb has only basic metadata — no `source { }` block.

The git log shows the font has been in google/fonts since the initial commit (`90abd17b4`, 2015-03-07). No font file updates have been pushed since then.

The copyright reads: "Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI) (astigma@astigmatic.com), with Reserved Font Name 'Jim Nightshade'." Designed by Brian J. Bonislawsky for Astigmatic in 2011.

The tracking JSON (`data/gfonts_library_sources.json`) records the upstream repository as `https://github.com/librefonts/jimnightshade` at commit `a04375d8b6c564c11f00a67fa5df1d7bf446527f` (subject: "update .travis.yml"). This is the librefonts GitHub organization's mirror repository.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/librefonts/jimnightshade`. The local clone has only one commit (shallow clone). The repository contains:
- `JimNightshade-Regular.ttf` (binary font)
- `src/JimNightshade-Regular.vfb` (FontLab Studio source)
- `src/JimNightshade-Regular.otf` (OTF binary)
- `src/JimNightshade-Regular-OTF.vfb` and `src/JimNightshade-Regular-TTF.vfb` (FontLab variants)
- TTX decompositions of the fonts
- `src/VERSIONS.txt`: "JimNightshade-Regular.ttf: Version 1.000"

The source format is `.vfb` (FontLab Studio binary format), which is NOT compatible with gftools-builder. No `.glyphs`, `.ufo`, or `.designspace` files exist.

### Conclusion

The upstream repository is `https://github.com/librefonts/jimnightshade` at commit `a04375d8b6c564c11f00a67fa5df1d7bf446527f`. However, the only sources available are `.vfb` (FontLab Studio) files, which are not gftools-builder compatible. No config.yaml is possible with these sources. A source block needs to be added to METADATA.pb but the status will remain `missing_config` until buildable sources become available.

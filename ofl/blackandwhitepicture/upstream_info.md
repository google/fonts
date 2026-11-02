# Black And White Picture

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Black And White Picture as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/blackandwhitepicture.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  BlackAndWhitePicture-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/blackandwhitepicture at `75469c6eb209`.
Builds with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/blackandwhitepicture.json`:
https://github.com/felipesanches/gf-source-modernization at `4e08bb3`.

`75469c6eb209` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release has no glyph instructions: its font program defines functions that no
  glyph calls, and its control value program sets up the rasterizer without hinting any
  glyph. These sources carry no TrueType instructions, and the build is hinted by
  ttfautohint, as for every release that has a font program: the outlines, spacing and
  layout are the release's, its rendering at small sizes under a TrueType interpreter is
  not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- None known: google/fonts has no source block for this family; the fonts were added as
  built in google/fonts#1459 (2018, "korean families r01"), and AsiaSoft Inc. publishes
  no source repository.

## Previous investigation

## Investigation: Black And White Picture

### Summary

| Field | Value |
|-------|-------|
| Family Name | Black And White Picture |
| Slug | black-and-white-picture |
| License Dir | ofl |
| Repository URL | unknown |
| Commit Hash | unknown |
| Config YAML | unknown |
| Status | missing_url |
| Confidence | LOW |

### Source Data (METADATA.pb)

```
No source block
```

### Investigation

The METADATA.pb has no source block at all — no repository URL, no commit hash, no config_yaml.

The font was added to google/fonts in commit `16680f868` (March 13, 2018, PR #1459, "korean families r01: added"). This was a bulk addition of multiple Korean font families with no upstream reference information included.

The copyright string in METADATA.pb reads: "Copyright (c) 1992-2018 AsiaSoft Inc. Seoul Korea All Rights Reserved." This indicates the font was created by AsiaSoft Inc., a commercial Korean type foundry. No GitHub or publicly accessible source repository was found — a search of the upstream repos cache at `upstream_repos/fontc_crater_cache/` found no AsiaSoft-related repositories.

The google/fonts family directory (`ofl/blackandwhitepicture/`) contains only the TTF binary, DESCRIPTION, METADATA.pb, and OFL.txt — no upstream.yaml, no source references of any kind.

Given that this is a commercial Korean foundry font from 1992-2018, it is likely that the source files (if any exist in a form usable for rebuilding) are proprietary to AsiaSoft Inc. No public upstream repository has been identified.

### Conclusion

No upstream source information is available. The font comes from AsiaSoft Inc., a commercial Korean type foundry, and no public repository has been found. This family likely cannot have a source block added without direct contact with AsiaSoft Inc. Status is `missing_url` with LOW confidence that a public upstream repo exists.

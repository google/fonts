# Junge

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Junge (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/junge.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Junge-Regular.ttf, the
  font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/junge at `bf830898b0c0`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/junge.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`bf830898b0c0` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/junge at 1753e7a229f48ac314ad3c54da9fcfb2d7946f75:
  src/Junge-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/junge"
      commit: "1753e7a229f48ac314ad3c54da9fcfb2d7946f75"
    }

## Previous investigation

## Investigation: Junge

### Summary

| Field | Value |
|-------|-------|
| Family Name | Junge |
| Slug | junge |
| License Dir | ofl |
| Repository URL | https://github.com/librefonts/junge |
| Commit Hash | 1753e7a229f48ac314ad3c54da9fcfb2d7946f75 |
| Config YAML | none (OTF-only sources in librefonts mirror) |
| Status | no_config_possible |
| Confidence | MEDIUM |

### Source Data (METADATA.pb)

```
No source block
```

### Investigation

The METADATA.pb for Junge has no source block. The font was designed by Alexei Vanyashin for Cyreal, as noted in the copyright string: "Copyright (c) 2011, Cyreal (www.cyreal.org a@cyreal.org) with Reserved Font Name 'Junge'."

The git history in google/fonts shows the font has been present since the initial commit (`90abd17b4`), with only metadata-level changes (language fields, stroke/classifications) since then. No font binary update has occurred since initial onboarding.

The DESCRIPTION.en_us.html credits Alexei Vanyashin (`@avanyashin` on Twitter) as the designer. No GitHub repository is mentioned. No override `config.yaml` exists in the google/fonts `ofl/junge/` directory.

Searching the upstream cache at `upstream_repos/fontc_crater_cache/cyrealtype/` shows many Cyreal-maintained fonts (Adamina, Alice, Alike, Lora, etc.) but no Junge repository.

A `librefonts` mirror of Junge exists in the cache at `upstream_repos/fontc_crater_cache/librefonts/junge/`. This contains TTX-decompiled OTF files and a `src/` directory with more TTX files. No Glyphs, UFO, or other gftools-builder compatible sources are present. The commit `1753e7a229f48ac314ad3c54da9fcfb2d7946f75` is the recorded commit in the tracking JSON.

The font directory in google/fonts contains only:
- `Junge-Regular.ttf`
- `METADATA.pb`
- `OFL.txt`
- `DESCRIPTION.en_us.html`
- `FONTLOG.txt`

No override `config.yaml` exists in the google/fonts directory.

### Conclusion

Junge has a librefonts mirror at `https://github.com/librefonts/junge` with commit `1753e7a229f48ac314ad3c54da9fcfb2d7946f75`. The librefonts mirror contains only TTX-decompiled OTF files — no gftools-builder compatible sources. No `config.yaml` can be created without first identifying original editable source files from Cyreal. Status: no_config_possible.

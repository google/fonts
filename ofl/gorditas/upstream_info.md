# Gorditas

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Gorditas (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/gorditas.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Gorditas-{Bold,Regular}.ttf, the fonts Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/gorditas at `3b508646e06e`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 2 styles. Those tools,
including this family's plan `plans/gorditas.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`3b508646e06e` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/librefonts/gorditas at 2212c0647e87c13121e408ee446dffe924792ac1:
  src/Gorditas-Bold-TTF.vfb, src/Gorditas-Regular-TTF.vfb, a FontLab import of the
  shipped fonts, not a source: Simon on google/fonts#10490 ("batch-converted from the
  binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/gorditas"
      commit: "2212c0647e87c13121e408ee446dffe924792ac1"
    }

## Previous investigation

## Investigation Report: Gorditas

### Summary

Gorditas is a display slab-serif family designed by Gustavo Dipre, first added to Google Fonts on 2012-03-14. The upstream repository is at `https://github.com/librefonts/gorditas`. The repo contains only VFB (FontLab) and TTX source files -- no gftools-buildable sources (.glyphs, .ufo, .designspace) and no config.yaml. There is only a single commit in the upstream repo. Building with gftools-builder is not possible without a source format conversion.

### Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Gorditas |
| Repository URL    | https://github.com/librefonts/gorditas |
| Commit Hash       | `2212c0647e87c13121e408ee446dffe924792ac1` |
| Config YAML       | None (VFB-only sources, not gftools-buildable) |
| Source Files      | `src/Gorditas-Regular-TTF.vfb`, `src/Gorditas-Bold-TTF.vfb`, plus TTX decompositions |
| Status            | **no_config_possible** |
| Confidence        | **HIGH** |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb on main has NO source block. A source block with `repository_url` and `commit` was added on the `sources_info_2026-02-25` branch (commit `9a14639f3c6d`) but has not been merged to main yet.

#### Git History in google/fonts

- `90abd17b4` (2015-03-07): Initial commit (repository creation, Gorditas included from the start).
- `76adaf1d2` (2021-11-01): Deploy commit that included Gorditas file changes (deletion/restructuring). This is the only commit that modified the TTF files after the initial import.
- No gftools-packager or onboarding-style commit message exists; this font predates the modern onboarding workflow.

#### Upstream Repository Verification

The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/gorditas/`. Findings:
- Remote URL confirmed: `https://github.com/librefonts/gorditas`
- The repo has exactly ONE commit: `2212c06` ("update .travis.yml", 2014-10-17).
- Source files in `src/` directory:
  - `Gorditas-Regular-OTF.vfb` and `Gorditas-Bold-OTF.vfb` (OTF FontLab sources)
  - `Gorditas-Regular-TTF.vfb` and `Gorditas-Bold-TTF.vfb` (TTF FontLab sources)
  - TTX decompositions of OTF files
  - `VERSIONS.txt` and `METADATA_comments.txt`
- Root directory contains TTX decompositions of TTF files.
- NO `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` / `config.yml` files anywhere.
- No SFD files either.

#### Source Format Assessment

VFB (FontLab 5) is a proprietary binary format that is NOT supported by gftools-builder or fontc. To build this font from source, the VFB files would need to be converted to a modern format (e.g., .glyphs or .ufo), which is outside the scope of metadata enrichment.

#### Commit Hash Verification

With only a single commit (`2212c06`) in the upstream repo, dated 2014-10-17, this must be the commit that corresponds to the font files in google/fonts. The font was part of google/fonts from the initial commit (2015-03-07), consistent with the upstream repo predating the google/fonts repository.

### Conclusion

Gorditas has a valid upstream repository at `https://github.com/librefonts/gorditas` with a single commit. The sources are in VFB format (FontLab 5 proprietary), which is not buildable by gftools-builder. No config.yaml exists and none can be created without first converting the sources to a modern format.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/gorditas"
  commit: "2212c0647e87c13121e408ee446dffe924792ac1"
}
```

**Status**: no_config_possible
**Confidence**: HIGH

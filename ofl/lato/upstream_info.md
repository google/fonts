# Lato

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Lato as binaries only (google/fonts at commit `2eb0b48d5f76`). No
source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/lato.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  Lato-{Black,BlackItalic,Bold,BoldItalic,ExtraBold,ExtraBoldItalic,ExtraLight,ExtraLightItalic,Italic,Light,LightItalic,Medium,MediumItalic,Regular,SemiBold,SemiBoldItalic,Thin,ThinItalic}.ttf,
  the fonts Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs
  branch 2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it
  (#117, typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/lato at `3a099680152e`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 18 styles. Those tools,
including this family's plan `plans/lato.json`:
https://github.com/felipesanches/gf-source-modernization at `f073f4e`.

`3a099680152e` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the releases', its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/LatoGFVersion at
  080cb69711ca050d91e9c866e58df7a73095c69a: the fonts as built (36 font files); no
  source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      commit: "080cb69711ca050d91e9c866e58df7a73095c69a"
      repository_url: "https://github.com/googlefonts/LatoGFVersion"
    }

## Previous investigation

## Investigation: Lato

### Summary

| Field | Value |
|-------|-------|
| Family Name | Lato |
| Slug | lato |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/LatoGFVersion |
| Commit Hash | unknown |
| Config YAML | none |
| Status | missing_commit |
| Confidence | MEDIUM |

### Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/LatoGFVersion"
}
```

### Investigation

The METADATA.pb has a `repository_url` pointing to `https://github.com/googlefonts/LatoGFVersion` but no commit hash.

The google/fonts git history for `ofl/lato/Lato-Regular.ttf` shows:
- `f3b885d55` — "lato: v2.015 added (#479)" — 2016-12-02

The commit body for `f3b885d55` references: "Version 2.015 release for Google Fonts. These fonts have been hot fixed from the original sources. The hot fix source repository is here https://github.com/googlefonts/LatoGFVersion"

The upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/LatoGFVersion/` was last updated on 2016-11-28 with commit `080cb69` ("fonts: regenerated"). This is almost certainly the commit used for the onboarding (matching the timing).

The LatoGFVersion repo structure:
- `build/` — build scripts (shell, Python)
- `fonts/` — output fonts directory
- `src/` — prebuilt TTF source files

This repo contains prebuilt TTF files in `src/` rather than design-time sources. There is no `config.yaml` for gftools-builder.

### Conclusion

The repository URL is present but the commit hash is missing. The most likely onboarding commit is `080cb69` ("fonts: regenerated", 2016-11-28), which is the HEAD of the LatoGFVersion repo at the time of the google/fonts addition. However, the source contains only prebuilt TTF files and custom shell/Python build scripts — no gftools-builder compatible sources. No `config.yaml` is possible without proper design sources.

### Commit Added (MEDIUM confidence)

Commit `080cb69711ca050d91e9c866e58df7a73095c69a` was determined by **date_correlation**. Found the latest upstream commit before the binary modification date in google/fonts (2016-12-02). This assumes the upstream HEAD at onboarding time was the commit used.

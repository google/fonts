# Dynalight

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Dynalight (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/dynalight.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Dynalight-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/dynalight at `928472e4d060`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Dynalight-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/dynalight.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`928472e4d060` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/dynalight at af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49:
  src/Dynalight-Regular-TTF.vfb, a FontLab import of the shipped font, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/dynalight"
      commit: "af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49"
    }

## Previous investigation

## Investigation Report: Dynalight

**Date investigated:** 2026-02-27
**Status:** `missing_config` (VFB-only sources, no gftools-builder config possible)
**Designer:** Brian J. Bonislawsky (Astigmatic)

### METADATA.pb Path

`ofl/dynalight/METADATA.pb`

### Source Data

| Field            | Value                                                    |
|------------------|----------------------------------------------------------|
| repository_url   | `https://github.com/librefonts/dynalight`                |
| commit           | `af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49`              |
| branch           | `master`                                                 |
| config_yaml      | N/A (VFB-only sources)                                   |

### How URL Was Found

The upstream repository URL `https://github.com/librefonts/dynalight` was already recorded in the tracking data (`data/gfonts_library_sources.json`). The `librefonts` GitHub organization hosts mirrors of Google Fonts source repositories, created by user hash3g. The repository is accessible (HTTP 200) and contains the font sources.

No original Astigmatic-owned repository was found. The librefonts mirror appears to be the only public source repository for this font.

### How Commit Hash Was Identified

The upstream repository contains exactly one commit:

```
af7642053cc1189c5c8a4b93d0b4c1b1c5edcb49 2014-10-17 "update .travis.yml"
```

This single commit, authored by hash3g on 2014-10-17, constitutes the entire repository content. It added all files including source VFBs, TTX decompositions, FONTLOG.txt, license, and a Travis CI configuration. Since there is only one commit, the hash identification is trivial.

The font was added to Google Fonts on 2011-12-19 (per METADATA.pb `date_added`), well before the librefonts mirror was created in 2014. The font binary was part of the google/fonts "Initial commit" on 2015-03-07, which was the bulk import of the entire existing catalog at the time.

### How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository, and none can be created because the source files are exclusively in FontLab VFB format:

- `src/Dynalight-Regular.vfb` -- Original source with contour overlaps
- `src/Dynalight-Regular-OTF.vfb` -- Merged contours for OTF
- `src/Dynalight-Regular-TTF.vfb` -- TrueType outlines with hinting

VFB is a proprietary FontLab Studio binary format that is not supported by gftools-builder. The repository also contains TTX decompositions of both TrueType and OpenType builds, but these are not suitable as gftools-builder sources either.

No override `config.yaml` exists in the google/fonts family directory (`ofl/dynalight/`).

### Verification

- **Repository accessible:** Yes (HTTP 200 at `https://github.com/librefonts/dynalight`)
- **Repository clean:** Yes (no local modifications)
- **Branch:** `master` (single branch)
- **Commit exists:** Yes, `af76420` is the sole commit in the repository
- **Font binary in google/fonts:** `Dynalight-Regular.ttf` (53,148 bytes), present since the initial commit (2015-03-07)
- **Font version:** 1.000 (per `src/VERSIONS.txt`)
- **Source block in METADATA.pb (main):** Not yet present (source block exists on `sources_info_2026-02-25` branch from PR #10278)

### Confidence

**HIGH** -- The repository URL and commit hash are unambiguous. The librefonts mirror has a single commit containing all sources. The font has never been updated in google/fonts since the initial bulk import. The limitation is purely that VFB sources cannot be built with gftools-builder, so no config.yaml is applicable.

### Notes

- This is a librefonts mirror, not an original designer-owned repository. The original sources were created by Brian J. Bonislawsky of Astigmatic (AOETI).
- The font was added to Google Fonts in December 2011, predating the google/fonts GitHub repository.
- The copyright field contains a Reserved Font Name ("Dynalight").
- The font is classified as both DISPLAY and HANDWRITING.
- No PRs to google/fonts specifically reference Dynalight.

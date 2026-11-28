# Chewy

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Chewy as binaries only (google/fonts at commit `2eb0b48d5f76`). No
source of the family was ever published, so it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/chewy.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Chewy-Regular.ttf, the
  font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/chewy at `5e436e354055`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/chewy.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`5e436e354055` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns with a legacy `kern` table (399 pairs) and has no GPOS; these
  sources kern through a GPOS kern feature, which is how fontc builds kerning. HarfBuzz
  shapes every kerned pair alike in both (the functional gate). Decided 2026-10-01:
  releases with an old kern table are accepted and disclosed.
- The released font is hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/librefonts/chewy at 7fae11600a5c13c94a0780ec22ae5309264c43d0: the
  font as built, dumped to TTX, and its metadata; no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/chewy"
      commit: "7fae11600a5c13c94a0780ec22ae5309264c43d0"
    }

## Previous investigation

## Investigation Report: Chewy

### Summary

Chewy is a display font designed by Sideshow (Font Diner DBA), added to Google Fonts on 2011-01-06. The upstream repository is `librefonts/chewy` on GitHub, which contains only TTX-decomposed source files -- no `.glyphs`, `.ufo`, or `.designspace` sources. The repository has a single commit and no `config.yaml`. Since the sources are TTX-only (not gftools-builder compatible), no config.yaml can be created.

### Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Chewy                                                    |
| Designer            | Sideshow                                                 |
| License             | Apache 2.0                                               |
| Date Added          | 2011-01-06                                               |
| Repository URL      | https://github.com/librefonts/chewy                      |
| Commit Hash         | 7fae11600a5c13c94a0780ec22ae5309264c43d0                 |
| Config YAML         | None (TTX-only sources, not gftools-builder compatible)  |
| Status              | **no_config_possible**                                   |
| Confidence          | HIGH                                                     |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb at `apache/chewy/METADATA.pb` has no `source { }` block. It lists a single font file `Chewy-Regular.ttf` at weight 400, normal style. The copyright attributes it to "Font Diner, Inc DBA Sideshow."

#### Git History in google/fonts

The binary TTF file was last modified in a single commit:

- **577b1ca8c** (2017-08-07) - `hotfix-chewy: v1.001 added (#767)` by Marc Foley. This renamed the file from `Chewy.ttf` to `Chewy-Regular.ttf`, updated METADATA.pb fields and DESCRIPTION. PR #767 had an empty body.

Before that, the font was present since the initial commit `90abd17b4` (2015-03-07) by Dave Crossland.

#### Upstream Repository Analysis

The repository at `https://github.com/librefonts/chewy` is accessible (not archived). It was created on 2014-07-16 and contains a single commit:

- **7fae116** (2014-10-17) - `update .travis.yml`

The repo contains:
- Root: TTX-decomposed font files (`Chewy.ttf.*.ttx`), a master TTX file (`Chewy.ttf.ttx`), `COPYRIGHT.txt`, `DESCRIPTION.en_us.html`, `LICENSE.txt`, `METADATA.json`, `.travis.yml`
- `src/`: VTT-hinted TTX-decomposed sources (`Chewy-VTT.ttf.*.ttx`), including TSI tables for VTT hints, plus `METADATA_comments.txt` and `VERSIONS.txt`

The `VERSIONS.txt` shows `Chewy.ttf: Version 1.000`. The `METADATA_comments.txt` contains legacy font-optimizer subset commands.

There are **no** `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files anywhere in the repository. The only "source" is the TTX decomposition of the original binary font. This is a legacy librefonts repo created as an automated dump of the Google Fonts font for CI testing purposes, not a true source repository.

#### Source File Assessment

The sources are TTX-only. TTX files are XML decompositions of compiled font binaries -- they are not editable design sources and cannot be used with gftools-builder. No `config.yaml` can be created for this repository because gftools-builder requires `.glyphs`, `.ufo`, or `.designspace` sources.

#### Hotfix Context

The PR #767 hotfix by Marc Foley (2017-08-07) applied filename normalization (adding `-Regular` suffix) as part of a batch of hotfixes for many Font Diner fonts. This was done directly in google/fonts, not from upstream sources.

### Conclusion

The `librefonts/chewy` repository is a legacy automated TTX dump, not a true design source repository. It has only one commit. Since the repo contains only TTX-decomposed files and no gftools-builder compatible sources, no `config.yaml` is possible.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/chewy"
  commit: "7fae11600a5c13c94a0780ec22ae5309264c43d0"
}
```

Note: `config_yaml` is omitted because the repository contains only TTX sources that are not compatible with gftools-builder.

#### Status: `no_config_possible`
#### Confidence: HIGH

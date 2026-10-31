# Coming Soon

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Coming Soon as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/comingsoon.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from ComingSoon-Regular.ttf,
  the font Google Fonts ships, with babelfont 58eedc8 (felipesanches/babelfont-rs branch
  2026-10-22: simoncozens/babelfont-rs main plus the TTF reader changes proposed to it):
  its TTF reader, no filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/comingsoon at `f371c8c2992f`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/comingsoon.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`f371c8c2992f` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns through a GPOS kern feature and also carries a legacy `kern` table
  (861 pairs). Shapers read the GPOS feature, which these sources keep; the legacy
  table, read only by software without GPOS support, is not carried.
- The release has no glyph instructions: its font program defines functions that no
  glyph calls, and its control value program only turns on dropout control (SCANCTRL
  511, SCANTYPE 4). These sources carry no TrueType instructions, and the build is
  hinted by ttfautohint, as for every release that has a font program: the outlines,
  spacing and layout are the release's, its rendering at small sizes under a TrueType
  interpreter is not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/librefonts/comingsoon at 27c886594addb8deb44976ee37f829f2c8253a9d:
  version 1.000 as built, dumped to TTX, and its metadata; no source. The release
  converted here is version 1.002, Google Fonts' 2017 contour fix.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/comingsoon"
      commit: "27c886594addb8deb44976ee37f829f2c8253a9d"
    }

## Previous investigation

## Investigation Report: Coming Soon

### Summary

Coming Soon is a handwriting font designed by Open Window, added to Google Fonts on 2011-01-06. The upstream repository is `librefonts/comingsoon` on GitHub, which contains only TTX-decomposed source files -- no `.glyphs`, `.ufo`, or `.designspace` sources. The repository has a single commit and no `config.yaml`. Since the sources are TTX-only (not gftools-builder compatible), no config.yaml can be created.

### Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Coming Soon                                              |
| Designer            | Open Window                                              |
| License             | Apache 2.0                                               |
| Date Added          | 2011-01-06                                               |
| Repository URL      | https://github.com/librefonts/comingsoon                 |
| Commit Hash         | 27c886594addb8deb44976ee37f829f2c8253a9d                 |
| Config YAML         | None (TTX-only sources, not gftools-builder compatible)  |
| Status              | **no_config_possible**                                   |
| Confidence          | HIGH                                                     |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb at `apache/comingsoon/METADATA.pb` has no `source { }` block. It lists a single font file `ComingSoon-Regular.ttf` at weight 400, normal style.

#### Git History in google/fonts

The binary TTF file has two modification commits:

1. **0fc4c4f4a** (2017-12-14) - `apache/comingsoon: contour issues fixed. v1.002 added.` by Micah Stupak. This is the most recent change to the binary, fixing contour issues and bumping to v1.002. This commit was made directly in google/fonts (not via a PR).

2. **58e6b4444** (2017-08-07) - `hotfix-comingsoon: v1.001 added (#768)` by Marc Foley. This renamed the file from `ComingSoon.ttf` to `ComingSoon-Regular.ttf` and updated METADATA.pb. PR #768 had an empty body.

Before that, the font was present since the initial commit `90abd17b4` (2015-03-07) by Dave Crossland.

#### Upstream Repository Analysis

The repository at `https://github.com/librefonts/comingsoon` is accessible (not archived). It was created on 2014-07-16 and contains a single commit:

- **27c8865** (2014-10-17) - `update .travis.yml`

The repo contains:
- Root: TTX-decomposed font files (`ComingSoon.ttf.*.ttx`), a master TTX file (`ComingSoon.ttf.ttx`), `COPYRIGHT.txt`, `DESCRIPTION.en_us.html`, `LICENSE.txt`, `METADATA.json`, `.travis.yml`
- `src/`: TTX-decomposed sources (`ComingSoon-TTX.ttf.*.ttx`), including TSI tables for VTT hints, plus `METADATA_comments.txt` and `VERSIONS.txt`

The `VERSIONS.txt` shows `ComingSoon.ttf: Version 1.000`. The `METADATA_comments.txt` is essentially empty (just `# COMMENTS`).

There are **no** `.glyphs`, `.ufo`, `.designspace`, or `.sfd` source files anywhere in the repository. The only "source" is the TTX decomposition of the original binary font. This is a legacy librefonts repo created as an automated dump of the Google Fonts font for CI testing purposes, not a true source repository.

#### Source File Assessment

The sources are TTX-only. TTX files are XML decompositions of compiled font binaries -- they are not editable design sources and cannot be used with gftools-builder. No `config.yaml` can be created for this repository because gftools-builder requires `.glyphs`, `.ufo`, or `.designspace` sources.

#### Binary Modification Note

The current binary in google/fonts (v1.002) was modified directly by Micah Stupak to fix contour issues. This modification was not reflected in the upstream librefonts repo, which still contains the original v1.000 TTX decomposition. The upstream repo predates both hotfixes and does not represent the current state of the font in google/fonts.

#### Hotfix Context

PR #768 by Marc Foley (2017-08-07) applied filename normalization (adding `-Regular` suffix). A subsequent direct commit by Micah Stupak (2017-12-14) fixed contour issues and bumped the version to 1.002. Both modifications were done directly in google/fonts.

### Conclusion

The `librefonts/comingsoon` repository is a legacy automated TTX dump, not a true design source repository. It has only one commit. The current binary in google/fonts (v1.002) has been modified beyond what the upstream repo contains (v1.000). Since the repo contains only TTX-decomposed files and no gftools-builder compatible sources, no `config.yaml` is possible.

#### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/librefonts/comingsoon"
  commit: "27c886594addb8deb44976ee37f829f2c8253a9d"
}
```

Note: `config_yaml` is omitted because the repository contains only TTX sources that are not compatible with gftools-builder. The upstream repo at this commit contains v1.000 sources, while google/fonts has v1.002 (contour-fixed binary modified directly in google/fonts).

#### Status: `no_config_possible`
#### Confidence: HIGH

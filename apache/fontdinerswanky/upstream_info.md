# Fontdiner Swanky

**Model**: Claude Opus 5.5
**Date**: 2026-10-23

Sources created 2026-10: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Fontdiner Swanky as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/fontdinerswanky.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  FontdinerSwanky-Regular.ttf, the font Google Fonts ships, with babelfont 58eedc8
  (felipesanches/babelfont-rs branch 2026-10-22: simoncozens/babelfont-rs main plus the
  TTF reader changes proposed to it): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/fontdinerswanky at `bcf47dbb493c`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/fontdinerswanky.json`:
https://github.com/felipesanches/gf-source-modernization at `e6f2b15`.

`bcf47dbb493c` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The release kerns with a legacy `kern` table (3290 pairs) and has no GPOS; these
  sources kern through a GPOS kern feature, which is how fontc builds kerning. HarfBuzz
  shapes every kerned pair alike in both (the functional gate). Decided 2026-10-01:
  releases with an old kern table are accepted and disclosed.
- The release has no glyph instructions: its font program defines functions that no
  glyph calls, and its control value program only turns on dropout control (SCANCTRL
  511, SCANTYPE 4). These sources carry no TrueType instructions, and the build is
  hinted by ttfautohint, as for every release that has a font program: the outlines,
  spacing and layout are the release's, its rendering at small sizes under a TrueType
  interpreter is not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/librefonts/fontdinerswanky at
  5b2cf4d5d4919c4d21a73ce08e1bf93d853571d2: version 1.000 as built, dumped to TTX, and
  its metadata; no source. The release converted here is version 1.001.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/fontdinerswanky"
      commit: "5b2cf4d5d4919c4d21a73ce08e1bf93d853571d2"
    }

## Previous investigation

## Investigation Report: Fontdiner Swanky

### Summary

Fontdiner Swanky is a display serif font designed by Font Diner, added to Google Fonts on 2011-01-06 under the Apache 2.0 license. The upstream repository is at `librefonts/fontdinerswanky` on GitHub. The repository contains only TTX table dumps -- no original editable source files at all (not even VFB). There is no `config.yaml` and no gftools-builder compatible sources. An override config.yaml is not feasible.

### Key Findings

| Field               | Value                                                    |
|---------------------|----------------------------------------------------------|
| Family Name         | Fontdiner Swanky                                         |
| Designer            | Font Diner                                               |
| License             | Apache 2.0                                               |
| Date Added          | 2011-01-06                                               |
| Repository URL      | https://github.com/librefonts/fontdinerswanky            |
| Commit Hash         | 5b2cf4d5d4919c4d21a73ce08e1bf93d853571d2                 |
| Branch              | master                                                   |
| Config YAML         | None (no gftools-builder compatible sources)             |
| Source Types         | TTX dumps only (no editable sources)                    |
| Status              | no_config_possible                                       |
| Confidence          | HIGH                                                     |

### Investigation Details

#### METADATA.pb Analysis

The current METADATA.pb at `apache/fontdinerswanky/METADATA.pb` has **no source block**. It contains basic metadata: family name "Fontdiner Swanky", designer "Font Diner", license Apache 2.0, font entry with weight 400, subsets (latin, menu), and classifications (DISPLAY, SERIF).

#### Git History in google/fonts

The font was part of the initial commit (`90abd17b4`, 2015-03-07, Dave Crossland) which imported all fonts. The binary was later updated in PR #775 (`c9bc5498a`, 2017-08-07, Marc Foley) with the commit message "hotfix-fontdinerswanky: v1.001 added". This hotfix renamed `FontdinerSwanky.ttf` to `FontdinerSwanky-Regular.ttf` and updated METADATA.pb. The PR body was empty. The file size remained identical at 45,524 bytes, suggesting only a metadata/naming fix.

#### Upstream Repository

The upstream repo `https://github.com/librefonts/fontdinerswanky` was created on 2014-07-16. It is part of the `librefonts` organization. The repo has a single commit:

- `5b2cf4d` (2014-10-17): "update .travis.yml" -- this is the only commit and therefore the only possible reference.

The repository is cached at `fontc_crater_cache/librefonts/fontdinerswanky/`. It is clean with no local modifications.

#### Source Files

The repository contains:
- Multiple `FontdinerSwanky.ttf.*.ttx` files -- TTX table dumps from the original binary
- `src/VERSIONS.txt` (records "FontdinerSwanky.ttf: Version 1.000")
- `src/METADATA_comments.txt` (empty)
- `METADATA.json`, `DESCRIPTION.en_us.html`, `LICENSE.txt`, `COPYRIGHT.txt`
- `.travis.yml` for CI

Critically, there are **no editable source files at all** -- no `.vfb`, `.glyphs`, `.ufo`, `.designspace`, or `.sfd` files. The `src/` directory contains only metadata text files. The TTX dumps could theoretically be reassembled into a TTF, but this is not a gftools-builder workflow and would not constitute proper source files.

#### Onboarding Commit Determination

The librefonts repo has only one commit (`5b2cf4d`), so it is trivially the correct reference. The hotfix in google/fonts (PR #775) appears to have been produced by Marc Foley running a naming fixup directly on the TTF binary rather than rebuilding from source.

### Conclusion

**Status: no_config_possible**

The upstream repo exists but only contains TTX table dumps with no editable source files. No config.yaml can be created because there are no gftools-builder compatible sources.

#### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/librefonts/fontdinerswanky"
  commit: "5b2cf4d5d4919c4d21a73ce08e1bf93d853571d2"
  branch: "master"
}
```

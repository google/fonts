# Flavors

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Flavors (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/flavors.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Flavors-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/flavors at `4131dec31a73`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/flavors.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`4131dec31a73` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/flavors at 494aad3c703cd55dfa728cded360b49e128dc101:
  src/Flavors-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/flavors"
      commit: "494aad3c703cd55dfa728cded360b49e128dc101"
    }

## Previous investigation

## Investigation: Flavors

### Summary

| Field | Value |
|---|---|
| Family Name | Flavors |
| Designer | Sideshow (Dave 'Squid' Cohen / Font Diner) |
| License | OFL |
| Date Added | 2011-12-19 |
| Category | DISPLAY, HANDWRITING |
| Repository URL | https://github.com/librefonts/flavors |
| Commit | `494aad3c703cd55dfa728cded360b49e128dc101` |
| Branch | master |
| Config YAML | N/A (no buildable sources) |
| Status | no_buildable_sources |
| Confidence | HIGH |

### Upstream Repository

The upstream repository is `https://github.com/librefonts/flavors`, a mirror/archive created by Mikhail Kashkin (GitHub: hash3g) on 2014-07-16. The initial commit message is "Move flavors font files to separate repository", indicating this was extracted from a larger collection (likely the googlefontdirectory monorepo).

The repository has 10 commits total, all from 2014, with the last one on 2014-10-17 being a Travis CI configuration update. The repo has not been modified since.

#### Commit History

| Commit | Date | Description |
|---|---|---|
| `629e1902dab3` | 2014-07-16 | Move flavors font files to separate repository (initial) |
| `bb8f7555dff2` | 2014-08-19 | Added .travis.yml |
| `67b1df3556d3` | 2014-08-21 | Travis.yml update |
| `8baf74b89005` | 2014-08-22 | Travis.yml update |
| `bf724f96a07d` | 2014-09-11 | update .travis.yml |
| `a67001dbf329` | 2014-09-14 | Installing ttfautohint from ppa |
| `74d03e6aaab9` | 2014-09-15 | Update .travis.yml |
| `c70aa0b57440` | 2014-09-19 | Update .travis.yml |
| `a2e43e07252c` | 2014-10-06 | Rename fontbakery |
| `494aad3c703c` | 2014-10-17 | update .travis.yml (HEAD) |

All commits after the initial one are Travis CI configuration changes. No font source files were modified after the initial commit.

### Source Files

The repository contains:

- `src/Flavors-Regular-TTF.vfb` - FontLab binary format (VFB), not buildable with gftools-builder
- `Flavors-Regular.ttf.*.ttx` - TTX table dumps (17 files), decomposed from the TTF binary
- `FONTLOG.txt`, `DESCRIPTION.en_us.html`, `METADATA.json`, `OFL.txt` - metadata files

There are NO gftools-builder compatible source files (.glyphs, .ufo, .designspace, .sfd). The only source is a VFB file, which is a proprietary FontLab format.

### Google Fonts History

#### Initial Addition (2015-03-07)

Flavors was part of the initial commit (`90abd17b4`) by Dave Crossland. The TTF file was 186,640 bytes, Version 1.000.

#### Name Table Fix - PR #1362 (merged 2019-07-08)

PR [#1362](https://github.com/google/fonts/pull/1362) by laerm0 (Micah Stupak) applied a FontForge roundtrip to fix an OS X name table validation issue. The TTF was updated to v1.01 (184,784 bytes). This was a direct fix, not built from the upstream repository. Commit `7da86e3f4`.

This is the last commit that modified the TTF file. The current binary in google/fonts does NOT correspond to any commit in the upstream repository -- it was modified directly by a FontForge roundtrip after the initial onboarding.

### Commit Hash Verification

The recorded commit `494aad3c703cd55dfa728cded360b49e128dc101` is the latest commit in the upstream repository (HEAD of master). Since the upstream repo is a mirror created in 2014 and the font was initially onboarded from the googlefontdirectory, and since all commits after the initial one are Travis CI changes only, this commit effectively represents the same font sources as the initial commit.

The font in google/fonts was further modified by PR #1362 (FontForge roundtrip, 2017) which was not reflected in the upstream repo. The upstream repo accurately represents the pre-fix version of the sources.

### Config YAML

No config.yaml is possible. The only source file is a VFB (FontLab binary), which cannot be built with gftools-builder. No override config.yaml should be created.

### METADATA.pb Source Block

Currently on main, there is no source block. A source block was added on branch `sources_info_2026-02-25` (commit `9a14639f3`) but has not been merged to main yet.

The proposed source block:

```
source {
  repository_url: "https://github.com/librefonts/flavors"
  commit: "494aad3c703cd55dfa728cded360b49e128dc101"
}
```

This is correct. No `config_yaml` field is needed since there are no buildable sources.

### Conclusion

Flavors is a display font by Font Diner (Dave 'Squid' Cohen). The upstream repository at `librefonts/flavors` is a mirror with VFB-only sources. The font cannot be rebuilt with gftools-builder. The source block with repository URL and commit hash is correct and complete for this family's capabilities. Status is `no_buildable_sources` -- the VFB format is proprietary and not supported by modern open-source font build tooling.

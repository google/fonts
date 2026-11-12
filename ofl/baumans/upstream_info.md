# Baumans

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Baumans (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontLab import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/baumans.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Baumans-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/baumans at `0940714afd9d`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/baumans.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`0940714afd9d` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/baumans at 00e0253a48feaa474db9cd5145ec21891f1d7214:
  src/Baumans-Regular-TTF.vfb, a FontLab import of the shipped font, not a source: Simon
  on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/baumans"
      commit: "00e0253a48feaa474db9cd5145ec21891f1d7214"
    }

## Previous investigation

## Baumans - Investigation Report

### Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Baumans |
| Repository URL | https://github.com/librefonts/baumans |
| Commit Hash | 00e0253a48feaa474db9cd5145ec21891f1d7214 |
| Config YAML | (none) |
| Status | missing_config |
| Category | DISPLAY |
| Designer | Cyreal |
| Date Added | 2011-12-07 |

### How the Repository URL Was Found

The repository URL `https://github.com/librefonts/baumans` was identified from the fontc_crater cache and added to METADATA.pb as part of a bulk source block addition (commit `9a14639f3` in google/fonts). The `librefonts` GitHub organization hosts mirrors of many Google Fonts projects, and this repository contains the Baumans source files.

### How the Commit Hash Was Determined

The commit hash `00e0253a48feaa474db9cd5145ec21891f1d7214` is the latest (and only visible) commit in the upstream repository, titled "update .travis.yml". The repository appears to have been cloned as a shallow clone with only 1 commit visible. Since this is the only commit available, and the repository only has this single grafted commit, it was used as the reference commit.

The font binary in google/fonts was last modified in commit `75a425850` ("hotfix-baumans: v1.002 added", PR #849, August 2017, by Marc Foley). The PR body was empty, so no upstream commit was referenced.

### Config YAML Status

**No config.yaml exists** in the upstream repository at the recorded commit. The repository contains only legacy source formats:
- `.vfb` files (FontLab Studio format) in the `src/` directory
- `.ttx` files (XML font table dumps) at the root level
- No `.glyphs`, `.ufo`, or `.designspace` source files

There is also no override `config.yaml` in the google/fonts family directory (`ofl/baumans/`).

This font predates the gftools-builder workflow. The source files are in VFB format, which is not directly buildable by gftools-builder. This is why the status is `missing_config` - there are no buildable source files to configure.

### Verification

- **Repository exists**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/baumans/`
- **Commit exists**: Yes, `00e0253` is confirmed in the repo ("update .travis.yml")
- **Repo structure**: Contains `.ttx` dumps, `.vfb` source files in `src/`, `OFL.txt`, `FONTLOG.txt`, `DESCRIPTION.en_us.html`
- **METADATA.pb has source block**: Yes (added in bulk, no config_yaml field)

### Confidence Level

**Medium** - The repository URL is correct (it contains Baumans font files), but the commit hash is simply the latest commit in the repo rather than a verified onboarding commit. The `librefonts` organization hosts many Google Fonts, and the repo predates modern tracking practices. There is no way to precisely trace which commit was used for the 2017 hotfix since the PR body was empty and the repo only has one visible commit (shallow clone).

### Open Questions

1. Should this family be considered "complete" despite having no buildable sources? The VFB format requires FontLab to convert, which is outside the gftools-builder workflow.
2. The upstream repo appears to be a shallow clone - fetching full history might reveal additional commits that could help identify the exact onboarding commit.

# Carrois Gothic SC

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Carrois Gothic SC (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/carroisgothicsc.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  CarroisGothicSC-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/carroisgothicsc at `ff248c4f388d`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/carroisgothicsc.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`ff248c4f388d` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/carroisgothicsc at
  cd21c85aa57e4b1fc55eca2e31692cbd749e4e46: src/CarroisGothicSC-Regular-TTF.vfb, a
  FontLab import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/carroisgothicsc"
      commit: "cd21c85aa57e4b1fc55eca2e31692cbd749e4e46"
    }

## Previous investigation

## Investigation: Carrois Gothic SC

### Source Data

| Field | Value |
|---|---|
| Family Name | Carrois Gothic SC |
| Designer | Carrois Apostrophe |
| License | OFL |
| Date Added | 2012-09-30 |
| Repository URL | https://github.com/librefonts/carroisgothicsc |
| Commit Hash | `cd21c85aa57e4b1fc55eca2e31692cbd749e4e46` |
| Branch | master |
| Config YAML | None |
| Override Config | No |
| Status | missing_config |

### How URL Found

The repository URL `https://github.com/librefonts/carroisgothicsc` was recorded in the tracking data and added to the METADATA.pb source block in commit `9a14639f3` on branch `sources_info_2026-02-25` (not yet merged to main). This is a librefonts mirror repository, separate from the Carrois Gothic (non-SC) repo.

### How Commit Determined

The commit hash `cd21c85aa57e4b1fc55eca2e31692cbd749e4e46` is the HEAD (and only) commit of the upstream repository, with the message "update .travis.yml". The repository has only a single commit, so there is no ambiguity.

The font was originally part of the initial google/fonts commit (`90abd17b4`). A hotfix was later applied in commit `e57e3eea9` (PR #875) by Marc Foley on 2017-05-08, updating the TTF from its original version to v1.002. This hotfix modified the binary and metadata but the upstream librefonts repo was not updated to reflect this.

### Verification

- **Commit exists in upstream repo**: Yes. `cd21c85` is the HEAD and sole commit.
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/librefonts/carroisgothicsc/`.
- **Source files present**: The `src/` directory contains VFB files (FontLab Studio binary format): `CarroisGothicSC-Regular.vfb`, `CarroisGothicSC-Regular-OTF.vfb`, `CarroisGothicSC-Regular-TTF.vfb`. No open-format sources (.glyphs, .ufo, .designspace, .sfd) are available.
- **TTX decomposed files**: The root directory and `orig/` directory contain TTX-decomposed font data, but these are not standard buildable sources for gftools-builder.

### Config YAML Status

**No config.yaml possible.** The upstream repository only contains VFB files (FontLab Studio proprietary binary format), which are not supported by gftools-builder. There are no SFD, Glyphs, UFO, or Designspace files that could be used as build sources.

No override config.yaml exists in the google/fonts family directory either.

### Relationship to Carrois Gothic

Carrois Gothic SC is the small-caps variant of Carrois Gothic. Both were designed by Ralph du Carrois (Carrois Apostrophe) and share the same history:
- Added in the initial google/fonts commit
- Hotfixed by Marc Foley in May 2017 (PR #875 for SC, PR #874 for regular)
- Upstream librefonts repos each have a single commit and contain VFB-only sources
- Neither has gftools-builder-compatible sources

### Confidence Level

**HIGH** -- The commit hash is the only commit in the single-commit repository. The repository URL is a standard librefonts mirror. The situation is identical to Carrois Gothic (non-SC).

### Open Questions

- Same as Carrois Gothic: VFB sources would need conversion to an open format before any config.yaml could be created.
- The hotfix PR #875 (2017) updated the binary in google/fonts but the upstream was never synced.
- The status should remain `missing_config` as there are no gftools-builder-compatible sources.

# Berkshire Swash

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Berkshire Swash (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/berkshireswash.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  BerkshireSwash-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/berkshireswash at `e18507cc4dd2`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts
2eb0b48d5f76, under tools/table_gate.py and tools/functional_gate.py:
BerkshireSwash-Regular: 2 blocking rows; functionally equivalent. Those tools, including
this family's plan `plans/berkshireswash.json`:
https://github.com/felipesanches/gf-source-modernization at `d6a61f4`.

`e18507cc4dd2` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/librefonts/berkshireswash at
  1a4fb49d514e01ada8934472cae85cc4590efa58: src/BerkshireSwash-Regular-TTF.vfb, a
  FontLab import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/librefonts/berkshireswash"
      commit: "1a4fb49d514e01ada8934472cae85cc4590efa58"
    }

## Previous investigation

## Berkshire Swash - Investigation Report

### Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Berkshire Swash |
| Repository URL | https://github.com/librefonts/berkshireswash |
| Commit Hash | 1a4fb49d514e01ada8934472cae85cc4590efa58 |
| Config YAML | (none) |
| Status | missing_config |
| Category | HANDWRITING / DISPLAY |

### How the Repository URL Was Found

The repository URL `https://github.com/librefonts/berkshireswash` comes from the librefonts organization on GitHub, a collection of decompiled font repos maintained by Marc Foley. The URL was recorded in the tracking data and added to METADATA.pb in commit `9a14639f3` (on branch `sources_info_2026-02-25`, not yet merged to main).

### How the Commit Hash Was Determined

The commit hash `1a4fb49d514e01ada8934472cae85cc4590efa58` is the latest (HEAD) commit in the librefonts/berkshireswash repo, dated 2014-10-17. This was set because it is the most recent commit in the repository, corresponding to a Travis CI config update ("update .travis.yml").

**Font history in google/fonts**:
- Initial commit `90abd17b4`: Font first added to google/fonts
- `5e3cf0753`: "hotfix-berkshireswash: v1.001 added" (PR #855, by Marc Foley, 2017-08-07)

The hotfix PR #855 by Marc Foley had an empty body. The librefonts repo's last commit predates the hotfix by about 3 years (2014 vs 2017).

### Config YAML Status

- **No `config.yaml`** exists in the upstream librefonts repo (not at any commit)
- **No override `config.yaml`** in `google/fonts/ofl/berkshireswash/`
- The repo contains only **VFB sources** (`src/BerkshireSwash-Regular-OTF.vfb`, `src/BerkshireSwash-Regular-TTF.vfb`, `src/BerkshireSwash-Regular.vfb`) and TTX-decomposed font files
- VFB (FontLab Studio format) is a proprietary binary format not compatible with gftools-builder
- No UFO, Glyphs, or DesignSpace sources are available

### Verification

- Commit hash `1a4fb49` exists in the repo (message: "update .travis.yml", dated 2014-10-17)
- It is the HEAD commit of the master branch (10 total commits in the repo)
- Repository URL is valid and accessible
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/berkshireswash`
- PR #855 body was empty

### Confidence Level

**Medium** - The commit hash is simply HEAD of the librefonts mirror repo. The librefonts repo is not the original design source. The original designer is Brian J. Bonislawsky (Astigmatic/AOETI). The repo only has VFB (proprietary FontLab) and TTX sources, making gftools-builder integration impossible without source conversion.

### Open Questions

- The original VFB source files from Astigmatic are proprietary format (FontLab Studio); conversion to UFO would be needed for gftools-builder compatibility
- The hotfix from 2017 may have used a process not reflected in the librefonts repo (which was last updated in 2014)
- Astigmatic (Brian Bonislawsky) designed many fonts for Google Fonts; it's unknown if more modern source formats are available from the designer
- The tracking notes say "No buildable source files at recorded commit" which is correct -- VFB files require proprietary software to open
- This font was added to Google Fonts in 2012 and has classification DISPLAY with SERIF stroke

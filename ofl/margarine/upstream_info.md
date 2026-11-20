# Margarine

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Margarine (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/margarine.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Margarine-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/margarine at `882077c78556`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Margarine-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/margarine.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`882077c78556` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Margarine-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Margarine — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

### Source Repository

The source files for Margarine are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `margarine/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Margarine-Regular.vfb` | FontLab VFB | Original source (proprietary, not buildable with gftools) |
| `Margarine-Regular-OTF.vfb` | FontLab VFB | Merged contours, optimized for OTF |
| `Margarine-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting |
| `Margarine-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable sources are VFB (FontLab Studio) format, which is a proprietary binary format not supported by gftools-builder.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/margarine, created on 2014-07-16 under the `librefonts` organization — a third-party effort by Mikhail Kashkin that extracted font files from the old Google Font Directory into individual GitHub repositories.

The repo has 12 commits total (all from 2014, by Mikhail Kashkin aka hash3g):
- `56637ab` (2014-07-16) — "Move margarine font files to separate repository" (initial commit)
- `645187d` (2014-07-18) — cleanup
- `70e841c` through `c612652` (2014-08-19 to 2014-10-17) — Various .travis.yml updates

The repo has been dormant since October 2014.

### Onboarding History

Margarine was added to google/fonts in the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the bulk import of the entire Google Fonts library. No PR or specific onboarding process was associated with this font.

The font was originally designed by Brian J. Bonislawsky (Astigmatic/AOETI) and released in November 2012 (Version 1.000). The font has never been updated in google/fonts since the initial commit (aside from metadata changes to METADATA.pb).

**Designer**: Brian J. Bonislawsky (Astigmatic/AOETI, astigma@astigmatic.com, www.astigmatic.com)
**GitHub**: https://github.com/astigmatic (exists but has no font repos)

### Build Configuration

No `config.yaml` exists and none can be created. The only source files are VFB (FontLab) binaries, which cannot be processed by gftools-builder. The TTX files in the librefonts mirror are decompositions of already-compiled binaries, not true design sources.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/margarine"
  commit: "c6126521f50b0be64bbc44cd287f71eb706127a1"
  branch: "master"
}
```

No `config_yaml` field is included because the repo has VFB-only sources not compatible with gftools-builder. The commit `c612652` is the latest commit in the repo.

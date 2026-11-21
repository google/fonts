# Marcellus

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Marcellus (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/marcellus.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from Marcellus-Regular.ttf,
  the font Google Fonts ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch
  2026-11-02: simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/marcellus at `81e2f726f299`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: Marcellus-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/marcellus.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`81e2f726f299` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/Marcellus-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Marcellus — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

### Source Repository

The source files for Marcellus are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `marcellus/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Marcellus-Regular.vfb` | FontLab VFB | Original source with contour overlaps (proprietary, not buildable) |
| `Marcellus-Regular-OTF.vfb` | FontLab VFB | Merged contours, optimized for OTF |
| `Marcellus-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting adjustments |
| `Marcellus-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable sources are VFB files (FontLab Studio proprietary format), which cannot be used with gftools-builder or fontc.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/marcellus, created on 2014-07-16 by Mikhail Kashkin (hash3g / m@xen.ru) as part of the fontbakery-dashboard project, which split fonts from the legacy Google Font Directory into individual repositories under the `librefonts` organization. This is not the original designer's source repository.

The repo has 11 commits total (all by hash3g, 2014-07-16 to 2014-10-17):
- `ae5b2de` (2014-07-16) — "Move marcellus font files to separate repository" (initial commit)
- `93dc35b` (2014-10-17) — latest commit (HEAD of master), a .travis.yml update

All commits after the initial one were CI/Travis configuration updates. No font source changes were ever made.

The `src/VERSIONS.txt` records "Marcellus-Regular.ttf: Version 1.000".

### Original Designer

The font was designed by **Brian J. Bonislawsky** of Astigmatic (AOETI). The designer's website was `www.astigmatic.com` and contact email was `astigma@astigmatic.com`. A GitHub account `astigmatic` exists but was created in 2017 and contains only two unrelated Java repositories — it does not appear to be the font designer's account.

No original source repository from the designer was found. The font was likely delivered directly to Google as compiled binaries, which was common practice for fonts onboarded in 2012.

### Onboarding History

Marcellus was added to the Google Fonts catalog on 2012-05-09 (per `date_added`). The font binary was included in the initial repository commit (`90abd17b4`, 2015-03-07, by Dave Crossland). The TTF file has never been modified since that initial commit.

The font version embedded in the binary is Version 1.000, and the FONTLOG records the initial release as "7 April 2012 (Brian J. Bonislawsky) Marcellus v1.001".

**Related family**: Marcellus SC (small caps variant), in the same VFB-only situation at librefonts/marcellussc.

#### Subsequent commits (metadata only):
- `480630de3` — METADATA.pb textproto conversion
- `883939708` — Remove METADATA.json files
- `633ebadbf` / `c6307ba83` / `701bd391b` — Language support metadata updates

### Build Configuration

No `config.yaml` exists and none can be created. The only sources are VFB (FontLab Studio) files, which are proprietary binary format. gftools-builder cannot process VFB files, and no .glyphs, .ufo, .designspace, or .sfd source files exist. The TTX decompositions in the repo are for analysis/archival purposes, not for building.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/marcellus"
  commit: "93dc35b5b10ccae45266e0661ae357d84dc0ec5d"
  branch: "master"
}
```

No `config_yaml` field is included because the repo has VFB-only sources not compatible with gftools-builder. The commit `93dc35b` is the latest commit, representing the state that includes all source files and TTX decompositions.

# Marcellus SC

**Model**: Claude Opus 5.5
**Date**: 2026-11-03

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Marcellus SC (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/marcellussc.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  MarcellusSC-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/marcellussc at `1570720f3e80`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0). Against google/fonts 2eb0b48d5f76,
under tools/table_gate.py and tools/functional_gate.py: MarcellusSC-Regular: 2 blocking
rows; functionally equivalent. Those tools, including this family's plan
`plans/marcellussc.json`: https://github.com/felipesanches/gf-source-modernization at
`d6a61f4`.

`1570720f3e80` is the equivalence commit: its build is functionally equivalent to the
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
  52f780bc9d197280a9f430574e179a5f233c56b6: src/MarcellusSC-Regular-TTF.vfb, a FontLab
  import of the shipped font, not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Marcellus SC — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

### Source Repository

The source files for Marcellus SC are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `marcellussc/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `MarcellusSC-Regular.vfb` | FontLab VFB | Original source with contour overlaps (proprietary, not buildable) |
| `MarcellusSC-Regular-OTF.vfb` | FontLab VFB | Merged contours, optimized for OTF output |
| `MarcellusSC-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting adjustments |
| `MarcellusSC-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable source files are in VFB (FontLab Studio 5) format, which is a proprietary binary format not supported by gftools-builder or fontc.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/marcellussc, created on 2014-07-16 under the `librefonts` GitHub organization (members: davelab6, felipesanches, pathumego). The repo contains a single commit:
- `75b6e93` (2014-10-17, author: hash3g) — "update .travis.yml"

This is a librefonts archive repository, not the original designer's repository. The librefonts organization was a community effort to archive Google Fonts source files on GitHub.

The repository also contains TTX decompositions, OTF TTX decompositions in `src/`, and `src/VERSIONS.txt` recording "MarcellusSC-Regular.ttf: Version 1.001".

### Onboarding History

Marcellus SC was added to the Google Fonts catalog on 2012-05-09 (per `date_added`), predating both the librefonts repo (2014) and the google/fonts repository initial commit (2015). The font was part of the initial bulk import (`90abd17b4`, 2015-03-07, by Dave Crossland).

The TTF binary has not been modified since the initial commit. MD5 checksum: `6c4b86cb0aeea480e0112d55752335c6`.

**Designer**: Brian J. Bonislawsky (Astigmatic)
**Single-weight**: Regular (400) only, no variable font version exists.
**Related family**: Marcellus (non-SC), sibling font with equivalent VFB-only sources at librefonts/marcellus.

#### Subsequent commits (metadata only):
- `701bd391b` — Undo rollback, remove languages from METADATA
- `c6307ba83` — Roll back language changes
- `28b492c0f` — Clear languages from METADATA.pb
- `633ebadbf` — Add language support metadata
- `883939708` — Remove METADATA.json files
- `27f377ab0` — Update copyright field in METADATA.pb
- `480630de3` — Update to METADATA.pb textprotos

### Build Configuration

No `config.yaml` exists and none can be created. The only source files are VFB (FontLab Studio 5) format, which cannot be processed by gftools-builder or fontc. The font would need to be converted to a modern format (.glyphs, .ufo, or .designspace) before a config.yaml could be meaningful.

The `.travis.yml` in the repo references the legacy `fontbakery-build.py` pipeline, which is long defunct.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/marcellussc"
  commit: "75b6e93759696a4d0bfd0cce86da0f9e4f38e10a"
  branch: "master"
}
```

No `config_yaml` field is included because the repo has VFB-only sources not compatible with gftools-builder.

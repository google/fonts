# Macondo

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontForge
`.sfd`, is an import of the fonts Google Fonts ships, so those fonts were converted to
Glyphs (`.glyphs`) sources, which build with gftools-builder and fontc. The repository,
commit and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Macondo (google/fonts at commit `2fe1e8c6b137`). Its only published
source is a FontForge import of the shipped fonts, not a design source (listed under
"Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/macondo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs`. Converted from Macondo-Regular.ttf, the font Google Fonts
  ships, with babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false
- Then what the conversion cannot carry, stated in the source, each in a documented
  commit of its own ("Source edit:"): state the release's GDEF glyph classes. The last
  of them is the equivalence commit.

## Final state

The source is https://github.com/googlefonts/macondo at `cdc06be3b7d7`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/macondo.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`cdc06be3b7d7` is the equivalence commit: its build is functionally equivalent to the
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

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: ofl/macondo/src/Macondo-Regular-TTF.sfd, a
  FontForge import of the shipped font (quadratic outlines, its TrueType instructions;
  tools/probes/ttf_sfd_origin), not a source: Simon on google/fonts#10490
  ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Macondo — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Macondo are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `macondo/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Macondo-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Macondo-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Macondo-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge) and VFB (FontLab) formats, which are not supported by gftools-builder.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/macondo, created on 2014-07-16 under the `librefonts` GitHub organization. It contains a single commit (`00c3eaaae24d702bce976a1766c31b8fc015f08a`) dated 2014-10-17, authored by hash3g. The repo was set up as part of the `librefonts` organization's mirror of Google Fonts source files and does not belong to the original designer (John Vargas Beltran).

The repository contains TTX decomposed tables at root level, the SFD/VFB sources in `src/`, and metadata files. The `src/VERSIONS.txt` records "Macondo-Regular.ttf: Version 2.001".

### Onboarding History

Macondo was added to the Google Fonts catalog on 2012-01-18 (per `date_added` in METADATA.pb), which aligns with the font's head table creation date of January 11, 2012. The font was created in 1997 (early versions) and substantially improved in 2009, with the v1.00 release dated December 14, 2011.

The font was included in the google/fonts repository from the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary has never been updated since — only metadata files (METADATA.pb/METADATA.json) were modified in subsequent commits for format changes, language support, and classification updates.

**Designer**: John Vargas Beltran
**Sister family**: Macondo Swash Caps (same designer, same SFD-only source situation at `librefonts/macondoswashcaps`)

#### Subsequent commits (metadata only):
- `480630de3` — Tentative update to METADATA.pb textprotos
- `27f377ab0` — Update copyright field in METADATA.pb
- `883939708` — Remove METADATA.json files
- `633ebadbf` — Add language support metadata
- `c6307ba83` / `701bd391b` — Language rollback and redo
- `47a6c224b` — Batch of 200 METADATA.pb changes for stroke and classifications

### Build Configuration

No `config.yaml` exists and none can be created. The only source files are in SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder. The `.travis.yml` in the upstream repo referenced `fontbakery-build.py`, an obsolete build tool from 2014.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/macondo"
  commit: "00c3eaaae24d702bce976a1766c31b8fc015f08a"
  branch: "master"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder.

### Confidence

**HIGH** for repository URL and commit hash. Both the googlefontdirectory-hg monorepo and the librefonts/macondo mirror contain TTX-decomposed font data matching the binary in google/fonts (same Version 2.001, same head table dates).

**N/A** for config — no gftools-builder configuration is possible due to legacy-only source formats.

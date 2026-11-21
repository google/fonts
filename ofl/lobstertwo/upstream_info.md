# Lobster Two

**Model**: Claude Opus 5.5
**Date**: 2026-11-04

Sources modernized 2026-11: the only published source of this family, a FontLab `.vfb`,
is an import of the fonts Google Fonts ships, so those fonts were converted to Glyphs
(`.glyphs`) sources, which build with gftools-builder and fontc. The repository, commit
and config are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Lobster Two (google/fonts at commit `2fe1e8c6b137`). Its only
published source is a FontLab import of the shipped fonts, not a design source (listed
under "Earlier sources"; Simon on google/fonts#10490: "batch-converted from the binary
files"), and it could not be built with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/lobstertwo.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  LobsterTwo-{Bold,BoldItalic,Italic,Regular}.ttf, the fonts Google Fonts ships, with
  babelfont 26fdcfa (felipesanches/babelfont-rs branch 2026-11-02:
  simoncozens/babelfont-rs main plus the name changes proposed to it (#117,
  typographic-family-names)): its TTF reader, no filters. sources/config.yaml:
  productionNames: false

## Final state

The source is https://github.com/googlefonts/lobstertwo at `8cf8dff7f78b`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/lobstertwo.json`:
https://github.com/felipesanches/gf-source-modernization at `65a4e2b`.

`8cf8dff7f78b` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released fonts are hinted (TrueType instructions). These sources carry no TrueType
  instructions, so the build is hinted by ttfautohint: the outlines, spacing and layout
  are the release's, its rendering at small sizes under a TrueType interpreter is not.
  Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a design source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6: src/LobsterTwo-Bold-TTF.vfb,
  src/LobsterTwo-BoldItalic-TTF.vfb, src/LobsterTwo-Italic-TTF.vfb,
  src/LobsterTwo-Regular-TTF.vfb, a FontLab import of the shipped fonts, not a source:
  Simon on google/fonts#10490 ("batch-converted from the binary files").

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Lobster Two - Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Confidence**: HIGH

### Source Repository

The original design sources for Lobster Two are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lobstertwo/src/`.

#### Source Files in googlefontdirectory-hg

- `LobsterTwo-Regular.vfb` / `LobsterTwo-Regular-TTF.vfb` -- FontLab binary sources (proprietary, not buildable with gftools-builder)
- `LobsterTwo-Bold.vfb` / `LobsterTwo-Bold-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-Italic.vfb` / `LobsterTwo-Italic-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-BoldItalic.vfb` / `LobsterTwo-BoldItalic-TTF.vfb` -- FontLab binary sources
- `LobsterTwo-Regular.otf`, `LobsterTwo-Bold.otf`, `LobsterTwo-Italic.otf`, `LobsterTwo-BoldItalic.otf` -- compiled OTF binaries, not design sources
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are exclusively VFB (FontLab binary) format. No `.glyphs`, `.ufo`, or `.designspace` files are present. VFB files are not compatible with gftools-builder.

### METADATA.pb Analysis

No source block exists in the current METADATA.pb. The file contains only font metadata (name, designer, license, category, fonts, subsets, stroke, classifications) with no `source { }` block.

### Upstream Repository (librefonts archive)

The upstream repository is **librefonts/lobstertwo** at https://github.com/librefonts/lobstertwo.

- **Not archived**, not a fork
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Single commit**: `0f38cf2` (2014-10-17) -- "update .travis.yml"
- **Single branch**: `master`

The repository contains the same VFB source files as the googlefontdirectory-hg monorepo, plus TTX table dumps of the TTF files. There are **no** `.glyphs`, `.ufo`, `.designspace`, or `config.yaml` files.

The `.travis.yml` references an old build pipeline using `fontbakery-build.py` (circa 2014), not gftools-builder.

#### Related Repository

A related but distinct repository exists: **impallari/The-Lobster-Font** (https://github.com/impallari/The-Lobster-Font). This repo contains a `Lobster.glyphs` source file but is for the original single-weight "Lobster" font (Regular only), not "Lobster Two" (Regular, Italic, Bold, BoldItalic). The two are related families but separate projects.

### Onboarding History

Lobster Two was added to google/fonts in the **initial commit** (`90abd17b`) on 2015-03-07 by Dave Crossland. This was a bulk import that added many font families at once. There were no PRs associated with the onboarding of this specific font.

Subsequent commits in google/fonts that touched the lobstertwo directory were all metadata-only changes (METADATA.pb textproto conversion, copyright field updates, METADATA.json removal, designer key updates, language metadata, stroke and classification metadata).

The TTF binary files have **never been updated** since the initial commit. All four TTF files are version 1.006.

### Designer Information

Designer: Pablo Impallari (impallari@gmail.com), with kerning by Igino Marini.

### Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the source files are VFB-only. VFB is a proprietary FontLab format that is **not compatible with gftools-builder**, which requires `.glyphs`, `.ufo`, or `.designspace` source files.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lobstertwo"
  commit: "0f38cf2a6f0ffd8e8334fa15ad761cedf78136cc"
}
```

The `config_yaml` field is **omitted** because no gftools-builder compatible config exists (VFB-only sources).

### Conclusion

The source block documents the only known upstream repository. The fonts cannot be rebuilt from source using modern tooling without first converting the VFB sources to a supported format.

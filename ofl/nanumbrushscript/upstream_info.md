# Nanum Brush Script

**Model**: Claude Fable 5.1
**Date**: 2026-11-02

Sources created 2026-11: no source of this family was ever published, so the fonts
Google Fonts ships were converted to Glyphs (`.glyphs`) sources, which build with
gftools-builder and fontc. The repository, commit and config are in the `source { }`
block of METADATA.pb.

## Initial state

Google Fonts shipped Nanum Brush Script as binaries only (google/fonts at commit
`2eb0b48d5f76`). No source of the family was ever published, so it could not be built
with fontc.

## Actions taken

- The fonts Google Fonts ships were imported unmodified as the first commit of
  https://github.com/googlefonts/nanumbrushscript.
- The Unified Font Repository template was adopted in its own commit; the README records
  the provenance and the known differences below.
- The conversion to `.glyphs` is the last change. Converted from
  NanumBrushScript-Regular.ttf, the font Google Fonts ships, with babelfont 26fdcfa
  (felipesanches/babelfont-rs branch 2026-11-02: simoncozens/babelfont-rs main plus the
  name changes proposed to it (#117, typographic-family-names)): its TTF reader, no
  filters. sources/config.yaml: productionNames: false

## Final state

The source is https://github.com/googlefonts/nanumbrushscript at `5b703ee26d2c`. Builds
with gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/nanumbrushscript.json`:
https://github.com/felipesanches/gf-source-modernization at `f073f4e`.

`5b703ee26d2c` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Any improvement is a
later commit that needs its own QA, and is left as future work for an onboarder to
review in a font-update PR.

## Known differences from the released fonts

Reviewed and deliberately left as they are; the repository's README lists them too:

- The released font is partly hinted (TrueType instructions in 5093 of 13799 glyphs).
  These sources carry no TrueType instructions, so the build is hinted by ttfautohint:
  the outlines, spacing and layout are the release's, its rendering at small sizes under
  a TrueType interpreter is not. Hinting is not compared by the gates.

## Earlier sources

Other copies of this family, kept on record; none of them is a source:

- https://github.com/googlefonts/googlefontdirectory-hg at
  52f780bc9d197280a9f430574e179a5f233c56b6, ofl/nanumbrushscript/: the font as built and
  its metadata; src/ holds METADATA_comments.txt, NanumBrush.otf, no source.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Nanum Brush Script — Source Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/nanumbrushscript/src/` |
| **Buildable** | No — compiled binary only, no design sources |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files (2)

- **Compiled binary** (not a design source): NanumBrush.otf
- **Metadata**: METADATA_comments.txt

The source directory contains only a compiled OTF binary and metadata — no editable design sources (VFB, Glyphs, UFO, SFD, etc.) are present.

### Build System

Not applicable — no source-based build pipeline exists.

### Notes

- Designed by Sandoll Communication, commissioned by Naver
- Naver distributes all Nanum fonts via https://hangeul.naver.com as binary downloads
- Naver has a GitHub org (`github.com/naver`) with a `nanumfont` repo, but it contains only binary releases (TTF/OTF), not editable source files
- No UFO, Glyphs, or other source format is publicly available — the font was designed using proprietary tools at Sandoll Communication
- All five Nanum families (Gothic, Gothic Coding, Myeongjo, Brush Script, Pen Script) share the same provenance
- Licensed under the SIL Open Font License
- Primary script: Korean (Kore)
- Single weight: Regular (400)
- Font version in Google Fonts: 2.000
- Any source metadata enrichment would require direct cooperation from Naver/Sandoll

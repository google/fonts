# Mr De Haviland

**Model**: Claude Opus 5.5
**Date**: 2026-10-09

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Mr De Haviland built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/mrdehaviland` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/mrdehaviland.
- Each change to the `.sfd` before conversion is its own commit: Name
  MrDeHaviland-Regular as the release does.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.
- The build config was then updated in its own commit, with the build gated again:
  productionNames: false replaces noProductionNames.
- METADATA.pb recorded `c64a446a39bd`, the conversion, until this update; `f92c920102e9`
  follows it and changes only the build config, so it is recorded now.

## Final state

The source is https://github.com/googlefonts/mrdehaviland at `f92c920102e9`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `7706a8f`.

`f92c920102e9` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Mr De Haviland — Source Investigation

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/mrdehaviland/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files (4)

- **.vfb** (FontLab, proprietary format): MrDeHaviland-Regular-OTF.vfb
- **.sfd** (FontForge, not supported by gftools-builder): MrDeHaviland-Regular-TTF.sfd
- **Compiled binary** (not a design source): MrDeHaviland-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are a VFB (proprietary) and an SFD (FontForge). Neither format is supported by gftools-builder.

### Build System

Not applicable — no gftools-builder-compatible sources exist.

### Notes

- Font was designed by Sudtipos
- No other public upstream repository has been identified
- Single style: Regular

# Herr Von Muellerhoff

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Herr Von Muellerhoff built from FontForge `.sfd` sources in the
family's directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/herrvonmuellerhoff` at
commit `52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own.
There was no source that builds with fontc. The shipped binary carries FontForge's
`FFTM` table, so FontForge generated it. The directory also holds FontLab `.vfb` files;
the `.sfd` is taken as the master because FontForge generated the shipped fonts and the
build from the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/herrvonmuellerhoff.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/herrvonmuellerhoff at `585d840f8362`.
Builds with gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`585d840f8362` is the equivalence commit: its build is functionally equivalent to the
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

## Herr Von Muellerhoff -- Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03

### Source Repository

**Repository**: [googlefontdirectory-hg](https://code.google.com/archive/p/googlefontdirectory/) (Mercurial monorepo)
**Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
**Source path**: `herrvonmuellerhoff/src/`

#### Source Files in googlefontdirectory-hg

| File | Format | Buildable |
|------|--------|-----------|
| `HerrVonMuellerhoff-Regular-TTF.sfd` | FontForge SFD | No (not supported by gftools-builder) |
| `Herr Von Muellerhoff-Regular-OTF.vfb` | FontLab binary | No |
| `HerrVonMuellerhoff-Regular.otf` | Compiled binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata | N/A |

The source directory contains an SFD file (FontForge Spline Font Database) and a VFB file (FontLab proprietary binary). While FontForge can compile fonts from SFD, gftools-builder and fontmake do not support SFD as an input format. Neither format is compatible with the gftools-builder toolchain (which requires `.glyphs`, `.ufo`, or `.designspace`). The `.otf` file is a compiled binary, not a design source.

### Designer

Alejandro Paul of Sudtipos. Copyright: "(c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name \"Herr Von Mullerhoff\"" (note the misspelling "Mullerhoff" vs "Muellerhoff" in the reserved font name). This is a handwriting/display font.

### librefonts Mirror

A mirror exists at `https://github.com/librefonts/herrvonmuellerhoff` with a single commit:
- `f49091c` (2014-10-17) by hash3g

The repo contains the same SFD/VFB sources, TTX table dumps, and metadata files. It adds no additional design sources beyond what is in googlefontdirectory-hg.

### google/fonts History

The font binary was added in the initial commit `90abd17b4` (2015-03-07, author: Dave Crossland). The font file (`HerrVonMuellerhoff-Regular.ttf`, 46624 bytes) has never been modified since. The `VERSIONS.txt` records "Version 1.000".

### Build Configuration

- **No config.yaml** exists in any known repository
- **No override config.yaml** exists in the google/fonts family directory
- The SFD and VFB source formats are not supported by gftools-builder
- A config.yaml cannot be created for this family with the current source formats

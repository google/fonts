# Keania One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Keania One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/keaniaone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/keaniaone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/keaniaone at `a0a653e1cfaa`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`a0a653e1cfaa` is the equivalence commit: its build is functionally equivalent to the
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

## Investigation: Keania One

**Model**: Claude Opus 4.6

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [https://github.com/googlefonts/googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `keaniaone/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`) that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files (5)

| File | Format | Notes |
|------|--------|-------|
| `KeaniaOne-Regular.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KeaniaOne-Regular-OTF.vfb` | FontLab VFB | Proprietary format, not buildable with gftools |
| `KeaniaOne-Regular-TTF.sfd` | FontForge SFD | Open format, not buildable with gftools-builder |
| `KeaniaOne-Regular.otf` | OpenType binary | Compiled font, not a design source |
| `METADATA_comments.txt` | Metadata | Not a design source |

The source directory contains legacy VFB (FontLab) and SFD (FontForge) files. These are original design sources but are not compatible with the gftools-builder pipeline.

### Investigation

The METADATA.pb has no `source` block. The font was added in the initial commit (`90abd17b4`) of the google/fonts repository.

The copyright notice reads: "Copyright (c) 2012, Julia Petretta (julia.petretta@googlemail.com), with Reserved Font Name 'Keania'"

A cached repository exists at `upstream_repos/fontc_crater_cache/librefonts/keaniaone` containing similar legacy source files. This librefonts repository is an archival mirror.

There is no publicly known upstream GitHub repository for this Julia Petretta font.

### Conclusion

The googlefontdirectory-hg monorepo contains original design sources in legacy formats (VFB, SFD), but these are not buildable with gftools-builder. No upstream GitHub repository is known for this family.

# Piedra

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Piedra built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/piedra` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/piedra.
- Each change to the `.sfd` before conversion is its own commit: Name Piedra-Regular as
  the release does.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/piedra at `4d4cb7ae3daa`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/piedra.json`:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`4d4cb7ae3daa` is the equivalence commit: its build is functionally equivalent to the
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

## Piedra — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

| Field | Value |
|-------|-------|
| **Repository** | [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) |
| **Commit** | `52f780bc9d197280a9f430574e179a5f233c56b6` |
| **Source path** | `ofl/piedra/src/` |
| **Buildable** | No — legacy formats only (.vfb/.sfd) |

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source files

- **.vfb** (FontLab, proprietary): Piedra-Regular-OTF.vfb
- **.sfd** (FontForge): Piedra-Regular-TTF.sfd
- **Compiled binary** (not a design source): Piedra-Regular.otf
- **Metadata**: METADATA_comments.txt

The design sources are VFB (FontLab, proprietary) and SFD (FontForge) format files. Neither format is buildable with gftools-builder. No modern buildable sources (.glyphs, .ufo, .designspace) are available.

### Investigation

Designer: Sudtipos (Angel Koziupa, Alejandro Paul). Script: Latin. Category: DISPLAY (serif stroke).

No source block was found in METADATA.pb. No canonical upstream GitHub repository was identified.

### Conclusion

No canonical upstream repository was found beyond the legacy googlefontdirectory-hg archive. Sources exist as VFB/SFD files, which are not buildable with gftools-builder. No METADATA.pb changes were made.

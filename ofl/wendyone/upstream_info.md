# Wendy One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Wendy One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/wendyone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/wendyone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/wendyone at `7e19d97bf5b4`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`7e19d97bf5b4` is the equivalence commit: its build is functionally equivalent to the
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

## Wendy One — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `wendyone/src/`.

#### Source Files

- **VFB (FontLab)**: WendyOne-Regular-OTF.vfb
- **SFD (FontForge)**: WendyOne-Regular-TTF.sfd
- **OTF (compiled)**: WendyOne-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

### Investigation Details

Wendy One was designed by Alejandro Inler in collaboration with Julieta Ulanovsky. Searches on GitHub for repositories by `alejandroinler`, combinations of "wendy one font", "wendy font inler", and "wendy font julieta" returned no results. No GitHub account for Alejandro Inler was found. The font's DESCRIPTION mentioned it was "developed by Alejandro Inler in conjunction with Julieta Ulanovsky" but contained no URL to a source repository.

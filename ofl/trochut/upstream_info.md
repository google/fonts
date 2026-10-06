# Trochut

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Trochut built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/trochut` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 3 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them. The directory also holds FontLab `.vfb` files; the `.sfd`
is taken as the master because FontForge generated the shipped fonts and the build from
the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/trochut.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/trochut at `1f3e4ae5a6f0`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 3 styles. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`1f3e4ae5a6f0` is the equivalence commit: its build is functionally equivalent to the
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

## Trochut — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Andreu Balius

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `trochut/src/`.

#### Source Files

- **VFB (FontLab)**: Trochut-Bold-OTF.vfb, Trochut-Italic-OTF.vfb, Trochut-Regular-OTF.vfb
- **SFD (FontForge)**: Trochut-Bold-TTF.sfd, Trochut-Italic-TTF.sfd, Trochut-Regular-TTF.sfd
- **OTF (compiled)**: Trochut-Bold.otf, Trochut-Italic.otf, Trochut-Regular.otf

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

### Investigation Details

Trochut was designed by Andreu Balius as an homage to Joan Trochut Blanchart (1920–1980), and is distributed commercially through TypeRepublic (typerepublic.com). A subset was released on Google Fonts under the OFL.

The following searches were conducted:

1. **GitHub user search**: No GitHub account was found for Andreu Balius (`andreubalius`).
2. **GitHub repository search**: Searches for "trochut font", "TypeRepublic font", and related terms returned no canonical upstream repositories. A repository `RichardBu/Trochut` was found but contained only a portfolio website (HTML/CSS), not font sources.
3. **librefonts mirror**: `librefonts/trochut` was found but is a downstream binary mirror (skipped per policy).
4. **Designer website**: andreubalius.com was checked but contained only portfolio information with no links to font source repositories.

Trochut is primarily a commercial typeface distributed through TypeRepublic. The Google Fonts subset was released under OFL, but the font sources have not been made publicly available in an editable format.

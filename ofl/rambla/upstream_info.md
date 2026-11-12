# Rambla

**Model**: Claude Opus 5.5
**Date**: 2026-10-22

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Rambla built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/rambla` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 4 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them. The directory also holds FontLab `.vfb` files; the `.sfd`
is taken as the master because FontForge generated the shipped fonts and the build from
the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/rambla.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/rambla at `30f485909fc7`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/rambla.json`:
https://github.com/felipesanches/gf-source-modernization at `488fa72`.

`30f485909fc7` is the equivalence commit: its build is functionally equivalent to the
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

## Rambla — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `rambla/src/`

### Source Files

The `rambla/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Rambla-Bold-OTF.vfb, Rambla-Bold.vfb, Rambla-BoldItalic-OTF.vfb, Rambla-BoldItalic.vfb, Rambla-Regular-Italic-OTF.vfb, Rambla-Regular-Italic.vfb, Rambla-Regular-OTF.vfb, Rambla-Regular.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Rambla-Bold-TTF.sfd, Rambla-BoldItalic-TTF.sfd, Rambla-Regular-Italic-TTF.sfd, Rambla-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Rambla-Bold.otf, Rambla-BoldItalic.otf, Rambla-Regular-Italic.otf, Rambla-Regular.otf

### Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

### Investigation Details

GitHub was searched for the font name "Rambla" and the designer name "Martin Sommaruga" / "Estudio Trama". The `flokk/font-rambla` repository was examined but contained only CSS and WOFF files, making it unsuitable as a source reference. The FONTLOG.txt referenced `http://code.google.com/p/googlefontdirectory/` (the old Google Font Directory project), which is no longer active. No other repositories were identified.

### Notes

The font's copyright year is 2011–2012, predating widespread use of GitHub for font source hosting. The designer appears to be from Argentina (email: `martin@estudiotrama.com`). No public Git repository with UFO or Glyphs sources was found.

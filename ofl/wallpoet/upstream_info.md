# Wallpoet

**Model**: Claude Opus 5.5
**Date**: 2026-10-22

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Wallpoet built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/wallpoet` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/wallpoet.
- Each change to the `.sfd` before conversion is its own commit: Set fsType to 0,
  installable embedding.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/wallpoet at `4d4a51f7dfc1`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/wallpoet.json`:
https://github.com/felipesanches/gf-source-modernization at `488fa72`.

`4d4a51f7dfc1` is the equivalence commit: its build is functionally equivalent to the
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

## Wallpoet — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Lars Berggren

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `wallpoet/src/`.

#### Source Files

- **VFB (FontLab)**: wallpoet.vfb
- **SFD (FontForge)**: Wallpoet-Regular-TTF.sfd
- **EPS glyph drawings**: 242 files in wallpoet_eps/

Sources are in VFB (FontLab, proprietary) and SFD (FontForge) formats, neither of which is buildable with gftools-builder.

### Investigation Details

The font was created by Lars Berggren (`punktlars@gmail.com`). Searches were conducted on GitHub for "Wallpoet", "Lars Berggren", and related terms, but no dedicated font source repository was identified. The `librefonts/wallpoet` mirror was found but excluded per policy. No UFO, Glyphs, or other open-format source files were found in any publicly accessible repository.

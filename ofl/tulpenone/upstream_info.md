# Tulpen One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Tulpen One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/tulpenone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/tulpenone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/tulpenone at `ccb2226a3f87`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`ccb2226a3f87` is the equivalence commit: its build is functionally equivalent to the
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

## Tulpen One — Upstream Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-25
**Investigator**: AI agent (Claude) under guidance of @felipesanches

**Designer**: Naima Ben Ayed

### Source Repository

Source files were found in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `tulpenone/src/`.

#### Source Files

- **SFD (FontForge)**: TulpenOne-Regular-TTF.sfd
- **TTF (compiled)**: Tulpen-Light.ttf

Sources are in SFD format (FontForge), which is not buildable with gftools-builder.

### Investigation Details

Tulpen One was designed by Naima Ben Ayed (naima.benayed@gmail.com). The font is a tall sans-serif display typeface.

The following searches were conducted:

1. **GitHub user search**: A GitHub user search for "naima ben ayed" returned no matching accounts associated with font design.
2. **Repository name search**: Searches for "tulpen", "tulpen one", and "tulpenone" on GitHub returned no font source repositories.
3. **Broader searches**: No relevant repositories were found using designer name and font name combinations.

Tulpen One appears to have been contributed to Google Fonts without a corresponding public source repository. The font was released in 2011 and the sources have not been made publicly available on GitHub or any other discoverable platform.

# Quantico

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Quantico built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/quantico` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 4 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them. The directory also holds FontLab `.vfb` files; the `.sfd`
is taken as the master because FontForge generated the shipped fonts and the build from
the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/quantico.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/quantico at `072c8f63d1f2`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`072c8f63d1f2` is the equivalence commit: its build is functionally equivalent to the
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

## Quantico — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `quantico/src/`

### Source Files

The `quantico/src/` directory contains design sources in VFB (FontLab) and SFD (FontForge) formats, neither of which can be built with gftools-builder:

- **VFB** (FontLab, proprietary format, not buildable with gftools): Quantico-Bold-OTF.vfb, Quantico-BoldItalic-OTF.vfb, Quantico-Italic-OTF.vfb, Quantico-Regular-OTF.vfb
- **SFD** (FontForge, not buildable with gftools-builder): Quantico-Bold-TTF.sfd, Quantico-BoldItalic-TTF.sfd, Quantico-Italic-TTF.sfd, Quantico-Regular-TTF.sfd
- **OTF** (compiled binaries, not design sources): Quantico-Bold.otf, Quantico-BoldItalic.otf, Quantico-Italic.otf, Quantico-Regular.otf

### Buildability

Not buildable with gftools-builder. The sources are in VFB (FontLab proprietary) and SFD (FontForge) formats. Neither format is supported by gftools-builder. Conversion to UFO or Glyphs format would be required.

### Investigation Details

The following searches were performed:

- Searched GitHub for "quantico font" repositories — no relevant font source repositories were found.
- Checked the `MadType` GitHub account — it exists but has no public repositories.
- Checked the `mattdesmond` GitHub account — found `mattdesmond/fonts`, which is a personal mirror of google/fonts with only TTF binaries in the `ofl/quantico/` subdirectory, not a source repository.
- Searched for dedicated Quantico repos by Matthew Desmond — none found.
- Reviewed the FONTLOG.txt, which references `http://www.madtype.com` as documentation and `mattdesmond@gmail.com` as contact, but no GitHub repository was linked.

No canonical upstream repository with font source files was found.

### Notes

- Designer: Matthew Desmond (MADType)
- The FONTLOG lists only a single initial release in December 2011, with no modern build pipeline references
- The `madtype.com` website was not investigated as GitHub search was the primary method used

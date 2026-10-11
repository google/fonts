# Loved by the King

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Loved by the King built from FontForge `.sfd` sources in the
family's directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/lovedbytheking` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/lovedbytheking.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/lovedbytheking at `50930a220782`. Builds
with gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`50930a220782` is the equivalence commit: its build is functionally equivalent to the
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

## Loved by the King - Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Confidence**: HIGH

### Source Repository

The original design sources for Loved by the King are preserved in the **googlefontdirectory-hg** Mercurial monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `lovedbytheking/src/`.

#### Source Files in googlefontdirectory-hg

- `LovedbytheKing-TTF.sfd` -- FontForge SFD file (legacy, not buildable with gftools-builder)
- `LovedbytheKing.vfb` -- FontLab binary source (proprietary, not buildable with gftools-builder)
- `LovedbytheKing.otf` -- compiled OTF binary, not a design source
- `METADATA_comments.txt` -- metadata file, not a design source

The design sources are in SFD and VFB legacy formats only. No `.glyphs`, `.ufo`, or `.designspace` files are present. These formats are not compatible with gftools-builder.

### METADATA.pb Analysis

No source block exists. The current METADATA.pb contains only basic font metadata (name, designer, license, category, fonts, subsets, classifications) with no `source { }` block.

### Upstream Repository (librefonts archive)

The only upstream repository found is **librefonts/lovedbytheking** on GitHub (`https://github.com/librefonts/lovedbytheking`).

- **Organization**: `librefonts` is an automated mirror organization that decomposed early Google Fonts binaries into TTX (XML) format for version control. It is not a design-source repository.
- **Created**: 2014-07-16
- **Last pushed**: 2014-10-17
- **Commits**: Single commit (`d22be35`) by `hash3g` dated 2014-10-17, titled "update .travis.yml"
- **Branches**: Only `master`

The repo contains decomposed TTX files of `LovedbytheKing.ttf`, the same SFD/VFB sources as the googlefontdirectory-hg monorepo, `METADATA.json`, `OFL.txt`, `DESCRIPTION.en_us.html`, and `.travis.yml`.

### Onboarding History

- **Added to Google Fonts**: 2011-07-06 (per `date_added` in METADATA.pb)
- **Git history**: The font binary was added in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the bulk import of all existing Google Fonts into the new Git-based repository.
- **No subsequent modifications**: The TTF file has never been updated since the initial commit.
- **No associated PRs**: The font was part of the initial bulk import, so there are no individual onboarding PRs to trace.

### Font Metadata (from TTX)

- **Version**: 1.002 (2006)
- **Copyright**: Copyright (c) 2006 by Kimberly Geswein. All rights reserved.
- **Designer**: Kimberly Geswein
- **Designer URL**: http://kimberlygeswein.com (site is live, returns HTTP 200)
- **Head table created/modified**: 2011-07-01

### Designer Context

Kimberly Geswein is a prolific handwriting font designer with 22 font families in Google Fonts. She does not appear to have a GitHub account. Her fonts were typically created in FontLab or FontForge (VFB/SFD formats), predating the modern .glyphs/.ufo workflow. No designer-maintained upstream repository was found for this font.

### Build Configuration

The source files are SFD (FontForge) and VFB (FontLab) formats only. These are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` source formats. Creating an override `config.yaml` is not feasible.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/lovedbytheking"
  commit: "d22be35555328ba7c5a7255b875f08dd420e6cdd"
}
```

No `config_yaml` field is included because there is no config.yaml in the repo and no gftools-builder compatible sources exist. This follows the same pattern as other Kimberly Geswein fonts (e.g., `architectsdaughter`) that reference `librefonts` repos with legacy-only sources.

### Conclusion

The librefonts/lovedbytheking repository is an archival mirror, not the designer's original source. The font lacks modern design sources (.glyphs/.ufo/.designspace) needed for gftools-builder compilation. The source block documents what exists (SFD/VFB legacy sources) but the font cannot be rebuilt from these sources using the current toolchain.

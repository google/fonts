# Medula One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Medula One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/medulaone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/medulaone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/medulaone at `adde69dc31b9`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`adde69dc31b9` is the equivalence commit: its build is functionally equivalent to the
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

## Medula One — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Medula One are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `medulaone/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `MedulaOne-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `MedulaOne-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `MedulaOne-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge, 269 KB) and VFB (FontLab, 102 KB) formats, which are not supported by gftools-builder.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/medulaone, created on 2014-07-16 by Mikhail Kashkin (@xen) as part of the `librefonts` organization's effort to create per-family repositories from the earlier googlefontdirectory collection.

The repo has 12 commits total (all from 2014):

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `71bda1c` | 2014-07-16 | Mikhail Kashkin (@xen) | Move medulaone font files to separate repository |
| `9559bbd` | 2014-10-17 | hash3g | update .travis.yml (HEAD) |

All commits after the initial one were Travis CI configuration updates. The source files (SFD, VFB) were never modified after the initial commit.

**Contributors**: Mikhail Kashkin (@xen), hash3g

The `src/VERSIONS.txt` indicates "Version 1.002".

### Onboarding History

Medula One was added to Google Fonts on 2011-12-19 (per `date_added` in METADATA.pb). The font file was included in the initial commit of the google/fonts repository (`90abd17b4`, 2015-03-07). The font binary was never modified after the initial commit.

The `librefonts/medulaone` repository was created on 2014-07-16, approximately 2.5 years after the font was added to Google Fonts, confirming the librefonts repo is a post-hoc archive.

**Designer**: LatinoType (Luciano Vergara, luciano@latinotype.com)
**Copyright**: Copyright (c) 2011

### Build Configuration

No `config.yaml` exists and none can be created. The only source files are SFD (FontForge) and VFB (FontLab) formats, neither of which is supported by gftools-builder. The `.travis.yml` used the legacy `fontbakery-build.py` tool.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/medulaone"
  commit: "9559bbd73be136d236851c03e0050708315aef2e"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder. The commit `9559bbd` is HEAD of master and the source files are identical to the initial commit.

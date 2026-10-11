# Nova Cut

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Nova Cut built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/novacut` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/novacut.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/novacut at `47f1668e12c0`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`47f1668e12c0` is the equivalence commit: its build is functionally equivalent to the
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

## Nova Cut — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/novacut/src/`
- **Buildable**: No — legacy format only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

#### Source Files

| File | Type |
|------|------|
| `NovaCut.sfd` | FontForge SFD source (not buildable with gftools-builder) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The SFD file is the only editable source and serves as the authoritative design file. It is FontForge format, not compatible with gftools-builder.

### Designer and Provenance

- **Designer**: Wojciech Kalinowski (wmk69), wmk69@o2.pl
- **Designer's canonical repo**: https://github.com/wmk69/Nova — covers the redesigned Nova 3.x family (2020-2022) but **intentionally excludes Nova Cut**, which was removed in v3.0.0 (May 2020) due to visual similarity with Gothica. The Google Fonts version (v2.000) predates this split.
- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG; individual page no longer available).

### Additional Mirror

A third-party mirror exists at https://github.com/librefonts/novacut (latest commit `aa17adb` on 2014-10-17, "update .travis.yml"). It contains the same SFD source plus TTX-decomposed TTF tables. The `src/VERSIONS.txt` records version 2.000, matching the Google Fonts binary. The repo used the legacy `fontbakery-build.py` pipeline (circa 2014), which is obsolete.

### Build System

Not applicable — the SFD source requires FontForge. Rebuilding from source would require FontForge and manual steps.

### config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

### Notes

- The Google Fonts binary (`NovaCut.ttf`) corresponds to version 2.000 (2011), redesigned September 2011.
- Nova Cut was officially dropped from the designer's active Nova family in 2020 and has no maintained upstream.
- The font covers Latin, Latin Extended, and a small set of Greek and mathematical symbols.
- **Confidence**: High — the monorepo SFD and librefonts mirror are the known sources for this family.

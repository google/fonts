# Miss Fajardose

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Miss Fajardose built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/missfajardose` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/missfajardose.
- Each change to the `.sfd` before conversion is its own commit: Name
  MissFajardose-Regular as the release does.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/missfajardose at `d4e2a937fa6f`. Builds
with gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/missfajardose.json`:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`d4e2a937fa6f` is the equivalence commit: its build is functionally equivalent to the
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

## Miss Fajardose — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Miss Fajardose are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/missfajardose/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MissFajardose-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MissFajardose-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MissFajardose-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

The VFB file is the OTF production source and the SFD file is the TTF production source. The `.otf` is a compiled binary, not a design source. No UFO, Glyphs, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary and the SFD format is not supported by gftools-builder.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Alejandro Paul / Sudtipos (`sudtipos@sudtipos.com`)
- **Copyright**: "Copyright (c) 2004 Alejandro Paul (sudtipos@sudtipos.com), with Reserved Font Name "MissFajardose""
- **Date added to Google Fonts**: 2011-11-30 (very early era, predates most open source font hosting practices)

Miss Fajardose is a legacy handwriting font from 2004, added to Google Fonts in the very early days (2011).

### Searches Conducted

- A `sudtipos` GitHub user or organization — not found (404)
- `MissFajardose` or `fajardose` repositories on GitHub — no results
- An official Sudtipos repository — Sudtipos does not appear to have a public GitHub presence

### Additional Repository

An unofficial archive mirror exists in the `librefonts` GitHub organization:

- **URL**: https://github.com/librefonts/missfajardose
- **Created**: 2014-07-16 ("Move missfajardose font files to separate repository") by the LibreFonts archiving project
- **Last pushed**: 2014-10-17. Only 11 commits. No stars, no forks.

This is a third-party archive with no connection to the original author, not suitable as an authoritative upstream.

### Notes

- Sudtipos does not appear to have a public GitHub presence. The designer has not published source files through any discoverable public channel.
- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- If source files in modern format are desired, direct outreach to `sudtipos@sudtipos.com` would be necessary.

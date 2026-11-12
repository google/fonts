# Merge One

**Model**: Claude Opus 5.5
**Date**: 2026-10-22

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Merge One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/mergeone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/mergeone.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last change to the font.

## Final state

The source is https://github.com/googlefonts/mergeone at `a244e59ac470`. Builds with
gftools-builder (gftools-rust 1e638bd, fontc 1.0.0) and matches the binaries
google/fonts 2eb0b48d5f76 ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/mergeone.json`:
https://github.com/felipesanches/gf-source-modernization at `488fa72`.

`a244e59ac470` is the equivalence commit: its build is functionally equivalent to the
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

## Merge One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The original design sources for Merge One are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/mergeone/src/`

#### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MergeOne-Regular.vfb` | FontLab VFB | No (proprietary) |
| `MergeOne-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MergeOne-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MergeOne-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Multiple VFB files are present: `MergeOne-Regular.vfb` appears to be the main master, while the `-OTF` variant is optimized for OTF output. The SFD file is a FontForge source for TTF production. No UFO, Glyphs, or other modern buildable sources are available.

### Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and the SFD format is not supported by gftools-builder.

### config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

### Designer & History

- **Designer**: Kosal Sen / Philatype (`holla@philatype.com`, `http://www.philatype.com`)
- **Copyright**: "Copyright (c) 2012, Kosal Sen, Philatype (holla@philatype.com), with Reserved Font Name 'Merge'"
- **Date added to Google Fonts**: 2012-10-05
- **Font**: Single weight, Regular (400), normal style. Covers Latin and Latin Extended subsets.

The font predates the common practice of maintaining open source font development on GitHub.

### Searches Conducted

- GitHub search for `kosal sen font`, `MergeOne font`, `philatype`, `merge one font` — all returned 0 results.
- GitHub user `kosal-sen` exists but has no public repositories.
- GitHub org `philatype` does not exist.
- `github.com/googlefonts/mergeone` and `github.com/googlefonts/MergeOne` — both 404.
- `philatype.com` website lists Merge (and commercial Merge Pro) but links to no source repository; the font is also sold commercially under a proprietary license.

### Notes

- The reserved font name is `Merge`, not `Merge One`.
- The Philatype website (`philatype.com`) sells a commercial version called "Merge Pro" with additional weights (Regular, Bold, Black), suggesting the OFL release of Merge One (Light weight) was an intentional partial open-source release.
- The font family has not been updated since its initial release in October 2012.
- Designer Kosal Sen's GitHub account (`github.com/KosalSen`) exists but has zero public repositories.
- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- If source files in modern format are desired, direct outreach to `holla@philatype.com` would be necessary.

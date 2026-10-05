# Puritan

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Puritan built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/puritan` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 4 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/puritan.
- Each change to the `.sfd` before conversion is its own commit: Scale the em to 1024 as
  src/generate.py did; Set the Italic's Win ascent to 880, as the release carries; Set
  the Italic's hhea ascender to 880, as the release carries.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/puritan at `df5efccea9a0`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools,
including this family's plan `plans/puritan.json`:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`df5efccea9a0` is the equivalence commit: its build is functionally equivalent to the
binaries Google Fonts ships. Source modernization adds no features. Where the shipped
binaries differ from the source, the difference is reproduced by a documented commit
before the conversion, never silently corrected. Any improvement is a later commit that
needs its own QA, and is left as future work for an onboarder to review in a font-update
PR.

## Future work

Not part of what Google Fonts ships; for review in a font-update PR:
- Raise Puritan Italic's Win ascent and hhea ascender from 880 to 881, so the top of
  Scaron is not clipped. 880 is a stale bounding box left by FontForge's em change; the
  two commits that reproduce it can be reverted.

## Original repository (dormant)

The source block this replaces, preserved for provenance:

    source {
      repository_url: "https://github.com/googlefonts/googlefontdirectory-hg"
      commit: "52f780bc9d197280a9f430574e179a5f233c56b6"
    }

## Previous investigation

## Puritan — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `puritan/src/`

### Source Files

The `puritan/src/` directory contains design sources in SFD (FontForge) format only, which cannot be built with gftools-builder:

- **SFD** (FontForge, not buildable with gftools-builder): Puritan-Bold.sfd, Puritan-BoldItalic.sfd, Puritan-Italic.sfd, Puritan-Regular.sfd
- **OTF** (compiled binaries, not design sources): Puritan-Bold.otf, Puritan-BoldItalic.otf, Puritan-Italic.otf, Puritan-Regular.otf
- **Other**: ben_weiner.jpg, ben_weiner.tif, generate.py

### Buildability

Not buildable with gftools-builder. The SFD sources are in FontForge format, which is not supported by the gftools-builder pipeline. Conversion to UFO or Glyphs format would be required.

### Designer

Ben Weiner (ben@readingtype.org.uk, http://www.readingtype.org.uk). The font was originally drawn as a student project at the University of Reading, UK, first released in 2001.

### Investigation Details

- **Checked cache**: the upstream repo cache — no cached entry.
- **GitHub search**: Searches for "Puritan font OFL", "Ben Weiner font", and "puritan font readingtype" returned no relevant results.
- **readingtype.org.uk**: The website was checked but contained no GitHub or repository links for the Puritan font.
- **Dave Crossland**: The FONTLOG notes that Dave Crossland made minor contributions in November 2010 (adding yacute, build script, metadata cleanup), but no repository link was provided.
- **FONTLOG evidence**: The FONTLOG describes conversion of source files from Macromedia Fontographer format to FontForge SFD ASCII text files (version 2.0a, March 2007). No repository URL is mentioned.

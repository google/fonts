# Numans

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Numans built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/numans` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it. The directory also holds FontLab `.vfb` files; the `.sfd` is
taken as the master because FontForge generated the shipped fonts and the build from the
`.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/numans.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/numans at `adaee3656634`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`adaee3656634` is the equivalence commit: its build is functionally equivalent to the
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

## Numans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `numans/src/`

#### Source Files in googlefontdirectory-hg

- `Numans-Regular.vfb` — FontLab source (proprietary format, not buildable with gftools)
- `Numans-Regular-TTF.sfd` — FontForge SFD (likely converted from VFB for TTF generation, not buildable with gftools-builder)
- `Numans-Regular.otf` — compiled OTF binary (not a design source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The primary design source is the `.vfb` file (FontLab proprietary format). The `.sfd` file is a TTF-flavored conversion. Neither format is buildable with gftools-builder.

### Search Results

- GitHub repository search for "Numans font", "Numans", "jovanny numans" — no results
- GitHub user search for Jovanny Lemonad — no GitHub profile found under that name; related fonts (Philosopher, Yeseva One) were maintained by others (alexeiva) after acquisition
- Designer's website (jovanny.ru / www.jovanny.ru) — not reachable (connection refused)
- The font binary references `http://www.jovanny.ru/` as the vendor URL, but the site is down
- No cached clone found in `/mnt/shared/upstream_repos/fontc_crater_cache/`

### Font Metadata

- **Designer**: Jovanny Lemonad
- **Copyright**: Copyright (c) 2011 by Jovanny Lemonad. All rights reserved.
- **Vendor URL**: http://www.jovanny.ru/
- **Version**: 001.001

### Notes

- Numans is a modern grotesque sans-serif with open forms, designed in 2011.
- The designer Jovanny Lemonad also designed Philosopher and Yeseva One (both on Google Fonts), but those fonts have been maintained in separate GitHub repos by third parties (alexeiva).
- No GitHub repository under Jovanny Lemonad's name was found. The original website (jovanny.ru) is unreachable.
- The googlefontdirectory-hg monorepo is the only known location of the original source files.
- Confidence in source identification: **Medium** — the VFB source in googlefontdirectory-hg is the original design source, but the proprietary format limits its usefulness for rebuilding.

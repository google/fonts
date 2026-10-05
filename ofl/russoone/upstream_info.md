# Russo One

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Russo One built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/russoone` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/russoone.
- Each change to the `.sfd` before conversion is its own commit: Set fsType to 0,
  installable embedding.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/russoone at `8c3b8424e9b7`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools,
including this family's plan `plans/russoone.json`:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`8c3b8424e9b7` is the equivalence commit: its build is functionally equivalent to the
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

## Russo One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

The `googlefontdirectory-hg` monorepo (the historical Google Font Directory Mercurial archive) contains files for this family.

- **Repository**: `googlefontdirectory-hg`
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `russoone/src/`

### Source Files

The `russoone/src/` directory contains design sources in SFD (FontForge) format only, which cannot be built with gftools-builder:

- **SFD** (FontForge, not buildable with gftools-builder): RussoOne-Regular-TTF.sfd

### Buildability

Not buildable with gftools-builder. The SFD sources are in FontForge format, which is not supported by the gftools-builder pipeline. Conversion to UFO or Glyphs format would be required.

### Designer

Jovanny Lemonad

### Investigation Details

Russo One was designed by Jovanny Lemonad (lemonad@jovanny.ru). The DESCRIPTION.en_us.html and FONTLOG.txt direct contributors to contact the designer directly at `lemonad@jovanny.ru`, but contain no upstream source repository links.

Searches were conducted for:
- `RussoOne` by name on GitHub
- `Russo One lemonad`
- `Russo One font Cyrillic`
- `jovanny lemonad` GitHub search
- GitHub user `jovanny`

The GitHub user `jovanny` was found but only had one unrelated repository (`jovanny/repositorio`). Jovanny Lemonad's font work appeared to be managed through third parties: the Google Fonts engineer `alexeiva` maintained repos for two other Jovanny Lemonad fonts (Philosopher and Yeseva One) but no Russo One repository was found.

The only repositories matching `RussoOne` were:
- `librefonts/russoone` — a librefonts mirror (skipped per policy)
- `google-fonts-bower/russoone-bower` — a bower packaging repo (skipped)

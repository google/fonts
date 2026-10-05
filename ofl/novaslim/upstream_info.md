# Nova Slim

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Nova Slim built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/novaslim` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. The shipped binary carries FontForge's `FFTM` table,
so FontForge generated it.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/novaslim.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/novaslim at `f3765a052f68`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 1 style. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`f3765a052f68` is the equivalence commit: its build is functionally equivalent to the
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

## Nova Slim — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

### Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/nicholasgross/googlefontdirectory-hg) (Mercurial-to-Git conversion of the original Google Font Directory)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `novaslim/src/`

#### Source Files in googlefontdirectory-hg

- `NovaSlim.sfd` — FontForge source file (primary editable source)
- `METADATA_comments.txt` — metadata notes (not a source file)

The `.sfd` (FontForge) format is the only design source. This format is not buildable with gftools-builder.

### Additional Repository Information

- **Librefonts mirror**: https://github.com/librefonts/novaslim
  - Branch: `master`
  - Latest commit: `feafcbc2bc2477576ee6c71a812eda28cb25f538` (2014-10-17, "update .travis.yml")
  - Status: Frozen since 2014; not archived but no activity since then.

- **Designer's canonical repo**: https://github.com/wmk69/Nova
  - Nova Slim as a standalone font is **not present** in `wmk69/Nova`. In the v3.x redesign (2020), "Nova Slim" was absorbed into "NovaRound Slim" (`NovaRoundSlim-Book.sfd`, etc.), and slim variants were also added for Nova Flat and Nova Square. The standalone Nova Slim font was discontinued as a separate family.

- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG).

### Build System

The librefonts repo uses the legacy `fontbakery-build.py` pipeline (circa 2014), driven by a `.travis.yml` CI config. This system is obsolete. No `Makefile` or modern build script is present. No `config.yaml` exists.

### Notes

- The Google Fonts binary (`NovaSlim.ttf`) corresponds to version 2.000 (2011).
- The designer merged Nova Slim into Nova Round Slim in v3.x (2020), ending it as a standalone family. Per the wmk69/Nova FONTLOG v3.0.0: "Nova Slim is now Nova Round Slim, because I did slim versions of other fonts."
- The librefonts mirror and googlefontdirectory-hg are the only available sources for the v2.000 design.
- Designer: Wojciech Kalinowski (wmk69), wmk69@o2.pl.
- Confidence in source identification: **High** — the SFD source in googlefontdirectory-hg matches the librefonts mirror and the Google Fonts binary.

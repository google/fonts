# Marvel

**Model**: Claude Opus 5.5
**Date**: 2026-10-05

Sources modernized 2026-10: the FontForge `.sfd` sources were converted to Glyphs
(`.glyphs`) and build with gftools-builder and fontc. The repository, commit and config
are in the `source { }` block of METADATA.pb.

## Initial state

Google Fonts shipped Marvel built from FontForge `.sfd` sources in the family's
directory in the googlefontdirectory-hg monorepo
(https://github.com/googlefonts/googlefontdirectory-hg, `ofl/marvel` at commit
`52f780bc9d197280a9f430574e179a5f233c56b6`); it had no repository of its own. There was
no source that builds with fontc. All 4 shipped binaries carry FontForge's `FFTM` table,
so FontForge generated them. The directory also holds FontLab `.vfb` files; the `.sfd`
is taken as the master because FontForge generated the shipped fonts and the build from
the `.sfd` is functionally equivalent to them.

## Actions taken

- The family's files were imported unmodified as the first commit of
  https://github.com/googlefonts/marvel.
- The `.sfd` needed no change: it was converted exactly as the designer left it.
- The `.sfd` was converted with babelfont-rs, using only filters that reproduce
  FontForge's own export, as the last commit.

## Final state

The source is https://github.com/googlefonts/marvel at `1fd5b632dcc4`. Builds with
gftools-builder (gftools-rust ade8776, fontc 1.0.0) and matches the binaries
google/fonts b5efa9c32e8f ships: 0 blocking rows under tools/table_gate.py, exactly the
release's codepoints, and functionally equivalent under tools/functional_gate.py (cmap,
shaping, rendering, names, line spacing, advances, GDEF), 4 styles. Those tools:
https://github.com/felipesanches/gf-source-modernization at `541f72b`.

`1fd5b632dcc4` is the equivalence commit: its build is functionally equivalent to the
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

## Marvel — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

### Source Repository

The source files for Marvel are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `marvel/src/`.

#### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Marvel-Regular-TTF.sfd` | FontForge SFD | Not gftools-builder compatible |
| `Marvel-Bold-TTF.sfd` | FontForge SFD | Not gftools-builder compatible |
| `Marvel-Italic-TTF.sfd` | FontForge SFD | Not gftools-builder compatible |
| `Marvel-BoldItalic-TTF.sfd` | FontForge SFD | Not gftools-builder compatible |
| `Marvel-Regular.vfb` | FontLab VFB | Proprietary, not buildable |
| `Marvel-Bold.vfb` | FontLab VFB | Proprietary, not buildable |
| `Marvel-Italic.vfb` | FontLab VFB | Proprietary, not buildable |
| `Marvel-BoldItalic.vfb` | FontLab VFB | Proprietary, not buildable |
| `Marvel-Regular.otf` | Compiled OTF binary | Not a design source |
| `Marvel-Bold.otf` | Compiled OTF binary | Not a design source |
| `Marvel-Italic.otf` | Compiled OTF binary | Not a design source |
| `Marvel-BoldItalic.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

Full 4-style family (Regular, Bold, Italic, BoldItalic) with SFD and VFB sources for each style. No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist.

### librefonts Mirror

The same source files are also available at https://github.com/librefonts/marvel, created on 2014-07-16 under the `librefonts` organization. The repo has 12 commits total (all from July-October 2014), where the initial commit moved the font files from a larger collection and all subsequent commits were Travis CI configuration updates — no font source changes were ever made.

| Commit | Date | Message |
|--------|------|---------|
| `a81adb15` | 2014-07-16 | Move marvel font files to separate repository |
| `80ed3d81` | 2014-10-17 | update .travis.yml (HEAD of master) |

The repository also contains TTX decomposed tables at root level for all 4 styles, OTF TTX decompositions in `src/`, and metadata files.

### Onboarding History

Marvel was added to Google Fonts on 2011-08-03 (per `date_added` in METADATA.pb). The font files were present from the initial google/fonts commit (`90abd17b4`, 2015-03-07). The TTF binaries have never been modified since their original addition.

**Designer**: Carolina Trebol (ca@fromzero.org)

Subsequent commits touching the Marvel directory were metadata-only:
- `480630de3` (2015-12-08) — METADATA.pb textproto update
- `27f377ab0` (2016-01-11) — Copyright field update
- `883939708` (2016-01-11) — Remove METADATA.json files
- Various language support and classification commits
- `6bda16478` (2024-02-16) — HTML description reformatting

### Build Configuration

No `config.yaml` exists and none can be created. The source files are in SFD (FontForge) and VFB (FontLab) formats, neither of which is supported by gftools-builder or fontc. The legacy `.travis.yml` used the old `fontbakery-build.py` pipeline (Python 2.7, FontForge-based).

### Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/marvel"
  commit: "80ed3d8114b8c8436dae8673d6cf8fd309376d57"
}
```

No `config_yaml` field is needed — the sources are SFD/VFB only and not compatible with gftools-builder. The commit `80ed3d8` is HEAD of master and encompasses all font source content (subsequent commits were CI-only changes).

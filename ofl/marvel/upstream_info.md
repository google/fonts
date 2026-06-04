# Marvel — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Marvel are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `marvel/src/`.

### Source Files in googlefontdirectory-hg

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

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/marvel, created on 2014-07-16 under the `librefonts` organization. The repo has 12 commits total (all from July-October 2014), where the initial commit moved the font files from a larger collection and all subsequent commits were Travis CI configuration updates — no font source changes were ever made.

| Commit | Date | Message |
|--------|------|---------|
| `a81adb15` | 2014-07-16 | Move marvel font files to separate repository |
| `80ed3d81` | 2014-10-17 | update .travis.yml (HEAD of master) |

The repository also contains TTX decomposed tables at root level for all 4 styles, OTF TTX decompositions in `src/`, and metadata files.

## Onboarding History

Marvel was added to Google Fonts on 2011-08-03 (per `date_added` in METADATA.pb). The font files were present from the initial google/fonts commit (`90abd17b4`, 2015-03-07). The TTF binaries have never been modified since their original addition.

**Designer**: Carolina Trebol (ca@fromzero.org)

Subsequent commits touching the Marvel directory were metadata-only:
- `480630de3` (2015-12-08) — METADATA.pb textproto update
- `27f377ab0` (2016-01-11) — Copyright field update
- `883939708` (2016-01-11) — Remove METADATA.json files
- Various language support and classification commits
- `6bda16478` (2024-02-16) — HTML description reformatting

## Build Configuration

No `config.yaml` exists and none can be created. The source files are in SFD (FontForge) and VFB (FontLab) formats, neither of which is supported by gftools-builder or fontc. The legacy `.travis.yml` used the old `fontbakery-build.py` pipeline (Python 2.7, FontForge-based).

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/marvel"
  commit: "80ed3d8114b8c8436dae8673d6cf8fd309376d57"
}
```

No `config_yaml` field is needed — the sources are SFD/VFB only and not compatible with gftools-builder. The commit `80ed3d8` is HEAD of master and encompasses all font source content (subsequent commits were CI-only changes).

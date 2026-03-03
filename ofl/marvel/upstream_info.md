# Marvel — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD-only sources)

## METADATA.pb Source Block (current)

The main branch of google/fonts currently has **no source block** for Marvel. However, a source block was added on the branch `sources_info_2026-02-25` in commit `9a14639f3`:

```
source {
  repository_url: "https://github.com/librefonts/marvel"
  commit: "80ed3d8114b8c8436dae8673d6cf8fd309376d57"
}
```

This has not yet been merged to main.

## Repository Analysis

**Repository**: https://github.com/librefonts/marvel
**Accessible**: Yes
**Archived**: No
**Fork**: No
**Created**: 2014-07-16
**Last pushed**: 2014-10-17

The repository was created under the `librefonts` GitHub organization. The initial commit message was "Move marvel font files to separate repository", indicating the sources were migrated from a larger collection (the old google/fonts monorepo structure) into individual per-family repositories.

### Commit History (12 commits total)

| Commit | Date | Message |
|--------|------|---------|
| `a81adb15` | 2014-07-16 | Move marvel font files to separate repository |
| `a28b30ee` | 2014-08-19 | Added .travis.yml |
| `3d5622c1` | 2014-08-21 | Travis.yml update |
| `5aa57893` | 2014-08-22 | Travis.yml update |
| `0c501da4` | 2014-08-22 | Travis.yml update |
| `1d7f1a19` | 2014-09-11 | update .travis.yml |
| `0611e7e4` | 2014-09-12 | Added raw=True to VDMX and FFTM |
| `051efe9a` | 2014-09-14 | Installing ttfautohint from ppa:fontforge/fontforge repository |
| `04417b0c` | 2014-09-15 | Update .travis.yml |
| `934271a0` | 2014-09-19 | Update .travis.yml |
| `9ce429a1` | 2014-10-06 | Rename fontbakery |
| `80ed3d81` | 2014-10-17 | update .travis.yml (HEAD of master) |

All commits after the initial one were CI/Travis configuration updates. No font source changes were ever made in this repository.

### Repository Contents

The repository contains:
- **TTX files** (decomposed TTF tables) at the root level for all 4 styles
- **SFD files** (FontForge format) in `src/` directory: `Marvel-Regular-TTF.sfd`, `Marvel-Bold-TTF.sfd`, `Marvel-Italic-TTF.sfd`, `Marvel-BoldItalic-TTF.sfd`
- **VFB files** (FontLab format) in `src/`: `Marvel-Regular.vfb`, `Marvel-Bold.vfb`, `Marvel-Italic.vfb`, `Marvel-BoldItalic.vfb`
- **OTF TTX decompositions** in `src/` (CFF outlines)
- `METADATA.json`, `DESCRIPTION.en_us.html`, `OFL.txt`
- `.travis.yml` for CI (using old fontbakery-build.py)

**No gftools-builder compatible sources** (.glyphs, .ufo, .designspace) exist in this repository. The original sources are in legacy formats (SFD and VFB).

## Onboarding History

Marvel was added to Google Fonts on **2011-08-03** (per `date_added` in METADATA.pb). The designer is **Carolina Trebol** (`ca@fromzero.org`).

In the google/fonts repository, the font files were present from the initial commit (`90abd17b4`, 2015-03-07). The font binaries have never been updated since their original addition — the only commits touching the Marvel directory were:
- `480630de3` (2015-12-08): METADATA.pb textproto update
- `27f377ab0` (2016-01-11): Copyright field update in METADATA.pb
- `883939708` (2016-01-11): Remove METADATA.json files
- Various metadata-only commits (language support, stroke/classification)
- `76adaf1d2` (2021-11-01): Deploy commit that temporarily deleted and restored files (part of repo restructuring)
- `6bda16478` (2024-02-16): HTML description reformatting

The TTF binaries themselves have never been modified since the initial commit.

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can meaningfully be created because:

1. The source files are in **SFD** (FontForge Spline Font Database) and **VFB** (FontLab binary) formats
2. Neither format is supported by gftools-builder or fontc
3. The TTX files in the repository are decomposed table dumps, not editable sources
4. The `.travis.yml` used the old `fontbakery-build.py` pipeline (Python 2.7, FontForge-based)

This font predates the modern gftools-builder workflow entirely. The original compilation was done using FontForge, as evidenced by the SFD source files and the Travis CI configuration.

## Findings

1. **Repository URL is correct**: `https://github.com/librefonts/marvel` is the canonical upstream repository for Marvel.

2. **Commit hash**: The source block on the `sources_info_2026-02-25` branch references `80ed3d8114b8c8436dae8673d6cf8fd309376d57`, which is the latest (HEAD) commit on master. This is appropriate since:
   - The repository only had 12 commits, all from July-October 2014
   - All commits after the initial one were Travis CI configuration updates
   - No font source changes were ever made after the initial commit
   - The font was added to Google Fonts in 2011, predating the librefonts repo (2014), so the binaries in google/fonts were compiled from sources outside this repo originally

3. **No config.yaml possible**: The sources are SFD-only (plus VFB), which are not compatible with gftools-builder. No override config.yaml can be created.

4. **Source block status**: A source block already exists on the `sources_info_2026-02-25` branch. It correctly identifies the repository and uses the HEAD commit hash. No `config_yaml` field is included, which is correct given the SFD-only sources.

5. **Local clone note**: The local clone at `fontc_crater_cache/librefonts/marvel` appears to be a shallow clone showing only 1 commit, while the GitHub API shows 12 commits in the full history. The HEAD commit (`80ed3d8`) is consistent.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/marvel"
  commit: "80ed3d8114b8c8436dae8673d6cf8fd309376d57"
}
```

No `config_yaml` field is needed — the upstream sources are SFD/VFB only and are not compatible with gftools-builder. The source block correctly identifies the repository and the latest commit, which encompasses all font source content (subsequent commits were CI-only changes).

# Marcellus SC — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (VFB-only sources, no gftools-builder compatible files)

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic family metadata:

```
name: "Marcellus SC"
designer: "Astigmatic"
license: "OFL"
category: "SERIF"
date_added: "2012-05-09"
```

## Repository Analysis

**Repository**: https://github.com/librefonts/marcellussc
**Created**: 2014-07-16 (two years after the font was added to Google Fonts)
**Last pushed**: 2014-10-17
**Archived**: No
**Organization**: librefonts (members: davelab6, felipesanches, pathumego)

The repository contains a single commit:
- `75b6e93` (2014-10-17, author: hash3g) — "update .travis.yml"

This is a librefonts archive repository, not the original designer's repository. The librefonts organization was a community effort to archive Google Fonts source files on GitHub. The repo was created in 2014, well after the font was added to the catalog in May 2012.

### Repository Contents

**Root directory**: TTX decompositions of the TTF binary, plus metadata files (DESCRIPTION.en_us.html, FONTLOG.txt, METADATA.json, OFL.txt), and a `.travis.yml` for fontbakery CI.

**src/ directory**: Contains the original source files:
- `MarcellusSC-Regular.vfb` — Original source with contour overlaps (FontLab VFB format)
- `MarcellusSC-Regular-OTF.vfb` — Merged contours, optimized for OTF output
- `MarcellusSC-Regular-TTF.vfb` — TrueType outlines with hinting adjustments
- OTF TTX decompositions
- `METADATA_comments.txt` — Legacy subsetting commands
- `VERSIONS.txt` — "MarcellusSC-Regular.ttf: Version 1.001"

**No gftools-builder compatible sources** (.glyphs, .glyphx, .ufo, .designspace) were found. The only editable source files are in VFB (FontLab Studio 5) format, which is a proprietary binary format not supported by gftools-builder or fontc.

### No config.yaml

No `config.yaml` exists in the repository. An override config.yaml cannot be created because there are no gftools-builder compatible source files to reference.

## Onboarding History

The font was part of the initial bulk import to the google/fonts repository:

- **Commit**: `90abd17b4` (2015-03-07) — "Initial commit" by Dave Crossland
  - This was the massive initial commit that populated the google/fonts repo with all existing Google Fonts families.
- **date_added**: 2012-05-09 — The font was originally added to the Google Fonts catalog in May 2012, predating both the librefonts repo (2014) and the google/fonts repository initial commit (2015).

The TTF binary has not been modified since the initial commit. MD5 checksum verification confirmed the file is identical: `6c4b86cb0aeea480e0112d55752335c6`.

Subsequent commits to the `ofl/marcellussc/` directory were only metadata housekeeping:
- `701bd391b` — Undo rollback, remove languages from METADATA
- `c6307ba83` — Roll back language changes
- `28b492c0f` — Clear languages from METADATA.pb
- `633ebadbf` — Add language support metadata
- `883939708` — Remove METADATA.json files
- `27f377ab0` — Update copyright field in METADATA.pb
- `480630de3` — Update to METADATA.pb textprotos

No PRs specific to Marcellus SC source metadata were found.

## Build Configuration

**Status**: No buildable sources available.

The upstream repository only contains VFB (FontLab Studio 5) source files. VFB is a proprietary binary format that cannot be processed by gftools-builder or fontc. The font would need to be converted to a modern format (.glyphs, .ufo, or .designspace) before a config.yaml could be meaningful.

The `.travis.yml` in the repo references the legacy `fontbakery-build.py` pipeline, which is long defunct.

## Findings

1. **No source block in METADATA.pb**: The file has no `source { }` block at all.
2. **VFB-only sources**: The upstream repo at librefonts/marcellussc contains only VFB source files, which are not compatible with gftools-builder or fontc.
3. **Archive repository, not original**: The librefonts repo was created in 2014 as an archive. The font was originally designed by Brian J. Bonislawsky (Astigmatic) and added to Google Fonts in 2012. There is no known GitHub repository from the original designer.
4. **Single-weight, static font**: Marcellus SC is a single-weight Regular font (400 weight). No variable font version exists.
5. **Font unchanged since onboarding**: The binary TTF has not been updated since its inclusion in the initial commit. It remains at Version 1.001 as released in April 2012.
6. **No config.yaml possible**: Without modern source files (.glyphs, .ufo, .designspace), no config.yaml can be created. The source block can reference the repository but cannot include a build configuration.
7. **Related family**: Marcellus (non-SC) is a sibling font in the same situation, with the same designer and an equivalent librefonts archive repo at librefonts/marcellus.

## Recommended Source Block

A source block can be added to document the repository URL and commit hash, even though no config.yaml is available:

```
source {
  repository_url: "https://github.com/librefonts/marcellussc"
  commit: "75b6e93759696a4d0bfd0cce86da0f9e4f38e10a"
  branch: "master"
}
```

**Notes on the recommendation**:
- The commit `75b6e93` is the only commit in the repository, so it is definitively the correct reference point.
- No `config_yaml` field is included because the repo has no gftools-builder compatible sources (VFB-only).
- The status should be recorded as "missing_config" — the repository is known and the commit is identified, but no buildable configuration exists.
- To achieve full buildability, the VFB sources would need to be converted to a modern format (e.g., .glyphs or .ufo) by someone with access to FontLab Studio or a VFB conversion tool.

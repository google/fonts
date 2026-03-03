# Macondo — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD-only sources, no gftools-builder config possible)

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic family metadata (name, designer, license, category, fonts, subsets, classifications).

## Repository Analysis

**Repository**: https://github.com/librefonts/macondo
**Default branch**: master
**Archived**: No
**Created**: 2014-07-16
**Last pushed**: 2014-10-17

The repository contains a single commit:

| Field | Value |
|-------|-------|
| Hash | `00c3eaaae24d702bce976a1766c31b8fc015f08a` |
| Date | 2014-10-17 13:42:39 +0300 |
| Author | hash3g |
| Message | "update .travis.yml" |

The repository was set up as a `librefonts` organization mirror of the font sources. It does not belong to the original designer (John Vargas Beltran). The `librefonts` GitHub organization was created 2013-10-20 and appears to host automated mirrors/backups of Google Fonts source files.

### Repository Structure

```
.travis.yml                          - CI config (fontbakery-build.py)
DESCRIPTION.en_us.html               - Font description
FONTLOG.txt                          - Font changelog
METADATA.json                        - Legacy metadata
OFL.txt                              - License
Macondo-Regular.ttf.*.ttx            - TTX decomposition of the TTF binary (multiple table files)
src/
  Macondo-Regular-OTF.vfb            - FontLab source (138 KB)
  Macondo-Regular-TTF.sfd            - FontForge source (443 KB)
  Macondo-Regular.otf.*.ttx          - TTX decomposition of the OTF binary
  METADATA_comments.txt              - Subsetting/build comments
  VERSIONS.txt                       - "Macondo-Regular.ttf: Version 2.001"
```

### Source Files

The repository contains only legacy source formats:
- **Macondo-Regular-OTF.vfb**: FontLab binary source
- **Macondo-Regular-TTF.sfd**: FontForge SFD source

No modern gftools-builder compatible sources exist (.glyphs, .glyphx, .ufo, .designspace). The font was created in 1997 (early versions) and substantially improved in 2009, with the v1.00 release dated December 14, 2011.

## Onboarding History

The font was included in the google/fonts repository from its very first commit:

| Field | Value |
|-------|-------|
| Commit | `90abd17b4f97671435798b6147b698aa9087612f` |
| Date | 2015-03-07 |
| Author | Dave Crossland |
| Message | "Initial commit" |

This was a bulk import of the entire Google Fonts library into the current git repository. The font itself was added to Google Fonts on **2012-01-18** according to the `date_added` field in METADATA.pb, which aligns with the font's head table creation date of January 11, 2012.

The font binary has never been updated since the initial commit. Only metadata files (METADATA.pb/METADATA.json) were modified in subsequent commits for format changes, language support, and classification updates.

### Subsequent commits (metadata only):
- `480630de3` - Tentative update to METADATA.pb textprotos
- `27f377ab0` - Update copyright field in METADATA.pb
- `883939708` - Remove METADATA.json files
- `633ebadbf` - Add language support metadata
- `c6307ba83` / `701bd391b` - Language rollback and redo
- `47a6c224b` - Batch of 200 METADATA.pb changes for stroke and classifications

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the only source files are in legacy formats (VFB and SFD) that are not supported by gftools-builder.

The `.travis.yml` file in the upstream repo referenced `fontbakery-build.py`, an obsolete build tool from 2014.

## Findings

1. **Legacy sources only**: The Macondo font has only FontLab (.vfb) and FontForge (.sfd) source files. These formats are not compatible with gftools-builder, which requires .glyphs, .ufo, or .designspace sources.

2. **No config.yaml possible**: Since the sources are not gftools-builder compatible, no config.yaml can be created (neither in the upstream repo nor as an override in google/fonts).

3. **Repository is a mirror**: The `librefonts/macondo` repository is not the original designer's repo. It was set up by the `librefonts` organization as a backup/mirror. The original designer (John Vargas Beltran) does not appear to have a GitHub presence for this project.

4. **Single commit repository**: The repo has only one commit (2014-10-17), which predates the google/fonts "Initial commit" (2015-03-07) but postdates the actual onboarding date (2012-01-18). The TTX files in the repo were generated from the same binary that appears in google/fonts (Version 2.001).

5. **Sister family**: Macondo Swash Caps is a related family by the same designer, hosted at `librefonts/macondoswashcaps` with the same SFD-only source situation.

6. **Font version alignment**: Both the upstream TTX decomposition and the binary in google/fonts report Version 2.001, with head table dates of January 11, 2012, confirming they represent the same font.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/macondo"
  commit: "00c3eaaae24d702bce976a1766c31b8fc015f08a"
  branch: "master"
}
```

Note: The `config_yaml` field is intentionally omitted because the upstream repository contains only SFD/VFB sources that are not compatible with gftools-builder. No override config.yaml can be created for the same reason.

## Confidence

**HIGH** for repository URL and commit hash: The `librefonts/macondo` repository is the only known upstream source. The single commit `00c3eaa` contains TTX-decomposed font data matching the binary in google/fonts (same Version 2.001, same head table dates). While the repo is a mirror rather than the designer's original workspace, it is the best available source reference.

**N/A** for config: No gftools-builder configuration is possible due to legacy-only source formats.

## Open Questions

1. Does John Vargas Beltran have original editable sources (.glyphs, .ufo) for Macondo, or only the legacy .vfb/.sfd files? If modern sources exist, they would enable a proper config.yaml.
2. Is there any plan to convert the SFD sources to a modern format to enable gftools-builder compatibility?

# Macondo Swash Caps — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD-only sources, no gftools-builder config possible)

## METADATA.pb Source Block (current)

No source block exists in the current METADATA.pb. The file contains only basic family metadata (name, designer, license, category, fonts, subsets, classifications).

## Repository Analysis

**Repository**: https://github.com/librefonts/macondoswashcaps
**Default branch**: master
**Archived**: No
**Created**: 2014-07-16
**Last pushed**: 2014-10-17

The repository contains a single commit:

| Field | Value |
|-------|-------|
| Hash | `2768d9b33c7d703085314fcd8c823ad1a8b02edb` |
| Date | 2014-10-17 13:42:41 +0300 |
| Author | hash3g |
| Message | "update .travis.yml" |

The repository was set up as a `librefonts` organization mirror of the font sources. It does not belong to the original designer (John Vargas Beltran, GitHub: vargas1974). The `librefonts` GitHub organization was created 2013-10-20 and appears to host automated mirrors/backups of Google Fonts source files. The designer's GitHub profile (vargas1974) does not contain a Macondo or Macondo Swash Caps repository; it holds other font projects (Salsa-Devanagari, Shingaling, Kyron, Ramabhadra).

### Repository Structure

```
.travis.yml                          - CI config (fontbakery-build.py, obsolete)
DESCRIPTION.en_us.html               - Font description
FONTLOG.txt                          - Font changelog
METADATA.json                        - Legacy metadata
OFL.txt                              - License
MacondoSwashCaps-Regular.ttf.*.ttx   - TTX decomposition of the TTF binary (multiple table files)
src/
  MacondoSwashCaps-Regular-OTF.vfb   - FontLab source (85 KB)
  MacondoSwashCaps-Regular-TTF.sfd   - FontForge source (290 KB)
  MacondoSwashCaps-Regular.otf.*.ttx - TTX decomposition of the OTF binary
  METADATA_comments.txt              - Subsetting/build comments
  VERSIONS.txt                       - "MacondoSwashCaps-Regular.ttf: Version 2.001"
```

### Source Files

The repository contains only legacy source formats:
- **MacondoSwashCaps-Regular-OTF.vfb**: FontLab binary source (85 KB)
- **MacondoSwashCaps-Regular-TTF.sfd**: FontForge SFD source (290 KB)

No modern gftools-builder compatible sources exist (.glyphs, .glyphx, .ufo, .designspace). The font was originally created in 1997 (early versions) and substantially improved in 2009, with the v1.00 release dated December 14, 2011.

## Onboarding History

The font was included in the google/fonts repository from its very first commit:

| Field | Value |
|-------|-------|
| Commit | `90abd17b4f97671435798b6147b698aa9087612f` |
| Date | 2015-03-07 |
| Author | Dave Crossland |
| Message | "Initial commit" |

This was a bulk import of the entire Google Fonts library into the current git repository. The font itself was added to Google Fonts on **2012-01-18** according to the `date_added` field in METADATA.pb.

The font binary has never been updated since the initial commit. Only metadata files (METADATA.pb/METADATA.json) were modified in subsequent commits for format changes, language support, and classification updates.

### Subsequent commits (metadata only):
- `480630de3` - Tentative update to METADATA.pb textprotos
- `27f377ab0` - Update copyright field in METADATA.pb
- `883939708` - Remove METADATA.json files
- `633ebadbf` - Add language support metadata (#4160)
- `c6307ba83` / `701bd391b` (#4677, #4706) - Language rollback and redo
- `28b492c0f` - Clear languages from METADATA.pb for non-Noto
- `47a6c224b` - Batch of 200 METADATA.pb changes for stroke and classifications

### Font Version Alignment

Both the upstream TTX decomposition and the binary in google/fonts report **Version 2.001**. The head table in the upstream TTX shows creation and modification dates of **Wed Jan 11 21:58:18 2012**, confirming the TTX was generated from the same font binary that was onboarded. The font binary in google/fonts is 33,016 bytes. The upstream repo does not contain a compiled TTF file; only TTX table dumps are present.

## Build Configuration

**No config.yaml exists** in the upstream repository, and none can be created because the only source files are in legacy formats (VFB and SFD) that are not supported by gftools-builder.

The `.travis.yml` file in the upstream repo referenced `fontbakery-build.py`, an obsolete build tool from 2014 that is no longer maintained.

The `METADATA_comments.txt` file in `src/` contains the original subsetting commands used to prepare the font for Google Fonts, using the legacy `subset.py` tool.

## Findings

1. **Legacy sources only**: Macondo Swash Caps has only FontLab (.vfb) and FontForge (.sfd) source files. These formats are not compatible with gftools-builder, which requires .glyphs, .ufo, or .designspace sources.

2. **No config.yaml possible**: Since the sources are not gftools-builder compatible, no config.yaml can be created (neither in the upstream repo nor as an override in google/fonts).

3. **Repository is a mirror**: The `librefonts/macondoswashcaps` repository is not the original designer's repo. It was set up by the `librefonts` organization as a backup/mirror. The original designer (John Vargas Beltran, GitHub: vargas1974) has several other font projects on GitHub but not Macondo or Macondo Swash Caps.

4. **Single commit repository**: The repo has only one commit (2014-10-17), which predates the google/fonts "Initial commit" (2015-03-07) but postdates the actual onboarding date (2012-01-18).

5. **Sister family**: Macondo Swash Caps is a sister family to Macondo (https://github.com/librefonts/macondo), designed by the same author with the same characteristics: SFD-only legacy sources, single-commit librefonts mirror, onboarded in the initial google/fonts commit.

6. **No TTF binary in upstream**: Unlike some librefonts mirrors, this repository does not contain a compiled .ttf file -- only TTX table dumps of the binary. However, the TTX data (Version 2.001, head table dates of Jan 11, 2012) matches the binary in google/fonts, confirming provenance.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/macondoswashcaps"
  commit: "2768d9b33c7d703085314fcd8c823ad1a8b02edb"
  branch: "master"
}
```

Note: The `config_yaml` field is intentionally omitted because the upstream repository contains only SFD/VFB sources that are not compatible with gftools-builder. No override config.yaml can be created for the same reason.

## Confidence

**HIGH** for repository URL and commit hash: The `librefonts/macondoswashcaps` repository is the only known upstream source. The single commit `2768d9b` contains TTX-decomposed font data matching the binary in google/fonts (same Version 2.001, same head table dates of Jan 11, 2012). While the repo is a mirror rather than the designer's original workspace, it is the best available source reference.

**N/A** for config: No gftools-builder configuration is possible due to legacy-only source formats.

## Open Questions

1. Does John Vargas Beltran have original editable sources (.glyphs, .ufo) for Macondo Swash Caps, or only the legacy .vfb/.sfd files? If modern sources exist, they would enable a proper config.yaml.
2. Is there any plan to convert the SFD sources to a modern format to enable gftools-builder compatibility?

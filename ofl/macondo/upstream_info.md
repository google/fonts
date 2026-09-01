# Macondo — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (SFD/VFB-only sources)

## Source Repository

The source files for Macondo are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `macondo/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Macondo-Regular-TTF.sfd` | FontForge SFD | Primary editable source (not gftools-builder compatible) |
| `Macondo-Regular-OTF.vfb` | FontLab VFB | Proprietary binary (not buildable with gftools) |
| `Macondo-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace) exist. The only editable sources are in SFD (FontForge) and VFB (FontLab) formats, which are not supported by gftools-builder.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/macondo, created on 2014-07-16 under the `librefonts` GitHub organization. It contains a single commit (`00c3eaaae24d702bce976a1766c31b8fc015f08a`) dated 2014-10-17, authored by hash3g. The repo was set up as part of the `librefonts` organization's mirror of Google Fonts source files and does not belong to the original designer (John Vargas Beltran).

The repository contains TTX decomposed tables at root level, the SFD/VFB sources in `src/`, and metadata files. The `src/VERSIONS.txt` records "Macondo-Regular.ttf: Version 2.001".

## Onboarding History

Macondo was added to the Google Fonts catalog on 2012-01-18 (per `date_added` in METADATA.pb), which aligns with the font's head table creation date of January 11, 2012. The font was created in 1997 (early versions) and substantially improved in 2009, with the v1.00 release dated December 14, 2011.

The font was included in the google/fonts repository from the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). The font binary has never been updated since — only metadata files (METADATA.pb/METADATA.json) were modified in subsequent commits for format changes, language support, and classification updates.

**Designer**: John Vargas Beltran
**Sister family**: Macondo Swash Caps (same designer, same SFD-only source situation at `librefonts/macondoswashcaps`)

### Subsequent commits (metadata only):
- `480630de3` — Tentative update to METADATA.pb textprotos
- `27f377ab0` — Update copyright field in METADATA.pb
- `883939708` — Remove METADATA.json files
- `633ebadbf` — Add language support metadata
- `c6307ba83` / `701bd391b` — Language rollback and redo
- `47a6c224b` — Batch of 200 METADATA.pb changes for stroke and classifications

## Build Configuration

No `config.yaml` exists and none can be created. The only source files are in SFD (FontForge) and VFB (FontLab) formats, which are not compatible with gftools-builder. The `.travis.yml` in the upstream repo referenced `fontbakery-build.py`, an obsolete build tool from 2014.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/macondo"
  commit: "00c3eaaae24d702bce976a1766c31b8fc015f08a"
  branch: "master"
}
```

No `config_yaml` field is included because the sources are SFD/VFB-only and not compatible with gftools-builder.

## Confidence

**HIGH** for repository URL and commit hash. Both the googlefontdirectory-hg monorepo and the librefonts/macondo mirror contain TTX-decomposed font data matching the binary in google/fonts (same Version 2.001, same head table dates).

**N/A** for config — no gftools-builder configuration is possible due to legacy-only source formats.

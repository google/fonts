# Nothing You Could Do — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/nothingyoucoulddo/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NothingYouCouldDo.vfb` | FontLab VFB source (proprietary, not buildable with gftools) |
| `NothingYouCouldDo-TTF.sfd` | FontForge SFD source, TTF variant (not buildable with gftools-builder) |
| `NothingYouCouldDo.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The VFB file is the original design source (FontLab proprietary format). The SFD is a FontForge conversion used for TrueType production. The presence of both indicates the original design was done in FontLab, with a FontForge conversion for the TrueType production build. Neither format is compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Kimberly Geswein (kimberlygeswein.com)
- The designer has no known GitHub presence.
- As of 2026, kimberlygeswein.com is still active and lists the KG Fonts catalog, but does not include GitHub links or source repositories.

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/nothingyoucoulddo (latest commit `545d208` on 2014-10-17, "update .travis.yml"). It contains the same VFB and SFD sources plus TTX table dumps. The `src/VERSIONS.txt` records version 1.005, matching the Google Fonts binary.

## Build System

Not applicable — the VFB source requires FontLab Studio and the SFD source requires FontForge. Neither is compatible with the modern gftools-builder pipeline. The original production workflow used the legacy `googlefontdirectory` toolchain.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The font binary in google/fonts (`NothingYouCouldDo.ttf`, Version 1.005) matches the version in the librefonts mirror's `VERSIONS.txt`.
- The VFB FontLab source is the most authoritative design file available, but requires FontLab Studio to open.
- The `librefonts` organization appears to have been a Google Fonts-affiliated archiving effort circa 2014 and does not represent active development.

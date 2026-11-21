# Neucha — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/neucha/src/`
- **Buildable**: No — legacy formats only (.vfb/.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `Neucha.vfb` | FontLab VFB source (proprietary, not buildable with gftools) |
| `Neucha-TTF.sfd` | FontForge SFD source (not buildable with gftools-builder) |
| `Neucha-hints.ttf` | Compiled/hinted TTF binary (not a design source) |
| `neucha.otf` | Compiled OTF binary (not a design source) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The VFB file is the original design source (FontLab proprietary format). The SFD is a FontForge conversion used for TrueType production. Neither format is compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Jovanny Lemonad (`lemonad@jovanny.ru`). The OFL copyright points to `http://www.jovanny.ru` (2008-2010).
- The designer's website `jovanny.ru` is currently unreachable (connection refused).
- The RPM packaging repo `OpenMandrivaAssociation/fonts-otf-neucha` identifies the upstream URL as `https://jovanny.ru/free-fonts.html`, where the font was distributed as a pre-built OTF binary — not as source files.
- No GitHub repository under any of the expected accounts (`jovanny`, `lemonad`, `jovannylemonad`, `googlefonts/neucha`) was found.

## Build System

Not applicable — the VFB source requires FontLab Studio and the SFD source requires FontForge. Neither is compatible with the modern gftools-builder pipeline.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- Neucha is a Cyrillic+Latin handwriting font, created by Jovanny Lemonad in 2005 and redesigned subsequently.
- The copyright dates in the OFL span 2005-2010; no updates to the Google Fonts binary have been identified.
- The font was added to Google Fonts on 2010-09-21, making it one of the earliest additions.
- The designer's online presence (`jovanny.ru`) is currently offline; the font may only have ever been distributed as a binary download.

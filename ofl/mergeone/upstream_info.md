# Merge One — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

The original design sources for Merge One are preserved in the **googlefontdirectory-hg** monorepo, a git mirror of the original Google Code Mercurial repository that was the canonical host for Google Fonts from 2010 to 2013.

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/mergeone/src/`

### Source files

| File | Format | Buildable |
|------|--------|-----------|
| `MergeOne-Regular.vfb` | FontLab VFB | No (proprietary) |
| `MergeOne-Regular-OTF.vfb` | FontLab VFB | No (proprietary) |
| `MergeOne-Regular-TTF.sfd` | FontForge SFD | No (not gftools-builder compatible) |
| `MergeOne-Regular.otf` | Compiled OTF binary | No (not a design source) |
| `METADATA_comments.txt` | Metadata notes | N/A |

Multiple VFB files are present: `MergeOne-Regular.vfb` appears to be the main master, while the `-OTF` variant is optimized for OTF output. The SFD file is a FontForge source for TTF production. No UFO, Glyphs, or other modern buildable sources are available.

## Build System

No modern build system (gftools builder, fontmake) is available. The VFB format is proprietary (FontLab Studio) and the SFD format is not supported by gftools-builder.

## config.yaml Status

No `config.yaml` exists. One cannot be created without converting sources to a modern format (UFO or Glyphs).

## Designer & History

- **Designer**: Kosal Sen / Philatype (`holla@philatype.com`, `http://www.philatype.com`)
- **Copyright**: "Copyright (c) 2012, Kosal Sen, Philatype (holla@philatype.com), with Reserved Font Name 'Merge'"
- **Date added to Google Fonts**: 2012-10-05
- **Font**: Single weight, Regular (400), normal style. Covers Latin and Latin Extended subsets.

The font predates the common practice of maintaining open source font development on GitHub.

## Searches Conducted

- GitHub search for `kosal sen font`, `MergeOne font`, `philatype`, `merge one font` — all returned 0 results.
- GitHub user `kosal-sen` exists but has no public repositories.
- GitHub org `philatype` does not exist.
- `github.com/googlefonts/mergeone` and `github.com/googlefonts/MergeOne` — both 404.
- `philatype.com` website lists Merge (and commercial Merge Pro) but links to no source repository; the font is also sold commercially under a proprietary license.

## Notes

- The reserved font name is `Merge`, not `Merge One`.
- The Philatype website (`philatype.com`) sells a commercial version called "Merge Pro" with additional weights (Regular, Bold, Black), suggesting the OFL release of Merge One (Light weight) was an intentional partial open-source release.
- The font family has not been updated since its initial release in October 2012.
- Designer Kosal Sen's GitHub account (`github.com/KosalSen`) exists but has zero public repositories.
- The googlefontdirectory-hg monorepo is the only known location of design source files for this family.
- If source files in modern format are desired, direct outreach to `holla@philatype.com` would be necessary.

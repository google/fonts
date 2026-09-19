# Nova Cut — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Source Repository

- **Repository**: [googlefontdirectory-hg](https://github.com/googlefonts/googlefontdirectory-hg) (Mercurial monorepo, pre-GitHub era)
- **Commit**: `52f780bc9d197280a9f430574e179a5f233c56b6`
- **Source path**: `ofl/novacut/src/`
- **Buildable**: No — legacy format only (.sfd)

The font sources are in the **googlefontdirectory-hg** monorepo, a git mirror of the
original Google Code Mercurial repository (`code.google.com/p/googlefontdirectory`)
that was the canonical host for Google Fonts from 2010 to 2013.

### Source Files

| File | Type |
|------|------|
| `NovaCut.sfd` | FontForge SFD source (not buildable with gftools-builder) |
| `METADATA_comments.txt` | Metadata comments (not a source file) |

The SFD file is the only editable source and serves as the authoritative design file. It is FontForge format, not compatible with gftools-builder.

## Designer and Provenance

- **Designer**: Wojciech Kalinowski (wmk69), wmk69@o2.pl
- **Designer's canonical repo**: https://github.com/wmk69/Nova — covers the redesigned Nova 3.x family (2020-2022) but **intentionally excludes Nova Cut**, which was removed in v3.0.0 (May 2020) due to visual similarity with Gothica. The Google Fonts version (v2.000) predates this split.
- **Open Font Library**: https://fontlibrary.org (listed as source in original FONTLOG; individual page no longer available).

## Additional Mirror

A third-party mirror exists at https://github.com/librefonts/novacut (latest commit `aa17adb` on 2014-10-17, "update .travis.yml"). It contains the same SFD source plus TTX-decomposed TTF tables. The `src/VERSIONS.txt` records version 2.000, matching the Google Fonts binary. The repo used the legacy `fontbakery-build.py` pipeline (circa 2014), which is obsolete.

## Build System

Not applicable — the SFD source requires FontForge. Rebuilding from source would require FontForge and manual steps.

## config.yaml

Does not exist. Cannot be created — no gftools-builder compatible sources available.

## Notes

- The Google Fonts binary (`NovaCut.ttf`) corresponds to version 2.000 (2011), redesigned September 2011.
- Nova Cut was officially dropped from the designer's active Nova family in 2020 and has no maintained upstream.
- The font covers Latin, Latin Extended, and a small set of Greek and mathematical symbols.
- **Confidence**: High — the monorepo SFD and librefonts mirror are the known sources for this family.

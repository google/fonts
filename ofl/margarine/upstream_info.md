# Margarine — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete (VFB-only sources)

## Source Repository

The source files for Margarine are available in the **googlefontdirectory-hg** monorepo at commit `52f780bc9d197280a9f430574e179a5f233c56b6`, under the path `margarine/src/`.

### Source Files in googlefontdirectory-hg

| File | Format | Notes |
|------|--------|-------|
| `Margarine-Regular.vfb` | FontLab VFB | Original source (proprietary, not buildable with gftools) |
| `Margarine-Regular-OTF.vfb` | FontLab VFB | Merged contours, optimized for OTF |
| `Margarine-Regular-TTF.vfb` | FontLab VFB | TrueType outlines with hinting |
| `Margarine-Regular.otf` | Compiled OTF binary | Not a design source |
| `METADATA_comments.txt` | Metadata | Legacy subsetting commands, not a source file |

No modern gftools-builder compatible sources (.glyphs, .ufo, .designspace, .sfd) exist. The only editable sources are VFB (FontLab Studio) format, which is a proprietary binary format not supported by gftools-builder.

## librefonts Mirror

The same source files are also available at https://github.com/librefonts/margarine, created on 2014-07-16 under the `librefonts` organization — a third-party effort by Mikhail Kashkin that extracted font files from the old Google Font Directory into individual GitHub repositories.

The repo has 12 commits total (all from 2014, by Mikhail Kashkin aka hash3g):
- `56637ab` (2014-07-16) — "Move margarine font files to separate repository" (initial commit)
- `645187d` (2014-07-18) — cleanup
- `70e841c` through `c612652` (2014-08-19 to 2014-10-17) — Various .travis.yml updates

The repo has been dormant since October 2014.

## Onboarding History

Margarine was added to google/fonts in the initial commit (`90abd17b4`, 2015-03-07, by Dave Crossland). This was the bulk import of the entire Google Fonts library. No PR or specific onboarding process was associated with this font.

The font was originally designed by Brian J. Bonislawsky (Astigmatic/AOETI) and released in November 2012 (Version 1.000). The font has never been updated in google/fonts since the initial commit (aside from metadata changes to METADATA.pb).

**Designer**: Brian J. Bonislawsky (Astigmatic/AOETI, astigma@astigmatic.com, www.astigmatic.com)
**GitHub**: https://github.com/astigmatic (exists but has no font repos)

## Build Configuration

No `config.yaml` exists and none can be created. The only source files are VFB (FontLab) binaries, which cannot be processed by gftools-builder. The TTX files in the librefonts mirror are decompositions of already-compiled binaries, not true design sources.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/margarine"
  commit: "c6126521f50b0be64bbc44cd287f71eb706127a1"
  branch: "master"
}
```

No `config_yaml` field is included because the repo has VFB-only sources not compatible with gftools-builder. The commit `c612652` is the latest commit in the repo.

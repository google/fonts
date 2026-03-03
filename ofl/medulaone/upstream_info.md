# Medula One — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (SFD/VFB-only sources, no gftools-builder config possible)

## METADATA.pb Source Block (current)

No source block exists. The current METADATA.pb contains only basic metadata:

```
name: "Medula One"
designer: "LatinoType"
license: "OFL"
category: "DISPLAY"
date_added: "2011-12-19"
fonts {
  name: "Medula One"
  style: "normal"
  weight: 400
  filename: "MedulaOne-Regular.ttf"
  post_script_name: "MedulaOne-Regular"
  full_name: "Medula One"
  copyright: "Copyright (c) 2011 by LatinoType Limitada (luciano@latinotype.com), with Reserved Font Names \"Medula\""
}
subsets: "menu"
subsets: "latin"
subsets: "latin-ext"
```

## Repository Analysis

**Upstream repository**: https://github.com/librefonts/medulaone

The repository belongs to the `librefonts` GitHub organization, which was used as a mirror/archive for Google Fonts library source files. It was created on 2014-07-16 by Mikhail Kashkin (@xen), whose initial commit message was "Move medulaone font files to separate repository" — indicating this was a reorganization of files from a larger collection into individual per-family repositories.

The repo is not a fork and has no description. It is not archived.

### Repository Contents (at HEAD, commit `9559bbd`)

The repository contains:
- **Decomposed TTX files** of the compiled TTF font (split into per-table `.ttx` files)
- **Source files** in `src/`:
  - `MedulaOne-Regular-TTF.sfd` — FontForge Spline Font Database (269 KB)
  - `MedulaOne-Regular-OTF.vfb` — FontLab VFB binary (102 KB)
  - Decomposed TTX files of the OTF version
  - `METADATA_comments.txt` — subsetting commands used during original onboarding
  - `VERSIONS.txt` — indicates "Version 1.002"
- `.travis.yml` — Travis CI configuration using fontbakery-build.py (legacy)
- `METADATA.json`, `DESCRIPTION.en_us.html`, `OFL.txt`

### Commit History (12 commits total, all from 2014)

| Hash | Date | Author | Message |
|------|------|--------|---------|
| `71bda1c` | 2014-07-16 | Mikhail Kashkin (@xen) | Move medulaone font files to separate repository |
| `895207b` | 2014-08-19 | hash3g | Added .travis.yml |
| `e4fa02a` | 2014-08-21 | hash3g | Travis.yml update |
| `9a7c880` | 2014-08-22 | hash3g | Travis.yml update |
| `ace72d0` | 2014-08-22 | hash3g | Travis.yml update |
| `03e838b` | 2014-09-11 | hash3g | update .travis.yml |
| `5a516c2` | 2014-09-12 | hash3g | Added raw=True to VDMX and FFTM |
| `2067801` | 2014-09-14 | hash3g | Installing ttfautohint from ppa |
| `5a468a8` | 2014-09-15 | hash3g | Update .travis.yml |
| `7a2807a` | 2014-09-19 | hash3g | Update .travis.yml |
| `31c582f` | 2014-10-06 | hash3g | Rename fontbakery |
| `9559bbd` | 2014-10-17 | hash3g | update .travis.yml |

All commits after the initial one were Travis CI configuration updates by hash3g. The source files (SFD, VFB) were never modified after the initial commit.

### Contributors
- **Mikhail Kashkin** (@xen) — created the repo by extracting files from a larger collection
- **hash3g** — contributed all Travis CI configuration updates

### No config.yaml

The repository has no `config.yaml` file. The Travis CI configuration used the legacy `fontbakery-build.py` tool, which is not compatible with modern gftools-builder.

## Onboarding History

Medula One was added to Google Fonts on **2011-12-19** (per `date_added` in METADATA.pb). The font file was included in the google/fonts repository in the **initial commit** (`90abd17b4`, dated 2015-03-07), which was the bulk import of all existing Google Fonts families into the current repository structure.

The font binary (`MedulaOne-Regular.ttf`) was **never modified** after the initial commit — no updates or rebuilds were ever applied.

The `librefonts/medulaone` repository was created on **2014-07-16**, approximately 2.5 years after the font was added to Google Fonts. This confirms the librefonts repo is a post-hoc archive of the source files, not the original development repository.

## Build Configuration

**No gftools-builder configuration is possible.**

The only source files available are:
1. **`MedulaOne-Regular-TTF.sfd`** — FontForge SFD format
2. **`MedulaOne-Regular-OTF.vfb`** — FontLab VFB binary format

Neither format is supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No override `config.yaml` can be created because there are no compatible source files to reference.

The original font was designed by **LatinoType** (Luciano Vergara, luciano@latinotype.com) and was likely compiled using FontForge or FontLab directly. The copyright notice dates to 2011.

## Findings

1. **No source block in METADATA.pb** — needs to be added with repository_url and commit hash.
2. **Repository is a post-hoc archive** — the librefonts/medulaone repo was created in 2014, while the font was added to Google Fonts in 2011. The repo was created by Mikhail Kashkin as part of the librefonts organization's effort to create per-family repositories from the earlier googlefontdirectory collection.
3. **SFD/VFB-only sources** — the upstream repo only has FontForge (.sfd) and FontLab (.vfb) source files. These are not compatible with gftools-builder and cannot be used with a config.yaml.
4. **Single commit for source files** — the initial commit `71bda1c` (2014-07-16) contains all source files. Subsequent commits only modified the Travis CI configuration.
5. **Font binary unchanged since initial import** — the TTF file in google/fonts was never updated after the bulk initial commit.
6. **Shallow clone in cache** — the local clone is shallow (depth=1), containing only the latest commit `9559bbd`. The full history was obtained via the GitHub API.
7. **The appropriate commit for the source block is `9559bbd`** (HEAD of master), since the source files are unchanged across all commits and this is the latest state of the repository.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/librefonts/medulaone"
  commit: "9559bbd73be136d236851c03e0050708315aef2e"
}
```

**Notes on the recommendation:**
- The `config_yaml` field is omitted because there are no gftools-builder compatible sources (SFD/VFB only).
- The commit `9559bbd` is used as it is HEAD of master and the source files are identical to the initial commit.
- No override config.yaml is possible since the source formats are incompatible with gftools-builder.
- Status: `missing_config` — this family has SFD-only sources that cannot be used with gftools-builder.

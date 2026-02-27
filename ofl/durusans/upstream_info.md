# Investigation: Duru Sans

- **Date investigated**: 2026-02-27
- **Status**: missing_config (SFD-only sources)
- **Designer**: Onur Yazicigil
- **METADATA.pb path**: `ofl/durusans/METADATA.pb`

## Source Data

| Field           | Value                                          |
|-----------------|------------------------------------------------|
| repository_url  | https://github.com/librefonts/durusans         |
| commit_hash     | 2895eb6c9842f80c1e01bbf9fbb6231eaef66724       |
| config_yaml     | N/A (SFD-only sources, not gftools-builder compatible) |

## How the Repository URL Was Found

The upstream repository at `https://github.com/librefonts/durusans` was found in the fontc_crater_cache at `librefonts/durusans`. The METADATA.pb in google/fonts has no `source` block and no `repository_url` field.

Verification that this is the correct repository:
- The FONTLOG.txt files in google/fonts and the upstream repo are **identical**.
- The OFL.txt license files are **identical**.
- The DESCRIPTION.en_us.html files differ only in HTML formatting (whitespace/tag structure), not in textual content.
- The METADATA.json in the upstream repo matches the METADATA.pb in google/fonts (same designer "Onur Yazicigil", same copyright, same date_added "2011-12-19").
- The `src/METADATA_comments.txt` in the upstream repo references `~/googlefontdirectory/ofl/durusans/`, confirming this project originates from the Google Font Directory (the predecessor of google/fonts hosted on Google Code).

The GitHub URL returns HTTP 200, confirming the repository is publicly accessible.

## How the Commit Hash Was Identified

The upstream repository contains exactly **one commit**:

```
2895eb6c9842f80c1e01bbf9fbb6231eaef66724 - "update .travis.yml" by hash3g, 2014-10-17
```

Since there is only one commit in the entire repository, this is necessarily the commit that represents the state of all source files. The commit message says "update .travis.yml" but it is actually the initial commit (squashed or force-pushed), containing all 39 files including the source files, TTX decompositions, FONTLOG, and license.

In google/fonts, the TTF file `DuruSans-Regular.ttf` was added in the initial commit (`90abd17b4`, March 7, 2015 by Dave Crossland) and has never been updated since. The font was originally added to Google Fonts on 2011-12-19 (per METADATA.pb `date_added`), predating the librefonts GitHub repository (Oct 2014). The librefonts repo is a post-hoc archival copy of the original Google Font Directory sources, not the original development repository.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files available are:

- `src/DuruSans-Regular.vfb` - FontLab VFB format (original source with contour overlaps)
- `src/DuruSans-Regular-OTF.sfd` - FontForge SFD for OTF (binary, merged contours)
- `src/DuruSans-Regular-TTF.sfd` - FontForge SFD for TTF (with hinting adjustments)
- Root directory contains decomposed TTX files for the TTF

These are **legacy formats** (VFB, SFD, TTX) that are **not compatible with gftools-builder**. The gftools-builder tool requires `.glyphs`, `.glyphx`, `.ufo`, or `.designspace` source formats. Therefore:

- No config.yaml can be created as an override
- The sources cannot be built with the modern gftools-builder pipeline
- This font would require source conversion before it could use gftools-builder

The `.travis.yml` in the repo uses the old `fontbakery-build.py` tool from 2014, which is a defunct build system.

## Verification

- [x] Repository URL returns HTTP 200
- [x] Repository is clean (no local modifications)
- [x] Repository is on branch `master`, up to date with `origin/master`
- [x] Only one branch exists (`master`)
- [x] FONTLOG.txt files are identical between google/fonts and upstream
- [x] OFL.txt files are identical between google/fonts and upstream
- [x] Copyright in upstream METADATA.json matches google/fonts METADATA.pb
- [x] Font was added to Google Fonts on 2011-12-19, upstream repo created Oct 2014 (archival copy)
- [x] Font has never been updated in google/fonts since initial commit

## Confidence

**HIGH** for repository_url and commit_hash identification. The librefonts/durusans repo is clearly the archival source repository for this font, with matching metadata, license, and supporting files. There is only one commit, so the hash is unambiguous.

**N/A** for config_yaml. The sources are in legacy formats (VFB/SFD) incompatible with gftools-builder. No config.yaml can be meaningfully created without first converting the sources to a modern format.

# Caesar Dressing - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Caesar Dressing |
| Designer | Open Window |
| License | OFL |
| Date Added | 2011-12-19 |
| Repository URL | https://github.com/librefonts/caesardressing |
| Commit Hash | fb212a606bc3f65a2b3d210c88e938f6090cff15 |
| Config YAML | None |
| Status | missing_config |

## How URL Was Found

The repository URL `https://github.com/librefonts/caesardressing` was added as part of the bulk source block addition in commit `9a14639f3` (2026-02-25). The librefonts GitHub organization hosts archived copies of many early Google Fonts projects. This is a standard librefonts archive repository containing TTX decompositions and metadata.

## How Commit Was Determined

The commit hash `fb212a606bc3f65a2b3d210c88e938f6090cff15` is the only commit in the repository (and therefore HEAD). It was made on 2014-10-17 with the message "update .travis.yml". This is a single-commit archive repository.

Caesar Dressing was part of the initial commit (`90abd17b4`) in the google/fonts repository, meaning it was one of the earliest families added to Google Fonts. The librefonts repository is an archive of the original source material, not an active development repository.

## Config YAML Status

**No config.yaml exists** in the upstream repository and none is expected. The repository contains only:
- `src/CaesarDressing-Regular-TTF.vfb` (FontLab format) - This is a legacy format not supported by gftools-builder.
- TTX decompositions of the font in the root directory.
- Standard metadata files (DESCRIPTION, FONTLOG, OFL, METADATA.json).

There is no override `config.yaml` in the google/fonts family directory either.

This family cannot be built with gftools-builder because the only source is in VFB (FontLab) format, which is not a supported input format. The font would need to be converted to Glyphs, UFO, or Designspace format before a config.yaml could be useful.

## Verification

- **Repository URL**: Valid. The librefonts/caesardressing repository exists and is accessible.
- **Commit Hash**: Verified. The hash `fb212a606bc3f65a2b3d210c88e938f6090cff15` is the sole commit in the repository.
- **Source Files**: VFB format only (legacy, not gftools-buildable).
- **Font Origin**: This is a very early Google Fonts family (initial commit). The librefonts repo is an archive, not the original development repository.

## Confidence Level

**HIGH** for the repository URL and commit hash. The librefonts repo is a well-known archive of early Google Fonts sources. Since there is only one commit, there is no ambiguity about the commit hash.

**Note**: This family is effectively "complete" in terms of source documentation, but cannot be made gftools-buildable without converting the VFB sources to a modern format.

## Open Questions

1. Is there any plan to convert the VFB sources to a modern format (Glyphs/UFO) for this family?
2. The designer "Open Window" (Dathan Boardman, dathanboardman@gmail.com per the copyright string) may have the original editable sources in a different format.

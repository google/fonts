# Cagliostro - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cagliostro |
| Designer | MADType |
| License | OFL |
| Date Added | 2011-11-30 |
| Repository URL | https://github.com/librefonts/cagliostro |
| Commit Hash | 5c0de59bedd45c878edfeeeb31e2105f987e7270 |
| Config YAML | None |
| Status | missing_config |

## How URL Was Found

The repository URL `https://github.com/librefonts/cagliostro` was added as part of the bulk source block addition in commit `9a14639f3` (2026-02-25). The librefonts GitHub organization hosts archived copies of many early Google Fonts projects. This is a standard librefonts archive repository.

## How Commit Was Determined

The commit hash `5c0de59bedd45c878edfeeeb31e2105f987e7270` is the only commit in the repository (and therefore HEAD). It was made on 2014-10-17 with the message "update .travis.yml". This is a single-commit archive repository.

Cagliostro was part of the initial commit (`90abd17b4`) in the google/fonts repository, making it one of the earliest families in the collection. The librefonts repository is an archive, not an active development repository.

## Config YAML Status

**No config.yaml exists** in the upstream repository and none is expected. The repository contains:
- `src/Cagliostro-Regular-TTF.sfd` (FontForge SFD format) - This is a legacy format not supported by gftools-builder.
- `src/Cagliostro-Regular.vfb` (FontLab format) - Also a legacy format not supported by gftools-builder.
- TTX decompositions of the OTF font in the root directory and src directory.
- Standard metadata files (DESCRIPTION, FONTLOG, OFL, METADATA.json).

There is no override `config.yaml` in the google/fonts family directory either.

This family cannot be built with gftools-builder because the only sources are in SFD (FontForge) and VFB (FontLab) formats, neither of which is a supported input format.

## Verification

- **Repository URL**: Valid. The librefonts/cagliostro repository exists and is accessible.
- **Commit Hash**: Verified. The hash `5c0de59bedd45c878edfeeeb31e2105f987e7270` is the sole commit in the repository.
- **Source Files**: SFD and VFB formats only (legacy, not gftools-buildable).
- **Font Origin**: This is a very early Google Fonts family (initial commit). The librefonts repo is an archive.

## Confidence Level

**HIGH** for the repository URL and commit hash. The librefonts repo is a well-known archive with only one commit, so there is no ambiguity.

**Note**: The designer is listed as "MADType" (Matthew Desmond, mattdesmond@gmail.com per the copyright string, http://www.madtype.com).

## Open Questions

1. Is there any plan to convert the SFD/VFB sources to a modern format (Glyphs/UFO) for this family?
2. The original designer Matthew Desmond (MADType) may have more recent source files.

# Merriweather Sans — Source Metadata Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-12

## Repository

- **URL**: https://github.com/SorkinType/Merriweather-Sans
- **Commit**: `bb6bd99bf9eb756723f2428629659a638702d335`
- **Commit date**: 2020-08-22
- **Commit message**: Merge branch 'master' of https://github.com/SorkinType/Merriweather-Sans
- **Author**: Eben Sorkin

## Source Files

The repository contains UFO sources and designspace files in the `sources/` directory:

- `MerriweatherSans.designspace` (Roman)
- `MerriweatherSans-Italic.designspace` (Italic)
- `MerriweatherSans-Light.ufo`
- `MerriweatherSans-Regular.ufo`
- `MerriweatherSans-ExtraBold.ufo`
- `MerriweatherSans-LightItalic.ufo`
- `MerriweatherSans-Italic.ufo`
- `MerriweatherSans-ExtraBoldItalic.ufo`

## Build System

- **Build script**: `sources/build.sh` using `fontmake` to build variable and static fonts
- **Build tool**: fontmake (designspace to variable TTF)
- **Post-processing**: gftools fix-dsig, fix-nonhinting, fix-vf-meta; MVAR table dropped via ttx

## Config

A `config.yaml` already exists in the google/fonts directory specifying the two designspace sources:

```yaml
sources:
  - sources/MerriweatherSans.designspace
  - sources/MerriweatherSans-Italic.designspace
```

No changes needed to config.yaml.

## Verification

- Font files in google/fonts are **byte-identical** to the pre-built variable fonts in the upstream repo's `fonts/variable/` directory (MD5 checksums match for both Roman and Italic).
- This confirms the fonts were taken directly from commit `bb6bd99bf9eb756723f2428629659a638702d335`.

## Confidence

**High** — Font binaries match exactly between google/fonts and the upstream repository at the identified commit.

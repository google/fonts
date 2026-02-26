# Clicker Script - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Clicker Script |
| Designer | Astigmatic |
| Repository URL | https://github.com/librefonts/clickerscript |
| Commit Hash | `f8f050697a52a8e2e10009db97c1a18b0099bb6f` |
| Config YAML | None (no buildable sources) |
| Status | Missing Config (no buildable sources) |
| Date Added | 2012-11-11 |

## How URL Found

The repository URL `https://github.com/librefonts/clickerscript` was already documented in the source block of METADATA.pb. The `librefonts` organization on GitHub hosts many Google Fonts families that were originally contributed as part of the open-source font initiative.

## How Commit Determined

The commit `f8f0506` ("update .travis.yml") is the only commit in the repository (single-commit repo). The source block was added as part of a batch commit (`9a14639f3` "Add source blocks to 602 more METADATA.pb files") that documented repository URLs and commit hashes for families without config.yaml.

## Config YAML Status

- **No config.yaml in upstream**: Not applicable -- the repository does not contain any modern buildable source files.
- **No override config.yaml**: There is no override config.yaml in `ofl/clickerscript/` in google/fonts.

Available source files at the recorded commit:
- `src/ClickerScript-Regular.vfb` (FontLab VFB format)
- `src/ClickerScript-Regular-OTF.vfb` (FontLab VFB format)
- `src/ClickerScript-Regular-TTF.vfb` (FontLab VFB format)
- Multiple `.ttx` files (XML font table dumps)

The VFB format is proprietary to FontLab and cannot be used with gftools-builder/fontmake. There are no `.glyphs`, `.ufo`, or `.designspace` files available for modern font building.

## Verification

- Commit hash `f8f0506` verified to exist in upstream repo (it is the only commit)
- Repository contains only legacy FontLab VFB sources and TTX dumps
- No modern buildable sources exist anywhere in the repo
- The font in google/fonts is a static single-weight Regular font

## Confidence Level

**High** - The repository URL and commit hash are verified. The status of "missing_config" is correct because no config.yaml can be created for legacy VFB sources.

## Open Questions

- To rebuild this font with modern tools, the VFB sources would need to be converted to UFO or Glyphs format. This is outside the scope of source documentation.

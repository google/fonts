# Days One - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Days One |
| Designer | Jovanny Lemonad |
| Repository URL | https://github.com/librefonts/daysone |
| Commit Hash | `76642af05e1a7734f94e1b22abdbc37b6bfb933c` |
| Branch | master |
| Config YAML | None (no gftools-builder compatible sources) |
| Status | missing_config |
| Date Added | 2011-08-17 |

## How URL Found

The repository URL `https://github.com/librefonts/daysone` is a librefonts archive repository. These repos were created by the Google Fonts team (hash3g) as archives of the font source files in TTX/SFD/VFB format.

## How Commit Determined

The upstream repository has only a single commit: `76642af05e1a7734f94e1b22abdbc37b6bfb933c` (hash3g, Oct 17 2014, "update .travis.yml"). This is the only commit and therefore the HEAD of the master branch. The font binary in google/fonts has not been updated since the initial commit (90abd17b4).

## Config YAML Status

- **No config.yaml in upstream**: The upstream repository does not contain a config.yaml file
- **No override config.yaml in google/fonts**: None exists
- **Source files are not gftools-builder compatible**: The upstream contains:
  - `src/DaysOne-Regular-TTF.sfd` (FontForge SFD format)
  - `src/DaysOne-Regular.vfb` (FontLab VFB format)
  - Various TTX decompositions
- These source formats (SFD, VFB) are not supported by gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` files
- **No source block in METADATA.pb**: The current METADATA.pb has no `source { }` block

## Verification

- Repository URL is valid and accessible: https://github.com/librefonts/daysone
- Commit `76642af` is the only commit in the repo and matches HEAD
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/librefonts/daysone/`
- This is a legacy font (added 2011-08-17) that predates gftools-builder infrastructure

## Confidence Level

**HIGH** for URL and commit. The librefonts archive is the only known upstream. The commit is trivially correct as there is only one commit.

**N/A** for config_yaml - there is no gftools-builder compatible source, so no config.yaml can be created without converting the sources first.

## Open Questions

- Would this font benefit from source conversion (SFD to .glyphs or .ufo) to enable gftools-builder compatibility?
- The librefonts archive is a secondary source; the original designer (Jovanny Lemonad) may have the original source files in a different format.

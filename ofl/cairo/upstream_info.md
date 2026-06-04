# Cairo - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cairo |
| Designer | Mohamed Gaber, Accademia di Belle Arti di Urbino |
| License | OFL |
| Date Added | 2019-03-21 |
| Repository URL | https://github.com/Gue3bara/Cairo |
| Commit Hash | 73d16933c6a0f341c27a69e401da83dcb0d53114 |
| Config YAML | sources/cairo.yaml |
| Branch | master |
| Status | complete |

## How URL Was Found

The repository URL `https://github.com/Gue3bara/Cairo` has been present in the METADATA.pb source block since at least the v3.120 update. "Gue3bara" is Mohamed Gaber's GitHub username. The URL is referenced consistently across multiple PRs and commits in google/fonts.

## How Commit Was Determined

The commit hash `73d16933c6a0f341c27a69e401da83dcb0d53114` was set by gftools-packager in the google/fonts commit `d2528f6d1` (2023-03-08) as part of PR #5971. The packager commit message explicitly states:

> Cairo Version 3.130;gftools[0.9.24] taken from the upstream repo https://github.com/Gue3bara/Cairo at commit https://github.com/Gue3bara/Cairo/commit/73d16933c6a0f341c27a69e401da83dcb0d53114.

In the upstream repo, this commit is "Merge pull request #94 from yanone/master" dated 2023-03-06. This is confirmed to be HEAD of the master branch. The timeline is consistent:

1. Yanone submitted PR #94 to the upstream Cairo repo
2. Mohamed Gaber merged it on 2023-03-06
3. Yanone submitted PR #5971 to google/fonts on 2023-03-08, updating the font to v3.130

The previous version (v3.120, PR #5328) referenced commit `f596f41991bc01d5865cdfb9fd751b8de04b6753`.

## Config YAML Status

**config.yaml exists** at `sources/cairo.yaml` in the upstream repository. It is a valid gftools-builder configuration.

Key settings from the config:
- Source: `CairoNormal.glyphs` (Glyphs format)
- Variable font build only (no static builds)
- TTF output only (no OTF or webfont)
- Output directory: `../fonts/Cairo`
- Axis order: slnt, wght
- Family name: "Cairo"
- STAT table configuration included for the slant and weight axes

The repo also contains `sources/cairoplay.yaml` for the Cairo Play variant and the main Glyphs source at `sources/Cairo.glyphs`.

## Verification

- **Repository URL**: Valid. The Gue3bara/Cairo repository exists and is accessible.
- **Commit Hash**: Verified. The hash `73d16933c6a0f341c27a69e401da83dcb0d53114` exists in the repo and is HEAD.
- **Config YAML**: Verified. `sources/cairo.yaml` exists at the recorded commit with valid gftools-builder configuration.
- **Font Files**: The METADATA.pb references `fonts/Cairo/variable/Cairo[slnt,wght].ttf` as the source file mapping, consistent with the config.yaml output directory.
- **gftools-packager**: The commit hash was set automatically by gftools-packager, providing strong confidence in accuracy.
- **PR Cross-reference**: PR #5971 by Yanone confirms the v3.130 update from the exact commit.

## Confidence Level

**HIGH** - All data is verified and consistent. The commit hash was set by gftools-packager with an explicit reference in the commit message. The config.yaml is present and valid. No further work needed.

## Open Questions

None. This family is fully documented and verified.

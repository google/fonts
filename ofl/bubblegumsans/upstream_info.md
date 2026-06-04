# Bubblegum Sans

**Date investigated**: 2026-02-26
**Status**: missing_config (SFD-only sources)
**Designer**: Sudtipos
**METADATA.pb path**: `ofl/bubblegumsans/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/bubblegumsans |
| Commit | `fcf8bdd5e83b65186641b2b67fd957ff061666e3` |
| Config YAML | N/A (SFD-only sources, not gftools-builder compatible) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/bubblegumsans` was identified from the `librefonts` organization, which hosts archived Google Fonts sources in a standardized structure. This was not added by gftools-packager but rather by the batch source block addition in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25). The METADATA.pb had no source block prior to this.

## How the Commit Hash Was Identified

The commit `fcf8bdd5e83b65186641b2b67fd957ff061666e3` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). This is a single-commit archive repository under the `librefonts` organization. Since there is only one commit, identification is unambiguous.

The font was originally added to google/fonts in the initial commit `90abd17b4` and last had its binary updated in commit `75e7dd823` ("Updating ofl/bubblegumsans/*ttf with nbspace and fsType fixes", 2015-04-27 by Dave Crossland). These updates were done directly in the google/fonts repo, not via gftools-packager from the upstream repo. The librefonts repo serves as an archive of the original source files.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are:
- `src/BubblegumSans-Regular-TTF.sfd` (FontForge SFD format)
- `src/BubblegumSans-Regular-OTF.vfb` (FontLab VFB format)

These are legacy source formats that are not compatible with gftools-builder, which requires `.glyphs`, `.ufo`, or `.designspace` sources. No override config.yaml exists in the google/fonts family directory either.

The font has not been rebuilt from sources using modern tooling. The binary in google/fonts was originally added and later patched directly.

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2014-10-17 13:31:31 +0300
- Commit message: "update .travis.yml"
- Commit author: hash3g
- Source files at commit: `src/BubblegumSans-Regular-TTF.sfd`, `src/BubblegumSans-Regular-OTF.vfb`
- Config YAML: Does not exist
- No gftools-packager history: Font was added before the packager workflow existed

## Confidence

**Medium**: The repository URL is correct for the librefonts archive. The commit hash is trivially correct (only one commit). However, the relationship between the upstream repo and the binary in google/fonts is weak -- the font binary was likely compiled outside of this repo and the repo serves primarily as an archive of source files and TTX dumps. The font cannot be rebuilt with gftools-builder from these sources.

## Open Questions

1. The font sources are in SFD/VFB format only. To enable rebuilding with gftools-builder, the sources would need to be converted to `.glyphs` or `.ufo` format and a new upstream repo or config.yaml created. This is a low priority for a single-weight static font that has not been updated since 2015.

# Cambo - Investigation Report

## Source Data

| Field | Value |
|---|---|
| Family Name | Cambo |
| Designer | Huerta Tipografica |
| License | OFL |
| Date Added | 2011-12-19 |
| Repository URL | https://github.com/librefonts/cambo |
| Commit Hash | 3b97d12b34a587e8868700ffa711df7dc6aa0d04 |
| Branch | master |
| Config YAML | N/A |
| Status | missing_config |

## How URL Found

The repository URL `https://github.com/librefonts/cambo` was added as part of a batch source blocks commit (9a14639f3, "Add source blocks to 602 more METADATA.pb files"). The librefonts organization on GitHub hosts mirrors of many Google Fonts projects. The METADATA.pb in google/fonts previously had no source block.

Note that the original designer is Huerta Tipografica, but no repo was found at `huertatipografica/cambo` on GitHub. The librefonts mirror is the only known upstream repository.

## How Commit Determined

The commit `3b97d12b34a587e8868700ffa711df7dc6aa0d04` is the HEAD (and only commit) of the librefonts/cambo repository, dated 2014-10-17. The commit message is "update .travis.yml". This is a single-commit repo that mirrors the original sources.

The font binary in google/fonts was last updated in commit d4b4f127f (2015-04-27, "Updating ofl/cambo/*ttf with nbspace and fsType fixes" by Dave Crossland), which was a metadata fix, not a rebuild from sources. The initial font was added in commit 90abd17b4 ("Initial commit").

Since the librefonts repo has only one commit, the recorded hash is the only valid option and represents the complete state of the upstream mirror.

## Config YAML Status

No `config.yaml` exists in the upstream repository. No override `config.yaml` exists in google/fonts either.

The upstream repo contains only FontForge SFD sources (`src/Cambo-Regular-TTF.sfd`) and VFB files (`src/Cambo-Regular-OTF.vfb`, `src/Cambo-Regular.vfb`). These are not gftools-builder compatible formats. A config.yaml for SFD sources could theoretically be created, but SFD building support in gftools-builder is limited.

## Verification

- **Commit hash verified**: The hash `3b97d12` exists in the librefonts/cambo repository and is HEAD of master. CONFIRMED.
- **Repository accessible**: librefonts/cambo is a valid GitHub repository. CONFIRMED.
- **Source files**: Only SFD and VFB formats available, no .glyphs/.ufo/.designspace sources.
- **Single-commit repo**: Only one commit in the entire history (2014-10-17).

## Confidence Level

**HIGH** - The repository URL and commit hash are correct. The librefonts mirror is the only known upstream. The font was originally added to Google Fonts in 2011 and has not been rebuilt from sources since.

## Open Questions

- The original designer (Huerta Tipografica) may have source files in other formats (e.g., .glyphs) that are not publicly available.
- No path to gftools-builder compatibility without source conversion from SFD/VFB format.

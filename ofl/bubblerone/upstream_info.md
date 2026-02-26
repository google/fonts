# Bubbler One

**Date investigated**: 2026-02-26
**Status**: missing_config (SFD-only sources)
**Designer**: Brenda Gallo
**METADATA.pb path**: `ofl/bubblerone/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/bubblerone |
| Commit | `be2343608e5751bca73956b02860a1758e1e29a7` |
| Config YAML | N/A (SFD-only sources, not gftools-builder compatible) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/bubblerone` was identified from the `librefonts` organization, which hosts archived Google Fonts sources. This was added by the batch source block addition in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25). The METADATA.pb had no source block prior to this.

## How the Commit Hash Was Identified

The commit `be2343608e5751bca73956b02860a1758e1e29a7` is the **only commit** in the repository (message: "update .travis.yml", by hash3g, 2014-10-17). This is a single-commit archive repository under the `librefonts` organization. Since there is only one commit, identification is unambiguous.

The font has a richer update history in google/fonts compared to many librefonts families:
1. Initial commit `90abd17b4` (2012)
2. Hotfix PR #867 (`70a30639c`, "hotfix-bubblerone: v1.002 added")
3. Compliance fixes (`011460f75`, "Several hotfixes to bring font into compliance (mainly vertical metrics)")
4. Version bump (`078516296`, "Bumped version")

These updates were done directly in the google/fonts repo, not by pulling from the librefonts archive. The librefonts repo contains the original source files only.

## How Config YAML Was Resolved

No `config.yaml` exists in the upstream repository. The source files are:
- `src/BubblerOne-Regular-TTF.sfd` (FontForge SFD format)

This is a legacy source format not compatible with gftools-builder. The repo also contains extensive TTX dumps of the compiled font tables. No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2014-10-17 13:31:34 +0300
- Commit message: "update .travis.yml"
- Commit author: hash3g
- Source files at commit: `src/BubblerOne-Regular-TTF.sfd`
- Config YAML: Does not exist
- No gftools-packager history: Font updates were done directly in google/fonts

## Confidence

**Medium**: The repository URL is correct for the librefonts archive. The commit hash is trivially correct (only one commit). However, the font binary in google/fonts was updated multiple times after the librefonts archive was created, so the compiled font does NOT correspond to these source files. The font cannot be rebuilt with gftools-builder from these sources.

## Open Questions

1. The font binary in google/fonts has been updated several times (hotfixes, version bumps) after the librefonts archive was created. The SFD source in the archive likely does not correspond to the current binary. To enable rebuilding, the sources would need to be converted to modern formats.
2. The hotfix in PR #867 and subsequent updates suggest the font was modified directly at the binary level or from sources not present in the librefonts repo.

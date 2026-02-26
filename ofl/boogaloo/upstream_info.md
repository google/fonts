# Boogaloo

**Date investigated**: 2026-02-26
**Status**: missing_config
**Designer**: John Vargas Beltran
**METADATA.pb path**: `ofl/boogaloo/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/librefonts/boogaloo |
| Commit | `9837380f883a9af75b9d4a9767020c1b1abc771a` |
| Config YAML | N/A (SFD-only sources, not gftools-builder compatible) |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/librefonts/boogaloo` was added to the METADATA.pb source block in commit `9a14639f3` ("Add source blocks to 602 more METADATA.pb files", 2026-02-25) by Felipe Sanches. The `librefonts` GitHub organization hosts many libre/open font projects including Boogaloo.

## How the Commit Hash Was Identified

The commit hash `9837380f883a9af75b9d4a9767020c1b1abc771a` was added in the same batch commit `9a14639f3` (2026-02-25). This commit ("update .travis.yml") is the latest commit (HEAD) in the upstream repository.

The font was last updated in google/fonts via PR #863 ("hotfix-boogaloo: v1.002 added") by Marc Foley (2017-08-07). The PR body was empty, providing no specific upstream commit reference. Given that the upstream repo contains only legacy sources (SFD format), the HEAD commit is the most reasonable reference point.

The METADATA.pb does not have a full `source { }` block with files/branch/config_yaml -- only the repository_url and commit hash were added.

## How Config YAML Was Resolved

There is no `config.yaml` in the upstream repository and none is expected. The upstream contains only legacy FontForge source files:

- `src/Boogaloo-Regular-TTF.sfd` (FontForge SFD format)
- Various TTX table dumps at the repo root

SFD sources are not compatible with gftools-builder, so no config.yaml can be created. There is also no override config.yaml in the google/fonts family directory (`ofl/boogaloo/`).

The METADATA.pb currently has no `source { }` block with `config_yaml` -- only a bare source block with `repository_url` and `commit`.

## Verification

- Commit exists in upstream repo: Yes (HEAD of master)
- Commit message: "update .travis.yml"
- Source files at commit: `src/Boogaloo-Regular-TTF.sfd` (FontForge format)
- No config.yaml in upstream repo: Confirmed
- No override config.yaml in google/fonts: Confirmed
- Source type: SFD only (not gftools-builder compatible)

## Confidence

**High**: The repository URL is well-established under the `librefonts` organization. The commit hash is HEAD of the repo, which is appropriate for a legacy font with SFD-only sources. The lack of config.yaml is expected and correctly documented as `missing_config` status.

## Open Questions

1. Could the SFD source be converted to a modern format (UFO or Glyphs) to enable gftools-builder compilation in the future? This would require creating an override config.yaml in google/fonts.

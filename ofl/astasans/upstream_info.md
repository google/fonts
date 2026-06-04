# Asta Sans

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: complete
- **Designer**: 42dot

## Source Data

| Field            | Value                                                              |
|------------------|--------------------------------------------------------------------|
| repository_url   | https://github.com/42dot/Asta-Sans                                 |
| commit           | 62b8301ac4b2e2ddf62eadca79b91fa944618848                           |
| branch           | main                                                               |
| config_yaml      | sources/config_variable.yaml                                       |

## Background

Asta Sans was originally onboarded to Google Fonts as "42dot Sans" on 2024-12-23 from the upstream repository `https://github.com/42dot/42dot-Sans`. The original onboarding commit in the upstream repo was `d23e87fe` ("Adding some metadata"), as documented in the google/fonts commit message:

> "Taken from the upstream repo https://github.com/42dot/42dot-Sans at commit https://github.com/42dot/42dot-Sans/commit/d23e87fe44d5b4f5afaa9dca9d5926d7c414d625"

In April 2025, the font was renamed from "42dot Sans" to "Asta Sans". The upstream GitHub repository was also renamed from `42dot/42dot-Sans` to `42dot/Asta-Sans`. The rename was performed in upstream commit `52c07071` ("name update 42dot Sans -> Asta Sans", 2025-04-22), which renamed all source files, font binaries, and config references from 42dotSans to AstaSans.

In google/fonts, the rename was performed in commit `db261113` ("Rename font family from 42dotSans to AstaSans", 2025-04-30) by Sandoll-DS. This commit moved the family from `ofl/42dotsans/` to `ofl/astasans/`, updated all names and references, and updated the source block to point to the renamed repo with the new commit hash.

## How URL Found

The `repository_url` was established during the original onboarding of 42dot Sans (commit `d60948ac` in google/fonts, 2024-12-23). The URL was updated from `https://github.com/42dot/42dot-Sans` to `https://github.com/42dot/Asta-Sans` during the rename commit `db261113`. GitHub automatically redirects the old URL to the new one, so both are valid, but the current URL correctly reflects the renamed repository.

## How Commit Identified

The current METADATA.pb references commit `62b8301ac4b2e2ddf62eadca79b91fa944618848`, which is a merge commit dated 2025-04-29 ("Merge pull request #6 from Sandoll-DS/patch-1 - Update config_variable.yaml"). This commit updated `sources/config_variable.yaml` to reference the renamed source files (`AstaSans.designspace` and `familyName: Asta Sans`).

This is appropriate because it is the commit that was used for the font rename in google/fonts. The rename commit `db261113` in google/fonts is dated 2025-04-30, just one day after the upstream merge. The binary font in google/fonts was rebuilt from sources at this commit (the .ttf file changed slightly between the old and new versions).

Note: The original onboarding commit was `d23e87fe` (previously recorded in the 42dot Sans source block, added in google/fonts commit `da0442cc` as part of PR #8772). The commit was correctly updated to `62b8301a` during the rename since the sources themselves were updated.

Also note: The upstream `origin/main` has one additional commit ahead (`69ecccd5` - "Merge pull request #5 - Update config_static.yaml"), which only modifies `config_static.yaml` (the static build config). Since google/fonts uses the variable build config, this newer commit is irrelevant to the current build.

## How Config Resolved

The config file `sources/config_variable.yaml` exists at the referenced commit `62b8301a` with the following content:

```yaml
sources:
  - AstaSans.designspace
familyName: Asta Sans
autohintTTF: False
buildOTF: False
buildStatic: False
buildVariable: True
buildWebfont: False
removeOutlineOverlaps: False
```

This is a standard gftools-builder configuration that builds a variable font from `AstaSans.designspace`. The source file `AstaSans.designspace` and the companion `AstaSans.glyphspackage` both exist at this commit. No override config.yaml is needed or present in the google/fonts family directory.

## Conclusion

The source block in METADATA.pb is complete and correct. The repository URL points to the renamed upstream repo. The commit hash `62b8301a` correctly reflects the state of the upstream repo used for the rename/rebuild in google/fonts. The config path `sources/config_variable.yaml` points to a valid gftools-builder config at that commit. No changes are needed.

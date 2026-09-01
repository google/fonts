# Catamaran

**Date investigated**: 2026-02-26
**Status**: missing_config (also has incorrect repository_url and commit hash)
**Designer**: Pria Ravichandran
**METADATA.pb path**: `ofl/catamaran/METADATA.pb`

## Source Data

### Current (in METADATA.pb)

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/VanillaandCream/Catamaran-Tamil |
| Commit | `7559b4906f9c9148fb22c6f89508c3053a78a296` |
| Config YAML | Missing |
| Branch | (not specified) |

### Correct (based on investigation)

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/Catamaran-Tamil |
| Commit | `375341acd5ac02e8ed1c942cf33fd3fa3ebdc62e` |
| Config YAML | Missing (needs override) |
| Branch | (not specified) |

## How the Repository URL Was Found

The current METADATA.pb has `repository_url: "https://github.com/VanillaandCream/Catamaran-Tamil"`. This was set by Simon Cozens in commit `f7455d788` (2023-08-15, "Populate source.repository_url"). However, this is the **original** upstream repo by the designer Pria Ravichandran, which only contains the v1.x static fonts built from Glyphs sources.

The current fonts in google/fonts are **v2.000** (variable font), added via PR #2547 by Marc Foley on 2020-07-15. The PR commit (`cf5f21315`) explicitly states: "Taken from the upstream repo https://github.com/TypeNetwork/Catamaran-Tamil at commit https://github.com/TypeNetwork/Catamaran-Tamil/commit/375341acd5ac02e8ed1c942cf33fd3fa3ebdc62e".

The TypeNetwork/Catamaran-Tamil repo has since been renamed/transferred to **googlefonts/Catamaran-Tamil** (GitHub confirms this is a fork of VanillaandCream/Catamaran-Tamil). The correct repository URL for the current fonts is therefore `https://github.com/googlefonts/Catamaran-Tamil`.

## How the Commit Hash Was Identified

The current METADATA.pb commit `7559b4906f9c9148fb22c6f89508c3053a78a296` was added by the batch enrichment commit `9a14639f3` (2026-02-25). This commit is the HEAD (and latest) commit in the VanillaandCream/Catamaran-Tamil repo, with message "u and o umlaut fixed" (2017-06-22). **This is incorrect** -- it corresponds to the v1.x era of the font, not the v2.000 variable font currently in google/fonts.

The correct commit is `375341acd5ac02e8ed1c942cf33fd3fa3ebdc62e`, as stated in PR #2547's commit message. This commit was verified to exist in the googlefonts/Catamaran-Tamil repository via the GitHub API:
- Author: Jill Pichotta
- Date: 2020-07-15
- Message: "New Build\n\nafter /Lcomma fix"

The date of this upstream commit (2020-07-15) matches the date of the google/fonts PR #2547, confirming it is the correct onboarding commit.

## How Config YAML Was Resolved

**No config.yaml exists anywhere.** Neither the VanillaandCream/Catamaran-Tamil repo, the googlefonts/Catamaran-Tamil repo, nor the google/fonts family directory (`ofl/catamaran/`) has a `config.yaml`.

At the correct commit (`375341ac`) in googlefonts/Catamaran-Tamil, the source file is `sources/Catamaran.designspace` along with multiple UFO master sources (Catamaran-Black.ufo, etc.). An override `config.yaml` could be created referencing this designspace file.

## Verification

- Current commit in METADATA.pb (`7559b490`): Exists in VanillaandCream repo, but wrong (v1.x era)
- Correct commit (`375341ac`): Exists in googlefonts/Catamaran-Tamil repo, verified via GitHub API
- Correct commit date: 2020-07-15
- Correct commit message: "New Build / after /Lcomma fix"
- Correct commit author: Jill Pichotta
- Source files at correct commit: `sources/Catamaran.designspace`, multiple UFO masters
- Override config.yaml in google/fonts: No
- Font was originally added to Google Fonts on 2015-07-08 (v1.x), updated to v2.000 on 2020-07-15

## Confidence Level

**HIGH** for the correct repository URL and commit hash -- the PR #2547 commit message explicitly states both, and the commit was verified to exist in the fork repo.

**ACTION REQUIRED** -- Three issues need fixing:
1. Repository URL should be changed from `VanillaandCream/Catamaran-Tamil` to `googlefonts/Catamaran-Tamil`
2. Commit hash should be changed from `7559b490...` to `375341ac...`
3. An override `config.yaml` needs to be created

## Open Questions

- Should the `repository_url` be set to `https://github.com/googlefonts/Catamaran-Tamil` (the current fork) or `https://github.com/TypeNetwork/Catamaran-Tamil` (the historical URL referenced in PR #2547)? The TypeNetwork URL now redirects to googlefonts/Catamaran-Tamil. Using the current googlefonts URL is recommended.
- The VanillaandCream/Catamaran-Tamil repo (the original by the designer) contains only v1.x Glyphs sources. If the intent is to document the original designer's repo, it could be noted, but for the current fonts in google/fonts, the googlefonts fork is the correct upstream.
- An override `config.yaml` should be created with content like:
  ```yaml
  sources:
    - sources/Catamaran.designspace
  ```

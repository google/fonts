# Eczar

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Rosetta, Vaibhav Singh
**METADATA.pb path**: `ofl/eczar/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/rosettatype/eczar |
| Commit | `f248ec9c0c5e3a9442d22824cc1cba6c713725d5` |
| Config YAML | `sources/builder.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/rosettatype/eczar` was already present in the METADATA.pb `source { repository_url }` field. It is also referenced in the copyright string in the font files ("Copyright 2014 The Eczar Project Authors (https://github.com/rosettatype/eczar)") and in the gftools-packager commit body for google/fonts PR #4321.

## How the Commit Hash Was Identified

The commit `f248ec9c0c5e3a9442d22824cc1cba6c713725d5` is explicitly referenced in the gftools-packager commit `597475e6f` in google/fonts, which states: "Eczar Version 2.000 taken from the upstream repo https://github.com/rosettatype/eczar at commit https://github.com/rosettatype/eczar/commit/f248ec9c0c5e3a9442d22824cc1cba6c713725d5."

This commit is the sole commit in the upstream repository. It is a merge commit (PR #26 from yanone/master) dated 2022-02-17, titled "Merge pull request #26 from yanone/master". The PR body explains: "I was commissioned to prepare Eczar for publication on Google Fonts. I removed all the old UFO and .fea files and moved everything into one variable Glyphs source." The PR was authored by Yanone and merged on 2022-02-17.

The google/fonts PR #4321 was created by Yanone on 2022-02-17 and merged by RosaWagner on 2022-02-18. The timeline is consistent: the upstream PR was merged first, then the google/fonts PR was created referencing that commit.

## How Config YAML Was Resolved

The config file `sources/builder.yaml` exists at the referenced commit in the upstream repository. Its contents:

```yaml
sources:
  - Eczar.glyphs
outputDir: "../release"
buildStatic: true
buildVariable: true
buildTTF: false
buildOTF: false
buildWebfont: false
```

No override `config.yaml` exists in the google/fonts family directory (`ofl/eczar/`). The `config_yaml` field was added to METADATA.pb in commit `35e809c6b` ("sources info for Eczar", 2025-04-02).

## Verification

- Commit exists in upstream repo: Yes (it is the only commit)
- Commit date: 2022-02-17 15:35:18 +0100
- Commit message: "Merge pull request #26 from yanone/master"
- Source files at commit: `sources/Eczar.glyphs`, `sources/builder.yaml`
- Binary match: The `Eczar[wght].ttf` in google/fonts is byte-identical to `release/variable/Eczar[wght].ttf` in the upstream repo (MD5: `2d26d338d36619e60fc98e285c3624d2`, 407304 bytes)
- Upstream repo is clean with no local modifications

## History in google/fonts

The font was originally added in the initial commit (`90abd17b4`) with static instances. Notable subsequent updates:
- `597475e6f` (2022-02-18): Version 2.000 added via gftools-packager (PR #4321) -- replaced 5 static TTFs with a single variable font `Eczar[wght].ttf`
- `66f91f10f` (2024-04-03): upstream.yaml merged into METADATA.pb, adding files and branch info
- `35e809c6b` (2025-04-02): `config_yaml` field added to source block

## Confidence

**HIGH**: All metadata is fully verified. The repository URL matches the copyright string and gftools-packager references. The commit hash is the sole commit in the upstream repo and is explicitly cited in the google/fonts onboarding commit body. The binary font file in google/fonts is byte-identical to the one in the upstream repo. The builder.yaml config is present at the referenced commit and correctly referenced in METADATA.pb. No open questions remain.

## Open Questions

None.

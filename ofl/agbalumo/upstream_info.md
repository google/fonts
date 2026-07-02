# Agbalumo

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Raphael Alegbeleleye, Sorkin Type, Eben Sorkin
**METADATA.pb path**: `ofl/agbalumo/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/SorkinType/Agbalumo |
| Commit | `261ad51ef2291821685c1bebf10cf0fb9f7e08f9` |
| Config YAML | `sources/config.yaml` |
| Branch | `main` |

## How the Repository URL Was Found

The repository URL was already present in the METADATA.pb source block. It was established during the initial onboarding (PR #6830, google/fonts commit `6a9a2d7b9`, 2023-10-06) which stated the font was "taken from the upstream repo https://github.com/SorkinType/Agbalumo.git". The copyright field also references this GitHub URL.

## How the Commit Hash Was Identified

The commit hash has gone through three distinct values as the font was updated:

1. **Initial onboarding** (PR #6830, google/fonts commit `6a9a2d7b9`, 2023-10-06): Version 1.000 was taken from upstream commit `c6c381d3704ef794dde69b80489d0cde36fb6f9b`. The PR body initially referenced an even earlier commit `3e64aac2795e538846e6412d444d307f345108ec`.

2. **Batch port from fontc_crater** (google/fonts commit `19cdcec59`, 2025-03-31): The commit was updated from `c6c381d3` to `9d9ec3e32c10533233c9e48835e436ff5e5aa451`, based on fontc_crater's target.json.

3. **Version 2.000 update** (PR #9344, google/fonts commit `dc6afb493`, 2025-06-05): Emma Marichal updated the font to Version 2.000 with ttfautohint, changing the commit to `261ad51ef2291821685c1bebf10cf0fb9f7e08f9`. The commit body explicitly states: "Taken from the upstream repo https://github.com/SorkinType/Agbalumo at commit 261ad51ef2291821685c1bebf10cf0fb9f7e08f9." This added Ethiopic script support (new subset).

The current METADATA.pb commit `261ad51e` is a proper onboarding commit that corresponds to the font binary update, making it the correct reference.

## How Config YAML Was Resolved

The `sources/config.yaml` path was added by the batch port commit `19cdcec59` (2025-03-31) and confirmed during the Version 2.000 update. The config file exists at the recorded commit and specifies:
- Source: `Agbalumo.glyphspackage`
- Family name: Agbalumo
- `buildOTF: false`

No override config.yaml exists in the google/fonts family directory.

## Verification

- Commit exists in upstream repo: Yes (it is HEAD of the shallow clone)
- Commit date: 2025-06-04 11:24:44 -0400
- Commit message: "Merge pull request #27 from emmamarichal/main"
- Source files at commit:
  - `sources/Agbalumo.glyphspackage/` (with fontinfo.plist, many glyph files)
  - `sources/config.yaml`
  - `.github/workflows/build.yaml`

## Confidence

**High**: The repository URL is well-established and confirmed across multiple onboarding events. The current commit hash `261ad51e` is the correct onboarding commit for Version 2.000, directly referenced in the google/fonts commit body by Emma Marichal (2025-06-05). The config.yaml file is verified to exist at this commit in the upstream repo. This is a properly documented, recent update with clear provenance.

## Open Questions

None. This family is well-documented with a clear chain of evidence from the latest font update.

# El Messiri

**Date investigated**: 2026-02-27
**Status**: complete
**Designer**: Mohamed Gaber, Jovanny Lemonad
**METADATA.pb path**: `ofl/elmessiri/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Gue3bara/El-Messiri |
| Commit | `553b98d8e374318694b50862849af666268fd278` |
| Config YAML | `sources/config.yaml` |
| Branch | `master` |

## How the Repository URL Was Found

The repository URL `https://github.com/Gue3bara/El-Messiri` was already present in the METADATA.pb `source { repository_url }` field. It is corroborated by multiple sources:

1. The copyright string in the font: "Copyright 2015 The El Messiri Project Authors (https://github.com/Gue3bara/El-Messiri)"
2. The gftools-packager commit `a1b41d3a8` in google/fonts (PR #3673, 2021-08-06) explicitly states: "El Messiri Version 2.020 taken from the upstream repo https://github.com/Gue3bara/El-Messiri"
3. The `upstream.yaml` file created during onboarding references the same URL
4. The DESCRIPTION.en_us.html links to the same repository

The repository is owned by Mohamed Gaber (GitHub: Gue3bara), the lead designer of the typeface.

## How the Commit Hash Was Identified

The commit hash `553b98d8e374318694b50862849af666268fd278` is explicitly cited in the gftools-packager commit message of PR #3673 (google/fonts commit `a1b41d3a8`, authored by Rosalie Wagner on 2021-08-06): "El Messiri Version 2.020 taken from the upstream repo https://github.com/Gue3bara/El-Messiri at commit https://github.com/Gue3bara/El-Messiri/commit/553b98d8e374318694b50862849af666268fd278."

This commit exists in the upstream repo and is a merge commit: "Merge pull request #23 from eliheuer/gf-bugfix-2021" (Google Fonts bugfixes 2021), dated 2021-08-06 09:52:27 +0200. The google/fonts commit was made the same day (2021-08-06 14:47:22 +0200), confirming the timeline is consistent.

Binary verification confirms the match: the `fonts/variable/ElMessiri[wght].ttf` file at this upstream commit has an identical MD5 checksum (`7fd7b06b35a99518599c32b5f4c9ecb9`) to the file in `ofl/elmessiri/ElMessiri[wght].ttf` in google/fonts. Both files are 138,664 bytes.

This commit is also the latest (and HEAD) commit on the `master` branch. No additional commits have been made to the upstream repo since this onboarding.

## How Config YAML Was Resolved

The config file `sources/config.yaml` exists in the upstream repository at the recorded commit. It contains gftools-builder configuration:

- Source: `ElMessiri.glyphs`
- Axis order: `wght`
- Family name: "El Messiri"
- STAT table definitions for the weight axis (Regular 400, Medium 500, SemiBold 600, Bold 700)

No override `config.yaml` exists in the google/fonts family directory (`ofl/elmessiri/`).

## Verification

- Repository URL accessible: Yes
- Commit exists in upstream repo: Yes
- Commit is HEAD of master: Yes
- Commit date: 2021-08-06 09:52:27 +0200
- Commit message: "Merge pull request #23 from eliheuer/gf-bugfix-2021"
- Binary file match: Yes (identical MD5 checksum, 138,664 bytes)
- Source files at commit: `sources/ElMessiri.glyphs`, `sources/config.yaml`
- Config YAML valid: Yes
- No newer upstream commits: Confirmed

## Confidence

**HIGH**: All metadata fields are fully verified. The repository URL is corroborated by the copyright string, PR history, and upstream.yaml. The commit hash is explicitly cited in the gftools-packager message and verified by identical binary checksums. The config.yaml is present at the recorded path with valid gftools-builder configuration. The referenced commit is the HEAD of master, with no subsequent changes.

## Open Questions

None. All source metadata is complete and verified.

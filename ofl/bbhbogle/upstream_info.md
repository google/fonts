# BBH Bogle

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Studio DRAMA
**METADATA.pb path**: `ofl/bbhbogle/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Studio-DRAMA/BBH |
| Commit | `b8d40ef62b138be4c7c3dac2de117217f261b24b` (not in METADATA.pb; identified through binary matching) |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/Studio-DRAMA/BBH` is recorded in the METADATA.pb `source` block and also in the copyright string. The repository was initially returning 404 during the PR review process (as noted by FontSpector in PR #10033 comments), suggesting it was private at the time of onboarding but has since been made public. The URL is now accessible and correctly cloned in the upstream cache at `upstream_repos/fontc_crater_cache/Studio-DRAMA/BBH`.

## How the Commit Hash Was Identified

The METADATA.pb does **not** contain a `commit` field. The commit was identified through binary matching:

1. The font was added to google/fonts on 2025-11-27 by Emma Marichal in commit `aa551acad` (PR #10033, "Add BBH Bogle (replaces BBH Sans Bogle)").
2. The upstream repo commit `b8d40ef` ("push fonts") was made on 2025-11-26 by Emma Marichal and is the last commit before the google/fonts PR was created on Nov 27.
3. Binary comparison confirms the font at commit `b8d40ef` is **byte-identical** to the one in google/fonts:
   - `fonts/ttf/BBHBogle-Regular.ttf` at `b8d40ef` = 15,656 bytes = identical to `ofl/bbhbogle/BBHBogle-Regular.ttf`
4. Note: this commit was on Emma's fork branch and was merged into the Studio-DRAMA/BBH `main` branch on 2025-12-04 via merge commit `5d71932`. The font file is identical at both commits.

The commit `b8d40ef` is the correct onboarding commit since Emma Marichal (the onboarder) pushed the fonts the day before creating the google/fonts PR.

## How Config YAML Was Resolved

The METADATA.pb specifies `config_yaml: "sources/config.yaml"`, which points to the upstream repo's `sources/config.yaml`. This file exists at commit `b8d40ef` and contains gftools-builder configuration:

```yaml
sources:
  - BBH-Bartle.glyphs
  - BBH-Bogle.glyphs
  - BBH-Hegarty.glyphs
familyName: "BBH Display"
buildVariable: false
buildStatic: true
buildTTF: true
buildOTF: true
autohintTTF: false
autohintOTF: false
includeSourceFixes: true
cleanUp: true
```

No override config.yaml exists in the google/fonts family directory. The `config_yaml` field was added to METADATA.pb in commit `5ddf312e6` ("Add config_yaml enrichment for 82 font families") on 2026-02-20.

## Verification

- Commit exists in upstream repo: Yes (`b8d40ef62b138be4c7c3dac2de117217f261b24b`)
- Commit date: 2025-11-26 14:40:26 +0100
- Commit message: "push fonts"
- Commit author: Emma Marichal <bonjour@emmamarichal.fr>
- Source files at commit: `sources/BBH-Bogle.glyphs`, `sources/BBH-Hegarty.glyphs`, `sources/BBH-Bartle.glyphs`, `sources/config.yaml`
- Binary match: Confirmed identical
- Repository accessible: Yes (was 404 during PR review, now public)

## Confidence

**High**: The commit was identified through exact binary matching of the font file. Emma Marichal both pushed the upstream commit and created the google/fonts PR, making the timeline very clear. The only gap is that the METADATA.pb itself does not contain a `commit` field, but the tracking data correctly records `b8d40ef` as the onboarding commit.

## Open Questions

- The METADATA.pb is missing the `commit` field. A PR to add `commit: "b8d40ef62b138be4c7c3dac2de117217f261b24b"` to the source block would be beneficial.
- The config.yaml `familyName` is set to "BBH Display" which is a shared family name covering Bartle, Bogle, and Hegarty -- this is the expected shared config for a multi-family repo.

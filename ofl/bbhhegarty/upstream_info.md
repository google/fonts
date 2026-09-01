# BBH Hegarty

**Date investigated**: 2026-02-26
**Status**: complete
**Designer**: Studio DRAMA
**METADATA.pb path**: `ofl/bbhhegarty/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/Studio-DRAMA/BBH |
| Commit | `b8d40ef62b138be4c7c3dac2de117217f261b24b` (not in METADATA.pb; identified through binary matching) |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Branch | main |

## How the Repository URL Was Found

The repository URL `https://github.com/Studio-DRAMA/BBH` is recorded in the METADATA.pb `source` block and the copyright string. BBH Hegarty shares the same upstream repository as BBH Bogle and BBH Bartle -- all three are separate font families built from source files in the same repo. The repository was initially returning 404 during the PR review (noted in FontSpector report for PR #10034) but is now publicly accessible.

## How the Commit Hash Was Identified

The METADATA.pb does **not** contain a `commit` field. The commit was identified through binary matching:

1. The font was added to google/fonts on 2025-11-27 by Emma Marichal in commit `d62d7d2a5` (PR #10034, "Add BBH Hegarty (replaces BBH Sans Hegarty)"), created just 12 minutes after the BBH Bogle PR.
2. The upstream repo commit `b8d40ef` ("push fonts") was made on 2025-11-26 by Emma Marichal -- the day before the google/fonts PR.
3. Binary comparison confirms the font at commit `b8d40ef` is **byte-identical** to the one in google/fonts:
   - `fonts/ttf/BBHHegarty-Regular.ttf` at `b8d40ef` = 28,752 bytes = identical to `ofl/bbhhegarty/BBHHegarty-Regular.ttf`
4. This commit was on Emma's fork branch and was merged into Studio-DRAMA/BBH `main` on 2025-12-04 via merge commit `5d71932`.

Both BBH Bogle and BBH Hegarty were onboarded from the same upstream commit `b8d40ef`, which makes sense since they share the same repo and the fonts were all pushed together.

## How Config YAML Was Resolved

The METADATA.pb specifies `config_yaml: "sources/config.yaml"`, pointing to the upstream repo's `sources/config.yaml`. This file exists at commit `b8d40ef` and contains:

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

No override config.yaml exists in the google/fonts family directory. The `config_yaml` field was added to METADATA.pb in commit `5ddf312e6` on 2026-02-20.

## Verification

- Commit exists in upstream repo: Yes (`b8d40ef62b138be4c7c3dac2de117217f261b24b`)
- Commit date: 2025-11-26 14:40:26 +0100
- Commit message: "push fonts"
- Commit author: Emma Marichal <bonjour@emmamarichal.fr>
- Source files at commit: `sources/BBH-Hegarty.glyphs`, `sources/BBH-Bogle.glyphs`, `sources/BBH-Bartle.glyphs`, `sources/config.yaml`
- Binary match: Confirmed identical
- Repository accessible: Yes (was 404 during PR review, now public)

## Confidence

**High**: Exact binary match confirms the commit. Same onboarder (Emma Marichal) for both the upstream commit and the google/fonts PR. The commit `b8d40ef` is shared with BBH Bogle as expected for a multi-family repo.

## Open Questions

- The METADATA.pb is missing the `commit` field. A PR to add `commit: "b8d40ef62b138be4c7c3dac2de117217f261b24b"` to the source block would be beneficial.

# Cute Font

**Date investigated**: 2026-02-26
**Status**: no_upstream_repo
**Designer**: TypoDesign Lab. Inc
**METADATA.pb path**: `ofl/cutefont/METADATA.pb`

## Source Data

| Field | Value |
|-------|-------|
| Repository URL | None |
| Commit | None |
| Config YAML | None |
| Branch | None |

## How the Repository URL Was Found

No repository URL exists in METADATA.pb. There is no `source { }` block at all. The font was added to Google Fonts as part of a batch of Korean fonts in PR #1459 ("korean families r01: added"), authored by Marc Foley (m4rc1e) on 2018-03-13. The PR body states: "Korean Font binaries have been mastered by Aaron Bell, https://www.sajatypeworks.com".

No upstream GitHub repository has been found for this font. Searches on GitHub for "CuteFont" and "TypoDesign Lab" did not reveal a source repository. The font appears to have been delivered as pre-compiled binary files by TypoDesign Lab. Inc, a Korean foundry, and mastered by Aaron Bell.

The copyright string in the font reads: "COPYRIGHT 2004-2017 by TypoDesign Lab. Inc. All rights reserved. Font designed by TypoDesign Lab. Inc." This does not reference any repository URL.

## How the Commit Hash Was Identified

No commit hash exists because there is no known upstream repository. The binary font file was directly submitted in PR #1459 without reference to a source repository.

## How Config YAML Was Resolved

Not applicable. Without an upstream repository, there is no config.yaml. No override config.yaml exists in the google/fonts family directory (`ofl/cutefont/`).

## Verification

- The font directory contains only: `CuteFont-Regular.ttf`, `DESCRIPTION.en_us.html`, `METADATA.pb`, `OFL.txt`
- No source block in METADATA.pb
- Font was added 2018-02-23 (date_added in METADATA.pb)
- PR #1459 was a batch PR adding multiple Korean fonts (Black And White Picture, Black Han Sans, Cute Font, Do Hyeon, Dokdo, East Sea Dokdo, Gaegu, Gamja Flower, and others)
- All Korean fonts in this batch were mastered by Aaron Bell from pre-existing font files

## Confidence

**High**: The font clearly has no known upstream repository. The onboarding was done from pre-compiled binaries provided by TypoDesign Lab. Inc, mastered by Aaron Bell. The `no_upstream_repo` status is correct.

## Open Questions

1. Does TypoDesign Lab. Inc maintain source files anywhere (even privately) that could be made available as an open-source upstream repo? This would require contacting the foundry.

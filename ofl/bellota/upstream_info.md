# Bellota - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Bellota |
| Repository URL | https://github.com/kemie/Bellota-Font |
| Commit Hash | db900d27103a2e9b37b76ef32386fbf9691ecac6 |
| Config YAML | null |
| **Status** | complete |
| Category | DISPLAY |

## How the Repository URL Was Found

The repository URL `https://github.com/kemie/Bellota-Font` is documented in the METADATA.pb `source {}` block and also referenced in the copyright strings of all font files ("Copyright 2019 The Bellota Project Authors (https://github.com/kemie/Bellota-Font)"). The URL was populated via the `f7455d788` commit ("Populate source.repository_url") in google/fonts.

## How the Commit Hash Was Determined

The commit hash `db900d27103a2e9b37b76ef32386fbf9691ecac6` was added as part of the batch source block update (commit `9a14639f3`, "Add source blocks to 602 more METADATA.pb files").

Cross-verification confirms this is the correct commit:

1. The upstream commit `db900d27` is "Merge pull request #5 from yanone/master" ("Updated Bellota to Google Fonts specs"), dated 2020-01-16.
2. The google/fonts onboarding commit `d22365f72` ("Added Bellota and Bellota Text") was authored by Yanone on 2020-01-16 - the exact same date.
3. The google/fonts PR #2309 ("Added Bellota and Bellota Text", by yanone) has the body "Upstream PR is merged." - referring to the upstream PR #5 which is the merge commit `db900d27`.
4. The commit modifies TTF files in the upstream repo, and file sizes match the onboarded versions closely (e.g., Bellota-Bold.ttf: 201076 bytes in upstream vs the same binary added to google/fonts).

## Config YAML Status

**No config.yaml exists** in the upstream repository at any commit. The repo structure at `db900d27` is:

```
FONTLOG.TXT
OFL.txt
authors.txt
build.sh
contributors.txt
otf/
readme.md
src/
  Bellota-Bold.ufo
  Bellota-Light.ufo
  Bellota-Regular.ufo
  Bellota.glyphs
  Bellota_autospace.py
ttf/
webfont/
```

The upstream repo has gftools-buildable sources: `src/Bellota.glyphs` (Glyphs format) and UFO files. However, no config.yaml was ever created, and no override config.yaml exists in the google/fonts family directory either.

**Note**: The upstream repo has been very active since onboarding, with significant development through 2024-2026 (Bellota 5.0, Cyrillic additions, etc.). The current HEAD (`84daec6b`, "Bellota 5.05", 2026-01-09) is far ahead of the onboarded commit.

## Verification

- Commit hash `db900d27` exists in the upstream repo
- The date of the upstream commit (2020-01-16) exactly matches the google/fonts onboarding date
- PR #2309 in google/fonts was created by Yanone, who also created the upstream PR #5
- The upstream repo contains `.glyphs` and `.ufo` source files (confirmed `source_types: ["glyphs", "ufo"]`)
- No config.yaml exists anywhere (not in upstream, not as override in google/fonts)

## Confidence Level

**High** - The commit hash is strongly corroborated by matching dates (2020-01-16 in both repos), the same author (Yanone) for both the upstream PR and google/fonts PR, and the explicit reference in PR #2309 to the upstream PR being merged.


## Override Config YAML

An override `config.yaml` has been added to the google/fonts family directory. Contents:

```yaml
sources:
  - src/Bellota.glyphs
familyName: Bellota
buildVariable: false
```

This override config enables gftools-builder to compile the font from upstream sources.

## Open Questions

1. **Missing config.yaml**: The upstream repo has buildable sources (`src/Bellota.glyphs`) but no config.yaml. An override config.yaml should be created in google/fonts to enable fontc_crater builds. A suitable config would be:
   ```yaml
   buildVariable: false
   sources:
     - src/Bellota.glyphs
   ```
2. **Significant upstream changes**: The upstream repo has been heavily updated since onboarding (Bellota 5.0, Cyrillic support, etc.). The current fonts in Google Fonts are from 2020 and would need a QA review before updating.
3. **Missing commit hash in METADATA.pb**: The METADATA.pb `source {}` block currently only has `repository_url` - the `commit` field should be added.

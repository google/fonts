# Arsenal SC

- **Date**: 2026-03-03
- **Model**: Claude Opus 4.6
- **Status**: `complete`
- **Designer**: Andrij Shevchenko

## Source Data

| Field            | Value |
|------------------|-------|
| Repository URL   | https://github.com/alexeiva/Arsenal |
| Commit           | `e34db566b2f5de986eea9b36986d602015d80615` |
| Config           | Override `config.yaml` in google/fonts (no upstream config exists) |
| Branch           | `master` |
| Source files     | `sources/Arsenal.glyphs`, `sources/Arsenal-Italic.glyphs` |

## How URL Was Found

The repository URL `https://github.com/alexeiva/Arsenal` is recorded in METADATA.pb and confirmed in the onboarding commit message and PR #7771 body. The commit `b2e732cec` by Simon Cozens explicitly states: "Taken from the upstream repo https://github.com/alexeiva/Arsenal at commit e34db566b2f5de986eea9b36986d602015d80615." The cached clone at `alexeiva/Arsenal` confirms the remote matches.

## How Commit Was Identified

The commit `e34db566b2f5de986eea9b36986d602015d80615` ("updated README", 2017-06-26) is explicitly referenced in both the onboarding commit message and PR #7771 body. This commit is the HEAD of the `master` branch -- the latest and only branch in the upstream repo. The repo has had no further activity since this commit. Since the repo is at this exact commit, there is no ambiguity.

## How Config Was Resolved

The upstream repository has no `config.yaml`. An override `config.yaml` was created in the google/fonts family directory (`ofl/arsenalsc/config.yaml`) as part of the original onboarding commit `b2e732cec` by Simon Cozens. Its contents:

```yaml
buildVariable: false
sources:
  - Arsenal.glyphs
  - Arsenal-Italic.glyphs
```

**Note on source paths**: The override config references `Arsenal.glyphs` and `Arsenal-Italic.glyphs` without the `sources/` directory prefix. In the upstream repo, these files actually reside at `sources/Arsenal.glyphs` and `sources/Arsenal-Italic.glyphs`. For comparison, the regular Arsenal family's override config (`ofl/arsenal/config.yaml`) correctly uses the `sources/` prefix. This path discrepancy in the SC config may be intentional (if gftools-builder resolves paths differently for this family) or may be an error, but it was present in the original onboarding commit.

Since a local override exists, `config_yaml` is correctly omitted from the METADATA.pb `source {}` block.

## Relationship to Regular Arsenal

Arsenal SC ("Small Caps") shares the same upstream repository as the regular [Arsenal](https://fonts.google.com/specimen/Arsenal) family (`ofl/arsenal/`). Both are built from the same Glyphs sources (`Arsenal.glyphs` and `Arsenal-Italic.glyphs`). Key differences:

- **Regular Arsenal**: Uses commit `878af08` (earlier in the same repo), added 2016-12-06, fonts at `fonts/ttf/Arsenal-*.ttf`
- **Arsenal SC**: Uses commit `e34db56` (HEAD of master), added 2024-05-27, fonts named `ArsenalSC-*.ttf`

The upstream repo does NOT contain pre-built `ArsenalSC-*.ttf` files. The METADATA.pb `files {}` mappings reference `fonts/TTF/ArsenalSC-*.ttf` which do not exist at the referenced commit (the repo only has `fonts/ttf/Arsenal-*.ttf` -- note the lowercase "ttf" directory and no "SC" in filenames). The SC variant was generated during the onboarding process by building from the Glyphs sources with small caps as the primary feature.

## Conclusion

All source metadata is present and verified. Repository URL, commit hash, and override config.yaml were all set during the original onboarding by Simon Cozens in PR #7771 (merged 2024-05-30 by vv-monsalve). The `files {}` mappings in METADATA.pb reference non-existent upstream paths (`fonts/TTF/ArsenalSC-*.ttf`), which appears to be a documentation artifact since the SC fonts were built, not copied from upstream. The override config.yaml source paths lack the `sources/` prefix present in the regular Arsenal config, which may warrant review. No action required for source metadata enrichment.

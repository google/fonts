# Darumadrop One - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Darumadrop One |
| Designer | Maniackers Design |
| Repository URL | https://github.com/ManiackersDesign/darumadrop |
| Commit Hash | `ddbe82834bdab1ecc24adad09cc122d6e8678a81` |
| Branch | master |
| Config YAML | Override in google/fonts (no config_yaml field needed) |
| Status | complete |
| Date Added | 2020-12-14 |

## How URL Found

The repository URL `https://github.com/ManiackersDesign/darumadrop` is documented in the copyright field of METADATA.pb and was present from the original onboarding PR #2864. The commit message in google/fonts explicitly states: "Daruma Drop One Version 1.000 taken from the upstream repo https://github.com/ManiackersDesign/darumadrop.git".

## How Commit Determined

The font has a complex onboarding history with multiple commit references:

1. **PR #2864 body** references commit `35ecca7fc3a038ea3f910e556a294edb0ddbcf61` (Aaron Bell's "Create OFL.txt" commit)
2. **Merged commit message** (140a3943d) references commit `9d5188a76086b0f011830dc191ee712c15a29d40` (Aaron Bell's "Updating copyright string" commit)
3. **Current METADATA.pb** uses commit `ddbe82834bdab1ecc24adad09cc122d6e8678a81` (the HEAD merge commit)

The discrepancy is explained by the renaming. The original font was "Daruma Drop One" (with spaces), onboarded at commit `9d5188a` or `35ecca7`. Later, PR #4177 renamed it to "Darumadrop One" (no space). This renaming was done by Yanone (Jan Gerner) both in the upstream repo and in google/fonts. The upstream rename was merged as commit `ddbe828` (Merge pull request #4 from yanone/master - "Darumadrop One ready for Google Fonts").

The current METADATA.pb correctly points to `ddbe828` because the renamed font binary (`DarumadropOne-Regular.ttf`) was taken from that commit via the `files` mapping: `source_file: "fonts/ttf/DarumadropOne-Regular.ttf"`.

## Config YAML Status

- **No config.yaml in upstream repo**: The upstream does not have a config.yaml file
- **Override config.yaml exists in google/fonts**: `/ofl/darumadropone/config.yaml` with content:
  ```yaml
  buildVariable: false
  sources:
    - source/DarumadropOne.glyphs
  ```
- The source file `source/DarumadropOne.glyphs` exists at commit `ddbe828`
- Since an override config exists, the `config_yaml` field is correctly omitted from the METADATA.pb source block

## Verification

- Repository URL is valid and accessible: https://github.com/ManiackersDesign/darumadrop
- Commit `ddbe828` exists in the upstream repo and is HEAD (master)
- The METADATA.pb `files` mapping correctly maps `fonts/ttf/DarumadropOne-Regular.ttf` to `DarumadropOne-Regular.ttf`
- The upstream repo is cached at `upstream_repos/fontc_crater_cache/ManiackersDesign/darumadrop/`

## Confidence Level

**HIGH** - All data is well-documented. The commit hash is correct for the renamed version. The override config.yaml correctly points to the .glyphs source.

## Open Questions

None. The investigation is complete.

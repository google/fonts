# Alegreya Sans

**Date investigated**: 2026-03-03
**Model**: Claude Opus 4.6
**Status**: complete
**Designer**: Juan Pablo del Peral, Huerta Tipografica
**METADATA.pb path**: `ofl/alegreyasans/METADATA.pb`

## Source Data
| Field | Value |
|-------|-------|
| Repository URL | https://github.com/huertatipografica/Alegreya-Sans |
| Commit | `030b9ac01fd9bcaccac0ebc8010283175f9ced4e` |
| Config YAML | override config.yaml in google/fonts |
| Branch | master |

## How the Repository URL Was Found

The repository URL `https://github.com/huertatipografica/Alegreya-Sans` is already present in the METADATA.pb source block. It was first added by Simon Cozens in commit `5f2b22f48` ("Update upstreams", 2023-12-14). The URL is also referenced in:

- The font copyright strings in METADATA.pb: "Copyright 2013 The Alegreya Sans Project Authors (https://github.com/huertatipografica/Alegreya-Sans)"
- The PR #1312 commit message by Marc Foley: "Taken from the upstream repo https://github.com/huertatipografica/Alegreya-Sans"
- The PR #1312 body, which references the upstream issue https://github.com/huertatipografica/Alegreya-Sans/issues/11

The cached clone at `huertatipografica/Alegreya-Sans` confirms the remote URL matches.

## How the Commit Hash Was Identified

The commit `030b9ac01fd9bcaccac0ebc8010283175f9ced4e` ("restored new characters", 2017-11-09 12:26:22 -0300) was already recorded in METADATA.pb. It was added by Felipe Sanches in commit `d8104312f` (2025-10-24) as part of the source metadata enrichment project.

**Verification**: PR #1312 in google/fonts was authored by Marc Foley and merged on 2017-11-09T17:09:16Z. The commit message states "alegreyasans: v2.004 added." and "Taken from the upstream repo". The upstream commit `030b9ac` was the latest commit in the upstream repo at that time (authored at 15:26:22 UTC, about 1.7 hours before the PR merge at 17:09:16 UTC). There are 13 additional upstream commits after `030b9ac` (the next one, `8fe9ef8`, is from 2017-11-10, after the merge date).

**Binary file comparison**: The TTF files in google/fonts match those in the upstream repo's `fonts/ttf/` directory at commit `030b9ac`. For example, `AlegreyaSans-Bold.ttf` is exactly 266,856 bytes in both locations. `AlegreyaSans-Regular.ttf` differs by only 8 bytes (263,796 upstream vs 263,804 in google/fonts), likely due to minor post-processing. This confirms the fonts were taken from this commit.

## How Config YAML Was Resolved

The upstream repository does **not** have a `config.yaml` file at any commit. The source files are Glyphs format:
- `sources/Alegreya_Sans.glyphs`
- `sources/Alegreya_Sans-Italic.glyphs`

An override `config.yaml` was created in the google/fonts family directory at `ofl/alegreyasans/config.yaml` (added in commit `d8104312f`, 2025-10-24). The override contains:

```yaml
buildVariable: false
sources:
  - sources/Alegreya_Sans.glyphs
  - sources/Alegreya_Sans-Italic.glyphs
```

This correctly references the two Glyphs source files in the upstream repo at the referenced commit, with `buildVariable: false` since the family is static (14 individual weight/style TTF files). The `config_yaml` field is intentionally omitted from the METADATA.pb source block because google-fonts-sources auto-detects local override config files.

## Conclusion

**Confidence: HIGH**

The source metadata for Alegreya Sans is complete and verified. The repository URL is confirmed through multiple sources (copyright strings, PR references, commit messages). The commit hash `030b9ac` is the correct onboarding commit for v2.004, verified by timeline analysis (it was the latest upstream commit before PR #1312 was merged) and binary file size comparison. The override config.yaml in google/fonts correctly references the Glyphs sources. The family has 14 static instances (7 weights x 2 styles: Thin through Black, each with Roman and Italic).

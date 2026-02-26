# Betania Patmos - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos |
| Repository URL | https://github.com/huertatipografica/betania-patmos |
| Commit Hash | 08c83ac9540b0b2bf86ddf6b632651142f31a93c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | HANDWRITING |

## How the Repository URL Was Found

The repository URL `https://github.com/huertatipografica/betania-patmos` was present in the METADATA.pb file's source block from the initial onboarding. The URL is also referenced in the copyright string: "Copyright 2024 The Betania Patmos Project Authors (https://github.com/huertatipografica/betania-patmos)". The onboarding commit message explicitly confirms: "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit ...".

## How the Commit Hash Was Determined

The commit hash `08c83ac9540b0b2bf86ddf6b632651142f31a93c` was present in the METADATA.pb source block from the initial onboarding. The onboarding commit (`9adc7b48d`) by Emma Marichal (2026-01-15) explicitly states: "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c".

Verification via GitHub API confirms the commit exists and is dated 2026-01-15T11:02:53Z, with message "Merge pull request #4 from emmamarichal/main - build fonts". This is a merge commit from Emma Marichal's PR that built the fonts, which was created on the same day the font was onboarded to Google Fonts. The timeline is consistent.

## Config YAML Status

- **Path**: `sources/config.yaml`
- **Exists at recorded commit**: Yes, verified via GitHub API
- **Contents**: Config specifies `betania-patmos.glyphs` as the source, with `buildVariable: false`, `buildStatic: true`, `buildTTF: true`, `buildOTF: true`, `buildWebfont: true`
- **Note**: The METADATA.pb source block does NOT include a `config_yaml` field. The tracking file records `config_yaml: "sources/config.yaml"` as the discovered path, but this has not been added to the METADATA.pb yet.
- **No override config.yaml** exists in the google/fonts family directory
- **Important**: The config.yaml only references one source file (`betania-patmos.glyphs`), yet the repo produces multiple font families (Betania Patmos, GDL, Guide Line, In, and InGDL). This single config likely generates all variants from the same Glyphs source.

## Verification

1. Commit hash `08c83ac9540b0b2bf86ddf6b632651142f31a93c` verified to exist via GitHub API
2. Commit is dated 2026-01-15, same day as the google/fonts onboarding commit - timeline is consistent
3. Font file `fonts/ttf/BetaniaPatmos-Regular.ttf` confirmed present at that commit
4. `sources/config.yaml` confirmed present at that commit
5. Repository URL confirmed accessible
6. The `branch: "main"` field is correct

## Confidence Level

**High** - The repository URL and commit hash are well-documented with full provenance in the onboarding commit message. The commit was created by Emma Marichal on the same day she onboarded the font, indicating a clean workflow. All file paths are verified.

## Open Questions

1. The METADATA.pb source block is missing the `config_yaml` field. Should `config_yaml: "sources/config.yaml"` be added to the METADATA.pb, or should an override config be placed in the google/fonts family directory?
2. There is a fifth variant "BetaniaPatmosInGDL" in the upstream repo's fonts/ttf directory that does not appear to have been onboarded to Google Fonts.

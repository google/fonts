# Betania Patmos In - Investigation Report

## Source Data (from tracking)

| Field | Value |
|-------|-------|
| Family Name | Betania Patmos In |
| Repository URL | https://github.com/huertatipografica/betania-patmos |
| Commit Hash | 08c83ac9540b0b2bf86ddf6b632651142f31a93c |
| Config YAML | sources/config.yaml |
| Status | complete |
| Category | HANDWRITING |

## How the Repository URL Was Found

The repository URL `https://github.com/huertatipografica/betania-patmos` was present in the METADATA.pb file's source block from the initial onboarding. This is the same repository used by all Betania Patmos variants. The copyright string confirms: "Copyright 2024 The Betania Patmos Project Authors (https://github.com/huertatipografica/betania-patmos)".

## How the Commit Hash Was Determined

The commit hash `08c83ac9540b0b2bf86ddf6b632651142f31a93c` was present in the METADATA.pb source block from the initial onboarding. The onboarding commit (`caf0f148c`) by Emma Marichal (2026-01-23) explicitly states: "Taken from the upstream repo https://github.com/huertatipografica/betania-patmos at commit https://github.com/huertatipografica/betania-patmos/commit/08c83ac9540b0b2bf86ddf6b632651142f31a93c".

This is the same commit hash used for all Betania Patmos variants. The commit is a merge of PR #4 ("build fonts") dated 2026-01-15. Betania Patmos In was onboarded on 2026-01-23, same day as the GDL and Guide Line variants (Betania Patmos base was onboarded 8 days earlier on 2026-01-15).

## Config YAML Status

- **Path**: `sources/config.yaml`
- **Exists at recorded commit**: Yes, verified via GitHub API
- **Contents**: Same config as the base Betania Patmos family - references `betania-patmos.glyphs` as the source file. The single Glyphs source generates all Betania Patmos variants.
- **Note**: The METADATA.pb source block does NOT include a `config_yaml` field. The tracking file records the discovered path but it has not been added to METADATA.pb yet.
- **No override config.yaml** exists in the google/fonts family directory

## Verification

1. Commit hash `08c83ac9540b0b2bf86ddf6b632651142f31a93c` verified to exist via GitHub API
2. Font file `fonts/ttf/BetaniaPatmosIn-Regular.ttf` confirmed present at that commit
3. `sources/config.yaml` confirmed present at that commit
4. Repository URL confirmed accessible
5. The `branch: "main"` field is correct
6. The upstream repo also contains `BetaniaPatmosInGDL-Regular.ttf` which was not onboarded to Google Fonts

## Confidence Level

**High** - Full provenance documented in the onboarding commit message. Same commit hash as the other Betania Patmos variants, all from the same upstream snapshot. All file paths verified.

## Open Questions

1. The METADATA.pb source block is missing the `config_yaml` field. Should it be added?
2. There is also a "BetaniaPatmosInGDL" variant in the upstream repo that was not onboarded to Google Fonts. It may be a companion "guideline" version of "Betania Patmos In", similar to how "Betania Patmos GDL" is the guideline version of "Betania Patmos".

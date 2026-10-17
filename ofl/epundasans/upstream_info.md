# Investigation Report: Epunda Sans

## Summary

| Field | Value |
|---|---|
| **Family Name** | Epunda Sans |
| **Designer** | Typofactur (Simon Atzbach) |
| **License** | OFL |
| **Repository URL** | https://github.com/typofactur/epundasans |
| **Commit** | `4a75d7da519ebed2c580e024a3e447a6bde69377` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |
| **Confidence** | HIGH |

## Source Block in METADATA.pb

The METADATA.pb at `ofl/epundasans/METADATA.pb` already contains a complete `source {}` block with:
- `repository_url`: https://github.com/typofactur/epundasans
- `commit`: `4a75d7da519ebed2c580e024a3e447a6bde69377`
- `config_yaml`: `sources/config.yaml`
- `branch`: main
- `files` mappings for OFL.txt, EpundaSans[wght].ttf, and EpundaSans-Italic[wght].ttf

## Upstream Repository

- **URL**: https://github.com/typofactur/epundasans
- **Cached at**: `upstream_repos/fontc_crater_cache/typofactur/epundasans`
- **Repository status**: Clean, up to date with origin/main

### Source Files

The upstream repo uses `.glyphspackage` format:
- `sources/EpundaSans.glyphspackage` (upright)
- `sources/EpundaSans-Italic.glyphspackage` (italic)

### config.yaml

A valid `sources/config.yaml` exists in the upstream repo at the referenced commit. It configures:
- Two sources: EpundaSans.glyphspackage and EpundaSans-Italic.glyphspackage
- `familyName`: "Epunda Sans"
- `buildVariable`: true, `buildStatic`: true, `buildTTF`: true, `buildOTF`: false
- `includeSourceFixes`: true
- Full STAT table configuration for both upright and italic variable fonts
- Weight axis: 300 (Light) to 900 (Black)

No override config.yaml exists in the google/fonts family directory.

## Onboarding History in google/fonts

### Initial Onboarding (v2.204)

- **Commit**: `27967bdbb515d7390c6c6069a34a64e870c5e2aa`
- **Date**: 2025-03-21
- **Author**: Emma Marichal
- **PR**: #9246 (merged 2025-04-01)
- **Message**: "Epunda Sans: Version 2.204 added" - "Taken from the upstream repo https://github.com/typofactur/epundasans at commit 0c85f7005b9513b2f0b0482830aa9e25c3b203cb"
- **Upstream commit**: `0c85f70` = "Merge pull request #2 from emmamarichal/main" (2025-03-19)
- Created the font family with METADATA.pb, OFL.txt, article, and variable font files

### Update to v2.205

- **Commit**: `4c7d23f6c054eb89fd818b15772847fdce311708`
- **Date**: 2025-06-12
- **Author**: Emma Marichal
- **PR**: #9563 (merged 2025-07-24)
- **Message**: "Epunda Sans: Version 2.205 added" - "Taken from the upstream repo https://github.com/typofactur/epundasans at commit 4a75d7da519ebed2c580e024a3e447a6bde69377"
- **Upstream commit**: `4a75d7d` = "Merge pull request #3 from emmamarichal/main" (2025-06-06)
- Updated binary font files and METADATA.pb

### Source Block Addition

- **Commit**: `7aea7ff8ce2d357e8666b1b772fbed3b5f159214`
- **Date**: 2025-09-18
- **Author**: Felipe Correa da Silva Sanches
- Added `config_yaml: "sources/config.yaml"` to the existing source block

## Commit Hash Verification

The commit hash `4a75d7da519ebed2c580e024a3e447a6bde69377` referenced in METADATA.pb:
- **Exists** in the upstream repo
- **Description**: "Merge pull request #3 from emmamarichal/main" (2025-06-06)
- **Matches the google/fonts onboarding commit message** which explicitly references this hash
- **Binary file sizes match exactly**:
  - `EpundaSans[wght].ttf`: 153,704 bytes (upstream at commit) = 153,704 bytes (google/fonts)
  - `EpundaSans-Italic[wght].ttf`: 156,748 bytes (upstream at commit) = 156,748 bytes (google/fonts)

### Newer Upstream Commits

There are 4 newer commits after the referenced hash:
- `fbeb3ea` (2025-06-29) - "lozenge and .notdef added"
- `ff34829` (2025-06-29) - merge
- `28bd544` (2025-06-29) - ".notdef added"
- `8618b8a` (2025-08-31) - "v2.3 alternative a, e and g"

These newer changes have NOT been incorporated into Google Fonts and would need separate review.

## Conclusion

The source metadata for Epunda Sans is **complete and verified**. The repository URL, commit hash, config.yaml path, and file mappings are all correct. Binary file sizes confirm the commit hash is accurate. No action needed.

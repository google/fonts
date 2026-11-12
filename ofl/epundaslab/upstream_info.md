# Investigation Report: Epunda Slab

## Summary

| Field | Value |
|---|---|
| **Family Name** | Epunda Slab |
| **Designer** | Typofactur (Simon Atzbach) |
| **License** | OFL |
| **Repository URL** | https://github.com/typofactur/epundaslab |
| **Commit** | `b7f3ef7ccf9e7f1c0d8ef23bd5c6017a8c77a268` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Status** | complete |
| **Confidence** | HIGH |

## Source Block in METADATA.pb

The METADATA.pb at `ofl/epundaslab/METADATA.pb` already contains a complete `source {}` block with:
- `repository_url`: https://github.com/typofactur/epundaslab
- `commit`: `b7f3ef7ccf9e7f1c0d8ef23bd5c6017a8c77a268`
- `config_yaml`: `sources/config.yaml`
- `branch`: main
- `files` mappings for OFL.txt, EpundaSlab[wght].ttf, and EpundaSlab-Italic[wght].ttf

## Upstream Repository

- **URL**: https://github.com/typofactur/epundaslab
- **Cached at**: `upstream_repos/fontc_crater_cache/typofactur/epundaslab`
- **Repository status**: Clean, up to date with origin/main

### Source Files

The upstream repo uses `.glyphspackage` format:
- `sources/EpundaSlab.glyphspackage` (upright)
- `sources/EpundaSlab-Italic.glyphspackage` (italic)

### config.yaml

A valid `sources/config.yaml` exists in the upstream repo at the referenced commit. It configures:
- Two sources: EpundaSlab.glyphspackage and EpundaSlab-Italic.glyphspackage
- `familyName`: "Epunda Slab"
- `buildVariable`: true, `buildStatic`: true, `buildTTF`: true, `buildOTF`: false
- `includeSourceFixes`: false
- Full STAT table configuration for both upright and italic variable fonts
- Weight axis: 300 (Light) to 900 (Black)

No override config.yaml exists in the google/fonts family directory.

## Onboarding History in google/fonts

### Initial Onboarding (v1.102)

- **Commit**: `1199401b6ca88c21fcda2719e4d6fc8459d57cc7`
- **Date**: 2025-03-20
- **Author**: Emma Marichal
- **PR**: #9241 (merged 2025-04-01)
- **Message**: "Epunda Slab: Version 1.102 added" - "Taken from the upstream repo https://github.com/typofactur/epundaslab at commit 6ad46fde8036ef359369bd922c0d8209f659b70f"
- **Upstream commit**: `6ad46fd` = "Merge pull request #1 from emmamarichal/main" (2025-03-19)
- Created the font family with METADATA.pb, OFL.txt, article, and variable font files

### Category Fix

- **Commit**: `8c13a0599d01a2d4ca4369708f741efa20517050`
- **PR**: #9699
- Changed category to "serif" in METADATA.pb

### Update to v1.103

- **Commit**: `9337675d4be7d49026d1a8c1518d97eeae8433ca`
- **Date**: 2025-06-12
- **Author**: Emma Marichal
- **PR**: #9562 (merged 2025-07-11)
- **Message**: "Epunda Slab: Version 1.103 added" - "Taken from the upstream repo https://github.com/typofactur/epundaslab at commit b7f3ef7ccf9e7f1c0d8ef23bd5c6017a8c77a268"
- **Upstream commit**: `b7f3ef7` = "Merge pull request #2 from emmamarichal/main" (2025-06-06)
- Updated binary font files and METADATA.pb

### Source Block Addition

- **Commit**: `c72cf555fd0949eb72e33c6d298672865e9511da`
- **Date**: 2025-09-18
- **Author**: Felipe Correa da Silva Sanches
- Added `config_yaml: "sources/config.yaml"` to the existing source block

## Commit Hash Verification

The commit hash `b7f3ef7ccf9e7f1c0d8ef23bd5c6017a8c77a268` referenced in METADATA.pb:
- **Exists** in the upstream repo
- **Description**: "Merge pull request #2 from emmamarichal/main" (2025-06-06)
- **Matches the google/fonts onboarding commit message** which explicitly references this hash
- **Binary file sizes match exactly**:
  - `EpundaSlab[wght].ttf`: 90,220 bytes (upstream at commit) = 90,220 bytes (google/fonts)
  - `EpundaSlab-Italic[wght].ttf`: 93,032 bytes (upstream at commit) = 93,032 bytes (google/fonts)

### Newer Upstream Commits

There are 7 newer commits after the referenced hash:
- `54e388d` (2025-06-29) - "lozenge and .notdef added"
- `93deffd` (2025-06-29) - ".notdef added"
- `f2afe95` (2025-08-30) - "single an double-storey a and g, alternative e, Macute"
- `e6b87dc` (2025-08-30) - "Update README.md"
- `d55af96` (2025-08-30) - "Italic: missing k added"
- `e8a1025` (2025-08-30) - "Version 1.300"
- `103e509` (2025-11-30) - "missing serifs added in diacritics of i and j"

These newer changes have NOT been incorporated into Google Fonts and would need separate review.

## Conclusion

The source metadata for Epunda Slab is **complete and verified**. The repository URL, commit hash, config.yaml path, and file mappings are all correct. Binary file sizes confirm the commit hash is accurate. No action needed.

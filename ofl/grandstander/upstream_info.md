# Investigation Report: Grandstander

## Summary

Grandstander is a variable display/handwriting font (weight axis 100-900, normal + italic) designed by Tyler Finck and ETC (Etcetera Type Company), added to Google Fonts on 2020-07-24. The upstream repository is `Etcetera-Type-Co/Grandstander`. The METADATA.pb has a source block with repository URL, commit hash, and config_yaml path. However, the commit hash in METADATA.pb (`0bf9e31`, from July 2023) is the latest HEAD of the upstream repo, not the original onboarding commit (`33c28849`, referenced in the google/fonts PR #2575 from July 2020). The font binaries in google/fonts have never been updated since onboarding, and the file sizes differ significantly from those at the current upstream HEAD, confirming the commit mismatch.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Grandstander                                       |
| Designer           | Tyler Finck, ETC                                   |
| Date Added         | 2020-07-24                                         |
| Repository URL     | https://github.com/Etcetera-Type-Co/Grandstander   |
| Onboarding Commit  | 33c288495d8ac7bc0b29a9f35801de1df7e6d010 (from PR #2575) |
| Current METADATA Commit | 0bf9e31d529d7a67b23510b841cb3597db0cb130 (repo HEAD, incorrect) |
| Config YAML        | Sources/config.yaml (in upstream repo)             |
| Source Files       | Sources/Grandstander.glyphs, Sources/Grandstander-Italic.glyphs |
| Status             | **needs_correction**                               |
| Confidence         | HIGH                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb source block:
```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Grandstander"
  commit: "0bf9e31d529d7a67b23510b841cb3597db0cb130"
  config_yaml: "Sources/config.yaml"
}
```

### Git History in google/fonts

Key commits for this family:

1. `ae1d37ea9` (2020-07-27) - **Grandstander: v2.111 added (#2575)**
   - By Rosalie Wagner
   - Commit message: "Taken at upstream repo https://github.com/Etcetera-Type-Co/Grandstander at commit https://github.com/Etcetera-Type-Co/Grandstander/tree/33c288495d8ac7bc0b29a9f35801de1df7e6d010"
   - Added VF files: `Grandstander[wght].ttf` (183,056 bytes) and `Grandstander-Italic[wght].ttf` (185,092 bytes)
   - Also added static font instances

2. `70b0fc8a8` (2021) - **Remove static fonts for unhinted variable font families (#3695)**
   - Removed the static font files, keeping only the VF files

3. `2423d2aef` (2023-12-14) - **Update upstreams** by Simon Cozens
   - Added initial source block with only `repository_url`

4. `19cdcec59` (2025-03-31) - **[Batch 1/4] port info from fontc_crater targets list**
   - Added commit hash `0bf9e31d529d7a67b23510b841cb3597db0cb130` and `config_yaml: "sources/config.yaml"`

5. `7190093b1` (2025-05-22) - Fixed config_yaml capitalization to `Sources/config.yaml`

### Upstream Repository

Cached at `fontc_crater_cache/Etcetera-Type-Co/Grandstander/` (shallow clone, depth 1).

- **HEAD/master**: `0bf9e31` (2023-07-10) - "sharp stylistic alternates" by Tyler Finck
- Branch: `master` (not `main`)
- Only the HEAD commit is visible due to shallow clone

Source structure:
- `Sources/Grandstander.glyphs` (711,511 bytes)
- `Sources/Grandstander-Italic.glyphs` (715,100 bytes)
- `Sources/config.yaml`
- `Sources/legacy-2axes/` (older 2-axis build configuration)
- `fonts/variable/Grandstander[wght].ttf` (190,984 bytes)
- `fonts/variable/Grandstander-Italic[wght].ttf` (191,872 bytes)

Config.yaml (at HEAD) specifies two sources, axis order [wght, ital], and builds static, variable, TTF, OTF, and webfont outputs with full STAT table configuration.

### Commit Hash Discrepancy

This is a clear case of commit mismatch:

| Aspect | Onboarding (2020) | METADATA.pb (current) |
|--------|-------------------|-----------------------|
| Commit | `33c28849` | `0bf9e31` |
| Date | Pre-July 2020 | July 10, 2023 |
| Description | Unknown (shallow clone) | "sharp stylistic alternates" |

**Evidence the commit is wrong:**

1. **File size mismatch**: The VF files in google/fonts (183,056 and 185,092 bytes) differ significantly from those at the current upstream HEAD (190,984 and 191,872 bytes). The upstream files are ~8KB larger per file.

2. **Font files never updated**: Git log shows the Grandstander VF files were only ever written once -- in the original onboarding commit `ae1d37ea9` (2020-07-27).

3. **Timeline**: The onboarding was in July 2020, but commit `0bf9e31` is from July 2023. The upstream repo had significant changes (including "sharp stylistic alternates") that were never pulled into google/fonts.

4. **Source of the incorrect hash**: The commit `0bf9e31` was added via the fontc_crater targets list batch port (commit `19cdcec59`), which used data from fontc_crater's target.json. The fontc_crater cache used shallow clones, so it captured the latest HEAD rather than the original onboarding commit.

The correct onboarding commit is `33c288495d8ac7bc0b29a9f35801de1df7e6d010` as stated in the original PR #2575 commit message.

### Config.yaml at Onboarding Time

Since we cannot inspect the repo at the onboarding commit `33c28849` (shallow clone), we cannot confirm whether `Sources/config.yaml` existed at that time. However, the font was onboarded as a variable font with two VF files, suggesting a build configuration was available. The current config.yaml at HEAD references the same source files structure.

## Conclusion

The Grandstander source block has the correct repository URL and config_yaml path, but the commit hash is wrong. The current hash `0bf9e31` (HEAD from 2023) should be replaced with the original onboarding commit `33c28849` as documented in PR #2575.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Grandstander"
  commit: "33c288495d8ac7bc0b29a9f35801de1df7e6d010"
  config_yaml: "Sources/config.yaml"
}
```

### Status: needs_correction

The commit hash must be corrected from `0bf9e31d529d7a67b23510b841cb3597db0cb130` (current repo HEAD, 2023) to `33c288495d8ac7bc0b29a9f35801de1df7e6d010` (original onboarding commit from PR #2575, 2020). The font binaries in google/fonts were built from the older commit and have never been updated.

Note: There are also significant upstream improvements (stylistic alternates, etc.) at the newer commit that have not been reviewed or incorporated into Google Fonts.

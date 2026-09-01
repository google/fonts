# Investigation Report: Grandiflora One

## Summary

Grandiflora One is a Korean serif/display font designed by Haesung Cho and JAMO, added to Google Fonts on 2023-05-18. The upstream repository is `JAMO-TYPEFACE/Grandiflora` on GitHub. The METADATA.pb has a complete source block with repository URL, commit hash, file mappings, branch, and config_yaml path. The original onboarding referenced commit `b016ca7`, but the current METADATA.pb correctly points to `5e5d39d` (the repo HEAD), which was a later merge by aaronbell that added a missing glyph. The binary in google/fonts was subsequently updated directly by Aaron (May 25, 2023) with kerning fixes, making it slightly different from the binary at the upstream HEAD. The source block is well-structured and largely correct.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Grandiflora One                                    |
| Designer           | Haesung Cho, JAMO                                  |
| Date Added         | 2023-05-18                                         |
| Repository URL     | https://github.com/JAMO-TYPEFACE/Grandiflora       |
| Onboarding Commit  | b016ca716dade21cb890efc78b9349275c4e7c99 (original packager) |
| Current Commit     | 5e5d39d3d49c5de0815020ba3996e9725d717e3f (repo HEAD) |
| Config YAML        | Sources/config.yaml (in upstream repo)             |
| Source Files       | Sources/Grandiflora.glyphs                         |
| Status             | **needs_correction**                               |
| Confidence         | MEDIUM                                             |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:
```
source {
  repository_url: "https://github.com/JAMO-TYPEFACE/Grandiflora"
  commit: "5e5d39d3d49c5de0815020ba3996e9725d717e3f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/GrandifloraOne-Regular.ttf"
    dest_file: "GrandifloraOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
```

### Git History in google/fonts

Key commits for this family:

1. `d4d84c80e` (2023-05-18) - **[gftools-packager] Grandiflora One: Version 1.000 added**
   - By Aaron (aaron@sajatypeworks.com)
   - Commit message references upstream commit `b016ca716dade21cb890efc78b9349275c4e7c99`
   - Added font file (2,342,268 bytes), DESCRIPTION, METADATA.pb, OFL.txt, upstream.yaml

2. `a1c17595e` (2023-05-24) - **Update GrandifloraOne-Regular.ttf**
   - By Aaron - "Adding missing glyph from GF Kernal"
   - File size: 2,342,268 -> 2,342,672 bytes

3. `7226d78ff` (2023-05-25) - **Update GrandifloraOne-Regular.ttf**
   - By Aaron - "Fixed some over kerns and did a general review of the other kerns"
   - File size: 2,342,672 -> 2,342,680 bytes

4. `66f91f10f` (2024-04-03) - Merge upstream.yaml into METADATA.pb (added files/branch fields)
5. `19cdcec59` (2025-03-31) - Batch port: updated commit from `b016ca7` to `5e5d39d`, added config_yaml
6. `7190093b1` (2025-05-22) - Fixed config_yaml capitalization: `sources/config.yaml` -> `Sources/config.yaml`

### Upstream Repository

Cached at `fontc_crater_cache/JAMO-TYPEFACE/Grandiflora/` (shallow clone).

- **HEAD**: `5e5d39d` (2023-05-24) - "Merge pull request #3 from aaronbell/main - Adding missing glyph from GF Kernal"
- This is the only commit visible (shallow clone)
- The original onboarding commit `b016ca7` is not available in the shallow clone

Source structure:
- `Sources/Grandiflora.glyphs` (5,675,072 bytes)
- `Sources/config.yaml`
- `Fonts/ttf/GrandifloraOne-Regular.ttf` (2,342,672 bytes)

Config.yaml contents:
```yaml
sources:
  - Grandiflora.glyphs
familyName: "Grandiflora One"
buildOTF: false
```

### Commit Hash Analysis

The commit history is nuanced:

1. **Original onboarding** (2023-05-18): Used commit `b016ca7` for the gftools-packager build
2. **Upstream update** (2023-05-24): aaronbell merged PR #3 into the upstream repo, creating commit `5e5d39d` (which added the missing glyph)
3. **Direct binary update** (2023-05-24 and 2023-05-25): Aaron manually updated the binary in google/fonts with glyph additions and kerning fixes

The current METADATA.pb points to `5e5d39d`, which is the upstream HEAD. However, the binary currently in google/fonts (2,342,680 bytes) differs from the binary at `5e5d39d` (2,342,672 bytes) because Aaron made an additional kerning fix directly in google/fonts on May 25, 2023, after the upstream merge.

This means:
- The commit `5e5d39d` does not exactly correspond to the binary in google/fonts
- The original onboarding commit `b016ca7` also does not match (it was the pre-PR version)
- The actual binary in google/fonts was manually edited after the upstream was updated

### Assessment

The commit hash `5e5d39d` is the closest available reference, as it includes the missing glyph that was also added to google/fonts. The 8-byte difference in file size is likely from the manual kerning fix Aaron applied directly. This is an acceptable approximation, but technically neither commit exactly matches the binary in google/fonts.

## Conclusion

The Grandiflora One source block is mostly correct but has a subtle issue: the binary in google/fonts was manually patched after the upstream commit, so neither the original `b016ca7` nor the current `5e5d39d` exactly matches. The current `5e5d39d` is the better reference since it includes the missing glyph fix.

### Recommended METADATA.pb Source Block

The current source block is acceptable as-is. If a correction were to be made, it would be to note that the binary was manually updated after the upstream commit, but the existing block is the best available approximation:

```
source {
  repository_url: "https://github.com/JAMO-TYPEFACE/Grandiflora"
  commit: "5e5d39d3d49c5de0815020ba3996e9725d717e3f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "Fonts/ttf/GrandifloraOne-Regular.ttf"
    dest_file: "GrandifloraOne-Regular.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
```

### Status: needs_correction

The commit hash `5e5d39d` is the repo HEAD but the binary in google/fonts was manually patched after this upstream commit (kerning fix on May 25, 2023). The binary does not exactly match what would be built from the upstream at this commit. Ideally, the kerning fix should be upstreamed to the JAMO-TYPEFACE/Grandiflora repo, and the binary rebuilt from there.

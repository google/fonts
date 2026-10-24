# Investigation Report: Gupter

## Summary

Gupter is a condensed serif font designed by Octavio Pardo, inspired by early 20th century English fonts such as Times New Roman. It was onboarded to Google Fonts on 2019-11-15 via PR #2255 by Viviana Monsalve. The upstream repository at `octaviopardo/GUPTER` has a `.glyphs` source file. An override `config.yaml` already exists in the google/fonts family directory. The source block in METADATA.pb is complete with the correct repository URL and commit hash.

## Key Findings

| Field              | Value |
|--------------------|-------|
| Family Name        | Gupter |
| Designer           | Octavio Pardo |
| Repository URL     | https://github.com/octaviopardo/GUPTER |
| Commit Hash        | 959e1580e02c8213898597aa076c33eafd0d6db6 |
| Branch             | master (default) |
| Config YAML        | Override `config.yaml` in google/fonts |
| Status             | **complete** |
| Confidence         | HIGH |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a source block:

```
source {
  repository_url: "https://github.com/octaviopardo/GUPTER"
  commit: "959e1580e02c8213898597aa076c33eafd0d6db6"
}
```

The source block has the repository URL and commit hash. No `config_yaml` field is present, which is correct because the override `config.yaml` in the google/fonts family directory is auto-detected by google-fonts-sources.

### Git History in google/fonts

| Commit | Date | Description |
|--------|------|-------------|
| `951829b` | 2025-11-18 | Sources info for Gupter (PR #2255) - added source block and override config.yaml |
| `7fe3878` | unknown | Updated DESCRIPTION.en_us.html |
| `d3d3474` | unknown | Link to upstream repo updated to last standard |
| `e87082f` | unknown | Updated DESCRIPTION.en_us.html |
| `2423d2a` | 2023-12-14 | "Update upstreams" - bulk addition of source blocks to multiple families |
| `53879c4` | 2019-11-15 | **Initial onboarding** - "[Font Bakery Dashboard] create family: Gupter (#2255)" |

### Upstream Repository Analysis

The repo `octaviopardo/GUPTER` is cached at `upstream_repos/fontc_crater_cache/octaviopardo/GUPTER/`. It has 35 total commits.

**Source files:**
- `SOURCES/Gupter-Family.glyphs` (1,670,113 bytes) - Glyphs source file containing all three masters (Regular, Medium, Bold)

**Output files:**
- `FONTS/TTF/Gupter-Regular.ttf` (52,376 bytes)
- `FONTS/TTF/Gupter-Medium.ttf` (52,112 bytes)
- `FONTS/TTF/Gupter-Bold.ttf` (53,204 bytes)

**No config.yaml exists in the upstream repo.**

### Commit Hash Verification

The referenced commit `959e158` is the HEAD of the `master` branch, dated 2019-11-13. It is a merge commit: "Merge pull request #5 from vv-monsalve/master" with message "Vertical metrics adjusted". This commit was created on the same day as the `date_added` in METADATA.pb (2019-11-13), and two days before the google/fonts onboarding commit (2019-11-15).

The contributor `vv-monsalve` (Viviana Monsalve) is the same person who submitted the google/fonts onboarding PR #2255, confirming this is the correct commit.

### File Size Verification

| File | Upstream (at `959e158`) | google/fonts (current) |
|------|------------------------|----------------------|
| Gupter-Regular.ttf | 52,376 bytes | 52,376 bytes |
| Gupter-Medium.ttf | 52,112 bytes | 52,112 bytes |
| Gupter-Bold.ttf | 53,204 bytes | 53,204 bytes |

All three file sizes match exactly. The TTFs in google/fonts have never been modified since onboarding.

### Override config.yaml

An override `config.yaml` exists in `google/fonts/ofl/gupter/config.yaml`:

```yaml
buildVariable: false
sources:
  - SOURCES/Gupter-Family.glyphs
```

This was added on 2025-11-18 (commit `951829b`). It correctly references the `.glyphs` source file in the upstream repo and sets `buildVariable: false` since Gupter is a static-only family with three discrete weights.

## Conclusion

The source metadata for Gupter is complete. The repository URL and commit hash are verified and correct. The override config.yaml in google/fonts is properly configured to point to the upstream `.glyphs` source file. No changes are needed.

### Recommended METADATA.pb Source Block

No changes needed. The current source block is correct:

```
source {
  repository_url: "https://github.com/octaviopardo/GUPTER"
  commit: "959e1580e02c8213898597aa076c33eafd0d6db6"
}
```

**Status: complete** - Source block and override config.yaml are both correct and verified.

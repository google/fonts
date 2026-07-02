# Investigation Report: Hanuman

## Summary

Hanuman is a Khmer serif font designed by Danh Hong, originally added to Google Fonts on 2010-09-21. It has been updated many times, most recently to Version 9.000 in May 2025. The upstream repository is at `https://github.com/danhhong/Hanuman`. The METADATA.pb has a complete source block with repository URL, commit hash, config_yaml, file mappings, and branch.

## Key Findings

| Field            | Value |
|------------------|-------|
| Family Name      | Hanuman |
| Repository URL   | https://github.com/danhhong/Hanuman |
| Commit           | `7188b3c0e5722ad0126f045d4eeb895176e12c14` |
| Branch           | master |
| Config YAML      | `Source/builder.yaml` |
| Source Files     | `Source/Hanuman.glyphs` |
| Status           | **complete** |
| Confidence       | HIGH |

## Investigation Details

### Onboarding History in google/fonts

Hanuman has a long history in Google Fonts, dating back to the initial commit (2015-03-07 in the current repo). The relevant recent updates:

1. **Commit bc4d15f26** (2025-05-16, by Yanone):
   - "Hanuman: Version 9.000 added"
   - Explicitly references: "Taken from the upstream repo https://github.com/danhhong/Hanuman at commit https://github.com/danhhong/Hanuman/commit/7188b3c0e5722ad0126f045d4eeb895176e12c14"
   - Resolves issue #8780
   - Converted from static fonts (5 TTFs: Thin, Light, Regular, Bold, Black) to a single variable font `Hanuman[wght].ttf`
   - Updated METADATA.pb with new source block

2. **Commit eb94c3c4e** (2025-05-21, by Felipe Sanches):
   - "sources info for Hanuman: Version 9.000 (PR #9469)"
   - Added `config_yaml: "Source/builder.yaml"` to the source block

### Earlier Updates

- Version 8.001 (PR #4022, 2021) -- ttfautohint update
- Version 8.000 (PR #3496, 2020) -- major update
- v2.001 (PR #889) -- hotfix

### Commit Hash Verification

- The commit `7188b3c0e5722ad0126f045d4eeb895176e12c14` exists in the cached upstream repo
- It is dated 2025-05-09 ("Merge pull request #5 from metrey/patch-1")
- The google/fonts onboarding commit is dated 2025-05-16, just 7 days later
- This is the only commit visible in the repo (shallow clone, depth 1)
- This is also the HEAD of the repository -- the timeline is consistent (upstream commit May 9, onboarded May 16)

### Upstream Repository Analysis

- **Repository**: `danhhong/Hanuman` (cached at `fontc_crater_cache/danhhong/Hanuman`)
- **Current HEAD**: `7188b3c` (2025-05-09) -- matches the referenced commit
- **Shallow clone**: Yes (only 1 commit visible)
- **Source files**: `Source/Hanuman.glyphs` (Glyphs format)
- **Config file**: `Source/builder.yaml` -- valid gftools-builder config
- **Variable font output**: `Release/variable/Hanuman[wght].ttf`
- **Static font outputs**: `Release/ttf/` directory with multiple weights

### Config YAML Verification

The `Source/builder.yaml` file contains:
```yaml
sources:
  - Hanuman.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: true
buildTTF: true
buildOTF: false
buildWebfont: false
```

This is a valid gftools-builder configuration. The source reference is relative (Hanuman.glyphs is in the same `Source/` directory), and the output goes to `../Release`.

### File Mapping Verification

The METADATA.pb maps:
- `OFL.txt` -> `OFL.txt` (license file, present in repo root)
- `Release/variable/Hanuman[wght].ttf` -> `Hanuman[wght].ttf` (variable font output, present at that path)

## Conclusion

The Hanuman source block is complete and accurate. The commit hash `7188b3c` is confirmed to exist in the upstream repo and matches the HEAD. The timeline is consistent (upstream commit May 9, 2025; google/fonts merge May 16, 2025). The config_yaml path `Source/builder.yaml` is verified and contains a valid gftools-builder configuration pointing to `Hanuman.glyphs`.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/danhhong/Hanuman"
  commit: "7188b3c0e5722ad0126f045d4eeb895176e12c14"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/variable/Hanuman[wght].ttf"
    dest_file: "Hanuman[wght].ttf"
  }
  branch: "master"
}
```

**Status**: complete
**Confidence**: HIGH

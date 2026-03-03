# Investigation Report: Gemunu Libre

## Summary

Gemunu Libre is a sans-serif typeface designed by Mooniak, supporting Latin and Sinhala scripts. It was originally added to Google Fonts on 2017-05-29 as static fonts and updated to a variable font (Version 1.100) in June 2021 via gftools-packager (PR #3567). The upstream repository is at `https://github.com/mooniak/gemunu-libre-font`. The commit hash `8a8867d` referenced in METADATA.pb matches the gftools-packager message and exists in the upstream repo. The builder config at `sources/builder.yaml` exists at that commit. The source block is complete.

## Key Findings

| Field | Value |
|---|---|
| **Family Name** | Gemunu Libre |
| **Repository URL** | https://github.com/mooniak/gemunu-libre-font |
| **Commit Hash** | `8a8867dd893adb9e82baef9d85ccbc3764a55b0c` |
| **Config YAML** | `sources/builder.yaml` |
| **Branch** | main |
| **Source Files** | `sources/GemunuLibre.glyphs` |
| **Status** | complete |
| **Confidence** | HIGH |

## Investigation Details

### Google Fonts History

1. **Initial onboarding** (2017): Commit `3d6d46b9` - `gemunulibre: v1.001 added` (static fonts, PR #667)
2. **Description update** (2018): Commit `7224f1c9` - `Update gemunu description` (PR #872)
3. **Version 1.100 update** (2021-06-28): Commit `77b7a870` - `Gemunu Libre: Version 1.100 added` (PR #3567)
   - gftools-packager message references: `https://github.com/mooniak/gemunu-libre-font.git` at commit `8a8867dd893adb9e82baef9d85ccbc3764a55b0c`
   - Author: Yanone (post@yanone.de)
4. **Source metadata** (2025-04-02): Commit `1f12f787` - Added commit hash and config_yaml to source block

### Upstream Repository Analysis

- **URL**: https://github.com/mooniak/gemunu-libre-font
- **Cached at**: `upstream_repos/fontc_crater_cache/mooniak/gemunu-libre-font/`
- **Default branch**: main
- **Total commits**: ~120+ (active development history from 2015 to 2021)
- **Latest commit**: `90f5ecf` (2021-06-29, "Update FONTLOG.txt") - 5 commits after the referenced hash

### Commit Verification

- Commit `8a8867d` exists in the upstream repo and is a merge commit: "Merge pull request #18 from yanone/main" (2021-06-24)
- This merge integrated Yanone's work preparing the font for variable font release (builder.yaml, copyright fixes, metric adjustments)
- Binary file at this commit matches google/fonts exactly:
  - `GemunuLibre[wght].ttf`: 256,512 bytes
- The google/fonts PR #3567 was merged on 2021-06-28, four days after the upstream commit
- There are 5 subsequent commits in upstream (through 2021-06-29) that were made after the gftools-packager snapshot, but they are minor (FONTLOG updates, binary rebuild, sinTouch width fix)

### Config YAML

The `sources/builder.yaml` at commit `8a8867d` contains:
- Source: `GemunuLibre.glyphs`
- outputDir: `../fonts`
- buildStatic: false
- buildVariable: true
- buildTTF: true
- buildOTF: false
- buildWebfont: false

This is a valid gftools-builder configuration file.

### Source Files at Referenced Commit

- `sources/GemunuLibre.glyphs` - Glyphs source file
- `sources/builder.yaml` - gftools-builder config

## Conclusion

The METADATA.pb source block is complete and accurate. All fields are verified: the repository URL is valid, the commit hash exists and matches the gftools-packager reference, the config_yaml path is correct, and the binary files match. No changes needed.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/mooniak/gemunu-libre-font"
  commit: "8a8867dd893adb9e82baef9d85ccbc3764a55b0c"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/GemunuLibre[wght].ttf"
    dest_file: "GemunuLibre[wght].ttf"
  }
  branch: "main"
}
```

**Status**: complete
**Confidence**: HIGH

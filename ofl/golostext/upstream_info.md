# Investigation Report: Golos Text

## Summary

Golos Text is a sans-serif variable font (weight axis 400-900) designed by Alexandra Korolkova and Vitaly Kuzmin. It was onboarded to Google Fonts on 2023-01-20 via PR #5753 by Emma Marichal using gftools-packager. The upstream repo is `googlefonts/golos-text` and the source block in METADATA.pb is complete with repository URL, commit hash, config_yaml, and file mappings.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Golos Text                                                         |
| Repository URL    | https://github.com/googlefonts/golos-text                          |
| Commit Hash       | cf2e27222937d97c2d858fff0499bcc667a64e9d                           |
| Config YAML       | sources/config.yaml                                                |
| Status            | complete                                                           |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Current State

The current METADATA.pb already contains a fully populated source block:
- `repository_url`: https://github.com/googlefonts/golos-text
- `commit`: cf2e27222937d97c2d858fff0499bcc667a64e9d
- `config_yaml`: sources/config.yaml
- `branch`: main
- File mappings for OFL.txt and GolosText[wght].ttf

### Onboarding History

1. **PR #5753** (merged 2023-01-20): "Golos Text: Version 2.004 added" by emmamarichal.
   - The gftools-packager commit message referenced upstream commit `d321a70cd12f84603617d4cf5d0e0321c2291dd9` ("Added some features in calt and frac + exported fonts", 2023-01-06).
   - This was the original onboarding commit.

2. **Commit 66f91f10f** (2024-04-03): "Merge upstream.yaml into METADATA.pb" -- automated migration.

3. **Commit 19cdcec59** (2025-03-31): "[Batch 1/4] port info from fontc_crater targets list" by felipesanches.
   - Changed the commit hash from `d321a70` to `cf2e272` based on fontc_crater target data.
   - Added file mappings, branch, and config_yaml fields.

### Commit Hash Analysis

The original onboarding referenced `d321a70cd12f84603617d4cf5d0e0321c2291dd9` (2023-01-06, "Added some features in calt and frac + exported fonts"). The current METADATA.pb has `cf2e27222937d97c2d858fff0499bcc667a64e9d` (2023-03-03, "Fix #3").

Between these two commits, only `README.md` and `requirements.txt` changed (3 commits total). The font binary (`fonts/variable/GolosText[wght].ttf`), source files, and `sources/config.yaml` are **identical** at both commits (same git blob SHA `05ee5ecc570b97818e24e58693662cd8294fdfc9` for the font, same blob SHA `527617c381493972b4b5091b9c68b97d946a6355` for config.yaml).

The font binary in google/fonts matches the upstream file exactly (MD5: `caa4693f600e511e0bb2aaad7e5457a8`).

Since `cf2e272` is the value used in fontc_crater targets and both commits produce identical font output, the current METADATA.pb is correct.

### Upstream Repository

- **URL**: https://github.com/googlefonts/golos-text
- **Cached at**: upstream_repos/fontc_crater_cache/googlefonts/golos-text (shallow clone, only has HEAD commit cf2e272)
- **Source files**: `sources/GolosText.glyphs` (Glyphs source), plus UFO exports
- **Config**: `sources/config.yaml` exists with gftools-builder configuration
  - Sources: GolosText.glyphs
  - Axis order: wght
  - Family name: "Golos Text"
  - Builds OTF and variable TTF
  - Has STAT table definitions

### Config YAML Contents

```yaml
sources:
  - GolosText.glyphs
axisOrder:
  - wght
familyName: "Golos Text"
buildOTF: true
stat:
  GolosText[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Regular
      value: 400
      linkedValue: 700
      flags: 2
    - name: Medium
      value: 500
    - name: SemiBold
      value: 600
    - name: Bold
      value: 700
    - name: ExtraBold
      value: 800
    - name: Black
      value: 900
```

## Conclusion

The METADATA.pb source block for Golos Text is **complete and correct**. No changes are needed.

### Recommended METADATA.pb Source Block (current, no changes needed)

```
source {
  repository_url: "https://github.com/googlefonts/golos-text"
  commit: "cf2e27222937d97c2d858fff0499bcc667a64e9d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/GolosText[wght].ttf"
    dest_file: "GolosText[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH

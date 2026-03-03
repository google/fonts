# Investigation Report: Huninn

## Summary

Huninn is a Traditional Chinese sans-serif font designed by justfont. It was added to Google Fonts on 2025-04-02. The METADATA.pb has a complete source block with repository URL, commit hash, and config_yaml path. All data has been verified against the upstream repository.

## Key Findings

| Field | Value | Status |
|-------|-------|--------|
| **Family Name** | Huninn | -- |
| **Repository URL** | https://github.com/justfont/Huninn | Verified |
| **Commit Hash** | `2f278099d0a6fdf77593c30bd6e4a44859800ee2` | Verified |
| **Config Path** | `sources/config.yaml` | Verified |
| **Source Type** | .glyphspackage | -- |
| **Status** | **complete** | -- |
| **Confidence** | HIGH | -- |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/huninn/METADATA.pb` contains a complete source block:

```
source {
  repository_url: "https://github.com/justfont/Huninn"
  commit: "2f278099d0a6fdf77593c30bd6e4a44859800ee2"
  config_yaml: "sources/config.yaml"
}
```

### Git History in google/fonts

The font was added to google/fonts through a series of commits:

1. `2f44570b1` (2025-04-02) - "Updating font name" - Initial addition as `ofl/huninn`, renamed from `ofl/justfonthuninn`. Added by Aaron Bell.
2. `c23a2b3d9` (2025-04-02) - "Update Huninn-Regular.ttf" - Tweaking license string.
3. `9c93ba363` - "Hani to Hant (#9384)" - Script classification change.
4. `ad45d3c64` - "Update justfont biography and Huninn font info" - Metadata updates.
5. `cbc944878` (2025-10-30) - "sources info for Huninn: Version 1.003 (PR #9228)" - Source block added to METADATA.pb by Felipe Sanches.

### Upstream Repository Verification

The upstream repository at https://github.com/justfont/Huninn is cached at `upstream_repos/fontc_crater_cache/justfont/Huninn/`.

The referenced commit `2f278099d0a6fdf77593c30bd6e4a44859800ee2` exists and is dated 2025-04-02, which is the same day the font was added to google/fonts. The commit message is "Update README.md".

### Config Verification

The config file at `sources/config.yaml` exists both at the referenced commit and in the current repo:

```yaml
sources:
  - Huninn.glyphspackage
familyName: Huninn
buildVariable: False
autohintTTF: False
buildOTF: False
buildWebfont: False
```

### Source Files

The sources directory contains:
- `Huninn.glyphspackage` - Main source file
- `config.yaml` - Build configuration
- `post.py` - Post-processing script

## Conclusion

**Status: complete**

All source metadata is correctly documented. The repository URL points to a valid upstream repo, the commit hash is verified and dates to the same day as the google/fonts onboarding, and the config.yaml path is correct with proper gftools-builder configuration. No changes needed.

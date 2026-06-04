# Investigation Report: Iansui

## Summary

Iansui is a Traditional Chinese handwriting font designed by But Ko. It was originally added to Google Fonts on 2024-11-25 at version 1.003, and has been updated multiple times since. The METADATA.pb has a complete source block with repository URL, commit hash, and config_yaml path. The current source block references commit `a66e7fe5b` (v1.011), which is a more recent version than the original onboarding commit.

## Key Findings

| Field | Value | Status |
|-------|-------|--------|
| **Family Name** | Iansui | -- |
| **Repository URL** | https://github.com/ButTaiwan/iansui | Verified |
| **Commit Hash** | `a66e7fe5bc492b358d8dc916f359157133a1d23c` | Verified |
| **Config Path** | `sources/config.yaml` | Verified |
| **Source Type** | .glyphspackage | -- |
| **Status** | **complete** | -- |
| **Confidence** | HIGH | -- |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/iansui/METADATA.pb` contains a complete source block:

```
source {
  repository_url: "https://github.com/ButTaiwan/iansui"
  commit: "a66e7fe5bc492b358d8dc916f359157133a1d23c"
  config_yaml: "sources/config.yaml"
}
```

### Git History in google/fonts

The font has a rich history in google/fonts:

1. `7bf55551d` (2024-11-25) - "Iansui: 1.003 added" - Original onboarding. Commit body: "Taken from the upstream repo https://github.com/ButTaiwan/iansui at commit https://github.com/ButTaiwan/iansui/tree/41190e8094a9a5b47626c5d927daf0dcb226babf"
2. `a1452e408` - "Forgot that we received permission to remove RFN"
3. `c6e196b54` - "Update METADATA.pb"
4. `ab1d5bc7f` - "Adding article image into article folder"
5. `925640c0c` - "Update OFL.txt"
6. `8813969bf` - "Update Iansui-Regular.ttf" - Font update: "Fonts are now building from .glyphspackage source; Vertical metrics updated"
7. `19cdcec59` (2025-03-31) - "[Batch 1/4] port info from fontc_crater targets list" - Source block added.
8. `6eac36785` (2025-04-02) - "Update Iansui-Regular.ttf" - Another font update with OO-poj glyphs and GASP/vmtx fixes.
9. `8df4a8215`, `ef006da2c`, `c2ab770a6` - METADATA.pb updates (localized name changes).
10. `d4e9f646b` (2025-05-14) - "removed localised family names" - Most recent change.

### Upstream Repository Verification

The upstream repository at https://github.com/ButTaiwan/iansui is cached at `upstream_repos/fontc_crater_cache/ButTaiwan/iansui/`.

**Original onboarding commit**: `41190e8094a9a5b47626c5d927daf0dcb226babf` - "Merge pull request #43 from aaronbell/main" - This was used for the initial v1.003 onboarding. At this commit, the sources contained `Iansui-Regular.ufo` and `config.yaml`.

**Current METADATA.pb commit**: `a66e7fe5bc492b358d8dc916f359157133a1d23c` (2025-01-28) - "v1.011 changelog" - This represents a newer version with significant source restructuring. Between the two commits, there were 10 intermediate commits including:
- Source migration from UFO to .glyphspackage format
- Addition of `-src` and `-build` versions
- Updated config and requirements

The current commit `a66e7fe5b` represents the v1.011 release, which aligns with the font updates pushed to google/fonts in early 2025.

### Config Verification

The config file at `sources/config.yaml` exists at the referenced commit `a66e7fe5b`:

```yaml
familyName: Iansui
sources:
- Iansui-build.glyphspackage
buildVariable: False
autohintTTF: False
buildOTF: False
buildWebfont: False
```

Note: The config at the original onboarding commit (`41190e80`) was different, referencing a UFO source:
```yaml
sources:
  - Iansui-Regular.ufo
familyName: Iansui
autohintTTF: False
buildOTF: False
buildWebfont: False
removeOutlineOverlaps: False
```

### Source Files

The current sources directory contains:
- `Iansui-build.glyphspackage` - Build-ready source
- `Iansui-src.glyphspackage` - Development source
- `config.yaml` - Build configuration
- `gen-iansui-build.py` - Build generation script
- `build-1757988489158208617.ninja` - Ninja build file

## Conclusion

**Status: complete**

All source metadata is correctly documented. The repository URL is valid, the commit hash `a66e7fe5b` is verified and corresponds to the v1.011 release used for the latest font update in google/fonts, and the config_yaml path correctly points to a valid gftools-builder configuration file. No changes needed.

# Investigation Report: Farsan

## Family Details
- **Family name**: Farsan
- **Designer**: Pooja Saxena
- **License**: OFL
- **Category**: DISPLAY
- **Date added**: 2016-06-20
- **Primary script**: Gujarati (Gujr)
- **Subsets**: gujarati, latin, latin-ext, vietnamese, menu
- **Classifications**: SANS_SERIF, HANDWRITING

## Upstream Repository
- **URL**: https://github.com/anexasajoop/farsan
- **Owner**: anexasajoop (Pooja Saxena)
- **Default branch**: master
- **Created**: 2015-08-02
- **Last pushed**: 2016-02-27
- **Status**: Accessible (HTTP 200), not archived, not a fork

## Repository Structure

The upstream repo has a single commit:
- `c9b4cee129f5844cfedc850d3d68cf2b518f3a6d` (2016-02-27) — "Merge pull request #1 from davelab6/patch-1"

### Files
```
Sources/Farsan.glyphs          (2.0 MB - Glyphs source file)
Sources/GlyphData.xml
Fonts/Farsan-Regular.ttf       (247,420 bytes - version 1.000)
Production/font.pfa            (AFDKO PostScript source)
Production/features            (OpenType feature code)
Production/classes.fea
Production/kern.fea
Production/lookups.fea
Production/markclasses.fea
Production/gdef.fea
Production/FontMenuNameDB
Production/GlyphOrderAndAliasDB
Production/current.fpr
OFL.txt
README.md
.gitignore
```

### Source Types
- **Glyphs** (`Sources/Farsan.glyphs`) — gftools-buildable
- **AFDKO Production files** (`Production/`) — legacy build chain

## Commit Hash Verification

### Only One Commit
The repository contains a single commit: `c9b4cee129f5844cfedc850d3d68cf2b518f3a6d`. This is the only possible source commit.

### Binary Comparison
- **Upstream binary** (`Fonts/Farsan-Regular.ttf`): 247,420 bytes, Version 1.000
- **google/fonts binary** (`ofl/farsan/Farsan-Regular.ttf`): 243,932 bytes, Version 1.001

The binaries differ. The google/fonts version is v1.001 (smaller file), while the upstream repo contains v1.000 (larger file). The PR title "hotfix-farsan: v1.001 added" confirms the font was recompiled/modified during onboarding by Marc Foley, likely applying hotfixes to the Glyphs source before compiling.

### Conclusion
Commit `c9b4cee` is the correct upstream reference. It is the only commit in the repo. Marc Foley recompiled the font from the Glyphs source (possibly with modifications) to produce v1.001 for google/fonts.

## google/fonts History

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| `719ffea3d` | 2017-08-07 | Marc Foley | hotfix-farsan: v1.001 added (#994) — initial onboarding |
| `76adaf1d2` | later | — | deploy commit (no font change) |
| `633ebadbf` | later | — | Add language support metadata |
| `9a14639f3` | 2026-02-25 | Felipe Sanches | Add source blocks to 602 more METADATA.pb files |

PR #994 (merged 2017-08-07) was the onboarding PR, authored by Marc Foley. The PR body was empty (no additional context provided).

## Config Assessment

### No config.yaml in upstream
The upstream repo does not contain a `config.yaml` file.

### Buildable source available
The repo contains `Sources/Farsan.glyphs`, which is a Glyphs source file compatible with gftools-builder.

### Override config.yaml needed
An override `config.yaml` should be created in the google/fonts family directory (`ofl/farsan/config.yaml`) to enable building from the Glyphs source. The config would reference:
```yaml
sources:
  - Sources/Farsan.glyphs
```

### No override config.yaml currently exists
There is currently no `config.yaml` in `ofl/farsan/` in google/fonts.

## Current METADATA.pb Source Block

The METADATA.pb currently has no source block in the main branch. A source block was prepared in commit `9a14639f3` (not yet merged to upstream google/fonts):
```
source {
  repository_url: "https://github.com/anexasajoop/farsan"
  commit: "c9b4cee129f5844cfedc850d3d68cf2b518f3a6d"
}
```

## Recommended Actions

1. **Add source block to METADATA.pb** with:
   - `repository_url`: `https://github.com/anexasajoop/farsan`
   - `commit`: `c9b4cee129f5844cfedc850d3d68cf2b518f3a6d`
   - No `config_yaml` field (override config will be auto-detected)

2. **Create override config.yaml** in `ofl/farsan/config.yaml`:
   ```yaml
   sources:
     - Sources/Farsan.glyphs
   ```

3. **Status after PR**: complete

## Summary

| Field | Value |
|-------|-------|
| **Repository URL** | https://github.com/anexasajoop/farsan |
| **Commit** | `c9b4cee129f5844cfedc850d3d68cf2b518f3a6d` |
| **Config** | Override config.yaml needed in google/fonts |
| **Status** | missing_config (will be complete with override) |
| **Confidence** | HIGH |

The upstream repository is straightforward: a single commit by the designer (Pooja Saxena), containing a Glyphs source file. The commit hash is unambiguous. Marc Foley recompiled the font with a version bump to v1.001 during the onboarding hotfix in August 2017.

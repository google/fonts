# Investigation Report: Gotu

## Summary

Gotu is a Devanagari and Latin sans-serif font by Ek Type, available in a single Regular weight. It was onboarded to Google Fonts on 2020-01-10 via PR #2303 ("gotu: v2.320 added") by Marc Foley, taken from the upstream release v2.32 at https://github.com/EkType/Gotu. The upstream repository contains only VFB (FontLab) sources, TTX files, and OpenType feature code -- no gftools-builder compatible sources (.glyphs, .ufo, .designspace). The repo has a single commit.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Gotu |
| Designer          | Ek Type |
| Repository URL    | https://github.com/EkType/Gotu |
| Commit Hash       | c02f2e586ef16daf60d2ed11fd0fd85c1aa5e403 |
| Branch            | master |
| Config YAML       | N/A (VFB-only sources) |
| Date Added        | 2020-01-10 |
| Status            | **no_config_possible** |
| Confidence        | HIGH |

## Investigation Details

### Onboarding History

Gotu was onboarded to Google Fonts via PR #2303, authored by Marc Foley and merged on 2020-01-14. The commit message and PR body explicitly state:

> "Taken from the upstream repo https://github.com/EkType/Gotu from release https://github.com/EkType/Gotu/releases/tag/2.32"

The release v2.32 was published on 2020-01-09 with a single asset: `Gotu.2.320.zip`. The release targets the `master` branch.

Commit in google/fonts: `ff7191617554f9d0857875625c4080402ffa72f9`

The TTF file has not been modified since the original onboarding.

### Upstream Repository Analysis

The upstream repository `EkType/Gotu` has a **single commit**:

- `c02f2e5` (2020-01-10) - "Minor changes." by Girish Dalvi

The repository contains:
- `Source/VFB/Gotu.vfb` - FontLab VFB source (proprietary format)
- `Source/features` - OpenType feature code
- `Source/FontMenuNameDB`, `GDEF`, `GPOS`, `GSUB`, `Groups`, `GlyphOrderAndAliasDB`, `tables` - AFDKO build files
- `TTX/Gotu-Regular.ttx` - TTX dump of the font
- `AUTHORS.txt`, `CONTRIBUTORS.txt`, `Copyright.txt`, `OFL.txt`, `README.md`
- `Promotion/Gotu_header.png` - Promotional image

**No gftools-builder compatible sources** exist. The VFB format is FontLab's proprietary binary format, not compatible with gftools-builder. The AFDKO source files and TTX could theoretically be used for building, but not via gftools-builder's standard pipeline.

### Release Information

Three releases exist:
- v1.000 (earliest)
- v2.3
- v2.32 (latest, used for onboarding)

The v2.32 release was published on 2020-01-09, one day before the commit (`c02f2e5` dated 2020-01-10). This suggests the release was created first from a pre-commit state, and the "Minor changes" commit was pushed afterward. Since the repo has only one commit, the commit represents the full repository state, and this is the correct reference.

### Previous Onboarding Attempt

A closed PR #6682 ("Gotu: Version 2.320;hotconv 1.0.109;makeotfexe 2.5.65596; ttfautohint (v1.8.1) added") by eliheuer attempted to update Gotu using gftools-packager, but the commit reference URL was incomplete (ending in `/commit/.`). This PR was closed without merging on 2023-09-08.

### Description Update

PR #6725 by eliheuer (merged 2023-09-19) updated the Gotu description to fix a broken repo link.

### Source Block Status

The METADATA.pb on the main branch of google/fonts does not currently have a source block.

## Conclusion

Gotu's upstream repository is confirmed as `EkType/Gotu` at commit `c02f2e5`. The repository contains only VFB (FontLab) sources and AFDKO build files, which are not compatible with gftools-builder. A config.yaml is not possible. The status is **no_config_possible**.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/EkType/Gotu"
  commit: "c02f2e586ef16daf60d2ed11fd0fd85c1aa5e403"
  branch: "master"
}
```

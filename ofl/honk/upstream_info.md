# Investigation Report: Honk

## Summary

Honk is a variable color display font designed by Ek Type, licensed under OFL. It was onboarded via gftools-packager in November 2023 (PR #6961) from the upstream repository at `https://github.com/EkType/Honk`. The METADATA.pb source block is complete with repository_url, commit hash, config_yaml, file mappings, and branch. The font has two custom axes (MORF and SHLN) and uses COLRv1 technology.

## Key Findings

| Field              | Value                                              |
|--------------------|----------------------------------------------------|
| Family Name        | Honk                                               |
| Designer           | Ek Type                                            |
| License            | OFL                                                |
| Directory          | ofl/honk                                           |
| Repository URL     | https://github.com/EkType/Honk                     |
| Commit Hash        | 99094d4f6e3e73745fe3f2a6387d56c19d2a04cd           |
| Original Onboarding Commit | 964739fca4b7f5485b21525df1e803fffbe6da99  |
| Config YAML        | sources/config.yaml                                |
| Status             | **needs_correction**                               |
| Confidence         | MEDIUM                                             |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/honk/METADATA.pb` has a comprehensive source block:

```
source {
  repository_url: "https://github.com/EkType/Honk"
  commit: "99094d4f6e3e73745fe3f2a6387d56c19d2a04cd"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Honk[MORF,SHLN].ttf"
    dest_file: "Honk[MORF,SHLN].ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

The font has two variable axes (MORF: 0-45, SHLN: 0-100) and a registry default override for MORF at 15.0.

### Git History in google/fonts

Key commits:

1. **b95114c98** (2023-11-15) by Yanone: "[gftools-packager] Honk: Version 1.000 added"
   - Commit body states: "Honk Version 1.000 taken from the upstream repo https://github.com/EkType/Honk at commit https://github.com/EkType/Honk/commit/964739fca4b7f5485b21525df1e803fffbe6da99"
   - Added the font binary, METADATA.pb (with commit 964739f), OFL.txt, DESCRIPTION, and upstream.yaml
2. **116fde266** (2023-11-16) by Rosalie Wagner: "Merge pull request #6961 from google/gftools_packager_ofl_honk"
3. **1f98594e2** (2023-11-15) by Yanone: "Update METADATA.pb" -- added registry_default_overrides
4. **66f91f10f** (2024-04-03) by Simon Cozens: "Merge upstream.yaml into METADATA.pb" -- moved file mappings from upstream.yaml into METADATA.pb source block
5. **19cdcec59** (2025-03-31) by Felipe Sanches: "[Batch 1/4] port info from fontc_crater targets list" -- **changed commit hash from 964739f to 99094d4** and added config_yaml field
6. **074b85abe** (2025-01-14) by Emma Marichal: "Honk" -- updated DESCRIPTION.en_us.html
7. **6be7efb62** (2025-02-06) by Emma Marichal: "Honk update" -- further DESCRIPTION update

### Commit Hash Discrepancy

The original gftools-packager onboarding (commit b95114c98) explicitly referenced upstream commit `964739fca4b7f5485b21525df1e803fffbe6da99`. However, the batch port commit (19cdcec59) changed it to `99094d4f6e3e73745fe3f2a6387d56c19d2a04cd`.

Examining the upstream repo:
- **99094d4** (2024-07-08): "Merge pull request #17 from EkType/dependabot/pip/certifi-2024.7.4" -- this is a **dependabot pip dependency update**, not a font source change
- **964739f**: Not accessible in the shallow clone (depth 1), but this was the commit explicitly referenced at onboarding time

The commit `99094d4` is from July 2024, which is 8 months AFTER the font was onboarded (November 2023). It is a dependabot security update for the `certifi` Python package, which would not affect font sources. The original commit `964739f` is the correct onboarding commit.

The batch port likely picked up the latest commit from fontc_crater targets rather than the original onboarding commit. Per policy, gftools-packager commit hashes are hints but should be cross-verified. In this case, the original packager hash (964739f) is more accurate for the onboarding, while 99094d4 may be the latest verified state but was never actually used for font compilation.

### Upstream Repository Analysis

The cached repository at `EkType/Honk` (remote: `https://github.com/EkType/Honk`) is a shallow clone with only 1 accessible commit (`99094d4`).

Source files present:
- `sources/HonkExportFile.glyphs` -- main source file referenced in config.yaml
- `sources/HonkBaseFile.glyphs` -- base design file
- `sources/config.yaml` -- gftools-builder configuration
- `sources/CustomFilter_GFLatinCore.plist`
- `sources/generatedfonts/` directory
- `fonts/variable/Honk[MORF,SHLN].ttf` -- pre-built variable font

### Config.yaml Contents

```yaml
sources:
  - HonkExportFile.glyphs
axisOrder:
  - MORF
  - SHLN
familyName: Honk
buildVariable: true
buildStatic: false
stat:
  - name: Morph
    tag: MORF
    values:
    - name: Brush
      value: 0
    - name: Ninja
      value: 5
    - name: Irregular
      value: 10
    - name: Regular
      value: 15
      flags: 2
    - name: Compressed
      value: 20
    - name: Rounded
      value: 25
    - name: Softie
      value: 30
    - name: Balloon
      value: 35
    - name: Wood
      value: 40
    - name: Flower
      value: 45
  - name: Shadow Length
    tag: SHLN
    values:
    - name: Default
      value: 0
      flags: 2
```

Well-structured configuration with axis ordering, STAT table definitions, and variable-only build flag.

## Conclusion

**Status: needs_correction**

The Honk source metadata is mostly complete but the commit hash should be corrected. The current commit `99094d4` is a dependabot dependency update from July 2024, which postdates the font's onboarding by 8 months. The original onboarding commit `964739f` (as documented in the gftools-packager message) is more appropriate. However, since the dependabot commit only changes a Python dependency and not font sources, the actual font sources at both commits are likely identical.

To verify this definitively, a full (non-shallow) clone of the Honk repo would be needed to access commit `964739f` and compare the source files. Until then, the commit hash `99094d4` is functional (the config.yaml and source files exist at that commit) but is not the historically accurate onboarding reference.

The repository_url and config_yaml fields are correct and verified.

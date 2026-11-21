# Investigation Report: Gelasio

## Summary

Gelasio is a serif typeface designed by Eben Sorkin, added to Google Fonts on 2019-12-03. It was originally onboarded as static fonts and later updated to variable fonts (Version 1.008) via gftools-packager in February 2024. The upstream repository is at `https://github.com/SorkinType/Gelasio`. The repo has been force-pushed/rewritten since the original onboarding, so the commit hash referenced in the gftools-packager message (`a6ee02d`) no longer exists. The current METADATA.pb references commit `9228e69` (set by the fontc_crater batch port), which is the current root commit after the force-push and contains binary files that are byte-identical to those in google/fonts. The source block is complete with a valid `config_yaml` path.

## Key Findings

| Field | Value |
|---|---|
| **Family Name** | Gelasio |
| **Repository URL** | https://github.com/SorkinType/Gelasio |
| **Commit Hash** | `9228e69b160d79f33950e026293f6e13ba9780d0` |
| **Config YAML** | `sources/config.yaml` |
| **Branch** | main |
| **Source Files** | `sources/Gelasio.glyphspackage`, `sources/Gelasio-Italic.glyphspackage` |
| **Status** | complete |
| **Confidence** | MEDIUM |

## Investigation Details

### Google Fonts History

1. **Initial onboarding** (2019-12-04): Commit `e23cd10a` - Static fonts added via Font Bakery Dashboard (PR #2268)
2. **Version 1.007 update** (2022-06-16): Commit `cb927e07` - Updated via gftools-packager, referencing upstream commit `bb66c796` (also no longer exists in the rewritten repo)
3. **Version 1.008 update** (2024-02-22): Commit `90eb9d28` - Updated via gftools-packager by Emma Marichal, referencing upstream commit `a6ee02d6ba3d3a038610aa0972f0d4c39b251539` (no longer exists)
4. **Batch source metadata port** (2025-03-31): Commit `19cdcec5` - Changed commit hash from `a6ee02d` to `9228e69` and added `config_yaml: "sources/config.yaml"` based on fontc_crater targets

### Upstream Repository Analysis

- **URL**: https://github.com/SorkinType/Gelasio
- **Cached at**: `upstream_repos/fontc_crater_cache/SorkinType/Gelasio/`
- **Repository was force-pushed/rewritten**: The repo currently has only 4 commits, with the root commit (`9228e69`) dated 2024-09-16, well after the google/fonts update from February 2024
- The original commit `a6ee02d` referenced by gftools-packager no longer exists
- The earlier commit `bb66c796` from the Version 1.007 update also no longer exists
- Current HEAD is `4d7a1d2` (.sc fixes, 2025-06-30) with additional African Latin & Greek support work

### Commit Verification

- Commit `9228e69` is the root commit of the rewritten repo (2024-09-16)
- Binary files at `9228e69` match google/fonts exactly:
  - `Gelasio[wght].ttf`: 168,556 bytes (SHA256: `4daecea457258c9ebeb8bc99ed3fd24353618bfad3ea4b93fa0b5d0468fc04e4`)
  - `Gelasio-Italic[wght].ttf`: 174,212 bytes
- The `sources/config.yaml` exists at this commit with valid gftools-builder configuration
- Sources are `.glyphspackage` files: `Gelasio.glyphspackage` and `Gelasio-Italic.glyphspackage`

### Config YAML

The config at `sources/config.yaml` references:
- `Gelasio.glyphspackage`
- `Gelasio-Italic.glyphspackage`
- Axis order: wght, ital
- Family name: Gelasio
- buildOTF: False
- Includes STAT table configuration

### Confidence Note

Confidence is MEDIUM because the upstream repo was force-pushed and the original commit hash no longer exists. The current commit `9228e69` was set by the fontc_crater batch port and contains matching binary files, but it is NOT the original onboarding commit. It is the best available reference after the repo rewrite. The actual onboarding commit was `a6ee02d` (from the gftools-packager message), which was lost during the force-push.

## Conclusion

The METADATA.pb source block is complete and functional. The commit `9228e69` is the best available reference given the force-pushed repo history, and the binary files match. No changes needed.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/SorkinType/Gelasio"
  commit: "9228e69b160d79f33950e026293f6e13ba9780d0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gelasio[wght].ttf"
    dest_file: "Gelasio[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Gelasio-Italic[wght].ttf"
    dest_file: "Gelasio-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: MEDIUM (repo was force-pushed; commit is best available, not original)

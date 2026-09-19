# Investigation Report: Genos

## Summary

Genos is a sans-serif display typeface designed by Robert Leuschke, supporting Latin, Latin Extended, Vietnamese, and Cherokee scripts. It was added to Google Fonts on 2021-10-08 as a variable font (Version 1.010) via gftools-packager (PR #3934). The upstream repository is at `https://github.com/googlefonts/genos`. The commit hash `7071818` referenced in METADATA.pb matches the gftools-packager message and is the only commit in the repo. The config file at `sources/config.yml` (note: `.yml` extension, not `.yaml`) exists at that commit. The source block is complete.

## Key Findings

| Field | Value |
|---|---|
| **Family Name** | Genos |
| **Repository URL** | https://github.com/googlefonts/genos |
| **Commit Hash** | `707181862a0fe1ceecc334bb54c63ea4377e95d8` |
| **Config YAML** | `sources/config.yml` |
| **Branch** | master |
| **Source Files** | `sources/Genos.glyphs`, `sources/Genos-Italic.glyphs` |
| **Status** | complete |
| **Confidence** | HIGH |

## Investigation Details

### Google Fonts History

1. **Initial onboarding** (2021-10-11): Commit `200bfba5` - `Genos: Version 1.010 added` (PR #3934)
   - gftools-packager message references: `https://github.com/googlefonts/genos` at commit `707181862a0fe1ceecc334bb54c63ea4377e95d8`
   - Author: Viviana Monsalve (viviana.monsalve.a@gmail.com)
2. **Batch source metadata port** (2025-03-31): Commit `19cdcec5` - Added source block data from fontc_crater targets

### Upstream Repository Analysis

- **URL**: https://github.com/googlefonts/genos
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/genos/`
- **Default branch**: master
- **Total commits**: 1 (single initial commit)
- **Only commit**: `7071818` (2021-10-08, "requirements updated")

### Commit Verification

- Commit `7071818` is the only commit in the repository
- It was created on 2021-10-08, three days before the google/fonts merge on 2021-10-11
- Binary files at this commit match google/fonts exactly:
  - `Genos[wght].ttf`: 135,320 bytes
  - `Genos-Italic[wght].ttf`: 144,248 bytes
- The gftools-packager message confirms this is the correct commit

### Config YAML

The config at `sources/config.yml` (note `.yml` extension) contains:
- Sources: `Genos.glyphs`, `Genos-Italic.glyphs`
- Axis order: wght, ital
- Family name: Genos
- Includes STAT table configuration for both Roman and Italic variable fonts
- Weight axis ranges from Thin (100) to Black (900)

### Source Files at Referenced Commit

- `sources/Genos.glyphs` - Glyphs source (upright)
- `sources/Genos-Italic.glyphs` - Glyphs source (italic)
- `sources/config.yml` - gftools-builder config

### Notes

- The config file uses the `.yml` extension rather than the more common `.yaml` extension, which is correctly reflected in the METADATA.pb `config_yaml` field
- The repo has only a single commit, which is the one referenced in METADATA.pb, making verification straightforward
- The default branch is `master` (not `main`), which is correctly reflected in METADATA.pb

## Conclusion

The METADATA.pb source block is complete and accurate. All fields are verified: the repository URL is valid, the commit hash exists and is the only commit in the repo, the config_yaml path correctly uses `.yml` extension, the branch is correctly set to `master`, and the binary files match. No changes needed.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/googlefonts/genos"
  commit: "707181862a0fe1ceecc334bb54c63ea4377e95d8"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Genos[wght].ttf"
    dest_file: "Genos[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Genos-Italic[wght].ttf"
    dest_file: "Genos-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status**: complete
**Confidence**: HIGH

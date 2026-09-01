# Investigation: Georama

## Summary

Georama is a variable-width sans-serif typeface designed by Production Type, onboarded to Google Fonts in July 2020 (v1.000) and updated to v1.001 in May 2021. The METADATA.pb source block is already complete with a correct repository URL, commit hash, and config_yaml path.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Georama |
| **Designer**      | Production Type |
| **Repository URL**| https://github.com/productiontype/Georama |
| **Commit Hash**   | `1b063b6256c228a56d13b8b2f8f1d807f41467f8` |
| **Config YAML**   | `sources/builder.yaml` |
| **Branch**        | master |
| **Status**        | complete |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Current State

The source block is already fully populated:
- `repository_url`: https://github.com/productiontype/Georama
- `commit`: 1b063b6256c228a56d13b8b2f8f1d807f41467f8
- `config_yaml`: sources/builder.yaml
- `branch`: master
- File mappings for OFL.txt, DESCRIPTION, and both variable font files

### Onboarding History in google/fonts

1. **Initial onboarding** (PR #2578, commit `d8f2f5f8f`, 2020-07-29): Georama 1.000 added by Yanone. Included variable fonts and static instances.
2. **Version 1.001 update** (PR #3358, commit `d9733b43f`, 2021-05-21): Updated via gftools-packager. Commit message explicitly states: "Georama Version 1.001 taken from the upstream repo https://github.com/productiontype/Georama.git at commit https://github.com/productiontype/Georama/commit/1b063b6256c228a56d13b8b2f8f1d807f41467f8." Static instances were removed in this update.
3. **Source info added** (commit `f766d186a`, 2025-04-02): Felipe Sanches added the source block referencing PR #3358.

### Upstream Repository Verification

The upstream repo at `upstream_repos/fontc_crater_cache/productiontype/Georama` contains:
- Only a single commit: `1b063b625` ("Added family name to builder.yaml") dated 2021-05-20
- This commit hash matches exactly what is recorded in METADATA.pb
- The repo is on the `master` branch

### Source Files

The upstream repo contains proper gftools-builder compatible sources:
- `sources/Georama.designspace` (Roman)
- `sources/Georama-Italic.designspace` (Italic)
- Multiple UFO master files (4 Roman masters, 4 Italic masters)
- `sources/builder.yaml` config file

### Config YAML Content

```yaml
sources:
  - Georama.designspace
  - Georama-Italic.designspace
axisOrder:
  - wdth
  - wght
  - ital
familyName: Georama
includeSourceFixes: true
buildVariable: true
buildStatic: false
buildOTF: false
outputDir: "../fonts"
```

### Commit Hash Verification

The commit `1b063b625` is the only commit in the upstream repo, and it was made on 2021-05-20, one day before the google/fonts PR #3358 was merged on 2021-05-21. The gftools-packager message in the commit body explicitly references this exact commit. The binary font files at this commit match in size with the files in google/fonts. **Confidence: HIGH**.

## Conclusion

The METADATA.pb source block for Georama is already complete and accurate. No changes needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/productiontype/Georama"
  commit: "1b063b6256c228a56d13b8b2f8f1d807f41467f8"
  config_yaml: "sources/builder.yaml"
  files {
    source_file: "ofl.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Georama[wdth,wght].ttf"
    dest_file: "Georama[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/Georama-Italic[wdth,wght].ttf"
    dest_file: "Georama-Italic[wdth,wght].ttf"
  }
  branch: "master"
}
```

**Status**: complete
**Confidence**: HIGH

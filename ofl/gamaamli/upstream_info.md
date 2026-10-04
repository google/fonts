# Investigation Report: Ga Maamli

## Summary

Ga Maamli is a display sans-serif typeface designed by Afotey Clement Nii Odai, Ama Diaka, and David Abbey-Thompson. It was onboarded to Google Fonts on June 6, 2024, by Emma Marichal. The upstream repository at `SorkinType/GaMaamli` has a complete source block already recorded in METADATA.pb with the correct commit hash, config.yaml path, and repository URL. The source block is fully accurate and complete.

## Key Findings

| Field             | Value                                                    |
|-------------------|----------------------------------------------------------|
| Family Name       | Ga Maamli                                                |
| Repository URL    | https://github.com/SorkinType/GaMaamli                   |
| Commit Hash       | aed1210a08dacfa86e419caf81fdb42940ee4e2a                 |
| Config Path       | sources/config.yaml                                      |
| Source Files      | sources/GaMaamli.glyphs                                  |
| Status            | **complete**                                             |
| Confidence        | **HIGH**                                                 |

## Investigation Details

### METADATA.pb Analysis

The existing METADATA.pb already contains a fully populated source block:
- `repository_url`: `https://github.com/SorkinType/GaMaamli`
- `commit`: `aed1210a08dacfa86e419caf81fdb42940ee4e2a`
- `config_yaml`: `sources/config.yaml`
- `branch`: `main`
- File mappings for OFL.txt, GaMaamli-Regular.ttf, and DESCRIPTION.en_us.html

### Onboarding Commit (google/fonts)

- **Commit**: `e25c9cf5f5dec0b076976b463cd9aac32c592bb6`
- **Date**: 2024-06-06
- **Author**: Emma Marichal
- **Message**: "Ga Maamli: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added"
- **Body**: Explicitly states "Taken from the upstream repo https://github.com/SorkinType/GaMaamli at commit https://github.com/SorkinType/GaMaamli/commit/aed1210a08dacfa86e419caf81fdb42940ee4e2a"

### Upstream Repository Verification

The upstream repo `SorkinType/GaMaamli` was inspected from the local cache at `upstream_repos/fontc_crater_cache/SorkinType/GaMaamli/`.

- **Total commits**: 1 (the merge commit on main)
- **HEAD commit**: `aed1210a08dacfa86e419caf81fdb42940ee4e2a` (2024-06-05) - "Merge pull request #5 from emmamarichal/main"
- The commit matches exactly what is recorded in METADATA.pb
- The commit date (June 5, 2024) is one day before the google/fonts onboarding (June 6, 2024), confirming chronological consistency

### Source Files and Config

- **Source file**: `sources/GaMaamli.glyphs` (Glyphs format)
- **Config file**: `sources/config.yaml` exists and contains:
  ```yaml
  sources:
    - GaMaamli.glyphs
  familyName: Ga Maamli
  buildOTF: false
  ```
- The config is a standard gftools-builder configuration

### Additional History

Commit `19cdcec59` in google/fonts ("[Batch 1/4] port info from fontc_crater targets list") also modified the METADATA.pb, adding the source block information that was ported from fontc_crater targets.

## Conclusion

The Ga Maamli source metadata is fully complete and accurate. The repository URL, commit hash, and config.yaml path are all correctly recorded. No changes needed.

### Recommended METADATA.pb Source Block

The existing source block is correct:

```
source {
  repository_url: "https://github.com/SorkinType/GaMaamli"
  commit: "aed1210a08dacfa86e419caf81fdb42940ee4e2a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/GaMaamli-Regular.ttf"
    dest_file: "GaMaamli-Regular.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH

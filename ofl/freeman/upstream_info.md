# Investigation Report: Freeman

## Summary

Freeman is a display sans-serif font designed by Rodrigo Fuenzalida, Aoife Mooney, and Vernon Adams, added to Google Fonts on 2024-04-11. The upstream repository at `rfuenzalida/Freeman` contains a single commit which is both HEAD and the commit referenced in METADATA.pb. The source block is fully populated with repository URL, commit hash, branch, config_yaml, archive_url, and file mappings. The upstream repo has a `sources/config.yaml` with gftools-builder configuration and `.glyphs` source files.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Freeman |
| Upstream Repo | https://github.com/rfuenzalida/Freeman |
| Commit Hash | `5ced8a95f5b0e0c3dcea3b033398ba93a56fb687` |
| Branch | master |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Source Files | `sources/Freeman.glyphs` |
| Status | **complete** |
| Confidence | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/rfuenzalida/Freeman"
  commit: "5ced8a95f5b0e0c3dcea3b033398ba93a56fb687"
  archive_url: "https://github.com/rfuenzalida/Freeman/releases/download/v1.000/Freeman-v1.000.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Freeman-Regular.ttf"
    dest_file: "Freeman-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

### Onboarding History in google/fonts

The font was onboarded in commit `88622a74c` (2024-04-11) by Viviana Monsalve with the message:

> Freeman: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added
> Taken from the upstream repo https://github.com/rfuenzalida/Freeman/master at commit https://github.com/rfuenzalida/Freeman/master/commit/5ced8a95f5b0e0c3dcea3b033398ba93a56fb687.
> Resolves #3121

The `config_yaml` field was added later in commit `19cdcec59` (2025-03-31, Batch 1/4 fontc_crater targets).

### Commit History in google/fonts for ofl/freeman/

1. `88622a74c` (2024-04-11) - Initial onboarding: Freeman v1.000
2. `b8c135d9f`, `211fc80fc`, `4a9de91c3` - DESCRIPTION updates
3. `d9c21eaf7` (2024-04-11) - METADATA.pb update
4. `6ca55c9ae` - OFL license URL update
5. `19cdcec59` (2025-03-31) - Added `config_yaml: "sources/config.yaml"`

### Upstream Repository Analysis

- **URL**: https://github.com/rfuenzalida/Freeman
- **Cached at**: `upstream_repos/fontc_crater_cache/rfuenzalida/Freeman`
- **Default branch**: master
- **Total commits**: 1 (single commit repo)
- **HEAD**: `5ced8a95f5b0e0c3dcea3b033398ba93a56fb687` (2024-04-11)

The entire repository was created in a single initial commit on the same day as the Google Fonts onboarding.

### Commit Hash Verification

The commit hash `5ced8a95f5b0e0c3dcea3b033398ba93a56fb687` is verified correct:

1. It is the only commit in the repo and matches HEAD
2. It is explicitly referenced in the google/fonts onboarding commit message
3. The upstream commit date (2024-04-11) matches the google/fonts onboarding date (2024-04-11)
4. The font binary at `fonts/ttf/Freeman-Regular.ttf` in the upstream repo is 241,164 bytes, matching the binary added to google/fonts

### Source Files and Build Configuration

The upstream repo contains:
- `sources/Freeman.glyphs` - Glyphs source file
- `sources/Legacy-source/` - Legacy source files (FrancoisOne.glyphs, Freeman.glyphs, Legacy-Freeman.glyphs)
- `sources/config.yaml` - gftools-builder configuration

Config.yaml contents:
```yaml
sources:
  - Freeman.glyphs
familyName: "Freeman"
buildVariable: false
```

No local override config.yaml exists in google/fonts.

## Conclusion

The source block in METADATA.pb is complete and correct. All fields (repository_url, commit, archive_url, files, branch, config_yaml) are properly set. No changes are needed.

### Recommended METADATA.pb Source Block

No changes required. The existing source block is correct:

```
source {
  repository_url: "https://github.com/rfuenzalida/Freeman"
  commit: "5ced8a95f5b0e0c3dcea3b033398ba93a56fb687"
  archive_url: "https://github.com/rfuenzalida/Freeman/releases/download/v1.000/Freeman-v1.000.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Freeman-Regular.ttf"
    dest_file: "Freeman-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH

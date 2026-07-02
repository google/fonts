# Dongle

## Summary

Dongle is a Korean sans-serif font by Yanghee Ryu available in Light, Regular, and Bold weights. It has complete source documentation with a repository URL, commit hash, and an override config.yaml in the google/fonts directory.

## Key Findings

| Field | Value |
|-------|-------|
| **Family Name** | Dongle |
| **Designer** | Yanghee Ryu |
| **License** | OFL |
| **Date Added** | 2021-06-14 |
| **Repository URL** | https://github.com/yangheeryu/Dongle |
| **Commit Hash** | `f7127c4d2450e1cad20254ec692591347e2fc260` |
| **Config YAML** | Override in google/fonts (`ofl/dongle/config.yaml`) |
| **Status** | complete |

## Investigation Details

### Onboarding History

Dongle v2.000 was added to Google Fonts via PR #3530 (commit `388be86af`) by Aaron Bell on 2021-06-22. The PR commit message states: "Dongle Version 2.000 taken from the upstream repo https://github.com/yangheeryu/Dongle.git at commit https://github.com/yangheeryu/Dongle/commit/71cc5162a79d65b3b9b5ad70398473152ce59ab9."

The source block and override config.yaml were later added in commit `5f31230ff` ("sources info for Dongle: Version 2.000 (PR #3530)").

### Upstream Repository

The upstream repo at https://github.com/yangheeryu/Dongle contains:
- `sources/Dongle.zip` - source files in a zip archive
- `fonts/ttf/` - compiled TTF files (Dongle-Light.ttf, Dongle-Regular.ttf, Dongle-Bold.ttf)
- No config.yaml in the upstream repo

The HEAD commit is `f7127c4` ("Update README.md"), which matches the METADATA.pb. The original onboarding was at commit `71cc516`, but the 3 commits between then and HEAD are only README/DESCRIPTION updates - no source or font changes.

### Commit Hash Analysis

The source files (`sources/Dongle.zip`) were last modified at commit `dbd7f34` ("Updated font metrics to match original"), which is earlier than both the onboarding commit (`71cc516`) and the recorded commit (`f7127c4`). Using HEAD is acceptable since no source changes occurred after onboarding.

### Config YAML

The METADATA.pb uses a `files` block to copy pre-compiled TTFs directly from the upstream repo (not rebuilding from sources). An override config.yaml exists in `ofl/dongle/config.yaml`:
```yaml
buildVariable: false
sources:
  - sources/Dongle.zip
```

Since the override config.yaml exists in the google/fonts directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Conclusion

Dongle is fully documented. The source block has the correct repository URL and commit hash. The override config.yaml in the google/fonts directory provides the build configuration. No further action needed.

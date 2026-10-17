# Investigation Report: Gluten

## Summary

Gluten is a display/handwriting variable font designed by Tyler Finck (ETC / Etcetera Type Company), added to Google Fonts on 2021-09-02. The upstream repository is `Etcetera-Type-Co/Gluten` on GitHub. The METADATA.pb source block is already complete with the correct repository URL, commit hash, branch, config path, and file mappings. No changes are needed.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Gluten                                                             |
| Designer          | Tyler Finck, ETC                                                   |
| Date Added        | 2021-09-02                                                         |
| Repository URL    | https://github.com/Etcetera-Type-Co/Gluten                        |
| Commit Hash       | c8525e6a8d31dde1795485cc66f622beed3e5e80                           |
| Branch            | master                                                             |
| Config Path       | Sources/config.yaml                                                |
| Source Files      | Gluten.glyphs (in Sources/)                                        |
| Status            | **complete**                                                       |
| Confidence        | **HIGH**                                                           |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a fully populated `source { }` block with:
- `repository_url`: `https://github.com/Etcetera-Type-Co/Gluten`
- `commit`: `c8525e6a8d31dde1795485cc66f622beed3e5e80`
- `branch`: `master`
- `config_yaml`: `Sources/config.yaml` (note the capital "S" in Sources)
- File mappings for OFL.txt and the variable font file

### Onboarding History in google/fonts

Initial onboarding was via commit `846eb7f39` (PR #3591) on 2021-09-03 by Rosalie Wagner:
- Commit message: "Gluten: Version 1.204 added"
- Referenced upstream at commit `e795b999daf6103f003891d2696282bf54e76ca4`
- Original font file: `Gluten[wght].ttf` (weight axis only)

The font was later updated via commit `d91618169` (PR #4716) on 2022-05-25 by Rosalie Wagner:
- Commit message: "[gftools-packager] Gluten: Version 1.300 added"
- Referenced upstream at commit `c8525e6a8d31dde1795485cc66f622beed3e5e80`
- Updated font file: `Gluten[slnt,wght].ttf` (added slant axis)
- This is the current version in google/fonts

A subsequent fix was made in commit `7190093b1` (2025-05-22) to correct the config_yaml path from `sources/config.yaml` to `Sources/config.yaml` (uppercase S), matching the actual directory name in the upstream repo.

### Upstream Repository Verification

The cached repo at `upstream_repos/fontc_crater_cache/Etcetera-Type-Co/Gluten/` confirms:
- Remote URL: `https://github.com/Etcetera-Type-Co/Gluten`
- Commit `c8525e6` exists and is the HEAD of `master` branch (the latest commit)
- Commit message: "Merge pull request #5 from RosaWagner/master" dated 2022-05-19
- The commit is 6 days before the google/fonts merge (2022-05-25), which is a normal timeline

### Config and Source Files

At commit `c8525e6`:
- `Sources/config.yaml` exists with valid gftools-builder configuration (note the capital "S")
- Source: `Gluten.glyphs`
- Config specifies `axisOrder: [slnt, wght]` and `familyName: Gluten`
- Output directory: `../fonts`
- STAT table entries for Slant and Weight axes

### Commit Hash Cross-Verification

The commit hash `c8525e6` in METADATA.pb matches exactly what the gftools-packager commit message for PR #4716 references. This is the update commit (Version 1.300), not the initial onboarding. The commit is HEAD of master, and its date (2022-05-19) predates the google/fonts merge date (2022-05-25) by 6 days.

## Conclusion

The Gluten source block in METADATA.pb is complete and accurate. All fields (repository_url, commit, branch, config_yaml, file mappings) are correctly set. The uppercase `Sources/config.yaml` path was corrected in a previous fix (commit `7190093b1`). No further changes are needed.

### Current METADATA.pb Source Block (no changes needed)

```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Gluten"
  commit: "c8525e6a8d31dde1795485cc66f622beed3e5e80"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gluten[slnt,wght].ttf"
    dest_file: "Gluten[slnt,wght].ttf"
  }
  branch: "master"
  config_yaml: "Sources/config.yaml"
}
```

**Status: complete**

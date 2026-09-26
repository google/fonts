# Investigation Report: Host Grotesk

## Summary

Host Grotesk is a sans-serif variable font (wght 300-800) with both upright and italic styles, designed by Element Type, Dogukan Karapinar, and Ibrahim Kactioglu. It was onboarded to Google Fonts on 2024-10-10. The upstream repository is at `github.com/Element-Type/HostGrotesk`. The METADATA.pb has a complete source block with repository URL, commit hash, config_yaml path, and an archive_url for the release. However, the onboarding commit message references a different commit hash (`4f267d3`) than what is currently in METADATA.pb (`ab2ba67`). The original commit `4f267d3` no longer exists in the upstream repository, which appears to have been force-pushed (the repo has only a single commit from a merge PR). The current METADATA.pb commit `ab2ba67` is the only commit in the repo and post-dates the onboarding (2024-11-13 vs 2024-10-10), indicating a correction was made. The source block references `sources/config.yaml`, which exists and is valid.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Host Grotesk |
| Repository URL | https://github.com/Element-Type/HostGrotesk |
| Commit Hash (METADATA.pb) | ab2ba6769119e7ae71aa2fab46eedcb993c670a3 |
| Commit Hash (onboarding msg) | 4f267d366fec1961bb219fe156fe7b4821ce8a15 |
| Config YAML | sources/config.yaml |
| Config Exists at Commit | Yes |
| Source Files | sources/HostGrotesk.glyphs, sources/HostGrotesk-Italic.glyphs |
| Date Added | 2024-10-03 |
| Status | needs_correction |
| Confidence | LOW |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains a complete source block:
- `repository_url`: `https://github.com/Element-Type/HostGrotesk`
- `commit`: `ab2ba6769119e7ae71aa2fab46eedcb993c670a3`
- `archive_url`: `https://github.com/Element-Type/HostGrotesk/releases/download/1.002/HostGrotesk-1.002.zip`
- `config_yaml`: `sources/config.yaml`
- `branch`: `main`
- File mappings for OFL.txt, variable TTFs from `fonts/variable/`

### Upstream Repository

The repo at `github.com/Element-Type/HostGrotesk` has only a single commit:
- `ab2ba67` (2024-11-13): "Merge pull request #14 from vv-monsalve/QA-Host2" — by ibrahim

This is a merge commit that introduced the entire repository contents (all 45 files show as additions). The repository was evidently force-pushed at some point, destroying the original history. The original onboarding commit `4f267d3` no longer exists in the repo.

### Commit Hash Discrepancy

The google/fonts onboarding commit `5b5a99da9` (2024-10-10) states:
> "Taken from the upstream repo https://github.com/Element-Type/HostGrotesk at commit https://github.com/Element-Type/HostGrotesk/commit/4f267d366fec1961bb219fe156fe7b4821ce8a15."

However, the current METADATA.pb references `ab2ba67` (dated 2024-11-13), which is approximately one month after the onboarding date. This commit was set by the fontc_crater batch update on 2025-03-31 (`19cdcec59`). Since the repo was force-pushed and only has one commit, the batch update picked the only available commit.

### Binary Files

The METADATA.pb source block references files from `fonts/variable/` but no such directory exists in the upstream repo at commit `ab2ba67`. The font binaries were obtained via the `archive_url` pointing to the GitHub release `1.002`. The source block's `files {}` mappings appear to reference the release archive contents, not the repo tree.

### Config YAML

The file `sources/config.yaml` exists at commit `ab2ba67` and contains:
```yaml
buildStatic: true
buildVariable: true
buildTTF: true
buildOTF: true
buildWebfont: true
sources:
  - HostGrotesk.glyphs
  - HostGrotesk-Italic.glyphs
axisOrder:
  - wght
familyName: Host Grotesk
```

The source files (`.glyphs`) are present in the `sources/` directory.

### Timeline

- 2024-10-10: Onboarded to google/fonts from commit `4f267d3`
- 2024-10-10 to 2024-11-13: Multiple updates (OFL, article, designers, fixes)
- 2024-11-13: Upstream repo force-pushed, resulting in single commit `ab2ba67`
- 2025-03-31: fontc_crater batch update set commit to `ab2ba67`

## Conclusion

**Status: needs_correction**

The source block is mostly complete, but the commit hash situation is problematic. The original onboarding commit `4f267d3` no longer exists in the upstream repo due to force-pushing. The current METADATA.pb commit `ab2ba67` post-dates the onboarding and is the only commit left in the repo. While the config.yaml and source files are all present at this commit, the provenance chain is broken. The `fonts/variable/` paths in the file mappings do not correspond to actual files in the repo tree -- they appear to reference the release archive. This is an unusual configuration that may need review. Confidence is LOW because the original commit is unverifiable.

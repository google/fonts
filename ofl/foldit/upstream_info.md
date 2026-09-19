# Investigation: Foldit

## Summary

| Field | Value |
|---|---|
| Family Name | Foldit |
| Designer | Sophia Tai |
| License | OFL |
| Repository URL | https://github.com/SophiaDesign/Foldit |
| Commit | 934034370b760240516ba533549436935c49fbc2 |
| Branch | main |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |
| Date Added | 2022-10-03 |

## Upstream Repository

- **URL**: https://github.com/SophiaDesign/Foldit
- **Description**: Variable Color Font using COLRv1 capabilities on Google Fonts
- **Default Branch**: main
- **Last Push**: 2024-12-10

The repository was originally named `GF-Foldit` and was later renamed to `Foldit`. The old URL (`https://github.com/SophiaDesign/GF-Foldit`) redirects to the current one. The OFL.txt and METADATA.pb copyright strings still reference the old GF-Foldit name in the URL.

## Source Files

The upstream repository contains gftools-builder compatible sources:

- `sources/config.yaml` - gftools-builder configuration
- `sources/glyphs-decomposed/Foldit.glyphs` - decomposed Glyphs source (used by config.yaml)
- `sources/Foldit-origin.glyphs` - origin Glyphs source (not used by config.yaml)

The `config.yaml` at `sources/config.yaml` builds from `./glyphs-decomposed/Foldit.glyphs` with the `wght` axis, producing only TTF (buildOTF: false).

## History in google/fonts

### Onboarding (PR #5361, merged 2022-10-06)

- **Commit**: a967ebad0378c777346605e7a120ef370230a5e6
- **Author**: Marc Foley (m4rc1e)
- **Merged by**: Rosalie Wagner (RosaWagner)
- **Closes**: Issue #5093 (Add Foldit)
- **Method**: gftools-packager, using a release archive download
- **Archive URL**: https://github.com/SophiaDesign/Foldit/releases/download/1.003/Foldit-fonts.zip

The commit message states: "Foldit Version 1.003 taken from the upstream repo https://github.com/SophiaDesign/Foldit at commit https://github.com/SophiaDesign/Foldit/commit/." -- note the empty commit hash after `/commit/`. The original onboarding did NOT record a specific commit hash; fonts were taken from the v1.003 release archive.

### Subsequent Changes

1. **81cf79f68** (PR #5845): Touch FoldIt metadata to have it reprocessed with harfbuzz fix (https://github.com/harfbuzz/harfbuzz/issues/4085) -- metadata-only change, no font binary update
2. **1db714082**: Stroke and classification metadata update
3. **6bda16478**: HTML formatter update
4. **66f91f10f**: Merge upstream.yaml into METADATA.pb (added files/branch fields)
5. **eb8de4660**: Description update by Emma Marichal
6. **6791a7644**: Another description update by Emma Marichal
7. **19cdcec59**: [Batch 1/4] port info from fontc_crater targets list -- this commit added the `commit` and `config_yaml` fields to the source block

The font binary `Foldit[wght].ttf` has only been modified once (the initial onboarding commit a967ebad0).

## Commit Hash Analysis

The commit hash currently in METADATA.pb (`934034370b760240516ba533549436935c49fbc2`) was added by the fontc_crater batch import (commit 19cdcec59 in google/fonts). This hash corresponds to the current HEAD of the upstream repository's `main` branch, dated 2024-12-10, which is a "Update README.md" commit.

### Repository History Anomaly

The upstream repository appears to have been force-pushed/squashed at some point. The current `main` branch has only a single commit (`9340343`, dated 2024-12-10), but the release tags (`1.000` through `1.003`) still reference the original full commit history. The `1.003` tag points to commit `4f1d1960651a2931a4f8d45734b38d22973e3db5` (dated 2022-09-01, "Update README.md").

The current HEAD (`9340343`) and the 1.003 tag commit (`4f1d1960`) are NOT in an ancestor-descendant relationship (the repo was squashed into one commit). However, the `sources/` directory is byte-identical between both commits (verified via md5sum), so the source files are the same.

### Which Commit is Correct?

The font binary in google/fonts was taken from the v1.003 release archive, not built from a specific source commit. The release 1.003 was created on 2022-09-01 and tagged at commit `4f1d1960651a2931a4f8d45734b38d22973e3db5`.

Since the fontc_crater target uses commit `934034370b760240516ba533549436935c49fbc2` (current HEAD) and the sources are identical at both commits, the current METADATA.pb entry is functionally correct for source building purposes. The `4f1d1960` commit would be historically more accurate as the commit associated with the 1.003 release, but since source content is identical, either works.

## Config YAML

The `config.yaml` exists in the upstream repository at `sources/config.yaml` and is present at both the 1.003 tag and the current HEAD. The METADATA.pb correctly references it as `sources/config.yaml`. No override config is needed.

## Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/SophiaDesign/Foldit"
  commit: "934034370b760240516ba533549436935c49fbc2"
  archive_url: "https://github.com/SophiaDesign/Foldit/releases/download/1.003/Foldit-fonts.zip"
  files {
    source_file: "Foldit-fonts/fonts/variable/Foldit[wght].ttf"
    dest_file: "Foldit[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Conclusion

The Foldit METADATA.pb source block is **complete** with repository URL, commit hash, config.yaml path, archive URL, file mappings, and branch. All fields are present and valid.

The only minor issue is that the commit hash (`9340343`) points to a squashed/force-pushed commit from 2024-12-10 rather than the historically accurate 1.003 release tag commit (`4f1d1960`). However, since the source files are byte-identical at both commits, this is functionally correct for fontc_crater building purposes. The status is **complete**.

No changes needed to METADATA.pb at this time.

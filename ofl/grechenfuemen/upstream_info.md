# Investigation Report: Grechen Fuemen

## Summary

Grechen Fuemen is a handwriting/display font designed by Robert Leuschke, added to Google Fonts on 2021-09-02. The upstream repository is `googlefonts/grechen-fuemen` on GitHub. The repository contains a single commit, and the METADATA.pb source block already has complete and correct data, including repository URL, commit hash, config path, file mappings, and branch.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Grechen Fuemen                                                     |
| Repository URL    | https://github.com/googlefonts/grechen-fuemen                      |
| Commit Hash       | `4e4ac4caeac05708e6b3a05f0d91d1bb0476c045`                         |
| Config Path       | `sources/config.yml`                                               |
| Source Files      | `sources/GrechenFuemen.glyphs`                                     |
| Status            | **complete**                                                       |
| Confidence        | **HIGH**                                                           |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a fully populated source block:
- `repository_url`: `https://github.com/googlefonts/grechen-fuemen`
- `commit`: `4e4ac4caeac05708e6b3a05f0d91d1bb0476c045`
- `config_yaml`: `sources/config.yml`
- `branch`: `master`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and GrechenFuemen-Regular.ttf

### Google Fonts Commit History

1. **`ac4afe52d`** (2021-09-08) - "Grechen Fuemen: Version 1.010; ttfautohint (v1.8.3) added (#3796)" by Viviana Monsalve. This was the original onboarding commit, created via gftools-packager. The commit message explicitly references the upstream repo at commit `4e4ac4caeac05708e6b3a05f0d91d1bb0476c045`.
2. **`66f91f10f`** (2024-04-03) - "Merge upstream.yaml into METADATA.pb [skip ci]" by Simon Cozens. Added the source block with repository_url, file mappings, and branch from the upstream.yaml file.
3. **`19cdcec59`** (2025-03-31) - "[Batch 1/4] port info from fontc_crater targets list" by Felipe Sanches. Added `commit` and `config_yaml` fields to the source block.

### Upstream Repository Verification

The upstream repo at `googlefonts/grechen-fuemen` is cached at `upstream_repos/fontc_crater_cache/googlefonts/grechen-fuemen/`. It contains a single commit:

- **`4e4ac4c`** (2021-08-30) - "Family name typo fixed" by Viviana Monsalve

This is the only commit in the repo, confirming this is the exact commit used for onboarding. The commit predates the google/fonts merge date (2021-09-08), which is consistent.

### Config File Verification

The config file at `sources/config.yml` contains:
```yaml
sources:
  - GrechenFuemen.glyphs
familyName: "Grechen Fuemen"
buildVariable: false
```

The source file `sources/GrechenFuemen.glyphs` exists in the repo. This is a static (non-variable) font build.

### File Mapping Verification

The upstream.yaml from the onboarding commit maps:
- `OFL.txt` -> `OFL.txt`
- `DESCRIPTION.en_us.html` -> `DESCRIPTION.en_us.html`
- `fonts/ttf/GrechenFuemen-Regular.ttf` -> `GrechenFuemen-Regular.ttf`

All source files exist at the referenced paths in the upstream repo.

## Conclusion

The METADATA.pb source block is complete and correct. No changes are needed.

### Current METADATA.pb Source Block (correct as-is)

```
source {
  repository_url: "https://github.com/googlefonts/grechen-fuemen"
  commit: "4e4ac4caeac05708e6b3a05f0d91d1bb0476c045"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GrechenFuemen-Regular.ttf"
    dest_file: "GrechenFuemen-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

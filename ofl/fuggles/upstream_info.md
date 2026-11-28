# Investigation Report: Fuggles

## Summary

Fuggles is a handwriting/display typeface designed by Robert Leuschke, added to Google Fonts on 2021-04-29. The upstream repository is at `https://github.com/googlefonts/fuggles`. The METADATA.pb already has a complete source block with repository URL, commit hash, and config_yaml. All fields verified as correct.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Fuggles |
| Designer          | Robert Leuschke |
| Repository URL    | https://github.com/googlefonts/fuggles |
| Commit Hash       | cc9766c14a1aabedb7ef7dbf3e9aa0e325542c5a |
| Config YAML       | sources/config.yml |
| Status            | **complete** |
| Confidence        | HIGH |

## Investigation Details

### Google Fonts History

The font was onboarded in commit `b5ca2d5f2` (2021-04-30) by Viviana Monsalve via PR #3354. The commit message references:
- Upstream repo: https://github.com/googlefonts/fuggles
- Original commit: `4c5e05f83e50f5eba878b69d85022283612fdb18`
- Built using gftools-packager

The source block was progressively built up:
1. Commit `f7455d788` (2023-08-15, Simon Cozens) - Added `repository_url`
2. Commit `66f91f10f` (2024-04-03, Simon Cozens) - Merged upstream.yaml into METADATA.pb, adding file mappings and branch
3. Commit `19cdcec59` (2025-03-31) - Added commit hash and config_yaml from fontc_crater targets list

### Upstream Repository

- **URL**: https://github.com/googlefonts/fuggles
- **Cached at**: `upstream_repos/fontc_crater_cache/googlefonts/fuggles`
- **Branch**: master
- **Single commit**: `cc9766c` (2021-11-16) - "Update README.md" by Dave Crossland

The repo has only one commit, meaning it was squashed or force-pushed at some point. The original onboarding commit `4c5e05f` referenced in the google/fonts commit message no longer exists. The current and only commit is `cc9766c`, which is the one recorded in METADATA.pb.

### Source Files

- `sources/Fuggles.glyphs` - Glyphs source file (7.2 MB)
- `sources/config.yml` - gftools-builder configuration

### Config YAML Verification

The config at `sources/config.yml` contains:
```yaml
sources:
  - Fuggles.glyphs
familyName: "Fuggles"
buildVariable: false
```

This is a valid gftools-builder configuration. Note the `.yml` extension (not `.yaml`).

### Commit Hash Analysis

The original onboarding referenced commit `4c5e05f` which no longer exists in the repo. The repo was likely squashed/recreated by Dave Crossland on 2021-11-16 (after onboarding on 2021-04-30). The current commit `cc9766c` is the only commit available and is the correct reference for the current state of the repository.

## Conclusion

The METADATA.pb source block is complete and correct. All fields are verified:
- Repository URL is valid and cached
- Commit hash `cc9766c` is the only commit in the repo (original was force-pushed away)
- Config YAML path `sources/config.yml` is correct (note `.yml` extension)
- Branch is correctly set to `master`

### Current METADATA.pb source block (verified correct)

```
source {
  repository_url: "https://github.com/googlefonts/fuggles"
  commit: "cc9766c14a1aabedb7ef7dbf3e9aa0e325542c5a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Fuggles-Regular.ttf"
    dest_file: "Fuggles-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

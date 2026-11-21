# Investigation: Inter Tight

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inter Tight |
| Slug | inter-tight |
| License Dir | ofl |
| Repository URL | https://github.com/rsms/inter-gf-tight |
| Commit Hash | c194f94c60b569b47876811321f5ef1f0c2614a2 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/rsms/inter-gf-tight"
  commit: "c194f94c60b569b47876811321f5ef1f0c2614a2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/InterTight[wght].ttf"
    dest_file: "InterTight[wght].ttf"
  }
  files {
    source_file: "fonts/variable/InterTight-Italic[wght].ttf"
    dest_file: "InterTight-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font was most recently updated in google/fonts by commit `fac60545c` ("Inter Tight: Version 3.004 added (#5681)"). The commit body confirms:

> Inter Tight Version 3.004 taken from the upstream repo https://github.com/rsms/inter-gf-tight at commit https://github.com/rsms/inter-gf-tight/commit/c194f94c60b569b47876811321f5ef1f0c2614a2.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/rsms/inter-gf-tight`. The commit `c194f94c60b569b47876811321f5ef1f0c2614a2` was verified to exist in the cached repo (2022-12-08, "very quick fix on some obvious spacing issues in Greek script"). This is the **only commit** in the repository.

**Source format**: The repository contains `sources/InterTight.glyphs` and `sources/InterTight-Italic.glyphs` (Glyphs format). A `config.yaml` exists at `sources/config.yaml` with content:
```yaml
sources:
    - InterTight.glyphs
    - InterTight-Italic.glyphs
buildOTF: False
axisOrder:
    - wght
    - ital
familyName: Inter Tight
```

The `config_yaml: "sources/config.yaml"` in METADATA.pb is correctly set and matches the file in the upstream repo.

The copyright notice references `https://github.com/rsms/inter-tight` which is a different repository name than the actual repo used (`inter-gf-tight`). This discrepancy is noted but does not affect the source tracking.

Note: The font was also updated in earlier commits `0f620f526` (Version 3.003) and `87338f0ad` (Version 3.002). The current METADATA.pb commit `c194f94c` corresponds to the latest version (3.004).

## Conclusion

The source block is complete and correct. The `repository_url`, `commit`, and `config_yaml` are all verified. The commit `c194f94c` exists in the cached repository and is the only commit in the `inter-gf-tight` repo. No changes needed.

# Investigation: K2D

## Summary

| Field | Value |
|-------|-------|
| Family Name | K2D |
| Slug | k2d |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/K2D |
| Commit Hash | 5df785dc3b0d17e7b57eedb2f4139436dbeb6440 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/K2D"
  commit: "5df785dc3b0d17e7b57eedb2f4139436dbeb6440"
}
```

## Investigation

The METADATA.pb for K2D has a source block with `repository_url` and `commit` but no `config_yaml` field. The upstream repository is `https://github.com/cadsondemak/K2D`, maintained by Cadson Demak.

The commit hash `5df785dc3b0d17e7b57eedb2f4139436dbeb6440` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/cadsondemak/K2D/`. This is a merge commit ("Merge pull request #7 from m4rc1e/metrics", dated 2018-08-23) that updated vertical metrics to stop first line clipping.

At the referenced commit, the repository contains `source/K2D.glyphs` — the gftools-builder compatible Glyphs source file. The upstream repo does NOT contain a `config.yaml` at this commit.

An override `config.yaml` exists in the google/fonts `ofl/k2d/` directory with content:

```yaml
buildVariable: false
sources:
  - source/K2D.glyphs
```

This correctly references `source/K2D.glyphs` which is present at the referenced commit. Per project policy, the `config_yaml` field is omitted from METADATA.pb when an override `config.yaml` exists in the google/fonts family directory, and the google-fonts-sources tool auto-detects the local override.

The copyright string in the font confirms the repository URL: "Copyright 2018 The K2D Project Authors (https://github.com/cadsondemak/K2D)".

## Conclusion

K2D is in a complete state. The METADATA.pb has `repository_url` and `commit` correctly set. A valid override `config.yaml` exists in google/fonts referencing `source/K2D.glyphs` which exists at the referenced commit. No `config_yaml` is needed in METADATA.pb. No action needed.

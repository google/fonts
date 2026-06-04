# Investigation: Kadwa

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kadwa |
| Slug | kadwa |
| License Dir | ofl |
| Repository URL | https://github.com/solmatas/Kadwa |
| Commit Hash | ec58500fc2026ed3125a609b8c617b4b0c4bce20 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/solmatas/Kadwa"
  commit: "ec58500fc2026ed3125a609b8c617b4b0c4bce20"
}
```

## Investigation

The METADATA.pb for Kadwa has a source block with `repository_url` and `commit` but no `config_yaml` field. The upstream repository is `https://github.com/solmatas/Kadwa`, authored by Sol Matas (Huerta Tipográfica).

The commit hash `ec58500fc2026ed3125a609b8c617b4b0c4bce20` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/solmatas/Kadwa/`. This is a merge commit ("Merge pull request #3 from davelab6/master — Minor improvements", dated 2015-06-15).

At the referenced commit, the repository tree contains `Kadwa-Regular.glyphs` and `Kadwa-Bold.glyphs` at the root level. The upstream repo does NOT contain a `config.yaml` at this commit.

An override `config.yaml` exists in the google/fonts `ofl/kadwa/` directory with content:

```yaml
buildVariable: false
sources:
  - Kadwa-Regular.glyphs
  - Kadwa-Bold.glyphs
```

This correctly references `Kadwa-Regular.glyphs` and `Kadwa-Bold.glyphs` which are present at the root of the repository at the referenced commit. Per project policy, the `config_yaml` field is omitted from METADATA.pb when an override `config.yaml` exists in the google/fonts family directory.

The complete file tree at the referenced commit also included related source files in `Kadwa Source Files/` and Cyrillic extension work (`Cyrillic/`), but the two main glyphs sources are at the root level.

## Conclusion

Kadwa is in a complete state. The METADATA.pb has `repository_url` and `commit` correctly set. A valid override `config.yaml` exists in google/fonts referencing `Kadwa-Regular.glyphs` and `Kadwa-Bold.glyphs`, which exist at the root level of the referenced commit. No `config_yaml` is needed in METADATA.pb. No action needed.

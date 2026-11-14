# Investigation: Jersey 20

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 20 |
| Slug | jersey-20 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey20.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey20.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey20-Regular.ttf"
    dest_file: "Jersey20-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

The upstream repository is shared with all Jersey families: `scfried/soft-type-jersey`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo. The file `sources/config-jersey20.yaml` exists in the upstream repo.

The google/fonts commit history shows the same pattern as other Jersey families. Commit messages from the version updates explicitly reference commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` as the source.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey20.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

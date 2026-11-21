# Investigation: Jersey 10 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 10 Charted |
| Slug | jersey-10-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey10charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey10charted.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey10Charted-Regular.ttf"
    dest_file: "Jersey10Charted-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

The upstream repository is shared with Jersey 10: `scfried/soft-type-jersey`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo (merge commit "Merge pull request #7 from emmamarichal/main", dated 2025-01-10). The file `sources/config-jersey10charted.yaml` exists in the upstream repo.

The google/fonts commit history for this font mirrors the pattern seen in Jersey 10 (initial onboarding followed by a version update referencing the same commit `d8446c4c9c2ba14cf408c295be35213c006e19ff`).

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey10charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

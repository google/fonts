# Investigation: Jersey 15 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 15 Charted |
| Slug | jersey-15-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey15charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey15charted.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey15Charted-Regular.ttf"
    dest_file: "Jersey15Charted-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

The upstream repository is shared with all Jersey families: `scfried/soft-type-jersey`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo. The file `sources/config-jersey15charted.yaml` exists in the upstream repo.

The google/fonts commit history for this font follows the same pattern as other Jersey families: initial gftools-packager onboarding commit followed by a version update referencing commit `d8446c4c9c2ba14cf408c295be35213c006e19ff`.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey15charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

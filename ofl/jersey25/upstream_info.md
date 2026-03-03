# Investigation: Jersey 25

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 25 |
| Slug | jersey-25 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey25.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey25.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey25-Regular.ttf"
    dest_file: "Jersey25-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits for this font:
- `220d0c5be` — "Jersey 25: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `ad0dcd62c` — "[gftools-packager] Jersey 25: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `220d0c5be` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jersey at commit https://github.com/scfried/soft-type-jersey/commit/d8446c4c9c2ba14cf408c295be35213c006e19ff."

The METADATA.pb was updated from the initial commit hash `f32179dbeffdb64d0401f34bf9e4e38a768f4cfb` to `d8446c4c9c2ba14cf408c295be35213c006e19ff` in commit `220d0c5be`.

The upstream repository `scfried/soft-type-jersey` is cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo. The file `sources/config-jersey25.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey25.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

# Investigation: Jersey 20 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 20 Charted |
| Slug | jersey-20-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey20charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey20charted.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey20Charted-Regular.ttf"
    dest_file: "Jersey20Charted-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits for this font:
- `df879ca44` — "Jersey 20 Charted: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `3ce7a4a6d` — "[gftools-packager] Jersey 20 Charted: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `df879ca44` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jersey at commit https://github.com/scfried/soft-type-jersey/commit/d8446c4c9c2ba14cf408c295be35213c006e19ff."

The METADATA.pb was updated from the initial commit hash `f32179dbeffdb64d0401f34bf9e4e38a768f4cfb` to `d8446c4c9c2ba14cf408c295be35213c006e19ff` in commit `df879ca44`.

The upstream repository `scfried/soft-type-jersey` is cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo. The file `sources/config-jersey20charted.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey20charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

# Investigation: Jersey 10

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jersey 10 |
| Slug | jersey-10 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jersey |
| Commit Hash | d8446c4c9c2ba14cf408c295be35213c006e19ff |
| Config YAML | sources/config-jersey10.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jersey"
  commit: "d8446c4c9c2ba14cf408c295be35213c006e19ff"
  config_yaml: "sources/config-jersey10.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jersey10-Regular.ttf"
    dest_file: "Jersey10-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits touching this font:
- `3c5464b4d` — "Jersey 10: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `f54018242` — "[gftools-packager] Jersey 10: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `3c5464b4d` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jersey at commit https://github.com/scfried/soft-type-jersey/commit/d8446c4c9c2ba14cf408c295be35213c006e19ff."

The METADATA.pb was updated from the initial commit hash `1e98ec50907b66062a3da4b8aaf63bb37b2542f2` to `d8446c4c9c2ba14cf408c295be35213c006e19ff` in commit `3c5464b4d`.

The upstream repository `scfried/soft-type-jersey` is cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jersey`. Commit `d8446c4c9c2ba14cf408c295be35213c006e19ff` exists in the repo — it is a merge commit ("Merge pull request #7 from emmamarichal/main") dated 2025-01-10. The file `sources/config-jersey10.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`d8446c4c9c2ba14cf408c295be35213c006e19ff`), and config_yaml (`sources/config-jersey10.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

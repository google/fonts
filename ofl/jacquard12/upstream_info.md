# Investigation: Jacquard 12

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquard 12 |
| Slug | jacquard-12 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquard |
| Commit Hash | b11565152caccd6eaedce5fe2ca0e377d1a7c597 |
| Config YAML | sources/config-jacquard12.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jacquard"
  commit: "b11565152caccd6eaedce5fe2ca0e377d1a7c597"
  config_yaml: "sources/config-jacquard12.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jacquard12-Regular.ttf"
    dest_file: "Jacquard12-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits touching this font:
- `32276db47` — "Jacquard 12: Version 1.002; ttfautohint (v1.8.4.7-5d5b) added" (Jan 14, 2025, by Emma Marichal)
- `6881138f3` — "[gftools-packager] Jacquard 12: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added"

The commit message for `32276db47` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquard at commit https://github.com/scfried/soft-type-jacquard/commit/b11565152caccd6eaedce5fe2ca0e377d1a7c597."

The METADATA.pb was updated from commit `9c5c14889fd148d385536658cc2d320be294f32d` (initial onboarding) to `b11565152caccd6eaedce5fe2ca0e377d1a7c597` (latest update) in that same commit `32276db47`.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquard`. Commit `b11565152caccd6eaedce5fe2ca0e377d1a7c597` exists in the repo and is a merge commit dated 2025-01-10 (matching the update timeline). The file `sources/config-jacquard12.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`b11565152caccd6eaedce5fe2ca0e377d1a7c597`), and config_yaml (`sources/config-jacquard12.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

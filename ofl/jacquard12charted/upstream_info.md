# Investigation: Jacquard 12 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquard 12 Charted |
| Slug | jacquard-12-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquard |
| Commit Hash | b11565152caccd6eaedce5fe2ca0e377d1a7c597 |
| Config YAML | sources/config-jacquard12charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jacquard"
  commit: "b11565152caccd6eaedce5fe2ca0e377d1a7c597"
  config_yaml: "sources/config-jacquard12charted.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jacquard12Charted-Regular.ttf"
    dest_file: "Jacquard12Charted-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits touching this font:
- `3516a36ac` — "Jacquard 12 Charted: Version 1.002 added" (latest update)
- `f4bb5afc5` — "[gftools-packager] Jacquard 12 Charted: Version 1.000 added" (initial onboarding)

The commit message for `3516a36ac` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquard at commit https://github.com/scfried/soft-type-jacquard/commit/b11565152caccd6eaedce5fe2ca0e377d1a7c597."

The METADATA.pb was updated from the initial commit hash `9c5c14889fd148d385536658cc2d320be294f32d` to `b11565152caccd6eaedce5fe2ca0e377d1a7c597` in commit `3516a36ac`.

The upstream repository is the same as Jacquard 12: `scfried/soft-type-jacquard`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquard`. Commit `b11565152caccd6eaedce5fe2ca0e377d1a7c597` exists in the repo. The file `sources/config-jacquard12charted.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`b11565152caccd6eaedce5fe2ca0e377d1a7c597`), and config_yaml (`sources/config-jacquard12charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

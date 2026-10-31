# Investigation: Jacquard 24 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquard 24 Charted |
| Slug | jacquard-24-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquard |
| Commit Hash | b11565152caccd6eaedce5fe2ca0e377d1a7c597 |
| Config YAML | sources/config-jacquard24charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jacquard"
  commit: "b11565152caccd6eaedce5fe2ca0e377d1a7c597"
  config_yaml: "sources/config-jacquard24charted.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jacquard24Charted-Regular.ttf"
    dest_file: "Jacquard24Charted-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows three commits touching this font:
- `49b165c1f` — "Jacquard 24 Charted: Version 1.002 added" (latest update)
- `2d29d846d` — "Jacquard 24 Charted: Version 1.001 added"
- `97f04cb44` — "[gftools-packager] Jacquard 24 Charted: Version 1.000 added" (initial onboarding)

The commit message for `49b165c1f` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquard at commit https://github.com/scfried/soft-type-jacquard/commit/b11565152caccd6eaedce5fe2ca0e377d1a7c597."

The METADATA.pb was updated from the intermediate commit hash `ff555eb48673d04b64e451d84d77b8742bc37544` to `b11565152caccd6eaedce5fe2ca0e377d1a7c597` in commit `49b165c1f`.

The upstream repository is the same as Jacquard 12, 12 Charted, and 24: `scfried/soft-type-jacquard`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquard`. Commit `b11565152caccd6eaedce5fe2ca0e377d1a7c597` exists in the repo. The file `sources/config-jacquard24charted.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`b11565152caccd6eaedce5fe2ca0e377d1a7c597`), and config_yaml (`sources/config-jacquard24charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

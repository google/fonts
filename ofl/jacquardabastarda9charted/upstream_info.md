# Investigation: Jacquard Abastarda 9 Charted

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquarda Bastarda 9 Charted |
| Slug | jacquard-abastarda-9-charted |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquarda-bastarda |
| Commit Hash | ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61 |
| Config YAML | sources/config-charted.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jacquarda-bastarda"
  commit: "ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/JacquardaBastarda9Charted-Regular.ttf"
    dest_file: "JacquardaBastarda9Charted-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config-charted.yaml"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Note: The family directory in google/fonts uses the slug `jacquardabastarda9charted` but the actual family name is "Jacquarda Bastarda 9 Charted".

Git history in google/fonts shows two commits touching this font:
- `40f58ba36` — "Jacquarda Bastarda 9 Charted: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `fd72fe7c4` — "[gftools-packager] Jacquarda Bastarda 9 Charted: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `40f58ba36` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquarda-bastarda at commit https://github.com/scfried/soft-type-jacquarda-bastarda/commit/ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61."

The METADATA.pb was updated from the initial commit hash `cfc133ee284c74b8f76980a1267f4a3d45671377` to `ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61` in commit `40f58ba36`.

The upstream repository is the same as Jacquarda Bastarda 9: `scfried/soft-type-jacquarda-bastarda`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquarda-bastarda`. Commit `ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61` exists in the repo. The file `sources/config-charted.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61`), and config_yaml (`sources/config-charted.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

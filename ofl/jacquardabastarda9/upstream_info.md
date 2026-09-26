# Investigation: Jacquard Abastarda 9

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquarda Bastarda 9 |
| Slug | jacquard-abastarda-9 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquarda-bastarda |
| Commit Hash | ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61 |
| Config YAML | sources/config.yaml |
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
    source_file: "fonts/ttf/JacquardaBastarda9-Regular.ttf"
    dest_file: "JacquardaBastarda9-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Note: The family directory in google/fonts uses the slug `jacquardabastarda9` but the actual family name is "Jacquarda Bastarda 9".

Git history in google/fonts shows two commits touching this font:
- `dc82d7003` — "Jacquarda Bastarda 9: Version 1.001; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `b6f62d890` — "[gftools-packager] Jacquarda Bastarda 9: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `dc82d7003` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquarda-bastarda at commit https://github.com/scfried/soft-type-jacquarda-bastarda/commit/ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61."

The METADATA.pb was updated from the initial commit hash `cfc133ee284c74b8f76980a1267f4a3d45671377` to `ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61` in commit `dc82d7003`.

The upstream repository is separate from the other Jacquard families: `scfried/soft-type-jacquarda-bastarda`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquarda-bastarda`. Commit `ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61` exists in the repo and is a merge commit dated 2025-01-10. The file `sources/config.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`ca6bf8560d7e3fd2aae341ffe0838b61b35b3c61`), and config_yaml (`sources/config.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

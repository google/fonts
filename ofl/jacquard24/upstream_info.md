# Investigation: Jacquard 24

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jacquard 24 |
| Slug | jacquard-24 |
| License Dir | ofl |
| Repository URL | https://github.com/scfried/soft-type-jacquard |
| Commit Hash | b11565152caccd6eaedce5fe2ca0e377d1a7c597 |
| Config YAML | sources/config-jacquard24.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/scfried/soft-type-jacquard"
  commit: "b11565152caccd6eaedce5fe2ca0e377d1a7c597"
  config_yaml: "sources/config-jacquard24.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Jacquard24-Regular.ttf"
    dest_file: "Jacquard24-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows two commits touching this font:
- `fd2716baa` — "Jacquard 24: Version 1.002; ttfautohint (v1.8.4.7-5d5b) added" (latest update)
- `9a8109084` — "[gftools-packager] Jacquard 24: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added" (initial onboarding)

The commit message for `fd2716baa` explicitly states: "Taken from the upstream repo https://github.com/scfried/soft-type-jacquard at commit https://github.com/scfried/soft-type-jacquard/commit/b11565152caccd6eaedce5fe2ca0e377d1a7c597."

The METADATA.pb was updated from the initial commit hash `0ef57f102270194f4e41ce609ad5888f14983b8e` to `b11565152caccd6eaedce5fe2ca0e377d1a7c597` in commit `fd2716baa`.

The upstream repository is shared with Jacquard 12 and Jacquard 12 Charted: `scfried/soft-type-jacquard`, cached at `upstream_repos/fontc_crater_cache/scfried/soft-type-jacquard`. Commit `b11565152caccd6eaedce5fe2ca0e377d1a7c597` exists in the repo. The file `sources/config-jacquard24.yaml` exists in the upstream repo.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`b11565152caccd6eaedce5fe2ca0e377d1a7c597`), and config_yaml (`sources/config-jacquard24.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

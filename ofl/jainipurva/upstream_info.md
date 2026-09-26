# Investigation: Jaini Purva

## Summary

| Field | Value |
|-------|-------|
| Family Name | Jaini Purva |
| Slug | jaini-purva |
| License Dir | ofl |
| Repository URL | https://github.com/EkType/Jaini |
| Commit Hash | 4d2bcf9760fccb42eb95a079a17c430907059f58 |
| Config YAML | Source/jaini-purva.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EkType/Jaini"
  commit: "4d2bcf9760fccb42eb95a079a17c430907059f58"
  config_yaml: "Source/jaini-purva.yaml"
  files {
    source_file: "fonts/ttf/JainiPurva-Regular.ttf"
    dest_file: "JainiPurva-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb already contains a complete source block with repository URL, commit hash, and config_yaml path.

Git history in google/fonts shows one commit touching this font:
- `9edfb3dc4` — "Jaini Purva: Version 2.000; ttfautohint (v1.8.4.7-5d5b) added" (onboarding commit)

The commit message for `9edfb3dc4` explicitly states: "Taken from the upstream repo https://github.com/EkType/Jaini at commit https://github.com/EkType/Jaini/commit/4d2bcf9760fccb42eb95a079a17c430907059f58."

Jaini Purva shares the same upstream repository as Jaini: `EkType/Jaini`, cached at `upstream_repos/fontc_crater_cache/EkType/Jaini`. Commit `4d2bcf9760fccb42eb95a079a17c430907059f58` exists in the repo. The file `Source/jaini-purva.yaml` exists in the upstream repo alongside `Source/jaini.yaml`.

## Conclusion

No action needed. The source block in METADATA.pb is complete and accurate with repository URL, commit hash (`4d2bcf9760fccb42eb95a079a17c430907059f58`), and config_yaml (`Source/jaini-purva.yaml`). All data is confirmed against the upstream repository and google/fonts commit history.

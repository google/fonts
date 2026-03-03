# Investigation: Black Ops One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Black Ops One |
| Slug | black-ops-one |
| License Dir | ofl |
| Repository URL | https://github.com/SorkinType/Black-Ops |
| Commit Hash | c955bed3517ad3d8606a8b0105d27538309fb70d |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/SorkinType/Black-Ops"
  commit: "c955bed3517ad3d8606a8b0105d27538309fb70d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/BlackOpsOne-Regular.ttf"
    dest_file: "BlackOpsOne-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb contains a source block with repository URL and commit hash. No `config_yaml` is set in METADATA.pb.

The font was last updated in google/fonts commit `d50a0d29b` (PR #4995), titled "Black Ops One: Version 1.004; ttfautohint (v1.8.4.7-5d5b) added". The commit body confirms: "Black Ops One Version 1.004; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/SorkinType/Black-Ops at commit https://github.com/SorkinType/Black-Ops/commit/c955bed3517ad3d8606a8b0105d27538309fb70d." This matches the commit hash in the current METADATA.pb.

Commit `c955bed3517ad3d8606a8b0105d27538309fb70d` is confirmed in the upstream repo cache at `upstream_repos/fontc_crater_cache/SorkinType/Black-Ops` (dated July 26, 2022, merging PR #1 "Black Ops Update" from emmamarichal/main).

The upstream `sources/` directory at commit `c955bed` contains only `BlackOpsOne.glyphs` — no `config.yaml`. However, an override `config.yaml` is present in the google/fonts family directory (`ofl/blackopsone/config.yaml`):
```yaml
sources:
  - sources/BlackOpsOne.glyphs
familyName: Black Ops One
buildStatic: true
buildOTF: false
```

Per policy, since an override `config.yaml` exists in the google/fonts directory, the `config_yaml` field is correctly omitted from METADATA.pb. The google-fonts-sources tool auto-detects the local override.

## Conclusion

The METADATA.pb source block is complete. The commit `c955bed3517ad3d8606a8b0105d27538309fb70d` is confirmed as the onboarding commit. An override `config.yaml` is present in the google/fonts family directory. No action needed.

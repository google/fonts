# Investigation: Kavoon

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kavoon |
| Slug | kavoon |
| License Dir | ofl |
| Repository URL | https://github.com/EbenSorkin/Kavoon |
| Commit Hash | 0b985571f93c97f70ce9065bfc1a883a21b9deac |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/EbenSorkin/Kavoon"
  commit: "0b985571f93c97f70ce9065bfc1a883a21b9deac"
}
stroke: "SERIF"
classifications: "DISPLAY"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `EbenSorkin/Kavoon` is cached at `upstream_repos/fontc_crater_cache/EbenSorkin/Kavoon`.

The repository structure contains:
- `SRC/Kavoon-Regular.ufo` (UFO format)
- `SRC/Kavoon-Regular.vfb` (FontLab)

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kavoon/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - SRC/Kavoon-Regular.ufo
```

The latest commit in the upstream cache is `0b98557` ("Fixed typos in the read me"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory referencing the UFO source. No changes needed to METADATA.pb.

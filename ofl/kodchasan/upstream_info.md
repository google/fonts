# Investigation: Kodchasan

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kodchasan |
| Slug | kodchasan |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/Kodchasan |
| Commit Hash | d68c1268f993ce0ee23a36ba6f2d1366e0d84453 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/Kodchasan"
  commit: "d68c1268f993ce0ee23a36ba6f2d1366e0d84453"
}
primary_script: "Thai"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `cadsondemak/Kodchasan` is cached at `upstream_repos/fontc_crater_cache/cadsondemak/Kodchasan`.

The repository contains a Glyphs source file at `source/Kodchasan-Master.glyphs`. No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kodchasan/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - source/Kodchasan-Master.glyphs
```

The latest commit in the upstream cache is `d68c126` ("Merge pull request #5 from m4rc1e/metrics"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

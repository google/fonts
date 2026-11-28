# Investigation: KoHo

## Summary

| Field | Value |
|-------|-------|
| Family Name | KoHo |
| Slug | koho |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/Koho |
| Commit Hash | 066267ad87e1bd2de617bf4129902317ccb6c04c |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/Koho"
  commit: "066267ad87e1bd2de617bf4129902317ccb6c04c"
}
primary_script: "Thai"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `cadsondemak/Koho` is cached at `upstream_repos/fontc_crater_cache/cadsondemak/Koho`.

The repository contains a Glyphs source file at `source/KoHo-Master.glyphs`. No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/koho/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - source/KoHo-Master.glyphs
```

The latest commit in the upstream cache is `066267a` ("Merge pull request #8 from m4rc1e/metrics"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

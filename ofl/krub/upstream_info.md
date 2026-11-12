# Investigation: Krub

## Summary

| Field | Value |
|-------|-------|
| Family Name | Krub |
| Slug | krub |
| License Dir | ofl |
| Repository URL | https://github.com/cadsondemak/Krub |
| Commit Hash | c568bc61bd5b8af816057893e527aa55d6f08908 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/cadsondemak/Krub"
  commit: "c568bc61bd5b8af816057893e527aa55d6f08908"
}
primary_script: "Thai"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `cadsondemak/Krub` is cached at `upstream_repos/fontc_crater_cache/cadsondemak/Krub`.

The repository contains a Glyphs source file at `source/Krub.glyphs`. No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/krub/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - source/Krub.glyphs
```

The latest commit in the upstream cache is `c568bc6` ("Merge pull request #8 from m4rc1e/metrics"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

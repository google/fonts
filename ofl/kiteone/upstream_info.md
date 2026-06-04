# Investigation: Kite One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kite One |
| Slug | kite-one |
| License Dir | ofl |
| Repository URL | https://github.com/etunni/Kite-One |
| Commit Hash | be1d4f26c91c29993c47fa4b4857337b0d94e2f2 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/etunni/Kite-One"
  commit: "be1d4f26c91c29993c47fa4b4857337b0d94e2f2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/KiteOne-Regular.ttf"
    dest_file: "KiteOne-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `etunni/Kite-One` is cached at `upstream_repos/fontc_crater_cache/etunni/Kite-One`.

The repository contains a Glyphs source file at `sources/Kite One.glyphs`. No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kiteone/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - sources/Kite One.glyphs
```

The latest commit in the upstream cache is `be1d4f2` ("Merge pull request #1 from emmamarichal/master"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

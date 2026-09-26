# Investigation: Knewave

## Summary

| Field | Value |
|-------|-------|
| Family Name | Knewave |
| Slug | knewave |
| License Dir | ofl |
| Repository URL | https://github.com/theleagueof/knewave |
| Commit Hash | f335d5ff1f12e4acf97d4208e1c37b4d386e57fb |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/theleagueof/knewave"
  commit: "f335d5ff1f12e4acf97d4208e1c37b4d386e57fb"
}
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `theleagueof/knewave` is cached at `upstream_repos/fontc_crater_cache/theleagueof/knewave`.

The repository contains UFO source files in the `source/` directory:
- `source/Knewave-Regular.ufo`
- `source/Knewave Outline-Regular.ufo`
- VFB backup files

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/knewave/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - source/Knewave-Regular.ufo
  - source/Knewave Outline-Regular.ufo
```

The latest commit in the upstream cache is `f335d5f` ("newest version! lots of corrections, slightly more slanted, some kerning added, outline thicker."), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory referencing UFO sources. No changes needed to METADATA.pb.

# Investigation: Klee One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Klee One |
| Slug | klee-one |
| License Dir | ofl |
| Repository URL | https://github.com/fontworks-fonts/Klee |
| Commit Hash | 8b0532731b63ad8a445ca341d8d7d941079b83ab |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/fontworks-fonts/Klee"
  commit: "8b0532731b63ad8a445ca341d8d7d941079b83ab"
  files {
    source_file: "fonts/ttf/KleeOne-Regular.ttf"
    dest_file: "KleeOne-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/KleeOne-SemiBold.ttf"
    dest_file: "KleeOne-SemiBold.ttf"
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

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `fontworks-fonts/Klee` is cached at `upstream_repos/fontc_crater_cache/fontworks-fonts/Klee`.

The repository contains separate Glyphs source files in the `sources/` directory:
- `sources/KleeOne-Regular.glyphs`
- `sources/KleeOne-SemiBold.glyphs`

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kleeone/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - sources/KleeOne-Regular.glyphs
  - sources/KleeOne-SemiBold.glyphs
```

The latest commit in the upstream cache is `8b05327` ("Fix jp90 feature"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

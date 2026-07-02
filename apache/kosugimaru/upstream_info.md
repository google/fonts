# Investigation: Kosugi Maru

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kosugi Maru |
| Slug | kosugi-maru |
| License Dir | apache |
| Repository URL | https://github.com/googlefonts/kosugi-maru |
| Commit Hash | bd22c671a9ffc10cc4313e6f2fd75f2b86d6b14b |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/kosugi-maru"
  commit: "bd22c671a9ffc10cc4313e6f2fd75f2b86d6b14b"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/ttf/KosugiMaru-Regular.ttf"
    dest_file: "KosugiMaru-Regular.ttf"
  }
  files {
    source_file: "LICENSE.txt"
    dest_file: "LICENSE.txt"
  }
  branch: "main"
}
primary_script: "Jpan"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `googlefonts/kosugi-maru` is cached at `upstream_repos/fontc_crater_cache/googlefonts/kosugi-maru`.

The `sources/config.yaml` file exists in the cached repository. The latest commit is `bd22c67` ("Optimized source files"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

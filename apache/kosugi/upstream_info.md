# Investigation: Kosugi

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kosugi |
| Slug | kosugi |
| License Dir | apache |
| Repository URL | https://github.com/googlefonts/kosugi |
| Commit Hash | 75171a2738135ab888549e76a9037e826094f0ce |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/kosugi"
  commit: "75171a2738135ab888549e76a9037e826094f0ce"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/ttf/Kosugi-Regular.ttf"
    dest_file: "Kosugi-Regular.ttf"
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

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `googlefonts/kosugi` is cached at `upstream_repos/fontc_crater_cache/googlefonts/kosugi`.

The `sources/config.yaml` file exists in the cached repository. The latest commit is `75171a2` ("Optimized outlines in source"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

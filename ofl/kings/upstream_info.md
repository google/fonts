# Investigation: Kings

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kings |
| Slug | kings |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/kings |
| Commit Hash | 316326276cb919f88ac51dbe887958e50a3bba49 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/kings"
  commit: "316326276cb919f88ac51dbe887958e50a3bba49"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Kings-Regular.ttf"
    dest_file: "Kings-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
classifications: "DISPLAY"
classifications: "HANDWRITING"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `googlefonts/kings` is cached at `upstream_repos/fontc_crater_cache/googlefonts/kings`.

The `sources/config.yml` file exists in the cached repository. The latest commit is `3163262` ("Description typo fixed"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields. Note: the config file uses `.yml` extension (not `.yaml`), which is correctly reflected in the `config_yaml` field.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

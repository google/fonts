# Investigation: Kolker Brush

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kolker Brush |
| Slug | kolker-brush |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/kolker-brush |
| Commit Hash | 03ba4eb35eb2801089ff9343695a1f54f9b8d5b7 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/kolker-brush"
  commit: "03ba4eb35eb2801089ff9343695a1f54f9b8d5b7"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/KolkerBrush-Regular.ttf"
    dest_file: "KolkerBrush-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
classifications: "DISPLAY"
classifications: "HANDWRITING"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `googlefonts/kolker-brush` is cached at `upstream_repos/fontc_crater_cache/googlefonts/kolker-brush`.

The `sources/config.yml` file exists in the cached repository. The latest commit is `03ba4eb` ("config file added"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields. Note: the config file uses `.yml` extension (not `.yaml`), which is correctly reflected in the `config_yaml` field.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

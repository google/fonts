# Investigation: Koulen

## Summary

| Field | Value |
|-------|-------|
| Family Name | Koulen |
| Slug | koulen |
| License Dir | ofl |
| Repository URL | https://github.com/danhhong/Koulen |
| Commit Hash | 387ec6f230e61fe85a90529543daeeb2a3625b7e |
| Config YAML | Source/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/danhhong/Koulen"
  commit: "387ec6f230e61fe85a90529543daeeb2a3625b7e"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/Koulen-Regular.ttf"
    dest_file: "Koulen-Regular.ttf"
  }
  branch: "master"
}
primary_script: "Khmr"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `danhhong/Koulen` is cached at `upstream_repos/fontc_crater_cache/danhhong/Koulen`.

The `Source/builder.yaml` file exists in the cached repository with gftools-builder compatible content:
```yaml
sources:
  - Koulen.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
```

The latest commit in the upstream cache is `387ec6f` ("Merge pull request #1 from yanone/master"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields. Note: this font uses `builder.yaml` rather than the conventional `config.yaml` filename, but the format is the same gftools-builder configuration format.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path (Source/builder.yaml).

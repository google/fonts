# Investigation: Koh Santepheap

## Summary

| Field | Value |
|-------|-------|
| Family Name | Koh Santepheap |
| Slug | koh-santepheap |
| License Dir | ofl |
| Repository URL | https://github.com/danhhong/KohSantepheap |
| Commit Hash | 316be9428c2fa32b872cb298e2439d2293dc006f |
| Config YAML | Source/builder.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/danhhong/KohSantepheap"
  commit: "316be9428c2fa32b872cb298e2439d2293dc006f"
  config_yaml: "Source/builder.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Release/ttf/KohSantepheap-Thin.ttf"
    dest_file: "KohSantepheap-Thin.ttf"
  }
  ...
}
primary_script: "Khmr"
stroke: "SANS_SERIF"
classifications: "DISPLAY"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `danhhong/KohSantepheap` is cached at `upstream_repos/fontc_crater_cache/danhhong/KohSantepheap`.

The `Source/builder.yaml` file exists in the cached repository with gftools-builder compatible content:
```yaml
sources:
  - KohSantepheap.glyphs
outputDir: "../Release"
buildStatic: true
buildVariable: false
```

The latest commit in the upstream cache is `316be94` ("Merge pull request #4 from yanone/master"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields. Note: this font uses `builder.yaml` rather than the conventional `config.yaml` filename, but the format is the same gftools-builder configuration format.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path (Source/builder.yaml).

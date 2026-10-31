# Investigation: Kode Mono

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kode Mono |
| Slug | kode-mono |
| License Dir | ofl |
| Repository URL | https://github.com/isaozler/kode-mono |
| Commit Hash | 2d427d3f44649656d2c1932bb671d0c4cd064041 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/isaozler/kode-mono"
  commit: "2d427d3f44649656d2c1932bb671d0c4cd064041"
  files {
    source_file: "fonts/variable/KodeMono[wght].ttf"
    dest_file: "KodeMono[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
minisite_url: "https://kodemono.com"
stroke: "SANS_SERIF"
classifications: "MONOSPACE"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `isaozler/kode-mono` is cached at `upstream_repos/fontc_crater_cache/isaozler/kode-mono`.

The `sources/config.yaml` file exists in the cached repository along with `sources/KodeMono.glyphs` and `sources/KodeMono.designspace`. The latest commit is `2d427d3` ("Fix/build template update (#53)"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

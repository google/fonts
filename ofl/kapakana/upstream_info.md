# Investigation: Kapakana

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kapakana |
| Slug | kapakana |
| License Dir | ofl |
| Repository URL | https://github.com/nagamaki008/kapakana |
| Commit Hash | 0074870cd85239e8c5cf8949da54e0b111333a87 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/nagamaki008/kapakana"
  commit: "0074870cd85239e8c5cf8949da54e0b111333a87"
  files {
    source_file: "fonts/ttf/Kapakana-Light.ttf"
    dest_file: "static/Kapakana-Light.ttf"
  }
  files {
    source_file: "fonts/ttf/Kapakana-Regular.ttf"
    dest_file: "static/Kapakana-Regular.ttf"
  }
  files {
    source_file: "fonts/variable/Kapakana[wght].ttf"
    dest_file: "Kapakana[wght].ttf"
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
primary_script: "Hira"
classifications: "DISPLAY"
classifications: "HANDWRITING"
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `nagamaki008/kapakana` is cached at `upstream_repos/fontc_crater_cache/nagamaki008/kapakana`.

The repository contains a Glyphs source file at `sources/kapakana.glyphs`. No `config.yaml` exists in the upstream repository. However, an override `config.yaml` exists in `google/fonts/ofl/kapakana/config.yaml`:

```yaml
buildVariable: true
sources:
  - sources/kapakana.glyphs
```

The latest commit in the upstream cache is `0074870` ("Added a basic trademark symbol"), which matches exactly the commit hash recorded in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

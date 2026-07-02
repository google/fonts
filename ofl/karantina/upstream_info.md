# Investigation: Karantina

## Summary

| Field | Value |
|-------|-------|
| Family Name | Karantina |
| Slug | karantina |
| License Dir | ofl |
| Repository URL | https://github.com/ronykoch/Karantina |
| Commit Hash | efb7e920f0a441badef8920cd87d894383a19e6a |
| Config YAML | Sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/ronykoch/Karantina"
  commit: "efb7e920f0a441badef8920cd87d894383a19e6a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/TTF/Karantina-Light.ttf"
    dest_file: "Karantina-Light.ttf"
  }
  files {
    source_file: "fonts/TTF/Karantina-Regular.ttf"
    dest_file: "Karantina-Regular.ttf"
  }
  files {
    source_file: "fonts/TTF/Karantina-Bold.ttf"
    dest_file: "Karantina-Bold.ttf"
  }
  branch: "main"
  config_yaml: "Sources/config.yaml"
}
primary_script: "Hebr"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `ronykoch/Karantina` is cached at `upstream_repos/fontc_crater_cache/ronykoch/Karantina`.

The `Sources/config.yaml` file exists in the cached repository along with `Sources/karantina.glyphs`. The latest commit in the upstream cache is `efb7e92` ("Add files via upload"), which matches exactly the commit hash in METADATA.pb (only one commit exists in the repo).

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

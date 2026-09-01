# Investigation: Karla

## Summary

| Field | Value |
|-------|-------|
| Family Name | Karla |
| Slug | karla |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/karla |
| Commit Hash | 69b25f663101efb4113dd7ed416c120dd2dce56a |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/karla"
  commit: "69b25f663101efb4113dd7ed416c120dd2dce56a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Karla[wght].ttf"
    dest_file: "Karla[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Karla-Italic[wght].ttf"
    dest_file: "Karla-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `googlefonts/karla` is cached at `upstream_repos/fontc_crater_cache/googlefonts/karla`.

The `sources/config.yaml` file exists in the cached repository. The latest commit in the upstream cache is `69b25f6` ("Merge pull request #11 from emmamarichal/main"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

# Investigation: Kantumruy Pro

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kantumruy Pro |
| Slug | kantumruy-pro |
| License Dir | ofl |
| Repository URL | https://github.com/sovichet/kantumruy-pro |
| Commit Hash | dfca20df61b64efa148539a0103e52189aca78bc |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/sovichet/kantumruy-pro"
  commit: "dfca20df61b64efa148539a0103e52189aca78bc"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/KantumruyPro[wght].ttf"
    dest_file: "KantumruyPro[wght].ttf"
  }
  files {
    source_file: "fonts/variable/KantumruyPro-Italic[wght].ttf"
    dest_file: "KantumruyPro-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
primary_script: "Khmr"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `config_yaml` fields. The upstream repository `sovichet/kantumruy-pro` is cached at `upstream_repos/fontc_crater_cache/sovichet/kantumruy-pro`.

The `sources/config.yaml` file exists in the cached repository. The latest commit in the upstream cache is `dfca20d` ("Merge pull request #16 from anagata-design/dependabot/pip/urllib3-1.26.18"), which matches exactly the commit hash in METADATA.pb.

The source block is fully populated with all required fields.

## Conclusion

Status is complete. No changes needed. The METADATA.pb source block is fully populated with repository URL, commit hash, and config_yaml path.

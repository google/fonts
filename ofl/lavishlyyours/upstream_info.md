# Investigation: Lavishly Yours

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lavishly Yours |
| Slug | lavishly-yours |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/lavishly-yours |
| Commit Hash | 06ea77a251dc2d763d199995ec06da0a0c1a85f1 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/lavishly-yours"
  commit: "06ea77a251dc2d763d199995ec06da0a0c1a85f1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LavishlyYours-Regular.ttf"
    dest_file: "LavishlyYours-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `06ea77a251dc2d763d199995ec06da0a0c1a85f1` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/lavishly-yours/`:

```
commit 06ea77a251dc2d763d199995ec06da0a0c1a85f1
Author: Viviana Monsalve <viviana.monsalve.a@gmail.com>
Date:   Thu Mar 3 13:29:05 2022 -0500

    v1.010 fonts added
```

The `config.yml` file exists at `sources/config.yml` in the upstream repo.

The google/fonts history shows:
- `a29b503a5` — "Lavishly Yours: Version 1.010; ttfautohint (v1.8.3) added (#4364)"

All fields are present and verified. The `config_yaml` path uses `.yml` extension (not `.yaml`) which is valid.

## Conclusion

All source metadata fields are complete and verified. No action needed.

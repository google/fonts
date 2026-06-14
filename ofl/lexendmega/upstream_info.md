# Investigation: Lexend Mega

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lexend Mega |
| Slug | lexend-mega |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/lexend |
| Commit Hash | 20491885ca2cf7ffc556432973e7bdbc701952b5 |
| Config YAML | sources/mega.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/mega.yaml"
  files {
    source_file: "fonts/mega/variable/LexendMega[wght].ttf"
    dest_file: "LexendMega[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `20491885ca2cf7ffc556432973e7bdbc701952b5` is the same commit used for all Lexend families and was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/lexend/`.

The `sources/mega.yaml` config file exists in the upstream repo.

All Lexend family variants share the same upstream repo and commit hash, with commit `beda156f5` in google/fonts confirming the reference.

## Conclusion

All source metadata fields are complete and verified. No action needed.

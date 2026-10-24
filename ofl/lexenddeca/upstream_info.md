# Investigation: Lexend Deca

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lexend Deca |
| Slug | lexend-deca |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/lexend |
| Commit Hash | 20491885ca2cf7ffc556432973e7bdbc701952b5 |
| Config YAML | sources/deca.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/deca.yaml"
  files {
    source_file: "fonts/deca/variable/LexendDeca[wght].ttf"
    dest_file: "LexendDeca[wght].ttf"
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

The `sources/deca.yaml` config file exists in the upstream repo.

The google/fonts commit body for `beda156f5` confirms: "Lexend Deca Version 1.007 taken from the upstream repo https://github.com/googlefonts/lexend at commit https://github.com/googlefonts/lexend/commit/20491885ca2cf7ffc556432973e7bdbc701952b5."

All Lexend family variants (Deca, Exa, Giga, Mega, Peta, Tera, Zetta) share the same upstream repo and commit hash, each with their own config YAML file.

## Conclusion

All source metadata fields are complete and verified. No action needed.

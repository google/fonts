# Investigation: Lexend

## Summary

| Field | Value |
|-------|-------|
| Family Name | Lexend |
| Slug | lexend |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/lexend |
| Commit Hash | 20491885ca2cf7ffc556432973e7bdbc701952b5 |
| Config YAML | sources/lexend.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/lexend"
  commit: "20491885ca2cf7ffc556432973e7bdbc701952b5"
  config_yaml: "sources/lexend.yaml"
  files {
    source_file: "fonts/lexend/variable/Lexend[wght].ttf"
    dest_file: "Lexend[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
}
```

## Investigation

The METADATA.pb has `repository_url`, `commit` hash, and `config_yaml` all populated. The commit `20491885ca2cf7ffc556432973e7bdbc701952b5` was verified to exist in the upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/lexend/`:

```
commit 20491885ca2cf7ffc556432973e7bdbc701952b5
Merge: 9455fae 6b22831
Author: Rosalie Wagner <mail@rosaliewagner.com>
Date:   Fri Jul 30 18:27:32 2021 +0200

    Merge pull request #2 from RosaWagner/main
```

The `sources/lexend.yaml` config file exists in the upstream repo.

The google/fonts commit body for `beda156f5` confirms: "Lexend Version 1.007 taken from the upstream repo https://github.com/googlefonts/lexend at commit https://github.com/googlefonts/lexend/commit/20491885ca2cf7ffc556432973e7bdbc701952b5."

The google/fonts history shows:
- `beda156f5` — "Lexend Tera: Version 1.007 added; ... Lexend: Version 1.007 added ... (#3623)"
- `da0650b86` — "Lexend Exa: Version 1.100 added; ... (#3517)"

All fields are present and verified.

## Conclusion

All source metadata fields are complete and verified. No action needed.

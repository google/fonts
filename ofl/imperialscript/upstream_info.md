# Investigation: Imperial Script

## Summary

| Field | Value |
|-------|-------|
| Family Name | Imperial Script |
| Slug | imperial-script |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/imperial-script |
| Commit Hash | 01a1656c6ffebe306262129aafee029fe6a7f3f3 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/imperial-script"
  commit: "01a1656c6ffebe306262129aafee029fe6a7f3f3"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/ImperialScript-Regular.ttf"
    dest_file: "ImperialScript-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The METADATA.pb for Imperial Script (at `google/fonts/ofl/imperialscript/METADATA.pb`) already contains a complete source block with `repository_url`, `commit`, and `config_yaml` fields.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/imperial-script/`. Verification confirmed:

1. **Commit hash**: `01a1656c6ffebe306262129aafee029fe6a7f3f3` exists in the upstream repo. The commit message is "v10 updated glyph info" authored by Viviana Monsalve on 2021-11-12. This is also the HEAD commit of the repository.

2. **Config file**: `sources/config.yml` exists at the referenced path and contains:
   ```yaml
   sources:
     - ImperialScript.glyphs
   familyName: "Imperial Script"
   buildVariable: false
   ```

3. **Source format**: The repository uses a `.glyphs` source file (`ImperialScript.glyphs`), which is gftools-builder compatible.

The font was designed by Robert Leuschke. The family was added to Google Fonts on 2021-11-18, shortly after the commit date (2021-11-12), consistent with the source metadata.

## Conclusion

The source block for Imperial Script is complete and verified. Repository URL, commit hash, and config_yaml all check out. No action needed.

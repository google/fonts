# Investigation: Inclusive Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inclusive Sans |
| Slug | inclusive-sans |
| License Dir | ofl |
| Repository URL | https://github.com/LivKing/Inclusive-Sans |
| Commit Hash | 38b8ed1dd67bd25ef4180140492810cf050ef501 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/LivKing/Inclusive-Sans"
  commit: "38b8ed1dd67bd25ef4180140492810cf050ef501"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/InclusiveSans[wght].ttf"
    dest_file: "InclusiveSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/InclusiveSans-Italic[wght].ttf"
    dest_file: "InclusiveSans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb for Inclusive Sans (at `google/fonts/ofl/inclusivesans/METADATA.pb`) already contains a complete source block with `repository_url`, `commit`, and `config_yaml` fields.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/LivKing/Inclusive-Sans/`. Verification confirmed:

1. **Commit hash**: `38b8ed1dd67bd25ef4180140492810cf050ef501` exists in the upstream repo. The commit message is "fixed r caron top anchor position in regular" authored by Olivia King on 2025-02-21. This is also the HEAD commit of the repository.

2. **Config file**: `sources/config.yaml` exists and contains:
   ```yaml
   sources:
     - InclusiveSans.glyphs
     - InclusiveSans-Italic.glyphs
   axisOrder:
     - wght
     - ital
   familyName: "Inclusive Sans"
   cleanUp: true
   stat:
     ...
   ```

3. **Source format**: The repository uses `.glyphs` source files, which are gftools-builder compatible.

The font was designed by Olivia King. The family was added to Google Fonts on 2023-08-04 and the referenced commit is dated 2025-02-21, suggesting the METADATA.pb was updated after the initial onboarding to reflect a recent maintenance commit.

## Conclusion

The source block for Inclusive Sans is complete and verified. Repository URL, commit hash, and config_yaml all check out. No action needed.

# Investigation: Ingrid Darling

## Summary

| Field | Value |
|-------|-------|
| Family Name | Ingrid Darling |
| Slug | ingrid-darling |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/ingrid-darling |
| Commit Hash | ea2b4893cf8dc8cd0e7fb2b89f9631b38fde4ed3 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/ingrid-darling"
  commit: "ea2b4893cf8dc8cd0e7fb2b89f9631b38fde4ed3"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/IngridDarling-Regular.ttf"
    dest_file: "IngridDarling-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The METADATA.pb for Ingrid Darling (at `google/fonts/ofl/ingriddarling/METADATA.pb`) already contains a complete source block with `repository_url`, `commit`, and `config_yaml` fields.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/ingrid-darling/`. Verification confirmed:

1. **Commit hash**: `ea2b4893cf8dc8cd0e7fb2b89f9631b38fde4ed3` exists in the upstream repo. The commit message is "description file moved o documentation" authored by Viviana Monsalve on 2022-03-11. This is also the HEAD commit of the repository.

2. **Config file**: `sources/config.yml` exists and contains:
   ```yaml
   sources:
     - IngridDarling.glyphs
   familyName: "Ingrid Darling"
   buildVariable: false
   ```

3. **Source format**: The repository uses a `.glyphs` source file (`IngridDarling.glyphs`), which is gftools-builder compatible.

The font was designed by Robert Leuschke. The family was added to Google Fonts on 2022-03-11, matching the commit date exactly, suggesting this was the onboarding commit.

## Conclusion

The source block for Ingrid Darling is complete and verified. Repository URL, commit hash, and config_yaml all check out. No action needed.

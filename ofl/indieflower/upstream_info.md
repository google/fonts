# Investigation: Indie Flower

## Summary

| Field | Value |
|-------|-------|
| Family Name | Indie Flower |
| Slug | indie-flower |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/indieflower |
| Commit Hash | db44d10c34c1d74011b7f3bee8c7c12123b6068e |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/indieflower"
  commit: "db44d10c34c1d74011b7f3bee8c7c12123b6068e"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb for Indie Flower (at `google/fonts/ofl/indieflower/METADATA.pb`) already contains a source block with `repository_url`, `commit`, and `config_yaml` fields.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/indieflower/`. Verification confirmed:

1. **Commit hash**: `db44d10c34c1d74011b7f3bee8c7c12123b6068e` exists in the upstream repo. The commit message is "Add sources/config.yaml" authored by Felipe Corrêa da Silva Sanches on 2025-02-25. This is also the HEAD commit of the repository.

2. **Config file**: `sources/config.yaml` exists and contains:
   ```yaml
   sources:
     - IndieFlower.glyphs
   ```

3. **Source format**: The repository uses a `.glyphs` source file (`IndieFlower.glyphs`), which is gftools-builder compatible.

The font was designed by Kimberly Geswein. The family was originally added to Google Fonts in 2011 and the repository is now maintained under the `googlefonts` organization. The referenced commit (`db44d10`) is very recent (2025-02-25), reflecting a maintenance commit that added the `config.yaml`.

## Conclusion

The source block for Indie Flower is complete and verified. Repository URL, commit hash, and config_yaml all check out. No action needed.

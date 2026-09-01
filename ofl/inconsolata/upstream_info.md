# Investigation: Inconsolata

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inconsolata |
| Slug | inconsolata |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/Inconsolata |
| Commit Hash | fc1fc21081558b39a2db43bfd9b65bf9acb50701 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/Inconsolata"
  commit: "fc1fc21081558b39a2db43bfd9b65bf9acb50701"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The METADATA.pb for Inconsolata (at `google/fonts/ofl/inconsolata/METADATA.pb`) already contains a source block with `repository_url`, `commit`, and `config_yaml` fields.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/Inconsolata/`. Verification confirmed:

1. **Commit hash**: `fc1fc21081558b39a2db43bfd9b65bf9acb50701` exists in the upstream repo. The commit message is "Merge pull request #70 from googlefonts/gf-mastering2" by Marc Foley on 2022-04-28. This is also the HEAD commit of the repository.

2. **Config file**: `sources/config.yaml` exists and contains:
   ```yaml
   sources:
     - Inconsolata.glyphs
   axisOrder:
     - wdth
     - wght
   familyName: Inconsolata
   buildStatic: true
   flattenComponents: false
   decomposeTransformedComponents: true
   vttSources:
     Inconsolata[wdth,wght].ttf: vtt_hinting.ttx
   includeSourceFixes: true
   ```

3. **Source format**: The repository uses a `.glyphs` source file (`Inconsolata.glyphs`), which is gftools-builder compatible. The font is a variable font with `wdth` and `wght` axes.

The font was originally designed by Raph Levien and is now maintained in the `googlefonts` organization. The family was originally added to Google Fonts in 2010, and the current source block reflects the modernized variable font version.

## Conclusion

The source block for Inconsolata is complete and verified. Repository URL, commit hash, and config_yaml all check out. No action needed.

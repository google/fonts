# Investigation: Imprima

## Summary

| Field | Value |
|-------|-------|
| Family Name | Imprima |
| Slug | imprima |
| License Dir | ofl |
| Repository URL | https://github.com/etunni/imprima |
| Commit Hash | efec6ee25d2ba461487c391b62ae26817614741a |
| Config YAML | unknown |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/etunni/imprima"
  commit: "efec6ee25d2ba461487c391b62ae26817614741a"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Imprima-Regular.ttf"
    dest_file: "Imprima-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb for Imprima (at `google/fonts/ofl/imprima/METADATA.pb`) contains a source block with `repository_url` and `commit` but no `config_yaml`.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/etunni/imprima/`. Verification confirmed:

1. **Commit hash**: `efec6ee25d2ba461487c391b62ae26817614741a` exists in the upstream repo. The commit is a merge commit ("Merge pull request #1 from emmamarichal/master") by Eduardo Rodríguez Tunni on 2023-02-10. This is also the HEAD commit of the repository (the latest commit on master).

2. **Source format**: The repository has a `sources/` directory containing `Imprima.glyphs`, which is a gftools-builder-compatible source file.

3. **Config file**: No `config.yaml` or `config.yml` exists anywhere in the repository. The `sources/` directory contains only `Imprima.glyphs`.

The font was designed by Eduardo Tunni and was originally added to Google Fonts on 2012-03-14. The source block was evidently updated with the commit hash and repo URL reflecting a 2023 mastering/update, but no `config.yaml` was added to the upstream repository.

An override `config.yaml` could be created in the google/fonts family directory referencing the `.glyphs` source, enabling automated rebuilds.

## Conclusion

The source block for Imprima has `repository_url` and `commit` but is missing `config_yaml`. The upstream repository has a `.glyphs` source file (`sources/Imprima.glyphs`) but no `config.yaml`. An override `config.yaml` should be created in the google/fonts `ofl/imprima/` directory referencing `sources/Imprima.glyphs`. Status: `missing_config`.

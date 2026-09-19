# Investigation: Julee

## Summary

| Field | Value |
|-------|-------|
| Family Name | Julee |
| Slug | julee |
| License Dir | ofl |
| Repository URL | https://github.com/etunni/julee |
| Commit Hash | 9a2efe6783e9ea590cee62c8aec51670a3dec51d |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/etunni/julee"
  commit: "9a2efe6783e9ea590cee62c8aec51670a3dec51d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Julee-Regular.ttf"
    dest_file: "Julee-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb for Julee has a complete source block with `repository_url` and `commit` hash. The upstream repository is `https://github.com/etunni/julee`, maintained by Julián Tunni.

The commit hash `9a2efe6783e9ea590cee62c8aec51670a3dec51d` was added to google/fonts in commit `2137a7edd` ("sources info for Julee: Version 1.002 (PR #5959)"). The commit was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/etunni/julee/`.

Checking the repository at the referenced commit, the following structure is present:
- `sources/Julee.glyphs` — gftools-builder compatible Glyphs source file
- `fonts/ttf/Julee-Regular.ttf`
- `fonts/otf/Julee-Regular.otf`
- `OFL.txt`, `README.md`, `AUTHOR.txt`, `CONTRIBUTORS.txt`

Although the METADATA.pb source block does not include a `config_yaml` field, there is an override `config.yaml` in the google/fonts `ofl/julee/` directory with content:

```yaml
buildVariable: false
sources:
  - sources/Julee.glyphs
```

This override correctly references `sources/Julee.glyphs` which exists at the referenced commit. Per project policy, when an override `config.yaml` exists in the google/fonts family directory, the `config_yaml` field can be omitted from METADATA.pb and the google-fonts-sources tool auto-detects the local override.

Recent git history for the julee repo shows the last commit is `9a2efe6` ("Update CONTRIBUTORS.txt"), confirming no further changes were made upstream after the recorded commit.

## Conclusion

Julee is in a complete state. The METADATA.pb has `repository_url` and `commit`, and a valid override `config.yaml` exists in google/fonts referencing the correct source file (`sources/Julee.glyphs`) at the referenced commit. No action needed.

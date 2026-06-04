# Investigation: Bungee Color

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bungee Color |
| Slug | bungee-color |
| License Dir | ofl |
| Repository URL | https://github.com/djrrb/Bungee |
| Commit Hash | bb29250eb071b59c4e48f44cf146943e2aafae61 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/djrrb/Bungee"
  commit: "bb29250eb071b59c4e48f44cf146943e2aafae61"
}
```

## Investigation

The source block was added to METADATA.pb by Cosimo Lupo (anthrotype) in google/fonts commit `e9ba362c8` ("Revert BungeeColor-Regular.ttf to COLRv0 only", PR #5137, 2022-08-26). The PR body states: "replaced the current BungeeColor-Regular.ttf with the upstream one found on djrrb/Bungee repository." This was the same commit that set the repository_url and commit fields.

The repository URL `https://github.com/djrrb/Bungee` is the shared upstream for all Bungee variants. It is cached at `upstream_repos/fontc_crater_cache/djrrb/Bungee/`.

The commit `bb29250eb071b59c4e48f44cf146943e2aafae61` (message: "SBIX font doesn't work, isn't needed anymore", David Jonathan Ross, 2022-08-16) is the commit at which the COLRv0 binary was taken. The PR body references commit `a8a8a215` for the actual binary file path, but the METADATA.pb records `bb29250e`. Both commits reference the same COLRv0 binary file (verified: SHA-256 identical at both commits). `bb29250e` was likely the HEAD of the relevant branch when Cosimo prepared the PR.

Bungee Color history in google/fonts:
1. 2021-12-01: Exploratory addition (PR #4128, rsheeter)
2. Multiple maximum_color experiments (adding SVG/CBDT color tables)
3. 2022-08-26: Reverted to COLRv0-only (PR #5137, anthrotype) — current state

The upstream repository does not contain a `config.yaml`. An override `config.yaml` was created in the google/fonts family directory (`ofl/bungeecolor/config.yaml`) by Felipe Sanches in commit `f6c68379a` ("Add override config.yaml for 50 font families", 2026-02-16). Contents:

```yaml
sources:
  - sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo
familyName: Bungee Color
buildStatic: true
buildOTF: false
```

The source file `sources/2-build/Bungee_Color/Bungee_Color-Regular.ufo` was verified to exist at the recorded commit `bb29250e`. Since an override config.yaml exists in google/fonts, the `config_yaml` field is correctly omitted from the METADATA.pb source block.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and override config.yaml are all in place. The status is `complete`. The minor discrepancy between the PR-referenced commit (`a8a8a21`) and the METADATA.pb-recorded commit (`bb29250e`) is not a functional issue since both produce identical COLRv0 font files.

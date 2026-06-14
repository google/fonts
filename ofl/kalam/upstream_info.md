# Investigation: Kalam

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kalam |
| Slug | kalam |
| License Dir | ofl |
| Repository URL | https://github.com/itfoundry/kalam |
| Commit Hash | 03a4d8a33849b1ad9afdee95006bc66d2d4aed94 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/itfoundry/kalam"
  commit: "03a4d8a33849b1ad9afdee95006bc66d2d4aed94"
}
```

## Investigation

The METADATA.pb for Kalam has a source block with `repository_url` and `commit` but no `config_yaml` field. The upstream repository is `https://github.com/itfoundry/kalam`, maintained by Indian Type Foundry (ITF).

The commit hash `03a4d8a33849b1ad9afdee95006bc66d2d4aed94` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/itfoundry/kalam/`. This commit ("Fix compatibility issues; build 2.001") is the latest commit in the repository, dated to the most recent update of the Kalam builds.

At the referenced commit, the repository contains `masters/Kalam.glyphs` — a gftools-builder compatible Glyphs source file. The upstream repo also has a custom build system (`build.py`, `config.py`, `itf.py`) but does NOT contain a gftools-builder `config.yaml`.

An override `config.yaml` exists in the google/fonts `ofl/kalam/` directory with content:

```yaml
buildVariable: false
sources:
  - masters/Kalam.glyphs
```

This correctly references `masters/Kalam.glyphs` which exists at the referenced commit. Per project policy, the `config_yaml` field is omitted from METADATA.pb when an override `config.yaml` exists in the google/fonts family directory.

Kalam is a Devanagari handwriting font supporting Latin and Devanagari scripts. It has three weights: Light (300), Regular (400), and Bold (700).

## Conclusion

Kalam is in a complete state. The METADATA.pb has `repository_url` and `commit` correctly set. A valid override `config.yaml` exists in google/fonts referencing `masters/Kalam.glyphs` which exists at the referenced commit. No action needed.

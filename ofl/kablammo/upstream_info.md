# Investigation: Kablammo

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kablammo |
| Slug | kablammo |
| License Dir | ofl |
| Repository URL | https://github.com/Vectro-Type-Foundry/kablammo |
| Commit Hash | cccc120d23cbf65f7f263122407d980a24f65f27 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Vectro-Type-Foundry/kablammo"
  commit: "cccc120d23cbf65f7f263122407d980a24f65f27"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Kablammo[MORF].ttf"
    dest_file: "Kablammo[MORF].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The METADATA.pb for Kablammo has a complete source block with `repository_url`, `commit`, `files`, `branch`, and `config_yaml`. The upstream repository is `https://github.com/Vectro-Type-Foundry/kablammo`, a variable font with a `MORF` axis.

The commit hash `cccc120d23cbf65f7f263122407d980a24f65f27` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/Vectro-Type-Foundry/kablammo/`. The `sources/config.yml` file (note: `.yml` extension, not `.yaml`) exists at this commit and contains a valid gftools-builder configuration:

```yaml
sources:
  - Kablammo.glyphs
buildOTF: True
buildTTF: False
axisOrder:
  - MORF
familyName: "Kablammo"
```

The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml` in the upstream repo. Note that the extension is `.yml` (not `.yaml`), which is correctly reflected in the METADATA.pb.

The copyright string confirms the repository: "Copyright 2023 The Kablammo Project Authors (https://github.com/Vectro-Type-Foundry/kablammo)".

Kablammo also has a minisite at `https://fonts.withgoogle.com/kablammo`.

## Conclusion

Kablammo is in a complete state. The METADATA.pb has `repository_url`, `commit`, and `config_yaml` (pointing to `sources/config.yml` in the upstream repo) all correctly set. The config file exists at the referenced commit. No action needed.

# Investigation: Joan

## Summary

| Field | Value |
|-------|-------|
| Family Name | Joan |
| Slug | joan |
| License Dir | ofl |
| Repository URL | https://github.com/PaoloBiagini/Joan |
| Commit Hash | 981cb73299f7d9164eedcb647e57fb34c9dc1139 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/PaoloBiagini/Joan"
  commit: "981cb73299f7d9164eedcb647e57fb34c9dc1139"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Joan-Regular.ttf"
    dest_file: "Joan-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font is stored at `ofl/joan/` in google/fonts. The METADATA.pb contains a complete source block with repository URL, commit hash, and config_yaml path.

The upstream repository at https://github.com/PaoloBiagini/Joan is cloned at `upstream_repos/fontc_crater_cache/PaoloBiagini/Joan`.

Verification of commit `981cb73299f7d9164eedcb647e57fb34c9dc1139`:
```
981cb73 Merge pull request #13 from emmamarichal/main
```
The commit exists in the upstream repo and is confirmed to be the HEAD (most recent commit as of the cache fetch).

The upstream `sources/config.yaml` exists and contains:
```yaml
    sources:
      - Joan.glyphs
    familyName: "Joan"
    buildVariable: false
```
(Note: the file appears to have leading whitespace indentation, which may be an issue for gftools-builder parsing, but the path referenced in METADATA.pb is correct.)

## Conclusion

The source block is complete with repository URL, commit hash, and config_yaml. All fields verified against the upstream repository. Status is complete.

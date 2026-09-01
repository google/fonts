# Investigation: Brygada 1918

## Summary

| Field | Value |
|-------|-------|
| Family Name | Brygada 1918 |
| Slug | brygada-1918 |
| License Dir | ofl |
| Repository URL | https://github.com/kosmynkab/Brygada-1918 |
| Commit Hash | 8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/kosmynkab/Brygada-1918"
  commit: "8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b"
  files {
    source_file: "fonts/variable/Brygada1918[wght].ttf"
    dest_file: "Brygada1918[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Brygada1918-Italic[wght].ttf"
    dest_file: "Brygada1918-Italic[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The font has three commits in google/fonts:

1. `4714790f8` — `Brygada 1918: Version 3.006 added (#3252)`
2. `bc90a8ac9` — `Brygada 1918: Version 3.005 added (#3095)`
3. `5bfd14ed2` — `Brygada 1918: Version 3.004 added (#2978)`

The most recent commit message (from PR #3252) states:

> Brygada 1918 Version 3.006 taken from the upstream repo https://github.com/kosmynkab/Brygada-1918 at commit https://github.com/kosmynkab/Brygada-1918/commit/8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b.

This directly confirms both the repository URL and the commit hash in METADATA.pb.

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/kosmynkab/Brygada-1918`. Commit `8325dc36ca87b8c7b8909c3e048fe90fd7e46c4b` was verified to exist — it is the most recent commit on the main branch ("Generated version 3.006", dated 2021-03-24 12:55:22 +0100).

### Config YAML

`sources/config.yaml` exists in the upstream repository at the referenced commit. It is located at `sources/config.yaml` (relative to repo root) and contains:

```yaml
sources:
  - Brygada1918.glyphs
  - Brygada1918-Italic.glyphs
axisOrder:
  - wght
familyName: Brygada 1918
```

The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly points to this file.

### Designers

The font was created by a team: Capitalics, Mateusz Machalski, Borys Kosmynka, Ania Wieluńska, and Przemysław Hoffer. The upstream repository is hosted under `kosmynkab` (Borys Kosmynka's GitHub account).

### METADATA.pb Status

All fields are complete and correct:
- `repository_url` matches the commit message in google/fonts
- `commit` matches the commit message and is verified in the upstream repo as the HEAD of main
- `config_yaml: "sources/config.yaml"` is set and the file exists at the referenced commit

## Conclusion

No action needed. The source block in METADATA.pb is complete and correct. Status is **complete** with HIGH confidence.

# Investigation: Joti One

## Summary

| Field | Value |
|-------|-------|
| Family Name | Joti One |
| Slug | joti-one |
| License Dir | ofl |
| Repository URL | https://github.com/etunni/joti |
| Commit Hash | 7feedf8bad69029e82ae281c7a100fb639d946e1 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/etunni/joti"
  commit: "7feedf8bad69029e82ae281c7a100fb639d946e1"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/JotiOne-Regular.ttf"
    dest_file: "JotiOne-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The `ofl/jotione/` directory contains the font, METADATA.pb, OFL.txt, DESCRIPTION, FONTLOG, and an override `config.yaml`.

The git history shows:
- `af137c900` ("sources info for Joti One: Version 1.002 (PR #5948)"): Added the source block to METADATA.pb with repository URL and commit hash, and created the override `config.yaml` in the google/fonts directory.
- `fa15a6093` ([gftools-packager] commit for Version 1.002): The font was onboarded via the gftools-packager.

The upstream repository at https://github.com/etunni/joti is cached at `upstream_repos/fontc_crater_cache/etunni/joti`. Verification of commit `7feedf8bad69029e82ae281c7a100fb639d946e1`:
```
7feedf8 Merge pull request #1 from emmamarichal/master
```
The commit exists and is the HEAD of the upstream repository.

The upstream `sources/` directory contains only `Joti.glyphs` — no config.yaml in the upstream repo. The override `config.yaml` in the google/fonts directory contains:
```yaml
buildVariable: false
sources:
  - sources/Joti.glyphs
```
This correctly references the Glyphs source file. The commit `af137c900` added both the override config.yaml and the source block to METADATA.pb.

## Conclusion

The source block is complete with repository URL and commit hash. An override `config.yaml` exists in the google/fonts family directory referencing `sources/Joti.glyphs` from the upstream repo. The `config_yaml` field is intentionally absent from METADATA.pb (local override is auto-detected). Status is complete.

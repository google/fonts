# Investigation: Island Moments

## Summary

| Field | Value |
|-------|-------|
| Family Name | Island Moments |
| Slug | island-moments |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/island-moments |
| Commit Hash | 665d59f297c782358f09699fc2231c0eee293f25 |
| Config YAML | sources/config.yml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/island-moments"
  commit: "665d59f297c782358f09699fc2231c0eee293f25"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/IslandMoments-Regular.ttf"
    dest_file: "IslandMoments-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font was added to google/fonts in commit `4eeaeee72` ("Island Moments: Version 1.010 added (#4085)"). The commit body confirms:

> Island Moments Version 1.010 taken from the upstream repo https://github.com/googlefonts/island-moments at commit https://github.com/googlefonts/island-moments/commit/665d59f297c782358f09699fc2231c0eee293f25.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/island-moments`. The commit `665d59f297c782358f09699fc2231c0eee293f25` was verified to exist in the cached repo. The repo has **only one commit** (2021-11-11, "sample image updated") which matches the METADATA.pb.

**Source format**: The repository contains `sources/IslandMomentsPro.glyphs` (a single Glyphs source file). A `config.yml` exists at `sources/config.yml`:
```yaml
sources:
  - IslandMomentsPro.glyphs
familyName: "Island Moments"
buildVariable: false
autohintTTF: false
```

The `config_yaml: "sources/config.yml"` in METADATA.pb is correctly set and the file exists in the upstream repo.

## Conclusion

The source block is complete and correct. The `repository_url`, `commit`, and `config_yaml` are all verified. The commit `665d59f` is the only commit in the repository and matches METADATA.pb exactly. No changes needed.

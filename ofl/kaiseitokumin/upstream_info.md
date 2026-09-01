# Investigation: Kaisei Tokumin

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kaisei Tokumin |
| Slug | kaisei-tokumin |
| License Dir | ofl |
| Repository URL | https://github.com/FontKai-Kaisei/Kaisei |
| Commit Hash | b396c906d67ddbfde60c2c78588f8de00b46c891 |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/FontKai-Kaisei/Kaisei"
  commit: "b396c906d67ddbfde60c2c78588f8de00b46c891"
  files {
    source_file: "fonts/ttf/tokumin/KaiseiTokumin-Regular.ttf"
    dest_file: "KaiseiTokumin-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/tokumin/KaiseiTokumin-Medium.ttf"
    dest_file: "KaiseiTokumin-Medium.ttf"
  }
  files {
    source_file: "fonts/ttf/tokumin/KaiseiTokumin-Bold.ttf"
    dest_file: "KaiseiTokumin-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/tokumin/KaiseiTokumin-ExtraBold.ttf"
    dest_file: "KaiseiTokumin-ExtraBold.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "tokumin_DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb for Kaisei Tokumin has a source block with `repository_url`, `commit`, `files`, and `branch` but no `config_yaml`. The upstream repository is `https://github.com/FontKai-Kaisei/Kaisei`, which hosts all four Kaisei family variants in a single repository.

The commit hash `b396c906d67ddbfde60c2c78588f8de00b46c891` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/FontKai-Kaisei/Kaisei/`. This commit ("Fixed jp90 unicodes") is the latest commit in the repository.

Kaisei Tokumin has four weights (Regular, Medium, Bold, ExtraBold), unlike the other three Kaisei variants which have only three weights.

At the referenced commit, the repository contains `sources/Kaisei-Tokumin.glyphs` — a gftools-builder compatible Glyphs source file. The upstream repo does NOT contain a `config.yaml`.

An override `config.yaml` exists in the google/fonts `ofl/kaiseitokumin/` directory with content:

```yaml
buildVariable: false
sources:
  - sources/Kaisei-Tokumin.glyphs
```

This correctly references `sources/Kaisei-Tokumin.glyphs` which exists at the referenced commit. Per project policy, the `config_yaml` field is omitted from METADATA.pb when an override `config.yaml` exists in the google/fonts family directory.

## Conclusion

Kaisei Tokumin is in a complete state. The METADATA.pb has `repository_url` and `commit` correctly set. A valid override `config.yaml` exists in google/fonts referencing `sources/Kaisei-Tokumin.glyphs` which exists at the referenced commit. No action needed.

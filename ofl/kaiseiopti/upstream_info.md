# Investigation: Kaisei Opti

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kaisei Opti |
| Slug | kaisei-opti |
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
    source_file: "fonts/ttf/opti/KaiseiOpti-Regular.ttf"
    dest_file: "KaiseiOpti-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/opti/KaiseiOpti-Medium.ttf"
    dest_file: "KaiseiOpti-Medium.ttf"
  }
  files {
    source_file: "fonts/ttf/opti/KaiseiOpti-Bold.ttf"
    dest_file: "KaiseiOpti-Bold.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "opti_DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb for Kaisei Opti has a source block with `repository_url`, `commit`, `files`, and `branch` but no `config_yaml`. The upstream repository is `https://github.com/FontKai-Kaisei/Kaisei`, which hosts all four Kaisei family variants in a single repository.

The commit hash `b396c906d67ddbfde60c2c78588f8de00b46c891` was verified to exist in the cached repository at `upstream_repos/fontc_crater_cache/FontKai-Kaisei/Kaisei/`. This commit ("Fixed jp90 unicodes") is the latest commit in the repository.

All four Kaisei families reference the same commit hash, confirming they were onboarded together.

At the referenced commit, the repository contains `sources/Kaisei-Opti.glyphs` — a gftools-builder compatible Glyphs source file. The upstream repo does NOT contain a `config.yaml`.

An override `config.yaml` exists in the google/fonts `ofl/kaiseiopti/` directory with content:

```yaml
buildVariable: false
sources:
  - sources/Kaisei-Opti.glyphs
```

This correctly references `sources/Kaisei-Opti.glyphs` which exists at the referenced commit. Per project policy, the `config_yaml` field is omitted from METADATA.pb when an override `config.yaml` exists in the google/fonts family directory.

## Conclusion

Kaisei Opti is in a complete state. The METADATA.pb has `repository_url` and `commit` correctly set. A valid override `config.yaml` exists in google/fonts referencing `sources/Kaisei-Opti.glyphs` which exists at the referenced commit. No action needed.

# Investigation: Bricolage Grotesque

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bricolage Grotesque |
| Slug | bricolage-grotesque |
| License Dir | ofl |
| Repository URL | https://github.com/ateliertriay/bricolage |
| Commit Hash | 84745e5b96261ae5f8c6c856e262fe78d1d6efdd |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/ateliertriay/bricolage"
  commit: "84745e5b96261ae5f8c6c856e262fe78d1d6efdd"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/BricolageGrotesque[opsz,wdth,wght].ttf"
    dest_file: "BricolageGrotesque[opsz,wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Git History in google/fonts

The font has two commits in google/fonts:

1. `b9f6c7120` — `[gftools-packager] Bricolage Grotesque: Version 1.001;gftools[0.9.33.dev8+g029e19f] added`
2. `92f1a0b27` — `[gftools-packager] Bricolage Grotesque: Version 1.000;gftools[0.9.30] added`

The most recent packager commit message states:

> Bricolage Grotesque Version 1.001;gftools[0.9.33.dev8+g029e19f] taken from the upstream repo https://github.com/ateliertriay/bricolage at commit https://github.com/ateliertriay/bricolage/commit/84745e5b96261ae5f8c6c856e262fe78d1d6efdd.

This directly confirms both the repository URL and the commit hash in METADATA.pb.

The first packager commit (`92f1a0b27`) referenced a different earlier commit: `95ddb0da9087a5f49f4616faea519e9e27d80a99` (Version 1.000).

### Upstream Repository

The repo is cached at `upstream_repos/fontc_crater_cache/ateliertriay/bricolage`. Commit `84745e5b96261ae5f8c6c856e262fe78d1d6efdd` was verified to exist — it is the most recent commit on the main branch ("Merge pull request #5 from emmamarichal/main", dated 2023-07-19).

### Config YAML

`sources/config.yaml` exists in the upstream repository at the referenced commit. Content:

```yaml
sources:
  - BricolageGrotesque.glyphs
axisOrder:
  - opsz
  - wdth
  - wght
familyName: Bricolage Grotesque
stat:
  BricolageGrotesque[opsz,wdth,wght].ttf:
  - name: Optical size
    tag: opsz
    values: [...]
  - name: Width
    tag: wdth
    values: [...]
  - name: Weight
    tag: wght
    values: [...]
```

The `config_yaml: "sources/config.yaml"` field in METADATA.pb correctly points to this file.

### METADATA.pb Status

All fields are complete and correct:
- `repository_url` matches the packager commit message
- `commit` matches the packager commit message and is verified in the upstream repo
- `config_yaml: "sources/config.yaml"` is set and the file exists at the referenced commit

## Conclusion

No action needed. The source block in METADATA.pb is complete and correct. Status is **complete** with HIGH confidence.

# Investigation Report: Grey Qo

## Summary

Grey Qo is a static handwriting/display font designed by Robert Leuschke. It was onboarded to Google Fonts in September 2021 via PR #3795 using gftools-packager. The upstream repo at `googlefonts/grey-qo` has only a single commit (`33db197`), which matches the commit hash in METADATA.pb. The repo contains a `.glyphs` source file and a `sources/config.yml` (note: `.yml` extension, not `.yaml`). The METADATA.pb source block is complete with repository URL, commit hash, config path, file mappings, and branch information.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Grey Qo                                                           |
| Repository URL    | https://github.com/googlefonts/grey-qo                            |
| Commit            | `33db197cb6b5c11851eee946d28a0380f9eced9d`                         |
| Config YAML       | `sources/config.yml`                                               |
| Source File       | `sources/GreyQo.glyphs`                                           |
| Status            | complete                                                           |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a detailed source block:
```
source {
  repository_url: "https://github.com/googlefonts/grey-qo"
  commit: "33db197cb6b5c11851eee946d28a0380f9eced9d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GreyQo-Regular.ttf"
    dest_file: "GreyQo-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

### Onboarding History in google/fonts

1. **Initial onboarding** (commit `c4f002a9e`, 2021-09-08): "Grey Qo: Version 2.010 added (#3795)" by Viviana Monsalve. The commit message explicitly states: "Grey Qo Version 2.010 taken from the upstream repo https://github.com/googlefonts/grey-qo at commit https://github.com/googlefonts/grey-qo/commit/33db197cb6b5c11851eee946d28a0380f9eced9d." This also included an upstream.yaml file.

2. **Upstream.yaml merged into METADATA.pb** (commit `66f91f10f`, 2024-04-03): Simon Cozens merged the upstream.yaml data into METADATA.pb, adding the source block with repository_url, file mappings, and branch.

3. **Commit and config added** (commit `19cdcec59`, 2025-03-31): Batch update added the commit hash and config_yaml path from fontc_crater targets list.

### Upstream Repository Verification

The cached repo at `fontc_crater_cache/googlefonts/grey-qo` is a shallow clone with a single commit:
- **Commit `33db197`** (2021-08-30): "v2.010 fonst added" by Viviana Monsalve

The repo contains:
- `sources/GreyQo.glyphs` -- Glyphs source file
- `sources/config.yml` -- gftools-builder configuration
- `fonts/ttf/GreyQo-Regular.ttf` -- Pre-built TTF file
- Standard files (OFL.txt, DESCRIPTION.en_us.html, README.md, etc.)

### Commit Hash Verification

The commit hash `33db197` in METADATA.pb matches:
- The only commit in the upstream repository
- The commit explicitly referenced in the google/fonts onboarding commit message (PR #3795)
- The commit was authored 9 days before the google/fonts merge (2021-08-30 vs 2021-09-08)

This is unambiguously the correct commit.

### Config and Source Files

The `sources/config.yml` contains:
```yaml
sources:
  - GreyQo.glyphs
familyName: "Grey Qo"
buildVariable: false
autohintTTF: false
```

This is a static-only font (buildVariable: false), which is consistent with google/fonts containing only `GreyQo-Regular.ttf` without variable font axes.

## Conclusion

The METADATA.pb source block is complete and correct. All fields (repository_url, commit, config_yaml, file mappings, branch) are properly set and verified against the upstream repository.

### Recommended METADATA.pb source block

No changes needed. The current source block is correct:

```
source {
  repository_url: "https://github.com/googlefonts/grey-qo"
  commit: "33db197cb6b5c11851eee946d28a0380f9eced9d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/GreyQo-Regular.ttf"
    dest_file: "GreyQo-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status**: complete
**Confidence**: HIGH

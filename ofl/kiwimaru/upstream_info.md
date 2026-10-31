# Investigation: Kiwi Maru

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kiwi Maru |
| Slug | kiwi-maru |
| License Dir | ofl |
| Repository URL | https://github.com/Kiwi-KawagotoKajiru/Kiwi-Maru |
| Commit Hash | 65a112c7ec9ffe81595406982a670c7f945d7c5b |
| Config YAML | override config.yaml in google/fonts |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Kiwi-KawagotoKajiru/Kiwi-Maru"
  commit: "65a112c7ec9ffe81595406982a670c7f945d7c5b"
  files {
    source_file: "fonts/ttf/KiwiMaru-Light.ttf"
    dest_file: "KiwiMaru-Light.ttf"
  }
  files {
    source_file: "fonts/ttf/KiwiMaru-Medium.ttf"
    dest_file: "KiwiMaru-Medium.ttf"
  }
  files {
    source_file: "fonts/ttf/KiwiMaru-Regular.ttf"
    dest_file: "KiwiMaru-Regular.ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb contains `repository_url` and `commit`. The upstream repository `Kiwi-KawagotoKajiru/Kiwi-Maru` is cached at `upstream_repos/fontc_crater_cache/Kiwi-KawagotoKajiru/Kiwi-Maru`.

The repository contains separate Glyphs source files in the `sources/` directory:
- `sources/KiwiMaru-Light.glyphs`
- `sources/KiwiMaru-Medium.glyphs`
- `sources/KiwiMaru-Regular.glyphs`

No `config.yaml` exists in the upstream repository. However, `google/fonts/ofl/kiwimaru/config.yaml` provides an override:

```yaml
buildVariable: false
sources:
  - sources/KiwiMaru-Regular.glyphs
  - sources/KiwiMaru-Medium.glyphs
  - sources/KiwiMaru-Light.glyphs
```

The latest commit in the upstream cache is `65a112c` ("Merge pull request #10 from aaronbell/master"), which matches exactly the commit hash in METADATA.pb.

Since there is no `config_yaml` field in METADATA.pb but there is an override `config.yaml` in the google/fonts family directory, google-fonts-sources will auto-detect the local override.

## Conclusion

Status is complete. The source block has repo URL and commit hash. An override `config.yaml` exists in the google/fonts directory. No changes needed to METADATA.pb.

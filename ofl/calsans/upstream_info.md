# Investigation: Cal Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Cal Sans |
| Slug | cal-sans |
| License Dir | ofl |
| Repository URL | https://github.com/calcom/font |
| Commit Hash | b833fb1129ba8c62c29b1d9f70861c77204affe2 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/calcom/font"
  commit: "b833fb1129ba8c62c29b1d9f70861c77204affe2"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/CalSans-Regular.ttf"
    dest_file: "CalSans-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

Cal Sans is a static single-weight font (Regular 400) by Mark Davis and Cal.com Inc., added to Google Fonts on 2025-03-19.

The source information was added by Felipe Sanches in google/fonts commit `b025485e8` ("sources info for Cal Sans", 2025-04-01), which added the `config_yaml: "sources/config.yaml"` field to an already-existing source block. The initial onboarding commit `59e4eb6ee` explicitly references the upstream commit: "Taken from the upstream repo https://github.com/calcom/font at commit https://github.com/calcom/font/commit/b833fb1129ba8c62c29b1d9f70861c77204affe2."

The upstream repo is cached at `upstream_repos/fontc_crater_cache/calcom/font/`. The commit `b833fb1129` (message: "Merge pull request #7 from 0xflotus/patch-1", Peer Richelsen, 2025-03-19) was verified to be the HEAD of the main branch at the time of onboarding. No further commits have been made to the upstream repo since.

The config file `sources/config.yaml` was verified to exist at the recorded commit with contents:

```yaml
sources:
  - Cal-Sans.glyphs
familyName: "Cal Sans"
cleanUp: True
```

This is a static font built from a Glyphs source. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yaml` in the upstream repository.

## Conclusion

All source metadata is complete and verified. The repository URL, commit hash, and config_yaml path are all in place and confirmed by the gftools-packager onboarding commit message. Status is `complete`.

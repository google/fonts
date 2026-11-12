# Investigation: Inspiration

## Summary

| Field | Value |
|-------|-------|
| Family Name | Inspiration |
| Slug | inspiration |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/inspiration |
| Commit Hash | 629ca27262fbcc6cfe745bd95d2e7b72a8e3b047 |
| Config YAML | override config.yaml in google/fonts (ofl/inspiration/config.yaml) |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/inspiration"
  commit: "629ca27262fbcc6cfe745bd95d2e7b72a8e3b047"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Inspiration-Regular.ttf"
    dest_file: "Inspiration-Regular.ttf"
  }
  branch: "master"
}
```

## Investigation

The font was added to google/fonts in commit `245758c4d` ("Inspiration: Version 2.010; ttfautohint (v1.8.3) added (#4114)"). The commit body confirms the source:

> Inspiration Version 2.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/inspiration at commit https://github.com/googlefonts/inspiration/commit/629ca27262fbcc6cfe745bd95d2e7b72a8e3b047.

The upstream repository is cached at `upstream_repos/fontc_crater_cache/googlefonts/inspiration`. The commit `629ca27262` was verified to exist in the cache. The log shows this commit was created on 2021-11-26 with message "v2.010 glyphs info updated".

**Source format**: The repository contains `sources/InspirationPro.glyphs` (a single Glyphs source file). There is **no `config.yaml`** in the upstream repository itself.

However, an override `config.yaml` exists in the google/fonts family directory at `ofl/inspiration/config.yaml` with content:
```yaml
buildVariable: false
sources:
  - sources/InspirationPro.glyphs
```

Per policy, when an override `config.yaml` exists locally, the `config_yaml` field in METADATA.pb is not needed. The current METADATA.pb does not set `config_yaml`, which is correct.

The commit hash in METADATA.pb (`629ca27262`) matches the onboarding commit confirmed in the gftools-packager message. This is verified against the cached repo.

## Conclusion

The source block is complete and correct. The `repository_url` and `commit` are verified. An override `config.yaml` exists in the google/fonts directory. No changes needed.

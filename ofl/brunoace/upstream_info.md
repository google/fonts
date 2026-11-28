# Investigation: Bruno Ace

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bruno Ace |
| Slug | bruno-ace |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/Bruno-ace |
| Commit Hash | 58dc219db32ffd9eaf573f2dc3be2e342410e15a |
| Config YAML | sources/brunoace-regular.yaml |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/Bruno-ace"
  commit: "58dc219db32ffd9eaf573f2dc3be2e342410e15a"
  config_yaml: "sources/brunoace-regular.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BrunoAce-Regular.ttf"
    dest_file: "BrunoAce-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

### Git History in google/fonts

The font has two commits in google/fonts:

1. `3169bfdfe` (2023-03-28) — `[gftools-packager] Bruno Ace: Version 1.100; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.27] added`
2. `90abd17b4` — `Initial commit`

The packager commit message states:

> Bruno Ace Version 1.100; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.27] taken from the upstream repo https://github.com/googlefonts/Bruno-ace at commit https://github.com/googlefonts/Bruno-ace/commit/4eb5f7fc38a1548b353b4ee03b1f7043b48ae181.

The commit message explicitly references **`4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`** as the upstream commit used for onboarding — NOT the `58dc219` currently in METADATA.pb.

### Commit Discrepancy Analysis

The upstream repository (cached at `upstream_repos/fontc_crater_cache/googlefonts/Bruno-ace`) is currently in a detached HEAD state at `58dc219`. The main branch head is `b6fea3b` ("rename sources/*.yaml files to what fontc_crater / google-fonts-sources like").

Timeline of relevant upstream commits:
- `58dc219` (2023-03-23) — "Update README.md" — only README change
- `4eb5f7f` (2023-03-28) — "Update BrunoAceSC-Regular.ttf" — TTF file update

The google/fonts packager commit ran on 2023-03-28 15:34:32 +0200. Upstream commit `4eb5f7f` (which updated the TTF files) was also created on 2023-03-28 at 15:34:03 +0200 — just 29 seconds before the packager commit. This timing confirms that `4eb5f7f` was the actual commit used for onboarding.

METADATA.pb incorrectly references `58dc219` (a README-only commit from March 23), which is an earlier commit that does not include the final TTF files that were actually packaged.

### Config YAML

At commit `4eb5f7f`, the file `sources/brunoace-regular.yaml` exists with content:

```yaml
sources:
  - BrunoAce-Regular.glyphs
buildTTF: true
buildOTF: false
buildStatic: true
buildWebfont: false
```

Note: In the latest main branch commit (`b6fea3b`), this file was renamed to `sources/config-regular.yaml`. The METADATA.pb `config_yaml` field still references the old name `sources/brunoace-regular.yaml`, which is correct for the commit `4eb5f7f` (the actual onboarding commit). If the commit is corrected to `4eb5f7f`, the config path remains valid.

## Conclusion

The commit hash in METADATA.pb needs correction from `58dc219db32ffd9eaf573f2dc3be2e342410e15a` to `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`. The packager commit message explicitly states `4eb5f7f` was the onboarding commit, and the timing (29 seconds before the packager ran) further confirms this. The `config_yaml` path `sources/brunoace-regular.yaml` is valid at `4eb5f7f`.

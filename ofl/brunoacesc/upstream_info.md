# Investigation: Bruno Ace SC

## Summary

| Field | Value |
|-------|-------|
| Family Name | Bruno Ace SC |
| Slug | bruno-ace-sc |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/Bruno-ace |
| Commit Hash | 58dc219db32ffd9eaf573f2dc3be2e342410e15a |
| Config YAML | sources/brunoacesc-regular.yaml |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/Bruno-ace"
  commit: "58dc219db32ffd9eaf573f2dc3be2e342410e15a"
  config_yaml: "sources/brunoacesc-regular.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/BrunoAceSC-Regular.ttf"
    dest_file: "BrunoAceSC-Regular.ttf"
  }
  branch: "main"
}
```

## Investigation

### Git History in google/fonts

The font has two commits in google/fonts:

1. `223112643` (2023-03-28) — `[gftools-packager] Bruno Ace SC: Version 1.100; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.27] added`
2. `90abd17b4` — `Initial commit`

The packager commit message states:

> Bruno Ace SC Version 1.100; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.27] taken from the upstream repo https://github.com/googlefonts/Bruno-ace at commit https://github.com/googlefonts/Bruno-ace/commit/4eb5f7fc38a1548b353b4ee03b1f7043b48ae181.

The commit message explicitly references **`4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`** as the upstream commit used for onboarding — NOT the `58dc219` currently in METADATA.pb. This is the same discrepancy as found in Bruno Ace.

### Commit Discrepancy Analysis

Bruno Ace SC shares the same upstream repository as Bruno Ace (`https://github.com/googlefonts/Bruno-ace`). The same commit discrepancy applies:

- `58dc219` (2023-03-23) — "Update README.md" — only README change; **currently in METADATA.pb (incorrect)**
- `4eb5f7f` (2023-03-28) — "Update BrunoAceSC-Regular.ttf" — explicitly updates `fonts/ttf/BrunoAceSC-Regular.ttf`; **referenced in packager commit message (correct)**

The name of this upstream commit ("Update BrunoAceSC-Regular.ttf") and the packager commit running seconds after on 2023-03-28 both confirm `4eb5f7f` is the correct onboarding commit.

### Config YAML

At commit `4eb5f7f`, the file `sources/brunoacesc-regular.yaml` exists with content:

```yaml
sources:
  - BrunoAceSC-Regular.glyphs
buildTTF: true
buildOTF: false
buildStatic: true
buildWebfont: false
```

Note: In the latest main branch commit (`b6fea3b`), this file was renamed to `sources/config-small-caps.yaml`. The METADATA.pb `config_yaml` field references `sources/brunoacesc-regular.yaml`, which is the correct name at commit `4eb5f7f`.

### Shared Repository Note

Both Bruno Ace and Bruno Ace SC live in the same upstream repository (`googlefonts/Bruno-ace`) and both METADATA.pb files reference the same incorrect commit hash. Both need to be corrected to `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`.

## Conclusion

The commit hash in METADATA.pb needs correction from `58dc219db32ffd9eaf573f2dc3be2e342410e15a` to `4eb5f7fc38a1548b353b4ee03b1f7043b48ae181`. The packager commit message explicitly states `4eb5f7f` was the onboarding commit. The commit name itself ("Update BrunoAceSC-Regular.ttf") confirms it contains the actual font file used. The `config_yaml` path `sources/brunoacesc-regular.yaml` is valid at `4eb5f7f`.

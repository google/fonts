# Investigation: Blaka Hollow

## Summary

| Field | Value |
|-------|-------|
| Family Name | Blaka Hollow |
| Slug | blaka-hollow |
| License Dir | ofl |
| Repository URL | https://github.com/Gue3bara/Blaka |
| Commit Hash | 7f264eee862d3e94c2cb6a728c6429c2f3b9adc3 |
| Config YAML | sources/blakahollow.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Gue3bara/Blaka"
  commit: "7f264eee862d3e94c2cb6a728c6429c2f3b9adc3"
  config_yaml: "sources/blakahollow.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/hollow/ttf/BlakaHollow-Regular.ttf"
    dest_file: "BlakaHollow-Regular.ttf"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

## Investigation

The METADATA.pb contains a complete source block with repository URL, commit hash, and config_yaml path.

The font was last updated in google/fonts commit `1c8403b96` ("[gftools-packager] Blaka Hollow: Version 1.003; ttfautohint (v1.8.4.7-5d5b) added"). The commit body confirms: "Blaka Hollow Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Gue3bara/Blaka at commit https://github.com/Gue3bara/Blaka/commit/7f264eee862d3e94c2cb6a728c6429c2f3b9adc3." This matches the commit hash in the current METADATA.pb.

Commit `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is confirmed in the upstream repo cache at `upstream_repos/fontc_crater_cache/Gue3bara/Blaka` (dated September 29, 2023, "Bumped version to 1.003 across all fonts").

The upstream `sources/` directory at this commit contains `blakahollow.yaml` with content:
```yaml
sources:
  - temp/BlakaHollow-Regular.glyphs
outputDir: "../fonts/hollow"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The `config_yaml: "sources/blakahollow.yaml"` in METADATA.pb correctly references this file. Note that the Blaka family uses a per-variant config approach — `blakahollow.yaml` for Blaka Hollow, `blakaink.yaml` for Blaka Ink, and `blakaregular.yaml` for the main Blaka family.

## Conclusion

The METADATA.pb source block is complete with repository URL, commit hash, and config_yaml path. The commit `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is confirmed as the onboarding commit. No action needed.

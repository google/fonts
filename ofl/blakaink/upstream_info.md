# Investigation: Blaka Ink

## Summary

| Field | Value |
|-------|-------|
| Family Name | Blaka Ink |
| Slug | blaka-ink |
| License Dir | ofl |
| Repository URL | https://github.com/Gue3bara/Blaka |
| Commit Hash | 7f264eee862d3e94c2cb6a728c6429c2f3b9adc3 |
| Config YAML | sources/blakaink.yaml |
| Status | complete |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Gue3bara/Blaka"
  commit: "7f264eee862d3e94c2cb6a728c6429c2f3b9adc3"
  config_yaml: "sources/blakaink.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ink/ttf/BlakaInk-Regular.ttf"
    dest_file: "BlakaInk-Regular.ttf"
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

The font was last updated in google/fonts commit `7dc85ffdb` ("[gftools-packager] Blaka Ink: Version 1.003; ttfautohint (v1.8.4.7-5d5b) added"). The commit body confirms: "Blaka Ink Version 1.003; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/Gue3bara/Blaka at commit https://github.com/Gue3bara/Blaka/commit/7f264eee862d3e94c2cb6a728c6429c2f3b9adc3." This matches the commit hash in the current METADATA.pb.

Commit `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is confirmed in the upstream repo cache at `upstream_repos/fontc_crater_cache/Gue3bara/Blaka` (dated September 29, 2023, "Bumped version to 1.003 across all fonts").

The upstream `sources/` directory at this commit contains `blakaink.yaml` with content:
```yaml
sources:
  - Blaka-Ink.glyphs
outputDir: "../fonts/ink"
buildStatic: true
buildVariable: false
buildTTF: true
buildOTF: false
buildWebfont: false
```

The `config_yaml: "sources/blakaink.yaml"` in METADATA.pb correctly references this file. The Blaka family uses per-variant config files — the same commit `7f264eee` is referenced by both Blaka Hollow and Blaka Ink. This is also the same repository as the main Blaka family.

The METADATA.pb diff in the most recent update commit shows the commit was changed from `023c078707d89764cbe9e720c37c11511eb1686b` to `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3`, confirming a proper version update occurred.

## Conclusion

The METADATA.pb source block is complete with repository URL, commit hash, and config_yaml path. The commit `7f264eee862d3e94c2cb6a728c6429c2f3b9adc3` is confirmed as the onboarding commit. No action needed.

# Investigation: Instrument Serif

## Summary

| Field | Value |
|-------|-------|
| Family Name | Instrument Serif |
| Slug | instrument-serif |
| License Dir | ofl |
| Repository URL | https://github.com/Instrument/instrument-serif |
| Commit Hash | 65c0ef225f386a3c7e87570a4aa9cc0262c2fd81 |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Instrument/instrument-serif"
  commit: "65c0ef225f386a3c7e87570a4aa9cc0262c2fd81"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/InstrumentSerif-Regular.ttf"
    dest_file: "InstrumentSerif-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/InstrumentSerif-Italic.ttf"
    dest_file: "InstrumentSerif-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font was initially added to google/fonts in commit `5e0122a40` ("Instrument Serif: Version 1.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.23] added (#5981)"). The original onboarding commit body stated:

> Instrument Serif Version 1.000; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.27] taken from the upstream repo https://github.com/Instrument/instrument-serif at commit https://github.com/Instrument/instrument-serif/commit/9aefd76b9b96dffbdc7b65d38c0dc5bcae2717a9.

The METADATA.pb was subsequently updated by two commits:
1. `66f91f10f` (2024-04-03) — "Merge upstream.yaml into METADATA.pb" — added `files` and `branch` fields
2. `19cdcec59` (2025-03-31) — "[Batch 1/4] port info from fontc_crater targets list" (by Felipe Sanches) — changed commit from `9aefd76b` to `65c0ef225f386a3c7e87570a4aa9cc0262c2fd81` and added `config_yaml: "sources/config.yaml"`

The upstream repository is cached at `upstream_repos/fontc_crater_cache/Instrument/instrument-serif`. **The repository has only a single commit**: `65c0ef225f386a3c7e87570a4aa9cc0262c2fd81` (2023-04-26, "Update README.md"). The original onboarding commit `9aefd76b` does not exist in the current repository, indicating the repo was likely squash-reset or recreated.

The current METADATA.pb commit `65c0ef22` is the only commit in the repo and is verified to exist. The `sources/config.yaml` file exists in the upstream repo.

**Source format**: The repository contains `sources/Instrument_Serif.glyphs` and `sources/Instrument_Serif_Italic.glyphs`. A `config.yaml` exists at `sources/config.yaml` with content listing both Glyphs sources.

Note: Confidence is MEDIUM because the original onboarding commit (`9aefd76b`) no longer exists in the repo. The current commit hash (`65c0ef22`) was set by the batch update from fontc_crater targets, corresponding to the only available state of the repository.

## Conclusion

The source block is complete. The `repository_url`, `commit`, and `config_yaml` are all set. The commit hash was updated by Felipe Sanches in the fontc_crater batch update to match the only available commit in the repository. No further changes are strictly needed.

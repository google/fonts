# Investigation: Instrument Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Instrument Sans |
| Slug | instrument-sans |
| License Dir | ofl |
| Repository URL | https://github.com/Instrument/instrument-sans |
| Commit Hash | 7fa22308a3d0c94ee2b3cd537a1196b65db34a3e |
| Config YAML | sources/config.yaml |
| Status | complete |
| Confidence | MEDIUM |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/Instrument/instrument-sans"
  commit: "7fa22308a3d0c94ee2b3cd537a1196b65db34a3e"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/InstrumentSans[wdth,wght].ttf"
    dest_file: "InstrumentSans[wdth,wght].ttf"
  }
  files {
    source_file: "fonts/variable/InstrumentSans-Italic[wdth,wght].ttf"
    dest_file: "InstrumentSans-Italic[wdth,wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

The font was initially added to google/fonts in commit `2fc9491da` ("Instrument Sans: Version 1.000;gftools[0.9.28] added"). The original onboarding commit body stated:

> Instrument Sans Version 1.000;gftools[0.9.28] taken from the upstream repo https://github.com/Instrument/instrument-sans at commit https://github.com/Instrument/instrument-sans/commit/4a27996becc1c7d8e8d4095df4bb485068252bb2.

The METADATA.pb was subsequently updated by two commits:
1. `66f91f10f` (2024-04-03) — "Merge upstream.yaml into METADATA.pb" — added `files` and `branch` fields, kept commit `4a27996`
2. `19cdcec59` (2025-03-31) — "[Batch 1/4] port info from fontc_crater targets list" (by Felipe Sanches) — changed commit to `7fa22308a3d0c94ee2b3cd537a1196b65db34a3e` and added `config_yaml: "sources/config.yaml"`

The upstream repository is cached at `upstream_repos/fontc_crater_cache/Instrument/instrument-sans`. **The repository has only a single commit**: `7fa22308a3d0c94ee2b3cd537a1196b65db34a3e` (2023-06-14, "feat: updated example gif"). The original onboarding commit `4a27996` does not exist in the current repository, indicating the repo was likely squash-reset or recreated.

The current METADATA.pb commit `7fa22308` is the only commit in the repo and is verified to exist. The `sources/config.yaml` file exists in the upstream repo with `.glyphs` sources listed.

**Source format**: The repository contains `sources/InstrumentSans.glyphs` and `sources/InstrumentSans-Italic.glyphs`. A `config.yaml` exists at `sources/config.yaml`.

Note: Confidence is MEDIUM because the original onboarding commit (`4a27996`) no longer exists in the repo. The current commit hash (`7fa22308`) was set by the batch update from fontc_crater targets, which corresponds to the only available state of the repository.

## Conclusion

The source block is complete. The `repository_url`, `commit`, and `config_yaml` are all set. The commit hash was updated by Felipe Sanches in the fontc_crater batch update to match the only available commit in the repository. No further changes are strictly needed, though the discrepancy between the original onboarding commit (now gone) and the current commit should be noted.

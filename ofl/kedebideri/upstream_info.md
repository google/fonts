# Investigation: Kedebideri

## Summary

| Field | Value |
|-------|-------|
| Family Name | Kedebideri |
| Slug | kedebideri |
| License Dir | ofl |
| Repository URL | https://github.com/silnrsi/font-kedebideri |
| Commit Hash | 4973b2e0258ef40acc0da3c2c1d155630faecc2c |
| Config YAML | none (SIL smith build system) |
| Status | missing_config |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/silnrsi/font-kedebideri"
  commit: "4973b2e0258ef40acc0da3c2c1d155630faecc2c"
  archive_url: "https://github.com/silnrsi/font-kedebideri/releases/download/v3.001/Kedebideri-3.001.zip"
  files {
    source_file: "Kedebideri-3.001/OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "Kedebideri-3.001/Kedebideri-Regular.ttf"
    dest_file: "Kedebideri-Regular.ttf"
  }
  ...
  branch: "main"
}
primary_language: "zag_Berf"
stroke: "SANS_SERIF"
```

## Investigation

The METADATA.pb contains `repository_url`, `commit`, and `archive_url` but no `config_yaml`. The upstream repository `silnrsi/font-kedebideri` is cached at `upstream_repos/fontc_crater_cache/silnrsi/font-kedebideri`.

This is a SIL International font for the Zaghawa script (Beria). The `source/` directory contains:
- `Kedebideri.designspace` (Designspace format)
- `KedebideriAxis.designspace`
- `masters/` (UFO masters)
- `opentype/` (OpenType feature files)

The repository uses SIL's wscript/smith build system, not gftools-builder. No `config.yaml` exists in the repository. The commit hash `4973b2e` is recorded and corresponds to the v3.001 release.

The latest git log entry is `142f05a` ("Update copyright date to 2026..."), which is more recent than the recorded commit hash.

## Conclusion

The source block has repository URL and commit hash. However, the SIL smith build system is not compatible with gftools-builder, so no `config.yaml` is possible. Status is missing_config with the understanding that the build system incompatibility makes config.yaml creation infeasible.

## Update (2026-04-24) — Override config.yaml

**Model**: Claude Opus 4.7 (1M context)

Added an override `config.yaml` in `ofl/kedebideri/` referencing the upstream gftools-builder-compatible source at the pinned commit `4973b2e` (`source/Kedebideri.designspace`). The upstream repo has no `config.yaml` of its own at this rev; `google-fonts-sources` auto-detects the override and records it in crater's `targets.json` as an external config on the next regeneration.

## Recent upstream/main activity (post-investigation)

- **2026-01-07** — Emma Marichal, commit [`1776dc2bb`](https://github.com/google/fonts/commit/1776dc2bb) ("Add subset 'beria-erfe' to METADATA.pb"): added a new entry `subsets: "beria-erfe"` (Beria-Erfe is the script-name token used in Google Fonts for the family's primary script). Outside the `source { ... }` block.
- **2026-01-15** — Garret Rieger, commit [`9711e9d18`](https://github.com/google/fonts/commit/9711e9d18) ("Use primary_language instead of script for Kedebideri so that sample text will be chosen correctly"): switched `primary_script` to `primary_language` so the catalog sample-text picker resolves correctly for this minority-script family. Outside the `source { ... }` block.

### Earlier (2025-10-02)

- **2025-10-02** — Emma Marichal, commit [`03f0d980e`](https://github.com/google/fonts/commit/03f0d980e) ("fix OFL"): fixed a typo in `OFL.txt` ("with an FAQ" → "with a FAQ", added a missing line about the SIL OFL license). License-file change tracked here per policy.

### Earlier (2025-09-17)

- **2025-09-17** — Emma Marichal, commit [`116a842bb`](https://github.com/google/fonts/commit/116a842bb) ("Kedebideri: Version 3.001 added"): initial onboarding via gftools-packager. Created `ofl/kedebideri/` with source block referencing `silnrsi/font-kedebideri@4973b2e0258ef40acc0da3c2c1d155630faecc2c`, archive_url to v3.001 release.

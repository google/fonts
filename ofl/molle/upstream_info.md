# Molle — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [SorkinType/Molle2](https://github.com/SorkinType/Molle2) |
| Commit | `3924159e0186e87a1a93d1ce80b5341164310f4f` |
| Binary Date | 2015-09-21 |
| Source Types | binary/TTX only |
| Buildable | No |
| Confidence | Medium (date correlation) |

## Notes

Source repository for molle. Commit determined by date correlation with the last binary modification in google/fonts (2015-09-21).


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "sources/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `3924159e` (via the bare mirror in `upstream_repos/repo_archive/SorkinType/Molle2.git`) confirms that `sources/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.

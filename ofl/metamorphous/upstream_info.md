# Metamorphous — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [SorkinType/Metamorphous](https://github.com/SorkinType/Metamorphous) |
| Commit | `d2d29bb34284baff0817ecfce363b6d0e621e738` |
| Binary Date | 2015-03-07 |
| Source Types | binary/TTX only |
| Buildable | No |
| Confidence | Medium (date correlation) |

## Notes

Source repository for metamorphous. Commit determined by date correlation with the last binary modification in google/fonts (2015-03-07).


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "sources/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `d2d29bb3` (via the bare mirror in `upstream_repos/repo_archive/SorkinType/Metamorphous.git`) confirms that `sources/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.

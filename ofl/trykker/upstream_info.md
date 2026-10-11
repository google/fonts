# Trykker — Source Repository Investigation

**Model**: Claude Opus 4.6

## Source Repository

| Field | Value |
|-------|-------|
| Repository | [SorkinType/Trykker](https://github.com/SorkinType/Trykker) |
| Commit | `5226cb075048ff1d3bd16fd0a0c42ece45629afb` |
| Binary Date | 2015-03-07 |
| Source Types | binary/TTX only |
| Buildable | No |
| Confidence | Medium (date correlation) |

## Notes

Source repository for trykker. Commit determined by date correlation with the last binary modification in google/fonts (2015-03-07).


## Update (2026-04-24)

**Model**: Claude Opus 4.7 (1M context)

Added `config_yaml: "sources/config.yaml"` to the METADATA.pb `source { }` block. Direct inspection of the upstream repo at the pinned commit `5226cb07` (via the bare mirror in `upstream_repos/repo_archive/SorkinType/Trykker.git`) confirms that `sources/config.yaml` exists at that commit and is a valid gftools-builder config — it declares the `sources:` key. The family should move from the dashboard's "missing_config" bucket into "covered" once `google-fonts-sources` regenerates crater's `targets.json`.

## fontc_crater Build Fix (2026-05-21)

**Model**: Claude Opus 4.7

### Initial state
METADATA.pb pointed `config_yaml` at the upstream `sources/config.yaml`. That file's `sources:` list contains a single entry, `Trykker`, with no file extension, so the build failed with `missing source 'Trykker'`. (This also corrects the "Source Types: binary/TTX only / Buildable: No" note above — the repo does contain a Glyphs 3 package source.)

### Investigation
At the recorded commit `5226cb07` the font source is the Glyphs 3 package directory `sources/Trykker.glyphspackage`. The upstream `sources/config.yaml` is a gftools-builder template whose `sources:` entry was left as `Trykker`, missing the `.glyphspackage` extension. The recorded commit is correct.

### Actions taken
An override `config.yaml` was created in the family directory with the corrected, repo-root-relative source path `sources/Trykker.glyphspackage`. The `config_yaml` field was removed from METADATA.pb so google-fonts-sources auto-detects the override.

### Final state
The override `config.yaml` references `sources/Trykker.glyphspackage`, which exists at the recorded commit `5226cb07`.

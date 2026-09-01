# Bilbo

**Status**: `complete`
**Date**: 2026-02-26
**Designer**: Robert Leuschke
**License**: OFL
**METADATA.pb**: `ofl/bilbo/METADATA.pb`

## Data

| Field | Value |
|-------|-------|
| Repository URL | https://github.com/googlefonts/bilbo |
| Commit | `1ffb16299d6f1ae0304a0ed6a36a95acbb1148e3` |
| Config YAML | `sources/config.yml` (in upstream repo) |
| Source types | glyphs |

## Methodology

### Repository URL
Documented in METADATA.pb `source.repository_url`. Confirmed by the copyright string ("The Bilbo Project Authors (https://github.com/googlefonts/bilbo)"). The repository is in the googlefonts organization, indicating it was migrated there as part of standard Google Fonts workflow.

### Commit Hash
The commit `1ffb16299d6f1ae0304a0ed6a36a95acbb1148e3` was added to METADATA.pb from the fontc_crater target list (commit `19cdcec59` in google/fonts, "[Batch 1/4] port info from fontc_crater targets list", 2025-03-31).

**Binary blob verification**: The file `fonts/ttf/Bilbo-Regular.ttf` at commit `1ffb162` in upstream has blob hash `b76f5e6e157d78ad0111840f70a48ea5d014b05b`, which exactly matches the current google/fonts file.

PR #3329 ("Bilbo: Version 1.100 added") referenced upstream commit `40148a3e58ba010aa87c4ebf09f357ffb23475ff`, but this commit is not available in the current shallow clone of the repo. The commit `1ffb162` is the HEAD of master ("legacy source deleted", 2021-08-30). Since the binary blob matches, `1ffb162` either contains the same font binary as `40148a3e`, or (more likely) `1ffb162` is a subsequent commit that deleted legacy sources without changing the font binaries.

The fontc_crater team independently identified `1ffb162` as the correct commit for their targets, and the binary match confirms this.

### Config YAML
The upstream repo at commit `1ffb162` contains `sources/config.yml` with gftools-builder configuration:
```yaml
sources:
  - BilboPro.glyphs
familyName: "Bilbo"
buildVariable: false
autohintTTF: false
```

This is correctly referenced in METADATA.pb as `config_yaml: "sources/config.yml"`.

## Evidence

### METADATA.pb source block (current main)
```
source {
  repository_url: "https://github.com/googlefonts/bilbo"
  commit: "1ffb16299d6f1ae0304a0ed6a36a95acbb1148e3"
  files { source_file: "OFL.txt" dest_file: "OFL.txt" }
  files { source_file: "DESCRIPTION.en_us.html" dest_file: "DESCRIPTION.en_us.html" }
  files { source_file: "fonts/ttf/Bilbo-Regular.ttf" dest_file: "Bilbo-Regular.ttf" }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

### google/fonts history
- `19cdcec59` (2025-03-31): "[Batch 1/4] port info from fontc_crater targets list" -- added commit hash and config_yaml
- `4af5d2170` (2021-04-26): "Bilbo: Version 1.100 added (#3329)" -- last font binary update
- `254c91e36`: "Updating ofl/bilbo/*ttf with nbspace and fsType fixes" (earlier modification)
- `90abd17b4`: "Initial commit" (original addition)

### PR #3329
- Title: "Bilbo: Version 1.100 added"
- Author: vv-monsalve (Viviana Monsalve)
- Commit message: "Bilbo Version 1.100 taken from the upstream repo https://github.com/googlefonts/bilbo at commit 40148a3e58ba010aa87c4ebf09f357ffb23475ff"

### Binary blob verification
| Source | Blob Hash |
|--------|-----------|
| Upstream at `1ffb162` | `b76f5e6e157d78ad0111840f70a48ea5d014b05b` |
| google/fonts current | `b76f5e6e157d78ad0111840f70a48ea5d014b05b` |

### Upstream repo cache
- Cached at: `googlefonts/bilbo` (shallow clone, depth=1)
- Commit `1ffb162` is HEAD of master
- `fonts/ttf/Bilbo-Regular.ttf` exists with matching blob hash
- `sources/config.yml` exists with valid gftools-builder config
- `sources/BilboPro.glyphs` is the build source

## Confidence

**High**: Binary blob verification confirms the font matches. The fontc_crater team independently verified this commit. Config YAML correctly documented.

## Notes
- Bilbo and Bilbo Swash Caps are in DIFFERENT upstream repos (googlefonts/bilbo vs librefonts/bilboswashcaps)
- Originally added to Google Fonts 2011-12-07, last font update 2021 (v1.100)
- The packager commit `40148a3e` is not in the shallow clone but `1ffb162` has the same binary
- Static font only (no variable font), consistent with `buildVariable: false` in config.yml

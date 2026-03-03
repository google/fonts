# Investigation Report: Gabriela

## Summary

Gabriela is a serif display font designed by Eduardo Tunni, originally added to Google Fonts in 2013. It was updated to version 2.001 on 2023-03-15 by Emma Marichal using gftools-packager, at which point the source block was added to METADATA.pb. The upstream repository at `etunni/Gabriela` contains a single commit (a merge of Emma Marichal's preparation PR) which is both HEAD and the referenced commit. The source block is fully populated with repository URL, commit hash, branch, and config_yaml. The upstream repo has gftools-builder compatible `.glyphs` source files and a `sources/config.yaml`.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Gabriela |
| Upstream Repo | https://github.com/etunni/Gabriela |
| Commit Hash | `961e4fb89c38cbe8ddcc3c9268c42d94c834d5da` |
| Branch | master |
| Config YAML | `sources/config.yaml` (in upstream repo) |
| Source Files | `sources/Gabriela.glyphs` |
| Status | **complete** |
| Confidence | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/etunni/Gabriela"
  commit: "961e4fb89c38cbe8ddcc3c9268c42d94c834d5da"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gabriela-Regular.ttf"
    dest_file: "Gabriela-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

### Onboarding and Update History in google/fonts

Gabriela has a longer history than the other two families in this batch:

1. **Original onboarding** (`90abd17b4`, early 2013) - Part of the initial Google Fonts commit
2. **v2.000 update** (`45b40149f`, 2017-01-17) by Marc Foley - "gabriela: v2.000 added (#551)"
3. **v2.001 update with source block** (`9a83790ee`, 2023-03-15) by Emma Marichal via gftools-packager:

> Gabriela: Version 2.001;gftools[0.9.26] added (#5995)
> [gftools-packager] Gabriela: Version 2.001;gftools[0.9.26] added
> Gabriela Version 2.001;gftools[0.9.26] taken from the upstream repo https://github.com/etunni/Gabriela at commit https://github.com/etunni/Gabriela/commit/961e4fb89c38cbe8ddcc3c9268c42d94c834d5da.

The `config_yaml` field was added later in commit `19cdcec59` (2025-03-31, Batch 1/4 fontc_crater targets).

### Commit History in google/fonts for ofl/gabriela/

1. `90abd17b4` - Initial commit (2013)
2. Various metadata/copyright updates
3. `45b40149f` (2017-01-17) - gabriela v2.000 added (#551)
4. Language support metadata updates
5. `9a83790ee` (2023-03-15) - v2.001 update with source block added (PR #5995)
6. `1db714082` - Stroke and classification metadata update
7. `113af68ff` - DESCRIPTION update
8. `66f91f10f` - Merge upstream.yaml into METADATA.pb
9. `19cdcec59` (2025-03-31) - Added `config_yaml: "sources/config.yaml"`

### Upstream Repository Analysis

- **URL**: https://github.com/etunni/Gabriela
- **Cached at**: `upstream_repos/fontc_crater_cache/etunni/Gabriela`
- **Default branch**: master
- **Total commits**: 1 (single merge commit)
- **HEAD**: `961e4fb89c38cbe8ddcc3c9268c42d94c834d5da` (2023-03-09)

The repository contains a single merge commit: "Merge pull request #6 from emmamarichal/master". This is the standard pattern where Emma Marichal prepared the upstream repo with gftools-compatible structure.

### Commit Hash Verification

The commit hash `961e4fb89c38cbe8ddcc3c9268c42d94c834d5da` is verified correct:

1. It is the only commit in the repo and matches HEAD
2. It is explicitly referenced in the gftools-packager commit message in google/fonts (PR #5995)
3. The upstream merge commit date (2023-03-09) is 6 days before the google/fonts merge (2023-03-15), a typical review turnaround
4. The font binary `fonts/ttf/Gabriela-Regular.ttf` in the upstream repo is 70,984 bytes, matching the binary size shown in the google/fonts commit diff

### Source Files and Build Configuration

The upstream repo contains:
- `sources/Gabriela.glyphs` - Glyphs source file
- `sources/config.yaml` - gftools-builder configuration
- `old/version 1.002/sources/Gabriela-Regular-Cyr.vfb` - Legacy VFB source

Config.yaml contents:
```yaml
sources:
  - Gabriela.glyphs
familyName: Gabriela
buildVariable: false
autohintTTF: false
```

No local override config.yaml exists in google/fonts.

### Font Details

- **Subsets**: cyrillic, cyrillic-ext, latin, latin-ext, menu
- **Style**: Regular only (weight 400)
- **Classifications**: Serif, Display
- The March 2023 update (v2.001) added a bigger glyph set, fractions, and minor aesthetic modifications

## Conclusion

The source block in METADATA.pb is complete and correct. All fields (repository_url, commit, files, branch, config_yaml) are properly set. No changes are needed.

### Recommended METADATA.pb Source Block

No changes required. The existing source block is correct:

```
source {
  repository_url: "https://github.com/etunni/Gabriela"
  commit: "961e4fb89c38cbe8ddcc3c9268c42d94c834d5da"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Gabriela-Regular.ttf"
    dest_file: "Gabriela-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yaml"
}
```

**Status**: complete
**Confidence**: HIGH

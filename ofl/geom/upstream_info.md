# Investigation Report: Geom

## Summary

Geom is a variable geometric sans-serif typeface designed by Thanos Poulakidas, added to Google Fonts on 2025-11-14. The source block in METADATA.pb is complete with repository URL, commit hash, and config_yaml path. All data has been verified against the upstream repository and the onboarding commit message.

## Key Findings

| Field              | Value                                                                      |
|--------------------|----------------------------------------------------------------------------|
| Family Name        | Geom                                                                       |
| Designer           | Thanos Poulakidas                                                          |
| Date Added         | 2025-11-14                                                                 |
| Repository URL     | https://github.com/ThanosPoulakidas/Geom                                   |
| Commit Hash        | c20a14c68c717e28fdb6e1cc7cc6b453fef5fef7                                   |
| Config YAML        | sources/config.yaml                                                        |
| Source Files       | sources/Geom.glyphs, sources/Geom-Italic.glyphs                           |
| Status             | complete                                                                   |
| Confidence         | HIGH                                                                       |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a complete source block:

```
source {
  repository_url: "https://github.com/ThanosPoulakidas/Geom"
  commit: "c20a14c68c717e28fdb6e1cc7cc6b453fef5fef7"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Geom[wght].ttf"
    dest_file: "Geom[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Geom-Italic[wght].ttf"
    dest_file: "Geom-Italic[wght].ttf"
  }
  branch: "main"
}
```

### Onboarding PR and Commit

The font was onboarded via PR #9998, merged on 2025-11-20. The onboarding commit is `56f2b097`:

> Geom: Version 1.102 added
>
> Taken from the upstream repo https://github.com/ThanosPoulakidas/Geom at commit https://github.com/ThanosPoulakidas/Geom/commit/c20a14c68c717e28fdb6e1cc7cc6b453fef5fef7.

The commit hash `c20a14c6` in METADATA.pb matches the onboarding commit message exactly.

### Upstream Repository Verification

The upstream repo at `https://github.com/ThanosPoulakidas/Geom` is cached at `upstream_repos/fontc_crater_cache/ThanosPoulakidas/Geom/`. The repo has a single commit (`c20a14c6`, "Merge pull request #8 from emmamarichal/main", dated 2025-11-14), confirming this is the exact state used for onboarding.

At commit `c20a14c6`:
- **config.yaml** exists at `sources/config.yaml`
- **Source files**: `sources/Geom.glyphs` and `sources/Geom-Italic.glyphs` (Glyphs format)
- **Variable fonts**: 2 files (upright and italic), each with wght axis (300-900)

The config.yaml specifies:
- Sources: `Geom.glyphs` and `Geom-Italic.glyphs`
- Axis order: wght, ital
- Family name: "Geom"
- Build options: removeOutlineOverlaps disabled, cleanUp enabled

### config_yaml Field Addition

The `config_yaml: "sources/config.yaml"` field was added to METADATA.pb in a later batch commit (`34926685`, 2026-02-16) that added config_yaml for 15 font families. This is a valid enrichment -- the config.yaml existed in the upstream repo at the onboarding commit.

### Onboarding Author

The onboarding was performed by Emma Marichal (emmamarichal), as evidenced by:
- The google/fonts onboarding commit author: Emma Marichal
- The upstream merge commit referencing PR #8 from `emmamarichal/main`

## Conclusion

### Current METADATA.pb Source Block (Already Correct)

```
source {
  repository_url: "https://github.com/ThanosPoulakidas/Geom"
  commit: "c20a14c68c717e28fdb6e1cc7cc6b453fef5fef7"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Geom[wght].ttf"
    dest_file: "Geom[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Geom-Italic[wght].ttf"
    dest_file: "Geom-Italic[wght].ttf"
  }
  branch: "main"
}
```

### Status: complete

All source metadata fields are present and verified. The repository URL, commit hash, and config_yaml path are all correct. No changes needed.

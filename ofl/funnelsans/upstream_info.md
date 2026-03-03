# Investigation Report: Funnel Sans

## Summary

Funnel Sans is a variable sans-serif typeface designed by NORD ID and Kristian Moller, added to Google Fonts on 2024-09-27. The upstream repository is at `https://github.com/Dicotype/Funnel`, which is a monorepo containing both Funnel Sans and Funnel Display families. The METADATA.pb source block is complete and correct - the `config_yaml` correctly points to `sources/config.yaml` which is the Funnel Sans config.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Funnel Sans |
| Designer          | NORD ID, Kristian Moller |
| Repository URL    | https://github.com/Dicotype/Funnel |
| Commit Hash       | f9509ce0df3c344ddc454600baf77df54b83c379 |
| Config YAML       | sources/config.yaml |
| Status            | **complete** |
| Confidence        | HIGH |

## Investigation Details

### Google Fonts History

The font was onboarded in commit `a0fd7975f` (2024-09-27) by Emma Marichal. The commit message explicitly references:
- Upstream repo: https://github.com/Dicotype/Funnel
- Commit: `f9509ce0df3c344ddc454600baf77df54b83c379`

The source block was enhanced in commit `19cdcec59` (2025-03-31, "Batch 1/4 port info from fontc_crater targets list") which added `config_yaml: "sources/config.yaml"`.

### Upstream Repository

- **URL**: https://github.com/Dicotype/Funnel
- **Cached at**: `upstream_repos/fontc_crater_cache/Dicotype/Funnel`
- **Branch**: main
- **HEAD commit**: `f9509ce` (2024-09-27) - "Merge pull request #3 from emmamarichal/main"

This is a monorepo containing both Funnel Sans and Funnel Display. The commit `f9509ce` is a merge commit by Emma Marichal, timestamped the same day as the google/fonts onboarding.

### Source Files

In the `sources/` directory at commit `f9509ce`:
- `FunnelSans.glyphs` - Funnel Sans source (523 KB)
- `FunnelSans-Italic.glyphs` - Funnel Sans Italic source (642 KB)
- `FunnelDisplay.glyphs` - Funnel Display source (524 KB)
- `config.yaml` - Config for **Funnel Sans** (familyName: "Funnel Sans")
- `config_display.yaml` - Config for **Funnel Display** (familyName: "Funnel Display")
- `build.sh` - Build script that runs both configs

### Config YAML Verification

The config at `sources/config.yaml` correctly configures Funnel Sans:
```yaml
sources:
  - FunnelSans.glyphs
  - FunnelSans-Italic.glyphs
familyName: "Funnel Sans"
axisOrder:
  - wght
  - ital
```

This is confirmed correct for the Funnel Sans family (unlike Funnel Display, which needs `config_display.yaml`).

### Commit Hash Verification

The commit `f9509ce` in the upstream repo is dated 2024-09-27, same day as the google/fonts onboarding commit `a0fd7975f`. The onboarding commit explicitly references this hash. This is confirmed correct.

### Font Files

The font ships as two variable font files:
- `FunnelSans[wght].ttf` - Roman (weight axis: 300-800)
- `FunnelSans-Italic[wght].ttf` - Italic (weight axis: 300-800)

## Conclusion

The METADATA.pb source block is complete and correct. All fields are verified:
- Repository URL is valid and cached
- Commit hash `f9509ce` matches the onboarding commit
- Config YAML path `sources/config.yaml` correctly points to the Funnel Sans config
- Branch is correctly set to `main`

### Current METADATA.pb source block (verified correct)

```
source {
  repository_url: "https://github.com/Dicotype/Funnel"
  commit: "f9509ce0df3c344ddc454600baf77df54b83c379"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Funnel_Sans/variable/FunnelSans[wght].ttf"
    dest_file: "FunnelSans[wght].ttf"
  }
  files {
    source_file: "fonts/Funnel_Sans/variable/FunnelSans-Italic[wght].ttf"
    dest_file: "FunnelSans-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

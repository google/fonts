# Investigation Report: Funnel Display

## Summary

Funnel Display is a variable display typeface designed by NORD ID and Kristian Moller, added to Google Fonts on 2024-09-25. The upstream repository is at `https://github.com/Dicotype/Funnel`, which is a monorepo containing both Funnel Display and Funnel Sans families. The METADATA.pb has a source block but the `config_yaml` field is **incorrect**: it points to `sources/config.yaml` which is actually the Funnel Sans config. The correct config for Funnel Display is `sources/config_display.yaml`.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Funnel Display |
| Designer          | NORD ID, Kristian Moller |
| Repository URL    | https://github.com/Dicotype/Funnel |
| Commit Hash       | f9509ce0df3c344ddc454600baf77df54b83c379 |
| Config YAML       | sources/config_display.yaml |
| Status            | **needs_correction** |
| Confidence        | HIGH |

## Investigation Details

### Google Fonts History

The font was onboarded in commit `f788e477` (2024-09-27) by Emma Marichal. The commit message explicitly references:
- Upstream repo: https://github.com/Dicotype/Funnel
- Commit: `f9509ce0df3c344ddc454600baf77df54b83c379`

The source block was enhanced in commit `19cdcec59` (2025-03-31, "Batch 1/4 port info from fontc_crater targets list") which added `config_yaml: "sources/config.yaml"`.

### Upstream Repository

- **URL**: https://github.com/Dicotype/Funnel
- **Cached at**: `upstream_repos/fontc_crater_cache/Dicotype/Funnel`
- **Branch**: main
- **HEAD commit**: `f9509ce` (2024-09-27) - "Merge pull request #3 from emmamarichal/main"

This is a monorepo containing both Funnel Display and Funnel Sans. The commit `f9509ce` is a merge commit by Emma Marichal, timestamped the same day as the google/fonts onboarding.

### Source Files

In the `sources/` directory at commit `f9509ce`:
- `FunnelDisplay.glyphs` - Funnel Display source (524 KB)
- `FunnelSans.glyphs` - Funnel Sans source (523 KB)
- `FunnelSans-Italic.glyphs` - Funnel Sans Italic source (642 KB)
- `config.yaml` - Config for **Funnel Sans** (familyName: "Funnel Sans")
- `config_display.yaml` - Config for **Funnel Display** (familyName: "Funnel Display")
- `build.sh` - Build script that runs both configs

### Config YAML Issue

The `build.sh` script confirms the config mapping:
```sh
gftools builder config.yaml         # Builds Funnel Sans
gftools builder config_display.yaml # Builds Funnel Display
```

The current METADATA.pb has `config_yaml: "sources/config.yaml"`, but this config builds Funnel Sans (familyName: "Funnel Sans"). The correct config for Funnel Display is `sources/config_display.yaml`.

This error was introduced in commit `19cdcec59` when porting from fontc_crater targets. The fontc_crater targets list likely had both configs for this repo, and the wrong one was assigned to Funnel Display.

### Commit Hash Verification

The commit `f9509ce` in the upstream repo is dated 2024-09-27, same day as the google/fonts onboarding commits. The onboarding commit `f788e477` explicitly references this hash. This is confirmed correct.

## Conclusion

The source block needs correction: the `config_yaml` field must be changed from `sources/config.yaml` to `sources/config_display.yaml`. All other fields are correct.

### Recommended METADATA.pb source block

```
source {
  repository_url: "https://github.com/Dicotype/Funnel"
  commit: "f9509ce0df3c344ddc454600baf77df54b83c379"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/Funnel_Display/variable/FunnelDisplay[wght].ttf"
    dest_file: "FunnelDisplay[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config_display.yaml"
}
```

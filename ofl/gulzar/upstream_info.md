# Investigation Report: Gulzar

## Summary

Gulzar is a contemporary Urdu Nasta'liq typeface with a Latin counterpart, designed by Borna Izadpanah, Simon Cozens, Alice Savoie, and Fiona Ross. It was onboarded to Google Fonts in May 2022 (PR #4674) by Simon Cozens from the upstream repository `simoncozens/Gulzar`. The METADATA.pb source block is complete with a verified commit hash. An override `config.yaml` already exists in the google/fonts family directory. The upstream repo uses a custom Makefile-based build (with fontmake, fez2fea, and hb-subset), but the override config.yaml provides gftools-builder compatibility using the `.glyphs` source.

## Key Findings

| Field              | Value                                                              |
|--------------------|--------------------------------------------------------------------|
| Family Name        | Gulzar                                                             |
| Repository URL     | https://github.com/simoncozens/Gulzar                              |
| Commit Hash        | 42b27958a84d56d8341ad1e2dc26b19dba03b15f                           |
| Config YAML        | Override config.yaml in google/fonts                               |
| Status             | complete                                                           |
| Confidence         | HIGH                                                               |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb at `ofl/gulzar/METADATA.pb` contains a complete source block:
- `repository_url`: `https://github.com/simoncozens/Gulzar`
- `commit`: `42b27958a84d56d8341ad1e2dc26b19dba03b15f`
- `branch`: `main`
- Files mapping `fonts/ttf/Gulzar-Regular.ttf`, `OFL.txt`, and `DESCRIPTION.en_us.html`

### Git History in google/fonts

The family was onboarded in commit `deb08dfb7` (2022-05-18) via PR #4674 by Simon Cozens with the message:
> "Gulzar: Version 1.000;[57fe3b0]; ttfautohint (v1.8.4) added (#4674)"

The gftools-packager initially referenced commit `7f736710573840523e68ea977843f7af7239632b` ("Add description"), but the PR body notes a "Rebuild" step. The METADATA.pb was later updated to commit `42b27958a84d56d8341ad1e2dc26b19dba03b15f` ("Fix typo, reset hb-subset settings, get cupcake"), which is 2 commits after the originally referenced hash.

Subsequent commits in google/fonts:
- `de68c326d` - Description updated (PR #4964)
- `9e6f34acf` - Documentation updated (PR #5040)
- `8c5e130d2` - Primary script added (PR #5234)
- `4fd6ab1bd` - Minisite URL added (PR #5570)
- `bf97c5065` / `2a7bb56a7` / `46dd229dd` - Gulzar article
- `ea42b7c32` - Stroke and classifications metadata
- `66f91f10f` - Merge upstream.yaml into METADATA.pb
- `b39ab414a` (2025-11-07) - "sources info for Gulzar: Version 1.000 (PR #4674)" by Felipe Sanches: added override config.yaml and updated METADATA.pb

### Binary File Verification

The binary file size confirms the correct commit:
- `Gulzar-Regular.ttf` in google/fonts: **963,496 bytes**
- At commit `42b2795` in upstream: **963,496 bytes** (match)
- At commit `7f73671` (originally referenced): **972,236 bytes** (does NOT match)

This confirms that `42b2795` is the correct onboarding commit. The gftools-packager initially referenced `7f73671`, but Simon Cozens made additional fixes (updating the description URL and fixing a typo/hb-subset settings) before the final binary was produced and merged.

### Upstream Repository Analysis

The upstream repo at `simoncozens/Gulzar` (cached at `fontc_crater_cache/simoncozens/Gulzar`) contains:
- **Source file**: `sources/Gulzar.glyphs` (Glyphs format)
- **Build system**: Custom `Makefile` using fontmake, fez2fea (for complex Nasta'liq shaping rules), hb-subset, ttfautohint, and gftools-fix-font
- **Output**: `fonts/ttf/Gulzar-Regular.ttf`
- **Extensive scripting**: Custom Python scripts in `scripts/` for glyph manipulation and feature generation

The build is significantly more complex than a standard gftools-builder workflow due to the Nasta'liq script's shaping requirements (fez2fea for connection rules, bariye drop, anchor attachment, etc.).

Note: The DESCRIPTION.en_us.html in the upstream repo (at the referenced commit) and in google/fonts both reference `github.com/googlefonts/Gulzar/`, suggesting the repo may have been transferred or forked to the googlefonts organization. However, the METADATA.pb correctly references `simoncozens/Gulzar`, which is where the original development and the referenced commit exist.

The repo has had significant post-onboarding development: versions 1.001 and 1.002, plus numerous bug fixes (issues #68 through #94).

### Config YAML Assessment

An override `config.yaml` already exists at `ofl/gulzar/config.yaml` with the following content:
```yaml
buildVariable: false
sources:
  - sources/Gulzar.glyphs
```

This was added in commit `b39ab414a` (2025-11-07). Since the override config.yaml exists in the google/fonts family directory, the `config_yaml` field is correctly omitted from the METADATA.pb source block (google-fonts-sources auto-detects local overrides).

Note: The override config.yaml provides a simplified gftools-builder configuration, but the actual upstream build is more complex (involving fez2fea and custom scripts). The override is sufficient for fontc_crater testing purposes.

## Conclusion

The METADATA.pb source block is complete and correct. The repository URL, commit hash, and file mappings are all verified. The binary file size at the referenced commit matches the file in google/fonts. An override config.yaml is already in place.

### Recommended METADATA.pb Source Block

The current source block is correct as-is:

```
source {
  repository_url: "https://github.com/simoncozens/Gulzar"
  commit: "42b27958a84d56d8341ad1e2dc26b19dba03b15f"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Gulzar-Regular.ttf"
    dest_file: "Gulzar-Regular.ttf"
  }
  branch: "main"
}
```

Override config.yaml (already present at `ofl/gulzar/config.yaml`):
```yaml
buildVariable: false
sources:
  - sources/Gulzar.glyphs
```

**Status**: complete
**Confidence**: HIGH

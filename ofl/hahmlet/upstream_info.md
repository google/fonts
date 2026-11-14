# Investigation Report: Hahmlet

## Summary

Hahmlet is a Korean serif variable font (weight axis: 100-900) designed by Hypertype. It was first added to Google Fonts in May 2021 (v1.001) via gftools-packager and updated to v1.002 in September 2021. The upstream repository at `hyper-type/hahmlet` contains a `.glyphs` source file and a `config.yaml` for gftools-builder. The METADATA.pb already has a complete source block with repository URL, commit hash, and config_yaml path -- all verified as correct.

## Key Findings

| Field             | Value |
|-------------------|-------|
| **Family Name**   | Hahmlet |
| **Designer**      | Hypertype |
| **Repository URL**| https://github.com/hyper-type/hahmlet |
| **Commit Hash**   | `106541144954a9b7037b8d3837097ba660312655` |
| **Config YAML**   | `sources/config.yaml` |
| **Status**        | complete |
| **Confidence**    | HIGH |

## Investigation Details

### METADATA.pb Review

The current METADATA.pb in `ofl/hahmlet/` contains a complete source block:

```
source {
  repository_url: "https://github.com/hyper-type/hahmlet/"
  commit: "106541144954a9b7037b8d3837097ba660312655"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/Hahmlet[wght].ttf"
    dest_file: "Hahmlet[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

This is a well-populated source block with all required fields: `repository_url`, `commit`, and `config_yaml`.

### Google Fonts Repository History

| Commit | Date | Description |
|--------|------|-------------|
| `df3bab672` | 2021-05-13 | v1.001 initial onboarding via gftools-packager (PR #3408) |
| `70b0fc8a8` | -- | Remove static fonts for unhinted variable font families (PR #3695) |
| `afb3b9481` | 2021-09-01 | v1.002 update via gftools-packager (PR #3759) |
| `9d738e639` | 2025-04-03 | Sources info added (commit, config_yaml fields) |

**PR #3408** (v1.001 onboarding): gftools-packager message states the font was taken from `https://github.com/hyper-type/hahmlet` at commit `98a376949035fe079839c17ad95db7917ec35ef4`.

**PR #3759** (v1.002 update): gftools-packager message states the font was taken from `https://github.com/hyper-type/hahmlet` at commit `106541144954a9b7037b8d3837097ba660312655`.

**Commit `9d738e639`** (2025-04-03): Added the `commit` and `config_yaml` fields to METADATA.pb, referencing the v1.002 commit hash from PR #3759.

### Upstream Repository Analysis

The repository at `https://github.com/hyper-type/hahmlet` is the original source repository maintained by the Hypertype team.

**Relevant commits timeline:**

| Commit | Date | Description |
|--------|------|-------------|
| `98a37694` | 2021-05-13 | "Updating postscript naming of variable font" (v1.001 onboarding) |
| `d02e1fa2` | 2021-08-09 | "remove non-export flag from '*comb' glyphs. closes #9" |
| `10654114` | 2021-08-16 | "Updating the source and build fonts" (v1.002 onboarding) |
| `f9c5dac2` | 2022-06-20 | "Update README.md" (latest commit) |

**Commit verification for v1.002 (current in google/fonts):**
- gftools-packager references commit `106541144954a9b7037b8d3837097ba660312655` (2021-08-16)
- The google/fonts merge was on 2021-09-01, about 2 weeks later -- timing is consistent
- The commit "Updating the source and build fonts" is a major restructuring that:
  - Added `.github/workflows/build.yaml` and `Makefile`
  - Added `.gitignore`, updated `README.md`
  - Removed `build.py`
  - Added OTF static fonts and updated TTF fonts
  - This is also the commit where `sources/config.yaml` was introduced
- The variable font `fonts/variable/Hahmlet[wght].ttf` exists at this commit

**Note**: The config.yaml did **not** exist at the v1.001 onboarding commit (`98a37694`). It was only introduced in the v1.002 commit (`10654114`) as part of a repo restructuring.

**Source files found:**
- `sources/Hahmlet.glyphs` -- Glyphs app format (gftools-builder compatible)
- `sources/config.yaml` -- gftools-builder configuration
- `sources/postprocessing.py` -- Post-processing script

### Build Configuration

The `sources/config.yaml` in the upstream repository:

```yaml
sources:
  - Hahmlet.glyphs
axisOrder:
  - wght
familyName: "Hahmlet"
stat:
    Hahmlet[wght].ttf:
    - name: Weight
      tag: wght
      values:
      - name: Thin
        value: 100
      - name: ExtraLight
        value: 200
      - name: Light
        value: 300
      - name: Regular
        value: 400
        linkedValue: 700
        flags: 2
      - name: Medium
        value: 500
      - name: SemiBold
        value: 600
      - name: Bold
        value: 700
      - name: ExtraBold
        value: 800
      - name: Black
        value: 900
```

This is a proper gftools-builder config referencing the `Hahmlet.glyphs` source file with weight axis configuration and STAT table values.

## Conclusion

Hahmlet has a fully complete source tracking setup in METADATA.pb. The repository URL, commit hash, and config_yaml path are all verified as correct. The commit `10654114` matches the v1.002 update referenced in PR #3759 and introduced the config.yaml to the upstream repo. No changes are needed.

### Recommended METADATA.pb source block

The existing source block is correct. No changes needed:

```
source {
  repository_url: "https://github.com/hyper-type/hahmlet/"
  commit: "106541144954a9b7037b8d3837097ba660312655"
  config_yaml: "sources/config.yaml"
  files {
    source_file: "fonts/variable/Hahmlet[wght].ttf"
    dest_file: "Hahmlet[wght].ttf"
  }
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "master"
}
```

### Status: `complete`
### Confidence: HIGH

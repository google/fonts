# Investigation Report: Fuzzy Bubbles

## Summary

Fuzzy Bubbles is a handwriting-style display family designed by Robert Leuschke. It was onboarded to Google Fonts on 2021-11-03 (v1.010) via gftools-packager. The upstream repository is at `https://github.com/googlefonts/fuzzy-bubbles` and the METADATA.pb already has a complete source block with repository URL, commit hash, config_yaml path, and file mappings.

## Key Findings

| Field             | Value |
|-------------------|-------|
| Family Name       | Fuzzy Bubbles |
| Repository URL    | https://github.com/googlefonts/fuzzy-bubbles |
| Commit Hash       | `16d63fbca17f057559d0187fa7c07dd302d2276d` |
| Config YAML       | `sources/config.yml` (in upstream repo) |
| Source Files      | `sources/FuzzyBubbles.glyphs` |
| Status            | **complete** |
| Confidence        | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb contains a complete source block:
- `repository_url`: `https://github.com/googlefonts/fuzzy-bubbles`
- `commit`: `16d63fbca17f057559d0187fa7c07dd302d2276d`
- `config_yaml`: `sources/config.yml`
- `branch`: `master`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and both TTF binaries (Regular, Bold)

### Git History in google/fonts

- `19311a025` (2021-11-03): Initial onboarding as v1.010 by Viviana Monsalve via gftools-packager (PR #4001). Commit message explicitly states: "taken from the upstream repo https://github.com/googlefonts/fuzzy-bubbles at commit https://github.com/googlefonts/fuzzy-bubbles/commit/16d63fbca17f057559d0187fa7c07dd302d2276d".
- `19cdcec59` (2025-03-31): Batch port from fontc_crater targets list added source block details.
- No subsequent font file updates since onboarding.

### Upstream Repository Verification

The upstream repo is cached at `upstream_repos/fontc_crater_cache/googlefonts/fuzzy-bubbles/`. Findings:
- Remote URL confirmed: `https://github.com/googlefonts/fuzzy-bubbles`
- The repo has only a single commit: `16d63fb` ("new v1.10 fonts added", 2021-11-02), which is both the HEAD and the only commit.
- This matches the METADATA.pb reference exactly.
- At commit `16d63fb`, the sources directory contains:
  - `sources/FuzzyBubbles.glyphs` (Glyphs format, gftools-buildable)
  - `sources/config.yml` with contents:
    ```yaml
    sources:
        - FuzzyBubbles.glyphs
    familyName: "Fuzzy Bubbles"
    buildVariable: false
    #autohintTTF: false
    ```

### Commit Hash Verification

The commit hash in METADATA.pb (`16d63fbca17f057559d0187fa7c07dd302d2276d`) matches the only commit in the upstream repo. The upstream commit is dated 2021-11-02, one day before the google/fonts onboarding commit (2021-11-03). The gftools-packager message in the commit body explicitly references this same commit. This is fully verified.

### Note on config file extension

The config file uses `.yml` extension rather than the more common `.yaml`. The METADATA.pb correctly references it as `sources/config.yml`.

## Conclusion

The METADATA.pb source block for Fuzzy Bubbles is already complete and correct. No changes are needed.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/fuzzy-bubbles"
  commit: "16d63fbca17f057559d0187fa7c07dd302d2276d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/FuzzyBubbles-Regular.ttf"
    dest_file: "FuzzyBubbles-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/FuzzyBubbles-Bold.ttf"
    dest_file: "FuzzyBubbles-Bold.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

**Status**: complete
**Confidence**: HIGH

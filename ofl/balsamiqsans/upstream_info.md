# Investigation: Balsamiq Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Balsamiq Sans |
| Slug | balsamiq-sans |
| License Dir | ofl |
| Repository URL | https://github.com/balsamiq/balsamiqsans |
| Commit Hash | b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4 |
| Config YAML | sources/config.yaml |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/balsamiq/balsamiqsans"
  commit: "009740f8b2c3915b1553182ec406aaddb1a12dc7"
  archive_url: "https://github.com/balsamiq/balsamiqsans/releases/download/1.020/balsamiqsans-fonts.zip"
  files {
    source_file: "balsamiqsans-fonts/fonts/ttf/BalsamiqSans-Bold.ttf"
    dest_file: "BalsamiqSans-Bold.ttf"
  }
  files {
    source_file: "balsamiqsans-fonts/fonts/ttf/BalsamiqSans-BoldItalic.ttf"
    dest_file: "BalsamiqSans-BoldItalic.ttf"
  }
  files {
    source_file: "balsamiqsans-fonts/fonts/ttf/BalsamiqSans-Italic.ttf"
    dest_file: "BalsamiqSans-Italic.ttf"
  }
  files {
    source_file: "balsamiqsans-fonts/fonts/ttf/BalsamiqSans-Regular.ttf"
    dest_file: "BalsamiqSans-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Investigation

### Google Fonts Git History

The `.ttf` files in `ofl/balsamiqsans/` were last modified by two commits:

1. `52964a87a` (2023-04-27) — `[gftools-packager] Balsamiq Sans: Version 1.020; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.26] added`
2. `cbaef391e` (2020-04-09) — `[Font Bakery Dashboard] create: ofl/balsamiqsans`

The gftools-packager commit message body reads:
> "Balsamiq Sans Version 1.020; ttfautohint (v1.8.4.7-5d5b);gftools[0.9.26] taken from the upstream repo https://github.com/balsamiq/balsamiqsans at commit https://github.com/balsamiq/balsamiqsans/commit/."

The commit URL is **truncated** — the hash after `/commit/` is empty. This means gftools-packager logged the action without capturing the commit hash.

The `archive_url` field points to `https://github.com/balsamiq/balsamiqsans/releases/download/1.020/balsamiqsans-fonts.zip`, confirming that the fonts were taken from the v1.020 release zip.

### Commit Hash Analysis

The METADATA.pb currently records `commit: "009740f8b2c3915b1553182ec406aaddb1a12dc7"`. This hash was added via the batch commit `19cdcec59` (2025-03-31, "[Batch 1/4] port info from fontc_crater targets list"). However, this commit is **incorrect**:

- `009740f8b2c3915b1553182ec406aaddb1a12dc7` dates to **2024-12-17** ("Merge pull request #23 from balsamiq/update_build_script"), which is well over a year **after** the google/fonts onboarding date (2023-04-27).

The correct commit is `b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4`, which is the `1.020` tag in the upstream repo. This commit dates to **2023-04-20** ("Merge pull request #17 from daltonmaag/master") — seven days before the google/fonts update — consistent with the v1.020 release zip being built from this commit.

Verification:
- `git rev-list -n 1 1.020` in the upstream repo returns `b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4`
- This commit predates the google/fonts merge (2023-04-27)

### Config YAML

`sources/config.yaml` exists in the upstream repo and was present at commit `b1dca64c` (the 1.020 tag). Contents:

```yaml
sources:
  - glyphs/BalsamiqSans-Roman.glyphs
  - glyphs/BalsamiqSans-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Balsamiq Sans

# Sources aren't VF compatible
buildVariable: false
checkCompatibility: false

# Outlines are quadratic
reverseOutlineDirection: false
removeOutlineOverlaps: false

# Hit the needed code paths to insert the right metadata into the sources before
# they hit the compiler.
interpolate: true
buildOTF: true
buildWebfont: true

autohintTTF: true
```

The `config_yaml: "sources/config.yaml"` field in METADATA.pb is correct.

### Upstream Repo Cache

Repository is cached at `upstream_repos/fontc_crater_cache/balsamiq/balsamiqsans/`.

## Conclusion

The `repository_url` and `config_yaml` fields are correct. The `commit` field must be corrected from `009740f8b2c3915b1553182ec406aaddb1a12dc7` (a 2024-12-17 commit, added erroneously by the fontc_crater batch import) to `b1dca64c3ceeaa3c274f69fae5a6f508b9a4dcc4` (the v1.020 release tag, 2023-04-20), which matches the `archive_url` version and predates the google/fonts onboarding.

Action needed: Fix `commit` in `ofl/balsamiqsans/METADATA.pb`.

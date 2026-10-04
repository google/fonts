# Investigation: Alumni Sans

## Summary

| Field | Value |
|-------|-------|
| Family Name | Alumni Sans |
| Slug | alumni-sans |
| License Dir | ofl |
| Repository URL | https://github.com/googlefonts/alumni |
| Commit Hash | 44a7998fa2bfa1b3e119983cdc565dd7f0f03bda |
| Config YAML | sources/config.yml |
| Status | needs_correction |
| Confidence | HIGH |

## Source Data (METADATA.pb)

```
source {
  repository_url: "https://github.com/googlefonts/alumni"
  commit: "28754a9295db605d4e4ffc7bf60b4a8301eef9ab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/AlumniSans[wght].ttf"
    dest_file: "AlumniSans[wght].ttf"
  }
  files {
    source_file: "fonts/variable/AlumniSans-Italic[wght].ttf"
    dest_file: "AlumniSans-Italic[wght].ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

## Investigation

The font file history in google/fonts shows two onboarding commits:

- `bc42a87b0` — "Alumni Sans: Version 1.014 added (#3559)", merged via gftools-packager, upstream commit `fae04c79a905f608bca0b7b2251706d732e81472`
- `9f8863f59` — "Alumni Sans: Version 1.018 added (#4180)", merged 2022-01-14, by Viviana Monsalve

The v1.018 commit body explicitly states:

> "Alumni Sans Version 1.018 taken from the upstream repo https://github.com/googlefonts/alumni at commit https://github.com/googlefonts/alumni/commit/44a7998fa2bfa1b3e119983cdc565dd7f0f03bda."

This documents the actual onboarding commit as `44a7998fa2bfa1b3e119983cdc565dd7f0f03bda` (dated 2021-12-18, message: "one blank line added to the OFL"), which is confirmed as the top commit in the cached upstream repo at `upstream_repos/fontc_crater_cache/googlefonts/alumni`.

However, the current METADATA.pb records commit `28754a9295db605d4e4ffc7bf60b4a8301eef9ab`. This was set by a later "sources info" commit `91fc42a96` ("sources info for Alumni Sans (PR #4180)"), which changed the hash from the correct `44a7998` to the older `28754a9295`. The commit `28754a9295` is dated 2021-12-08 (message: "changelog added") — it predates the actual onboarding commit by 10 days, making it an incorrect and older reference.

A separate shallow clone exists at `upstream_repos/fontc_crater_cache/googlefonts/alumni_28754a9295` stopping at the incorrect commit, confirming it was investigated previously.

The `sources/config.yml` file exists in the upstream repo and contains gftools-builder configuration referencing `AlumniSans.glyphs` and `AlumniSans-Italic.glyphs` with full STAT axis table definitions. The `config_yaml` field in METADATA.pb correctly points to `sources/config.yml`.

**Finding**: The METADATA.pb `commit` field is wrong. It records `28754a9295` (2021-12-08) but the actual onboarding used `44a7998` (2021-12-18).

## Conclusion

The METADATA.pb source block requires a correction: the `commit` field must be changed from `28754a9295db605d4e4ffc7bf60b4a8301eef9ab` to `44a7998fa2bfa1b3e119983cdc565dd7f0f03bda`. This is the commit explicitly documented in the google/fonts onboarding commit message for PR #4180. The `repository_url` and `config_yaml` fields are correct and do not need changes.

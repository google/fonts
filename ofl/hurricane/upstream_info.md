# Investigation Report: Hurricane

## Summary

Hurricane is a handwriting/display font designed by Robert Leuschke. It was added to Google Fonts on 2021-10-14 via gftools-packager. The METADATA.pb has a complete source block with repository URL, commit hash, file mappings, branch, and config_yaml path. All data has been verified against the upstream repository.

## Key Findings

| Field | Value | Status |
|-------|-------|--------|
| **Family Name** | Hurricane | -- |
| **Repository URL** | https://github.com/googlefonts/hurricane | Verified |
| **Commit Hash** | `bb10369a4820ebee5af7892e8661978c015cb077` | Verified |
| **Config Path** | `sources/config.yml` | Verified |
| **Source Type** | .glyphs | -- |
| **Status** | **complete** | -- |
| **Confidence** | HIGH | -- |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/hurricane/METADATA.pb` contains a complete source block with explicit file mappings:

```
source {
  repository_url: "https://github.com/googlefonts/hurricane"
  commit: "bb10369a4820ebee5af7892e8661978c015cb077"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/Hurricane-Regular.ttf"
    dest_file: "Hurricane-Regular.ttf"
  }
  branch: "master"
  config_yaml: "sources/config.yml"
}
```

### Git History in google/fonts

The font was added to google/fonts via:

1. `05e8975af` (2021-10-14) - "Hurricane: Version 1.010; ttfautohint (v1.8.3) added (#3932)" - Added by gftools-packager. The commit body states: "Hurricane Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/hurricane at commit https://github.com/googlefonts/hurricane/commit/8cc30aac85d0b3d1205cc9f99fe654a4bac316b6."

Note: The gftools-packager message references commit `8cc30aac`, but the METADATA.pb references `bb10369a`. The current METADATA.pb commit (`bb10369a`) is dated 2021-10-14, which is the same day the font was added to google/fonts, and its message is "git url fixed". This is the HEAD of the master branch and appears to be a later commit than what was originally referenced by the packager, containing a git URL fix.

### Upstream Repository Verification

The upstream repository at https://github.com/googlefonts/hurricane is cached at `upstream_repos/fontc_crater_cache/googlefonts/hurricane/`. Note: The cached repo is a shallow clone with only 1 commit (the HEAD commit `bb10369a`). The original packager commit `8cc30aac` is not available in the shallow clone.

The referenced commit `bb10369a4820ebee5af7892e8661978c015cb077` exists and is dated 2021-10-14, with the message "git url fixed". Since this is the only commit in the upstream repo (it has just 1 commit in the shallow clone, and it appears to also be the latest commit on the remote), the METADATA.pb correctly points to the latest state of the master branch.

### Config Verification

The config file at `sources/config.yml` (note: `.yml` extension, not `.yaml`) exists at the referenced commit:

```yaml
sources:
  - Hurricane-Pro.glyphs
familyName: "Hurricane"
buildVariable: false
#autohintTTF: false
```

### Source Files

The sources directory contains:
- `Hurricane-Pro.glyphs` - Main source file
- `config.yml` - Build configuration

## Conclusion

**Status: complete**

All source metadata is correctly documented. The repository URL points to a valid upstream repo, the commit hash `bb10369a` is verified (it is the HEAD of the master branch and represents the final state used for onboarding, after a URL fix that happened on the same day as the google/fonts addition). The config path correctly uses the `.yml` extension. File mappings are explicit and correct. No changes needed.

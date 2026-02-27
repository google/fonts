# Investigation Report: Google Sans Code

## Summary

Google Sans Code is a monospace variable font (weight axis 300-800) designed by Google and Universal Thirst. It was first onboarded at version 6.000 via PR #9629 (merged 2025-07-02) and updated to version 6.001 via PR #9762 (merged 2025-08-28) by MariannaPaszkowska. The upstream repo is `googlefonts/googlesans-code`. The source block is mostly complete but is missing `config_yaml`, even though the upstream repo has `sources/config.yaml`.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Google Sans Code                                                   |
| Repository URL    | https://github.com/googlefonts/googlesans-code                     |
| Commit Hash       | edcd56e39fb7e98d6f1b697e187c144cef2fd994                           |
| Config YAML       | sources/config.yaml (exists upstream, not referenced in METADATA.pb)|
| Status            | needs_correction                                                   |
| Confidence        | HIGH                                                               |

## Investigation Details

### METADATA.pb Current State

The current METADATA.pb contains a source block with:
- `repository_url`: https://github.com/googlefonts/googlesans-code
- `commit`: edcd56e39fb7e98d6f1b697e187c144cef2fd994
- `archive_url`: https://github.com/googlefonts/googlesans-code/releases/download/v6.001/GoogleSansCode-v6.001.zip
- `branch`: main
- File mappings for OFL.txt, GoogleSansCode[wght].ttf, and GoogleSansCode-Italic[wght].ttf
- **Missing**: `config_yaml` field

### Onboarding History

1. **PR #9629** (merged 2025-07-02): "Google Sans Code: Version 6.000 added"
   - Initial onboarding, taken from upstream commit `18523d8837d98e6be89316017d323bc610b21c66`.

2. Various metadata and article updates (July 2025).

3. **PR #9762** (merged 2025-08-28): "Google Sans Code: Version 6.001 added" by MariannaPaszkowska.
   - Updated to version 6.001, referencing upstream commit `edcd56e39fb7e98d6f1b697e187c144cef2fd994`.
   - Font binaries taken from release archive `GoogleSansCode-v6.001.zip`.

4. **PR #9824** (merged 2025-09-12): "Update googlesanscode/METADATA.pb"
   - Added `sample_text` block and corrected category to MONOSPACE.

### Commit Hash Analysis

The referenced commit `edcd56e39fb7e98d6f1b697e187c144cef2fd994` (2025-08-21) is a dependabot merge: "Bump cargo-bins/cargo-binstall from 1.14.1 to 1.14.4". It only changed `.github/workflows/build-test.yml`.

This commit was the HEAD of the `main` branch when the v6.001 release was created. The release was published on 2025-08-21T13:28:21Z, and this commit dates to 2025-08-21T13:24:11Z. The actual font source changes were in the earlier commit `369bb832d7641676f2b7ef3609a63dc331eecaee` ("Merge pull request #37 from googlefonts/6.001-prep", 2025-08-21T13:23:51Z), which merged the version update commit `cce24bdc` that modified the .glyphspackage fontinfo.plist files and CHANGELOG.md.

Since the onboarder used the release zip (pre-built binaries) and the release was tagged at the same commit (`edcd56e`), this commit hash correctly identifies the state of the repository at the time of the release. The commit hash is valid as a reference point.

### Upstream Repository

- **URL**: https://github.com/googlefonts/googlesans-code
- **Cached at**: upstream_repos/fontc_crater_cache/googlefonts/googlesans-code (empty directory, not a valid clone)
- **Source files**: `sources/GoogleSansCode.glyphspackage` and `sources/GoogleSansCode-Italic.glyphspackage`
- **Config**: `sources/config.yaml` exists at the referenced commit

### Config YAML Contents (at commit edcd56e)

```yaml
sources:
  - GoogleSansCode.glyphspackage
  - GoogleSansCode-Italic.glyphspackage
familyName: Google Sans Code

buildVariable: true
buildStatic: false
buildTTF: true
buildOTF: false
```

### Missing config_yaml Field

The upstream repo has a proper `sources/config.yaml` with gftools-builder configuration at the referenced commit. The METADATA.pb source block should include `config_yaml: "sources/config.yaml"` to enable source-based builds via fontc_crater.

Note: The current onboarding uses pre-built binaries from the release archive (`archive_url`), not source compilation. However, the upstream repo has proper build sources (.glyphspackage files) and a config.yaml, so the `config_yaml` field should be added for fontc_crater compatibility.

### Release Archive

The v6.001 release (published 2025-08-21) contains pre-built font files in a zip archive. The `archive_url` in METADATA.pb correctly points to this release. The `files` mappings reference paths within the extracted archive (`variable/GoogleSansCode[wght].ttf`, etc.).

## Conclusion

The METADATA.pb source block for Google Sans Code is mostly correct but should have the `config_yaml` field added to reference the upstream build configuration.

### Recommended METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/googlefonts/googlesans-code"
  commit: "edcd56e39fb7e98d6f1b697e187c144cef2fd994"
  archive_url: "https://github.com/googlefonts/googlesans-code/releases/download/v6.001/GoogleSansCode-v6.001.zip"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "variable/GoogleSansCode[wght].ttf"
    dest_file: "GoogleSansCode[wght].ttf"
  }
  files {
    source_file: "variable/GoogleSansCode-Italic[wght].ttf"
    dest_file: "GoogleSansCode-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

**Status**: needs_correction (missing config_yaml field)
**Confidence**: HIGH

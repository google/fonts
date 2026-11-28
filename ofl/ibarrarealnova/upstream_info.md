# Investigation Report: Ibarra Real Nova

## Summary

Ibarra Real Nova is a serif/display variable font designed by Jose Maria Ribagorda and Octavio Pardo. It was added to Google Fonts on 2020-10-07 via gftools-packager at version 2.000. The METADATA.pb has a source block with repository URL, commit hash, explicit file mappings, and branch, but no config_yaml field. An override `config.yaml` exists in the google/fonts family directory, which is the correct approach since the upstream repo at the referenced commit had no config.yaml (it used a custom `build.sh` script).

## Key Findings

| Field | Value | Status |
|-------|-------|--------|
| **Family Name** | Ibarra Real Nova | -- |
| **Repository URL** | https://github.com/googlefonts/ibarrareal | Verified |
| **Commit Hash** | `7ae92a27f13f8e187db49312e7111041d1fa2a17` | Verified |
| **Config Path** | Override config.yaml in google/fonts | Verified |
| **Source Type** | .designspace + .ufo | -- |
| **Status** | **complete** | -- |
| **Confidence** | HIGH | -- |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/ibarrarealnova/METADATA.pb` contains a source block with explicit file mappings but no config_yaml:

```
source {
  repository_url: "https://github.com/googlefonts/ibarrareal"
  commit: "7ae92a27f13f8e187db49312e7111041d1fa2a17"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/IbarraRealNova-Italic[wght].ttf"
    dest_file: "IbarraRealNova-Italic[wght].ttf"
  }
  files {
    source_file: "fonts/variable/IbarraRealNova[wght].ttf"
    dest_file: "IbarraRealNova[wght].ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-Bold.ttf"
    dest_file: "static/IbarraRealNova-Bold.ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-BoldItalic.ttf"
    dest_file: "static/IbarraRealNova-BoldItalic.ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-Italic.ttf"
    dest_file: "static/IbarraRealNova-Italic.ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-Regular.ttf"
    dest_file: "static/IbarraRealNova-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-SemiBold.ttf"
    dest_file: "static/IbarraRealNova-SemiBold.ttf"
  }
  files {
    source_file: "fonts/ttf/IbarraRealNova-SemiBoldItalic.ttf"
    dest_file: "static/IbarraRealNova-SemiBoldItalic.ttf"
  }
  branch: "master"
}
```

The absence of `config_yaml` in the source block is correct because an override config.yaml exists in the google/fonts family directory.

### Override config.yaml

The file `ofl/ibarrarealnova/config.yaml` exists in google/fonts with the following content:

```yaml
buildVariable: true
sources:
  - sources/IbarraRealNova-Roman.designspace
  - sources/IbarraRealNova-Italic.designspace
```

This was added on 2025-10-30 in commit `e980bb401` ("sources info for Ibarra Real Nova: Version 2.000 (PR #2709)"). The config references two designspace files that exist at the referenced commit `7ae92a27`.

### Git History in google/fonts

1. `89ade4fa7` (2020-10-07) - "Ibarra Real Nova: Version 2.000 added (#2709)" - Added by gftools-packager. Commit body: "Ibarra Real Nova Version 2.000 taken from the upstream repo https://github.com/googlefonts/ibarrareal at commit https://github.com/googlefonts/ibarrareal/commit/7ae92a27f13f8e187db49312e7111041d1fa2a17."
2. `9f77052d4` - "Fix license text."
3. `70b0fc8a8` - "Remove static fonts for unhinted variable font families (#3695)"
4. Various metadata-only updates (language support, stroke/classification).
5. `e980bb401` (2025-10-30) - "sources info for Ibarra Real Nova: Version 2.000 (PR #2709)" - Source block and override config added by Felipe Sanches.

### Upstream Repository Verification

The upstream repository at https://github.com/googlefonts/ibarrareal is cached at `upstream_repos/fontc_crater_cache/googlefonts/ibarrareal/`.

The referenced commit `7ae92a27f13f8e187db49312e7111041d1fa2a17` (2020-09-30) exists and is a merge commit: "Merge pull request #15 from TypeNetwork/master". This predates the google/fonts addition by about a week, which is consistent with a normal packaging workflow.

The gftools-packager message in the google/fonts commit directly confirms this exact commit hash, providing strong corroboration.

**Note**: The upstream repo has since been modernized. Commit `e19809f` (2025-02-05) "Modernize tooling; upgrade to designspace v5" merged PR #41, which consolidated the two separate designspace files (`IbarraRealNova-Roman.designspace` and `IbarraRealNova-Italic.designspace`) into a single `IbarraRealNova.designspace` and removed the old `build.sh` script. However, the METADATA.pb correctly references the older commit `7ae92a27` which was the version actually used for the google/fonts onboarding.

### Source Files at Referenced Commit

At commit `7ae92a27`, the sources directory contained:
- `IbarraRealNova-Roman.designspace` - Roman variable font source
- `IbarraRealNova-Italic.designspace` - Italic variable font source
- `IbarraRealNova-Regular.ufo/` - Regular master
- `IbarraRealNova-Bold.ufo/` - Bold master
- `IbarraRealNova-Italic.ufo/` - Italic master
- `IbarraRealNova-BoldItalic.ufo/` - Bold Italic master
- `build.sh` - Custom build script (no config.yaml at this commit)

The override config.yaml in google/fonts correctly references `sources/IbarraRealNova-Roman.designspace` and `sources/IbarraRealNova-Italic.designspace`, both of which exist at the referenced commit.

## Conclusion

**Status: complete**

All source metadata is correctly documented. The repository URL is valid, the commit hash is verified and matches what gftools-packager recorded, and an override config.yaml in the google/fonts family directory correctly references the designspace files at the referenced commit. The `config_yaml` field is intentionally omitted from METADATA.pb since google-fonts-sources auto-detects local override configs. No changes needed.

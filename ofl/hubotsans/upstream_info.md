# Investigation Report: Hubot Sans

## Summary

Hubot Sans is a variable sans-serif font (wdth 75-125, wght 200-900) with both upright and italic styles, designed by Tobias Bjerrome Ahlin for GitHub. It was onboarded to Google Fonts on 2024-10-04 by Emma Marichal. The METADATA.pb source block points to `github.com/github/hubot-sans` with commit `d4b2f67` and config at `sources/config.yaml`. However, the original onboarding commit message in google/fonts references a different repository (`googlefonts/hubot-sans`) and a different commit hash (`9c2cc3ac`). The commit `9c2cc3ac` does not exist in the `github/hubot-sans` repo, suggesting it was in the `googlefonts/hubot-sans` fork used during onboarding. The current METADATA.pb commit `d4b2f67` is the only commit in the `github/hubot-sans` repo (a merge of PR #37 "Add Hubot Sans - PR n1" dated 2024-10-17, after the google/fonts onboarding date of 2024-10-04). The config.yaml and source files are present. The repo URL was corrected from the fork to the canonical repo.

## Key Findings

| Field | Value |
|---|---|
| Family Name | Hubot Sans |
| Repository URL (METADATA.pb) | https://github.com/github/hubot-sans |
| Repository URL (onboarding msg) | https://github.com/googlefonts/hubot-sans |
| Commit Hash (METADATA.pb) | d4b2f67cd7686f5907296d3f027112bbc4f69f42 |
| Commit Hash (onboarding msg) | 9c2cc3ac30ac77cc7c3b40e0813b3487a0c56b7b |
| Config YAML | sources/config.yaml |
| Config Exists at Commit | Yes |
| Source Files | sources/HubotSans.glyphspackage |
| Date Added | 2024-10-04 |
| Status | needs_correction |
| Confidence | MEDIUM |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb file contains a source block:
- `repository_url`: `https://github.com/github/hubot-sans`
- `commit`: `d4b2f67cd7686f5907296d3f027112bbc4f69f42`
- `config_yaml`: `sources/config.yaml`
- `branch`: `main`
- File mappings for OFL.txt and variable TTFs from `googlefonts/variable/`

### Google Fonts Commit History

The onboarding commit `ccca81e56` (2024-10-04) by Emma Marichal states:
> "Taken from the upstream repo https://github.com/googlefonts/hubot-sans at commit https://github.com/googlefonts/hubot-sans/commit/9c2cc3ac30ac77cc7c3b40e0813b3487a0c56b7b."

Key discrepancies:
1. The onboarding references `googlefonts/hubot-sans` but METADATA.pb points to `github/hubot-sans`
2. The onboarding commit hash `9c2cc3ac` does not exist in the `github/hubot-sans` repo

Subsequent google/fonts commits:
- `fe31254d7` (2024-11-14): "update metadata (designers)"
- `1470dc70c` (2024-11-14): "Update METADATA.pb"
- `c72a13bd2` (2024-11-14): "Update METADATA.pb"
- `80f7d5650` (2025-01-07): "Capitalize H in GitHub"
- `19cdcec59` (2025-03-31): fontc_crater batch update (set source block with commit/config)

### Upstream Repository

The repo at `github.com/github/hubot-sans` has a single commit:
- `d4b2f67` (2024-10-17): "Merge pull request #37 from emmamarichal/v1.1" — by Tobias Ahlin

This merge commit introduced the entire repository contents. The PR title "Add Hubot Sans - PR n1" suggests this was the initial setup of the canonical repo. The merge date (2024-10-17) is 13 days after the google/fonts onboarding date (2024-10-04).

The `googlefonts/hubot-sans` fork was not found in the local cache and likely contains the original commit `9c2cc3ac` used during onboarding. The work was done in the fork first, then merged into the canonical `github/hubot-sans` repo.

### Config YAML

The file `sources/config.yaml` exists at commit `d4b2f67` and contains:
```yaml
sources:
  - HubotSans.glyphspackage
outputDir: "../googlefonts"
buildOTF: False
buildWebfont: False
buildTTF: false
axisOrder:
  - wdth
  - wght
familyName: "Hubot Sans"
stat:
  - name: Width
    tag: wdth
    values: [Condensed(75), SemiCondensed(87.5), Normal(100), SemiExpanded(112.5), Expanded(125)]
  - name: Weight
    tag: wght
    values: [ExtraLight(200), Light(300), Regular(400), Medium(500), SemiBold(600), Bold(700), ExtraBold(800), Black(900)]
```

The source file `sources/HubotSans.glyphspackage` exists. The config builds only variable fonts (no static, no OTF, no webfont).

### Binary Font Verification

The font files at `googlefonts/variable/` exist at commit `d4b2f67`:
- `HubotSans[wdth,wght].ttf` (369,548 bytes)
- `HubotSans-Italic[wdth,wght].ttf` (381,520 bytes)

The repo also contains `master_ufo/` with a designspace and UFO masters, in addition to the `sources/HubotSans.glyphspackage`.

### Timeline

- 2024-10-04: Onboarded to google/fonts from `googlefonts/hubot-sans` fork at commit `9c2cc3ac`
- 2024-10-17: Canonical `github/hubot-sans` repo receives merge of PR #37 (commit `d4b2f67`)
- 2024-11-14: Multiple METADATA.pb updates (designers, etc.)
- 2025-01-07: Capitalization fix in METADATA.pb
- 2025-03-31: fontc_crater batch update set commit to `d4b2f67` and config_yaml

## Conclusion

**Status: needs_correction**

The source block exists but has a provenance issue. The onboarding was done from the `googlefonts/hubot-sans` fork at commit `9c2cc3ac`, which does not exist in the canonical `github/hubot-sans` repo. The METADATA.pb commit `d4b2f67` is the only commit in the canonical repo, corresponding to the merge of the fork's work. While this commit contains the correct source files, config.yaml, and built fonts, the original onboarding commit cannot be verified in the current repo. The repository URL correction from `googlefonts/hubot-sans` to `github/hubot-sans` appears intentional (pointing to the canonical repository). The config_yaml and source files are valid. Confidence is MEDIUM because while the data is internally consistent within the canonical repo, the original onboarding commit is from a different repository and cannot be cross-verified.

# Capriola - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| **Family Name** | Capriola |
| **Designer** | Viktoriya Grabowska |
| **Repository URL** | https://github.com/SorkinType/Capriola-VF |
| **Commit** | `048a515c14cebe8ffe4a821c3c9c075450a80b97` |
| **Branch** | main |
| **Config YAML** | `sources/config.yaml` |
| **Date Added** | 2012-07-10 (original static); upgraded to VF in 2025 |
| **License** | OFL |
| **Status** | Complete |

## How URL Was Found

The repository URL `https://github.com/SorkinType/Capriola-VF` is recorded in METADATA.pb and was added when the font was upgraded from static to variable in PR #9944 (October 2025). The copyright string also references this URL.

## How Commit Was Determined

The commit history is nuanced:

1. **gftools-packager original**: PR #9944 (by Emma Marichal) originally referenced commit `bc902b75ef32988b6c2dc97183b44c6c307d3081` ("build fonts", 2025-10-22). This is the commit where the font binaries were built.

2. **Updated commit**: The METADATA.pb was later updated (by @felipesanches in commit `30f5c125f` on 2025-11-28) to point to `048a515c14cebe8ffe4a821c3c9c075450a80b97` ("Update AUTHORS.txt", 2025-10-23). This commit is 3 commits after `bc902b75`, with only metadata changes (AUTHORS.txt, CONTRIBUTORS.txt, DESCRIPTION.en_us.html).

3. **Binary verification**: The variable font file `Capriola[wght].ttf` is identical at both commits (SHA-256: `03bd906c00b8618af3b0844a45165b699e2fcccd589d29812b5c9f83afd49e75`), matching the file in google/fonts. The font was not modified between these commits.

The update from `bc902b75` to `048a515c` was done to correct the config_yaml path (from `Capriola-VF/sources/config.yaml` to `sources/config.yaml`) and to point to the tip of the repository at the time of onboarding, which includes metadata corrections made the same day.

## Config YAML Status

The file `sources/config.yaml` exists at the recorded commit and contains:

```yaml
sources:
  - Capriola.glyphspackage
familyName: "Capriola"
cleanUp: true
stat:
  Capriola[wght].ttf:
  - name: Weight
    tag: wght
    values:
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
```

No override config.yaml exists in the google/fonts family directory.

## Verification

- **Commit exists in upstream repo**: Yes, verified
- **Binary match**: The VF file `Capriola[wght].ttf` matches between upstream and google/fonts
- **config.yaml present at commit**: Yes, at `sources/config.yaml`
- **Onboarding author**: Emma Marichal (PR #9944), with Eben Sorkin as upstream maintainer

## Confidence Level

**HIGH** - Both the gftools-packager commit (`bc902b75`) and the updated commit (`048a515c`) produce identical font binaries. The config.yaml is present and correct. The update to `048a515c` was a deliberate correction to capture metadata updates made the same day as the font build.

## Open Questions

None. This family is fully documented and verified.

# Cormorant Infant - Investigation Report

## Source Data

| Field | Value |
|---|---|
| **Family Name** | Cormorant Infant |
| **Designer** | Christian Thalmann (CatharsisFonts) |
| **Repository URL** | https://github.com/CatharsisFonts/Cormorant |
| **Commit** | `6d210fd3550b7358ca62d6ba3e354ec1ec940813` |
| **Branch** | master |
| **Config YAML** | `sources/config-infant.yaml` |
| **Date Added** | 2017-01-18 |
| **License** | OFL |
| **Status** | Complete |

## How URL Found

The repository URL `https://github.com/CatharsisFonts/Cormorant` is the shared upstream repo for all Cormorant variants (Cormorant, Cormorant Garamond, Cormorant Infant, Cormorant SC, Cormorant Unicase, Cormorant Upright). It is documented in:

1. METADATA.pb source block
2. Copyright strings: "Copyright 2015 The Cormorant Project Authors (github.com/CatharsisFonts/Cormorant)"
3. google/fonts commit d9f209312 (PR #4891, v4.000): "taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"
4. google/fonts commit 1b9fdaa5c (v4.001): "Taken from the upstream repo https://github.com/CatharsisFonts/Cormorant"
5. DESCRIPTION.en_us.html links to the same repo

## How Commit Determined

The commit `6d210fd3550b7358ca62d6ba3e354ec1ec940813` is explicitly referenced in:

1. **METADATA.pb source block**: `commit: "6d210fd3550b7358ca62d6ba3e354ec1ec940813"`
2. **google/fonts commit 1b9fdaa5c** (by Simon Cozens, 2024-11-26): "Cormorant Infant: Version 4.001 added ... Taken from the upstream repo https://github.com/CatharsisFonts/Cormorant at commit https://github.com/CatharsisFonts/Cormorant/commit/6d210fd3550b7358ca62d6ba3e354ec1ec940813"

This commit is "Merge pull request #75 from simoncozens/vf-and-gf" (2024-11-26), which added the variable font build process and generated VFs to the repo. Simon Cozens both authored the upstream PR and made the corresponding google/fonts commit on the same day.

### Onboarding and Update History

| Version | Date | google/fonts Commit | Author | Upstream Commit |
|---|---|---|---|---|
| v3.301 | 2017-01-18 | 43dfb2565 (PR #581) | Initial onboarding | (not recorded) |
| v3.302 | 2017-01-20 | 1d34f8e1b (PR #594) | Update | (not recorded) |
| v3.303 | 2017-02-07 | b6e8dd55d (PR #635) | Update | (not recorded) |
| v4.000 | 2022-07-05 | d9f209312 (PR #4891) | Marc Foley | `cc1bfb51ce` |
| v4.001 | 2024-11-26 | 1b9fdaa5c | Simon Cozens | `6d210fd355` |
| rebuild | 2024-12-06 | af3a90ce2 | Simon Cozens | (same commit, babelfont 3.1.2 rebuild) |

The v4.001 update converted Cormorant Infant from 10 static .ttf files to 2 variable font files (`CormorantInfant[wght].ttf` and `CormorantInfant-Italic[wght].ttf`). A subsequent rebuild (af3a90ce2) regenerated the binaries using babelfont 3.1.2 from the same upstream commit.

The `config_yaml` field was added later in google/fonts commit a20b18752 (2025-04-02, by Felipe Sanches), which added source info across all Cormorant variants.

### Upstream Status

As of 2026-02-27, the upstream master has 3 newer commits after `6d210fd`:
- `78a664cd` (2025-01-10): "Fixed ydotbelow and kcaron"
- `b149467f` (2025-01-10): "Preparing for release 4.002"
- `e716640d` (2025-06-11): "Fixed Upright udieresiscaron"

These newer commits have not been incorporated into google/fonts and would need separate review.

## Config YAML Status

At commit `6d210fd`, the file `sources/config-infant.yaml` exists and contains a valid gftools-builder config:
```yaml
sources:
  - generated/CormorantInfant.glyphs
  - generated/CormorantInfant-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: Cormorant Infant
buildStatic: False
buildWebfont: True
buildSmallCap: False
postCompile:
  - operation: rename
    args: --just-family
    name: Cormorant Infant
stat:
  CormorantInfant[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Roman
      value: 0
      linkedValue: 1
      flags: 2
  CormorantInfant-Italic[wght].ttf:
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
  - name: Italic
    tag: ital
    values:
    - name: Italic
      value: 1
```

This config was added as part of the vf-and-gf branch (upstream PR #75 by Simon Cozens). The source files are generated .glyphs files at `generated/CormorantInfant.glyphs` and `generated/CormorantInfant-Italic.glyphs`. No override config.yaml exists in the google/fonts family directory.

## Source Files

At commit `6d210fd`, the upstream repo contains:
- **Source files**: `sources/Cormorant.glyphs`, `sources/Cormorant-Italic.glyphs` (master sources)
- **Generated sources**: `generated/CormorantInfant.glyphs`, `generated/CormorantInfant-Italic.glyphs` (used by config)
- **Pre-built VFs**: `fonts/variable/CormorantInfant[wght].ttf`, `fonts/variable/CormorantInfant-Italic[wght].ttf`
- **Config**: `sources/config-infant.yaml`
- **Build system**: Makefile, requirements.txt

Cormorant Infant is one of several stylistic variants generated from the master Cormorant sources, each with its own config file (config-cormorant.yaml, config-garamond.yaml, config-infant.yaml, config-unicase.yaml, config-upright.yaml).

## Verification

- **Upstream repo cached**: Yes, at `CatharsisFonts/Cormorant/`
- **Commit exists**: Yes, verified in local cache
- **Config file exists at commit**: Yes, `sources/config-infant.yaml` is present at `6d210fd`
- **Font files match**: METADATA.pb correctly maps `fonts/variable/CormorantInfant[wght].ttf` and `fonts/variable/CormorantInfant-Italic[wght].ttf`
- **Repository accessible**: Yes, remote URL verified as https://github.com/CatharsisFonts/Cormorant
- **Timeline consistent**: Upstream merge and google/fonts commit both dated 2024-11-26

## Confidence Level

**HIGH** - All data is explicitly documented in commit messages and METADATA.pb. The commit hash is directly stated in the google/fonts commit message by the same person (Simon Cozens) who authored both the upstream PR and the google/fonts update, on the same day. Multiple independent confirmations exist.

## Open Questions

None. This family is fully documented and verified.

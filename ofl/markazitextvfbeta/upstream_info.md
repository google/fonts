# Markazi Text VF Beta — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: incomplete (legacy VF beta directory — no METADATA.pb, superseded by non-beta "Markazi Text")

## METADATA.pb Source Block (current)

There is **no METADATA.pb** file in `ofl/markazitextvfbeta/`. The directory contains only two files:
- `MarkaziText-VF.ttf` (218,808 bytes)
- `OFL.txt`

This is one of five "VF Beta" directories in google/fonts that lack METADATA.pb files entirely. The others are `lemonadavfbeta`, `mavenprovfbeta`, `podkovavfbeta`, and `rokkittvfbeta`. All five have corresponding non-beta versions with full METADATA.pb files.

## Repository Analysis

**Upstream repository**: https://github.com/BornaIz/markazitext

The repository is shared with the non-beta "Markazi Text" family. It contains:
- **Source file**: `sources/Markazi-Text.glyphs` (Glyphs format)
- **Config**: `sources/config.yaml` (added in commit `38c03b2`, 2021-07-06, "Updating to UFR")
- **Compiled fonts**: `fonts/` directory with static instances and variable font
- **License**: OFL
- **Designers**: Borna Izadpanah (primary), with contributions from Marc Foley (m4rc1e) and Aaron Bell (aaronbell)

The config.yaml at HEAD (`a876c4f`) specifies:
```yaml
sources:
  - MarkaziText.glyphs
axisOrder:
  - wght
familyName: Markazi Text
stat:
  MarkaziText[wght].ttf:
  - name: Weight
    tag: wght
    values:
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

**Note**: At the time of the VF beta onboarding (commit `89f9a2f`, 2018-05-09), no `config.yaml` existed in the repository. The config was added in 2021 during the UFR (Upstream Font Repository) update.

## Onboarding History

The VF beta was an early variable font experiment that predated the formal Markazi Text release. The timeline:

1. **2018-05-09**: Upstream commit `89f9a2f` — "Merge pull request #2 from m4rc1e/gf-mastering2" (readded variable font). This commit contained `sources/Markazi-Text.glyphs` and `fonts/MarkaziText-VF.ttf`.

2. **2018-05-17**: Marc Foley (m4rc1e) created google/fonts commit `a2dce78` adding `ofl/markazitextvfbeta/MarkaziText-VFBeta.ttf`, as part of PR #1565. The commit message explicitly stated: "Taken from the upstream repo https://github.com/BornaIz/markazitext, commit 89f9a2fd100e912e572c873c187a854bac4f0635".

3. **2018-05-30**: Two additional upstream commits were made by Marc Foley:
   - `20dbd56` — "Regenerated variable font using fontmake"
   - `795ef72` — "added dsig to variable font"
   - These were merged upstream as PRs #3 (`9f2ecdd`) and #4 (`b1badc2`)

4. **2018-05-30**: Corresponding google/fonts commits updated the VF beta:
   - `dce2b3f` — "markazitext v1.000: Regenerated variable font using fontmake"
   - `8889879` — "markazitextvfbeta: v1.000 added dsig table" (also renamed file from `MarkaziText-VFBeta.ttf` to `MarkaziText-VF.ttf`)

5. **2018-06-06**: The non-beta `ofl/markazitext/` was added via PR #1594 by Marc Foley. His PR comment stated: "I've kept the previous markazitextvfbeta dir and added this family to a new dir markazitext. The family is no longer a beta imo."

6. **2018-08-21**: PR #1565 (the VF beta PR) was merged — after the non-beta was already in place.

7. **2024-12-17**: OFL.txt was added to `markazitextvfbeta` by Svante Richter via PR #8745 ("Add missing licenses").

The final font file in the VF beta directory (`MarkaziText-VF.ttf`) corresponds to upstream commit `b1badc2` (2018-05-30, the dsig merge), not the originally cited `89f9a2f`.

## Build Configuration

**No config.yaml existed** at the time the VF beta was onboarded (May 2018). The `sources/config.yaml` was added to the upstream repo in July 2021 as part of the UFR update (commit `38c03b2`).

Since this is a legacy VF beta directory without METADATA.pb, and the non-beta "Markazi Text" family already has a complete source block pointing to the same upstream repository with `config_yaml: "sources/config.yaml"`, no separate build configuration is needed for the VF beta.

## Findings

1. **Legacy VF beta directory**: `ofl/markazitextvfbeta/` is a legacy artifact from the early days of variable font support in Google Fonts (2018). It was created as a "beta" release before the formal non-beta version was added.

2. **No METADATA.pb**: The directory has never had a METADATA.pb file. This is consistent with all five VF beta directories in google/fonts, which appear to be early experiments that were later superseded.

3. **Superseded by non-beta**: The `ofl/markazitext/` directory contains the current, production version of Markazi Text, with a complete METADATA.pb including a source block:
   ```
   source {
     repository_url: "https://github.com/BornaIz/markazitext"
     commit: "a876c4f0111b96f407741a877e79f207e9117338"
     config_yaml: "sources/config.yaml"
   }
   ```

4. **Same upstream repo**: Both the VF beta and non-beta versions come from the same upstream repository (https://github.com/BornaIz/markazitext).

5. **Commit hash discrepancy**: The VF beta was originally onboarded from upstream commit `89f9a2f` but was subsequently updated with font files from later upstream commits (`20dbd56` for fontmake regeneration and `795ef72`/`b1badc2` for dsig). The final font file corresponds to upstream commit `b1badc2`.

6. **Not actively served**: The VF beta directory appears to be a historical artifact. Without a METADATA.pb, it is not served through the Google Fonts API in the standard way. The non-beta version is the production family.

## Recommended Source Block

**No source block is recommended** for the VF beta directory. This is a legacy artifact that has been fully superseded by the non-beta "Markazi Text" family (`ofl/markazitext/`), which already has a complete and correct source block.

The appropriate action for this directory would be for the Google Fonts team to decide whether to:
- **Remove the VF beta directory entirely** (since the non-beta version supersedes it)
- **Leave it as-is** as a historical artifact

If a source block were ever needed for documentation purposes, it would be:
```
source {
  repository_url: "https://github.com/BornaIz/markazitext"
  commit: "b1badc2229cdc16cefb2b2886f01a8a29063e2c8"
}
```

This references commit `b1badc2` (2018-05-30, "Merge pull request #4 from m4rc1e/dsig"), which is the upstream state that matches the final font file in the VF beta directory. No `config_yaml` would apply because no config existed at that commit.

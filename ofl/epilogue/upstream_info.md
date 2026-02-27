# Investigation: Epilogue

## Summary

| Field | Value |
|---|---|
| Family Name | Epilogue |
| Designer | Tyler Finck, ETC |
| License | OFL |
| Date Added | 2020-06-26 |
| Repository URL | https://github.com/Etcetera-Type-Co/Epilogue |
| Commit (in METADATA.pb) | `76bd97a82f0105535fb06e6940f2140b2c1a660c` |
| Correct Commit (original onboarding) | `d3aea77a4ac80e394ffabef183d13d36a1c1bc1d` |
| Correct Commit (last font update) | `7a46afad13fd6e996e387559478fe8b4c7bb1807` |
| Config YAML | `sources/config.yaml` (at commit `7a46afa`) |
| Source Format | Glyphs (.glyphs) |
| Status | needs_correction |
| Confidence | HIGH |

## METADATA.pb Source Block (Current)

```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Epilogue"
  commit: "76bd97a82f0105535fb06e6940f2140b2c1a660c"
  config_yaml: "sources/config.yaml"
}
```

## Repository URL

The repository URL `https://github.com/Etcetera-Type-Co/Epilogue` is confirmed correct. It is referenced in:
- The copyright string in METADATA.pb fonts entries
- The DESCRIPTION.en_us.html
- PR #2518 (original onboarding) body text
- PR #3634 (UFR update) body text

## Onboarding History

### Original Onboarding: PR #2518 (merged 2020-06-29)

- **Author**: Rosalie Wagner (@RosaWagner)
- **Title**: "Epilogue: v2.111 added"
- **Commit message**: "Taken from the upstream repo <https://github.com/Etcetera-Type-Co/Epilogue> at commit <https://github.com/Etcetera-Type-Co/Epilogue/tree/d3aea77a4ac80e394ffabef183d13d36a1c1bc1d>"
- **Upstream commit**: `d3aea77a4ac80e394ffabef183d13d36a1c1bc1d` (2020-06-26, "Merge pull request #13 from RosaWagner/master")
- **Tag**: This commit is tagged as `2.111` in the upstream repo
- **Source structure at this commit**: `Sources/` directory (capitalized) containing `Epilogue.glyphs`, `epilogue_italic.glyphs`, `build.sh`, and a `legacy/` subfolder. No `config.yaml` existed at this commit.

### Font Update: PR #3634 (merged 2021-08-05)

- **Author**: Aaron Bell (@aaronbell)
- **Title**: "Epilogue v2.112 (stat fix)"
- **Body**: "Font repro updated to the UFR format (https://github.com/Etcetera-Type-Co/Epilogue). Font files rebuilt."
- **No specific upstream commit hash mentioned in the PR**
- **Context**: Aaron Bell submitted upstream PR #17 ("Updating to UFR Format") which was merged on 2021-07-24 at commit `7a46afa`. This PR converted the repo to the Google Unified Font Repository format, adding `sources/config.yaml`, renaming the sources directory from `Sources/` to `sources/`, and adding proper build infrastructure.
- **Most likely upstream commit used**: `7a46afad13fd6e996e387559478fe8b4c7bb1807` (2021-07-24, "Merge pull request #17 from aaronbell/master")

At commit `7a46afa`, the config.yaml produces two output files matching what's in google/fonts:
- `Epilogue[wght].ttf` (upright, wght axis)
- `Epilogue-Italic[wght].ttf` (italic, wght axis)

## Commit Hash Issue (CRITICAL)

The commit hash currently in METADATA.pb (`76bd97a`) is **incorrect** for the fonts currently serving in google/fonts. Here is why:

### Commit `76bd97a` (2023-10-11) - Currently in METADATA.pb

This is the HEAD of the upstream repo. Tyler Finck combined italic and upright into a single source file with slant axis support. At this commit:
- Source: single `Epilogue.glyphs` file
- Config axes: `slnt` (slant) + `wght`
- Would produce a **single** `Epilogue[slnt,wght].ttf` (not two separate files)
- This does NOT match the fonts in google/fonts (`Epilogue[wght].ttf` + `Epilogue-Italic[wght].ttf`)

### Commit `7a46afa` (2021-07-24) - Correct for last font update

This was the state used for PR #3634:
- Sources: `Epilogue.glyphs` + `Epilogue-Italic.glyphs` (two separate files)
- Config axes: `wght` + `ital`
- Produces `Epilogue[wght].ttf` + `Epilogue-Italic[wght].ttf`
- This **matches** the fonts currently in google/fonts

### How the wrong commit got into METADATA.pb

The commit hash `76bd97a` was ported from the fontc_crater targets.json list in commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list", 2025-03-31). The fontc_crater targets list apparently referenced HEAD of the upstream repo at the time it was compiled, rather than the commit that was actually used to build the fonts serving in google/fonts.

## Timeline of Upstream Commits After Last Font Update

After `7a46afa` (used for PR #3634), the following upstream commits were made:

| Date | Hash | Description |
|---|---|---|
| 2021-11-02 | `c9f23c2` | added woff2 files to the variable folder |
| 2021-11-02 | `6029d9a` | fixed transformed components from issue 19 |
| 2021-11-02 | `63728f0` | fixed Sacutedotaccent compatibility |
| 2021-11-02 | `2284f14` | transformed component issue resolved |
| 2021-11-02 | `ffddee0` | more transformed component corrections |
| 2022-01-05 | `90d226a` | updated underline value |
| 2023-10-11 | `76bd97a` | combined italic and upright to one source file, variable font has slant support |

These commits include source changes, component fixes, and a fundamental restructuring of the source files. None of these changes are reflected in the fonts currently in google/fonts.

## Source Files

### At correct commit (`7a46afa`)

```
sources/
  Epilogue.glyphs
  Epilogue-Italic.glyphs
  config.yaml
  legacy/
    2axesVF/
      build.sh
      buildVF_test.sh
      epilogue-slnt,wght.glyphs
      stat.stylespace
```

### config.yaml at `7a46afa`

```yaml
sources:
  - Epilogue.glyphs
  - Epilogue-Italic.glyphs
axisOrder:
  - wght
  - ital
familyName: "Epilogue"
stat:
    Epilogue[wght].ttf:
    - name: Weight
      tag: wght
      values:
      - name: Thin
        value: 100
      ...
      - name: Black
        value: 900
    - name: Italic
      tag: ital
      values:
      - name: Roman
        value: 0
        linkedValue: 1
        flags: 2
    Epilogue-Italic[wght].ttf:
    ...
```

## Font Files in google/fonts

- `ofl/epilogue/Epilogue[wght].ttf` (variable, wght axis 100-900)
- `ofl/epilogue/Epilogue-Italic[wght].ttf` (variable, wght axis 100-900)

No override `config.yaml` exists in the google/fonts family directory.

## Recommended Correction

The METADATA.pb source block should be corrected to reference commit `7a46afa` instead of `76bd97a`:

```
source {
  repository_url: "https://github.com/Etcetera-Type-Co/Epilogue"
  commit: "7a46afad13fd6e996e387559478fe8b4c7bb1807"
  config_yaml: "sources/config.yaml"
}
```

This commit:
1. Has a `sources/config.yaml` that produces the correct output files
2. Was the state of the repo when PR #3634 rebuilt the fonts
3. Predates the google/fonts merge date (Aug 5, 2021)

## People Involved

- **Tyler Finck** (@tylerfinck): Designer and owner of Etcetera Type Co, creator of Epilogue
- **Rosalie Wagner** (@RosaWagner): Performed the original onboarding (PR #2518)
- **Aaron Bell** (@aaronbell): Performed the UFR update (PR #3634) and upstream PR #17

## Investigation Date

2026-02-27

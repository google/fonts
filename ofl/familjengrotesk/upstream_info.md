# Investigation: Familjen Grotesk

## Summary

| Field | Value |
|---|---|
| **Family Name** | Familjen Grotesk |
| **Designer** | Familjen STHLM AB |
| **License** | OFL |
| **Repository URL** | https://github.com/Familjen-Sthlm/Familjen-Grotesk |
| **Commit (in METADATA.pb)** | `de7dfe09f6014e43bfad3724ac4a07b95972763c` |
| **Correct Onboarding Commit** | `3db181c2b39766045aff4a99663f515d3247512a` |
| **Branch** | master |
| **Config YAML** | `sources/config.yaml` (in upstream repo) |
| **Status** | needs_correction |
| **Confidence** | HIGH |

## METADATA.pb Analysis

The METADATA.pb already has a complete source block with repository URL, commit hash, branch, config_yaml, and file mappings. The source block was built up incrementally:

1. **PR #4338** (2022-03-03): Initial onboarding of Version 2.000 by Emma Marichal
2. **PR #4738** (2022-06-02): Updated to Version 2.001 by Emma Marichal
3. **PR #4799** (2022-06-16): Updated to Version 2.002 by Emma Marichal (last font binary update)
4. **upstream.yaml merge** (2024-04-03): Simon Cozens merged upstream.yaml data into METADATA.pb, adding file mappings and branch info, with commit `3db181c` (from gftools-packager Version 2.002 message)
5. **Batch 1/4** (2025-03-31): Felipe Sanches ported fontc_crater targets data, changing commit from `3db181c` to `de7dfe0` and adding `config_yaml: "sources/config.yaml"`

## Commit Hash Analysis

### Commits Referenced in google/fonts History

| Version | Upstream Commit | Upstream Date | google/fonts PR | Merge Date |
|---|---|---|---|---|
| 2.000 | `2bd3741f` (Merge PR #2 from emmamarichal) | 2022-02-24 | [#4338](https://github.com/google/fonts/pull/4338) | 2022-03-03 |
| 2.001 | `58b0bedd` (Merge PR #5 from emmamarichal) | 2022-06-02 | [#4738](https://github.com/google/fonts/pull/4738) | 2022-06-02 |
| 2.002 | `3db181c2` (Merge PR #6 from emmamarichal) | 2022-06-16 | [#4799](https://github.com/google/fonts/pull/4799) | 2022-06-16 |

### Current METADATA.pb Commit

The current METADATA.pb references `de7dfe09f6014e43bfad3724ac4a07b95972763c` (2023-06-17, "Version 1.000; Beta; Release 3; Build 23"), which is the HEAD of the master branch. This commit was made by Kristian Moeller one year after the last google/fonts update, and it only added static font exports in a new `fonts/fonts 13.03.40/` directory. It did NOT change the source files, config.yaml, or variable font binaries.

### Correct Commit

The correct commit should be `3db181c2b39766045aff4a99663f515d3247512a` (2022-06-16, "Merge pull request #6 from emmamarichal/master"). This is the commit explicitly referenced in the gftools-packager message for the last binary update (Version 2.002, PR #4799).

### Verification

- Binary files in google/fonts are **byte-identical** to `fonts/variable/` at both `3db181c` and `de7dfe0`
- Source files (`sources/FamiljenGrotesk.glyphs`, `sources/FamiljenGrotesk-Italic.glyphs`) are **identical** at both commits
- `sources/config.yaml` is **identical** at both commits
- The only difference at `de7dfe0` is the addition of `fonts/fonts 13.03.40/` directory with static and variable font exports

While using `de7dfe0` would produce identical build results (since sources are unchanged), `3db181c` is the historically accurate commit and should be preferred.

## Upstream Repository

- **URL**: https://github.com/Familjen-Sthlm/Familjen-Grotesk (verified, accessible)
- **Default branch**: master
- **Created**: 2020-08-26
- **Last pushed**: 2023-06-17
- **Total commits**: 30 (full history, repo was previously a shallow clone)
- **Status**: Clean, up to date with origin

### Source Files at `3db181c`

- `sources/FamiljenGrotesk.glyphs` (Glyphs source)
- `sources/FamiljenGrotesk-Italic.glyphs` (Glyphs source)
- `sources/config.yaml` (gftools-builder configuration)

### config.yaml Content

```yaml
    sources:
      - FamiljenGrotesk.glyphs
      - FamiljenGrotesk-Italic.glyphs
    axisOrder:
      - wght
      - ital
    familyName: "Familjen Grotesk"
```

## Font Files

| File | Source in Upstream |
|---|---|
| `FamiljenGrotesk[wght].ttf` | `fonts/variable/FamiljenGrotesk[wght].ttf` |
| `FamiljenGrotesk-Italic[wght].ttf` | `fonts/variable/FamiljenGrotesk-Italic[wght].ttf` |
| `OFL.txt` | `OFL.txt` |

Binary comparison (MD5):
- `FamiljenGrotesk[wght].ttf`: `d09a3a1a2e40790267115507817c8d8c` (google/fonts = upstream at both `3db181c` and `de7dfe0`)
- `FamiljenGrotesk-Italic[wght].ttf`: `ca5821d684da76b509c3135fb7a13733` (google/fonts = upstream at both `3db181c` and `de7dfe0`)
- `OFL.txt`: Identical between google/fonts and upstream

## Onboarding History

The font was contributed by Kristian Moeller of Familjen STHLM AB via [issue #4144](https://github.com/google/fonts/issues/4144). All three updates (Version 2.000, 2.001, 2.002) were handled by Emma Marichal using gftools-packager. The upstream repository shows Emma Marichal submitted pull requests (#2, #5, #6) to the upstream repo to prepare sources before each onboarding.

### Key People

- **Kristian Moeller** (@ktkm): Lead designer, repository owner
- **Emma Marichal** (@emmamarichal): Font engineer who handled all three onboarding updates

## Recommended Correction

The commit hash in METADATA.pb should be corrected from `de7dfe09f6014e43bfad3724ac4a07b95972763c` to `3db181c2b39766045aff4a99663f515d3247512a` to reflect the actual commit used for the last google/fonts update (Version 2.002). All other fields in the source block are correct.

**Note**: This is a low-impact correction since sources are identical at both commits, but it improves historical accuracy.

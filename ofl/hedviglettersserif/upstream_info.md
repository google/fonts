# Investigation Report: Hedvig Letters Serif

## Summary

Hedvig Letters Serif is a variable serif typeface with an optical size axis, designed by Kanon Foundry (Alexander Orn, Tor Weibull) for Hedvig. It was onboarded to Google Fonts on 2023-10-24 by Rosalie Wagner using gftools-packager. The upstream repository, config.yaml, and commit hash are all well-documented and verified. The source block in METADATA.pb is complete and correct.

## Key Findings

| Field               | Value |
|---------------------|-------|
| **Family Name**     | Hedvig Letters Serif |
| **Designer**        | Kanon Foundry, Alexander Orn, Tor Weibull, Hedvig |
| **Repository URL**  | https://github.com/KanonFoundry/HedvigLetters |
| **Commit Hash**     | `345b4d9015af6a26eb05e436460ca41fc42784df` |
| **Config YAML**     | `sources/Serif.yaml` |
| **Branch**          | `main` |
| **Status**          | **complete** |
| **Confidence**      | **HIGH** |

## Investigation Details

### METADATA.pb Analysis

The METADATA.pb at `ofl/hedviglettersserif/METADATA.pb` contains a fully populated source block with:
- `repository_url`: `https://github.com/KanonFoundry/HedvigLetters`
- `commit`: `345b4d9015af6a26eb05e436460ca41fc42784df`
- `config_yaml`: `sources/Serif.yaml`
- `branch`: `main`
- File mappings for OFL.txt and `HedvigLettersSerif[opsz].ttf`

### Git History in google/fonts

The font was onboarded via commit `c65d9f34d1a5e41d5e6e05935d045912e7e9c3e3` on 2023-10-24:
```
[gftools-packager] Hedvig Letters Serif: Version 1.000 added
* Hedvig Letters Serif Version 1.000 taken from the upstream repo
  https://github.com/KanonFoundry/HedvigLetters at commit
  https://github.com/KanonFoundry/HedvigLetters/commit/345b4d9015af6a26eb05e436460ca41fc42784df.
```

This commit was authored by Rosalie Wagner (mail@rosaliewagner.com). It added the binary font, METADATA.pb, DESCRIPTION, OFL.txt, and upstream.yaml.

Subsequent commits added description updates, designer info, default overrides, and config_yaml field. The `branch` field was removed and then re-added via `f19b6da7d`.

### Upstream Repository Verification

The cached repository at `fontc_crater_cache/KanonFoundry/HedvigLetters/` has been verified:
- Remote: `https://github.com/KanonFoundry/HedvigLetters`
- HEAD is detached at commit `345b4d9` (matching the referenced commit exactly)
- This commit is "Merge pull request #6 from RosaWagner/main" titled "Should be ready for GF", dated 2023-10-24
- No newer commits exist on the main branch beyond this commit in the cached repo

### Config YAML Verification

The file `sources/Serif.yaml` exists at the referenced commit and contains:
```yaml
sources:
  - HedvigLettersSerif.glyphs
buildVariable: true
familyName: "Hedvig Letters Serif"
outputDir: ../fonts/HedvigLettersSerif
axisOrder:
  - opsz
  - wght
```

The source file `sources/HedvigLettersSerif.glyphs` is present. The output directory `fonts/HedvigLettersSerif/variable/` contains the expected `HedvigLettersSerif[opsz].ttf`.

### Source Files

- `sources/HedvigLettersSerif.glyphs` -- Glyphs source file
- `sources/Serif.yaml` -- gftools-builder config
- `sources/HedvigLettersSans.glyphs` -- Sans variant (separate family)
- `sources/Sans.yaml` -- Sans config (separate family)

### Onboarding Timeline

- 2023-09-27: Initial commit in upstream repo
- 2023-09-28 to 2023-10-24: Font development by RosaWagner
- 2023-10-24 14:08 (UTC+2): PR #6 merged in upstream (commit `345b4d9`)
- 2023-10-24 15:33 (UTC+2): Onboarded to google/fonts by Rosalie Wagner

The onboarding happened the same day as the final upstream merge, confirming the commit hash is correct.

## Conclusion

The source block in METADATA.pb is complete and fully verified. The repository URL, commit hash, and config_yaml path are all correct. The font was built from `sources/HedvigLettersSerif.glyphs` using the gftools-builder configuration at `sources/Serif.yaml`. No changes needed.

### Recommended Source Block

```
source {
  repository_url: "https://github.com/KanonFoundry/HedvigLetters"
  commit: "345b4d9015af6a26eb05e436460ca41fc42784df"
  config_yaml: "sources/Serif.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/HedvigLettersSerif/variable/HedvigLettersSerif[opsz].ttf"
    dest_file: "HedvigLettersSerif[opsz].ttf"
  }
  branch: "main"
}
```

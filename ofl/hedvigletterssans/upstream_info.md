# Investigation Report: Hedvig Letters Sans

## Summary

Hedvig Letters Sans is a sans-serif typeface designed by Kanon Foundry (Alexander Orn, Tor Weibull) for Hedvig, added to Google Fonts on 2023-10-24. The METADATA.pb already has a complete source block with repository URL, commit hash, config_yaml path, and file mappings. The upstream repository and config are verified. The source block is complete as-is.

## Key Findings

| Field              | Value                                                                 |
|--------------------|-----------------------------------------------------------------------|
| Family Name        | Hedvig Letters Sans                                                   |
| Designer           | Kanon Foundry, Alexander Orn, Tor Weibull, Hedvig                     |
| Repository URL     | https://github.com/KanonFoundry/HedvigLetters                        |
| Commit Hash        | 345b4d9015af6a26eb05e436460ca41fc42784df                              |
| Config YAML        | sources/Sans.yaml                                                     |
| Status             | complete                                                              |
| Confidence         | HIGH                                                                  |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb has a fully populated source block:
- `repository_url`: `https://github.com/KanonFoundry/HedvigLetters`
- `commit`: `345b4d9015af6a26eb05e436460ca41fc42784df`
- `config_yaml`: `sources/Sans.yaml`
- `files`: mapping for OFL.txt and the regular TTF
- `branch`: `main`

### Google Fonts Git History

Key commits in `ofl/hedvigletterssans/`:

1. **c8dfe32dd** - `[gftools-packager] Hedvig Letters Sans: Version 1.000; ttfautohint (v1.8.4.7-5d5b) added` -- Oct 24, 2023, by gftools-packager. Commit message states: "taken from the upstream repo https://github.com/KanonFoundry/HedvigLetters at commit https://github.com/KanonFoundry/HedvigLetters/commit/345b4d9015af6a26eb05e436460ca41fc42784df"
2. **723b70b4e** - `Hedvig Letters Sans: added description`
3. **34a552ef7** - `Hedvig Letters (Sans+Serif): description updated`
4. **620c142c6** - `Hedvig Letters: added designer`
5. **53995c52a** - `[METADATA.pb] Populate font sources related fields for a few font families.` -- added source block fields
6. **f19b6da7d** - `revert removal of 'branch' values on METADATA.pb files` -- restored branch field

### Upstream Repository Verification

The upstream repo at `KanonFoundry/HedvigLetters` is cached at `fontc_crater_cache/KanonFoundry/HedvigLetters`.

- The referenced commit `345b4d9` exists and is dated 2023-10-24 14:08:33 +0200. Its message: "Merge pull request #6 from RosaWagner/main". This is a merge commit by Rosa Wagner.
- The google/fonts onboarding commit `c8dfe32dd` is dated 2023-10-24 15:35:14 +0200 -- just 1.5 hours after the upstream merge commit. This confirms the commit hash is the correct onboarding reference.
- There are subsequent commits in the upstream repo (through 2025-04-02) that have NOT been incorporated into google/fonts.

### Source Files and Config

The upstream repo contains gftools-builder compatible sources:
- `sources/HedvigLettersSans.glyphs` -- Glyphs source file for Sans
- `sources/HedvigLettersSerif.glyphs` -- Glyphs source file for Serif (separate family)

The config file at `sources/Sans.yaml`:

```yaml
sources:
  - HedvigLettersSans.glyphs
buildVariable: false
familyName: "Hedvig Letters Sans"
outputDir: ../fonts/HedvigLettersSans
```

This config exists at the referenced commit `345b4d9` and matches the `config_yaml: "sources/Sans.yaml"` field in METADATA.pb.

Note: The repo also contains `sources/Serif.yaml` for the Hedvig Letters Serif family (a separate font family with its own METADATA.pb in google/fonts).

No override config.yaml exists in the google/fonts directory (not needed since the upstream repo has its own config).

### Timing Verification

- Upstream commit `345b4d9`: Oct 24, 2023, 14:08 +0200
- Google/fonts onboarding `c8dfe32dd`: Oct 24, 2023, 15:35 +0200
- Same-day onboarding confirms this is the correct commit reference.

## Conclusion

The source block is fully complete and verified. All fields (repository_url, commit, config_yaml, files, branch) are present and correct. No changes are needed.

### Recommended METADATA.pb Source Block

No changes needed. Current source block is correct:

```
source {
  repository_url: "https://github.com/KanonFoundry/HedvigLetters"
  commit: "345b4d9015af6a26eb05e436460ca41fc42784df"
  config_yaml: "sources/Sans.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/HedvigLettersSans/ttf/HedvigLettersSans-Regular.ttf"
    dest_file: "HedvigLettersSans-Regular.ttf"
  }
  branch: "main"
}
```

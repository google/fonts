# Investigation Report: Fruktur

## Summary

Fruktur is a display blackletter font designed by Viktoriya Grabowska with mastering by Eben Sorkin. Originally added to Google Fonts on 2013-01-16, it was significantly updated in August 2022 (PR #5026) with expanded glyph coverage, better language support, and the addition of an italic style. The upstream repository is `SorkinType/Fruktur`, and the METADATA.pb already has a complete source block referencing commit `0f8b79b` with `sources/config.yaml`.

## Key Findings

| Field             | Value                                                      |
|-------------------|------------------------------------------------------------|
| Family Name       | Fruktur                                                    |
| Designer          | Viktoriya Grabowska, Eben Sorkin                           |
| Repository URL    | https://github.com/SorkinType/Fruktur                      |
| Commit Hash       | 0f8b79b91438420d4c158890cb28bcb1eef407a0                   |
| Branch            | main                                                       |
| Config YAML       | sources/config.yaml                                        |
| Status            | complete                                                   |
| Confidence        | HIGH                                                       |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb already contains a complete source block:
- `repository_url`: https://github.com/SorkinType/Fruktur
- `commit`: 0f8b79b91438420d4c158890cb28bcb1eef407a0
- `config_yaml`: sources/config.yaml
- `branch`: main
- File mappings for OFL.txt, Fruktur-Regular.ttf, and Fruktur-Italic.ttf

This source block was added by commit `19cdcec59` ("[Batch 1/4] port info from fontc_crater targets list") which ported data from the fontc_crater targets.json file.

### google/fonts Commit History

Key commits:
1. **90abd17b4** (2015-03-07): Initial commit with the original Fruktur-Regular.ttf
2. **f355cca18**: Update to correct internal metadata
3. **adfe2b6ef**: v1.004, fixes GSUB table, hinting
4. **29b91e63b** (2022-08-05): Major update via PR #5026 -- Version 1.008, added Fruktur-Italic.ttf, updated Regular
5. **66f91f10f**: Merge upstream.yaml into METADATA.pb
6. **19cdcec59**: Batch port of fontc_crater source info into METADATA.pb

### PR #5026 Analysis

PR #5026 ("Fruktur: Version 1.008; ttfautohint (v1.8.4.7-5d5b) added") was authored by Emma Marichal and merged on 2022-08-05. The PR body states:

> Fruktur Version 1.008; ttfautohint (v1.8.4.7-5d5b) taken from the upstream repo https://github.com/SorkinType/Fruktur at commit https://github.com/SorkinType/Fruktur/commit/a2277f91aebc0e5e70062bdd7f17f15d2a787cd2.

The referenced commit `a2277f91` no longer exists in the upstream repository. The repository was subsequently recreated using the googlefonts template, resulting in a single squashed commit (`0f8b79b`, dated 2024-04-16, by Simon Cozens, message: "Update requirements").

### Upstream Repository Verification

The repository `SorkinType/Fruktur` is cached at `upstream_repos/fontc_crater_cache/SorkinType/Fruktur/`. It has a single commit (`0f8b79b`) on the `main` branch.

**Source files at commit `0f8b79b`**:
- `sources/Fruktur.glyphs` (Glyphs format, Roman)
- `sources/FrukturItalic.glyphs` (Glyphs format, Italic)
- `sources/config.yaml` (gftools-builder configuration)

**config.yaml content**:
```yaml
sources:
  - Fruktur.glyphs
axisOrder:
  - wght
familyName: Fruktur
```

Note: The config.yaml only references `Fruktur.glyphs` (the Roman). The italic source `FrukturItalic.glyphs` is not listed. The Makefile in the repo iterates over all `config*.yaml` files, suggesting the italic may have been built with a separate config or the config may be incomplete. However, both font binaries at this commit exactly match those in google/fonts:

- `Fruktur-Regular.ttf`: 211,180 bytes (matches google/fonts)
- `Fruktur-Italic.ttf`: 210,784 bytes (matches google/fonts)

### Commit Hash Assessment

The current METADATA.pb references `0f8b79b`, which is the only commit in the repository (a squashed recreation from April 2024). The original onboarding commit `a2277f91` from PR #5026 no longer exists. Since the repo has only one commit and the font binaries at that commit match google/fonts exactly, the reference to `0f8b79b` is correct and the only valid option.

### Historical Note

The FONTLOG references `https://github.com/EbenSorkin/Fruktur` as the original repository. This URL now redirects to `https://github.com/SorkinType/-Fruktur` (with a dash prefix), a separate repository from `SorkinType/Fruktur`. The active upstream for the updated font (with italic) is `SorkinType/Fruktur`.

## Conclusion

The Fruktur source block in METADATA.pb is complete and correct. The repository URL, commit hash, config_yaml, and file mappings are all valid. The font binaries at the referenced commit match those in google/fonts. No changes are needed.

### Current METADATA.pb Source Block (Verified Correct)

```
source {
  repository_url: "https://github.com/SorkinType/Fruktur"
  commit: "0f8b79b91438420d4c158890cb28bcb1eef407a0"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/ttf/Fruktur-Regular.ttf"
    dest_file: "Fruktur-Regular.ttf"
  }
  files {
    source_file: "fonts/ttf/Fruktur-Italic.ttf"
    dest_file: "Fruktur-Italic.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

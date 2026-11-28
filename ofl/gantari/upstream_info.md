# Investigation Report: Gantari

## Summary

Gantari is a sans-serif variable font family by Lafontype, added to Google Fonts on June 2, 2022 via PR #4720. The upstream repo at `https://github.com/Lafontype/Gantari` has a single commit (`363a3dd`) which contains the complete project including source `.glyphs` files, compiled variable fonts, and a `sources/config.yaml`. The METADATA.pb source block is complete and correct.

## Key Findings

| Field             | Value                                                         |
|-------------------|---------------------------------------------------------------|
| Family Name       | Gantari                                                       |
| Repository URL    | https://github.com/Lafontype/Gantari                         |
| Commit Hash       | 363a3dd5634bfec7e9f7db11ca3e1f4739a182ab                      |
| Config YAML       | sources/config.yaml                                           |
| Status            | **complete**                                                  |
| Confidence        | **HIGH**                                                      |

## Investigation Details

### Onboarding History

The font was onboarded via commit `b57c3acbd` (google/fonts PR #4720) on June 2, 2022, authored by Emma Marichal with co-author Rosalie Wagner. The commit message states:

> Gantari Version 1.000 taken from the upstream repo https://github.com/Lafontype/Gantari at commit https://github.com/Lafontype/Gantari/commit/5115aa79532c3b442fa22f94507e611ed369e2ba.

The referenced commit hash `5115aa7` no longer exists in the upstream repository. The repo appears to have been force-pushed at some point, leaving only a single commit `363a3dd` (dated June 1, 2022 -- the day before the google/fonts onboarding merge).

### METADATA.pb Evolution

1. **Initial onboarding** (b57c3acbd, June 2, 2022): Created METADATA.pb with `upstream.yaml` referencing commit `5115aa7`.
2. **upstream.yaml merge** (66f91f10f, April 3, 2024): Simon Cozens merged upstream.yaml into the METADATA.pb source block, still with the old commit hash.
3. **fontc_crater batch** (19cdcec59, March 31, 2025): Updated commit hash from `5115aa7` to `363a3dd` (the current and only commit in the repo) and added `config_yaml: "sources/config.yaml"`.

### Upstream Repository Analysis

- **URL**: https://github.com/Lafontype/Gantari
- **Remote verified**: Yes, `git fetch` succeeds
- **Repo status**: Clean, on branch `main`, up to date
- **Total commits**: 1 (`363a3dd`, "Add files via upload", June 1, 2022)
- **Author**: Lafontype (lafontype@gmail.com)

The single commit contains:
- Source files: `sources/Gantari.glyphs`, `sources/Gantari-Italic.glyphs`
- Build config: `sources/config.yaml`
- Compiled variable fonts: `fonts/variable/Gantari[wght].ttf`, `fonts/variable/Gantari-Italic[wght].ttf`
- Static OTF and TTF instances
- Documentation images

### Binary Verification

The compiled variable fonts in the upstream repo at `363a3dd` are identical to those in google/fonts:

| File                        | Size (bytes) | SHA256 Match |
|-----------------------------|-------------|--------------|
| Gantari[wght].ttf           | 124,976     | Yes          |
| Gantari-Italic[wght].ttf    | 131,240     | Yes          |

### Config YAML

The upstream repo has `sources/config.yaml` with proper gftools-builder configuration:
- Sources: `Gantari.glyphs`, `Gantari-Italic.glyphs`
- Axis order: wght, ital
- Family name: "Gantari"
- Includes STAT table definitions

No override config.yaml exists in the google/fonts family directory.

### Note on Original Commit Hash

The original onboarding referenced commit `5115aa7` which no longer exists. It is likely that the repo was force-pushed between the onboarding and the fontc_crater batch update. Since the current sole commit `363a3dd` produces binary-identical fonts, this commit is the correct reference.

## Conclusion

The METADATA.pb source block is **complete and correct**. No changes needed.

### Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/Lafontype/Gantari"
  commit: "363a3dd5634bfec7e9f7db11ca3e1f4739a182ab"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Gantari[wght].ttf"
    dest_file: "Gantari[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Gantari-Italic[wght].ttf"
    dest_file: "Gantari-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

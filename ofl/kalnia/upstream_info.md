# Kalnia — Investigation Report

**Date**: 2026-03-03
**Model**: Claude Opus 4.6
**Family slug**: `kalnia`
**Status**: complete

## Initial State

METADATA.pb already contained a complete source block with:
- `repository_url`: `https://github.com/fridamedrano/Kalnia-Typeface`
- `commit`: `b58d2689de548478ed6cee6937c37eabc4140958`
- `config_yaml`: `sources/config.yaml`
- `branch`: `main`
- File mappings for OFL.txt, DESCRIPTION.en_us.html, and Kalnia[wdth,wght].ttf

The font was added to Google Fonts on 2023-10-19 and the font binary had not been updated since.

## Investigation

### Onboarding History

Kalnia was onboarded via PR #6879 by Viviana Monsalve on 2023-10-19 using gftools-packager. The original commit message referenced upstream commit `22e2d855245c5a4f94aa12461e1b1be5c0da841b`.

### Commit Hash Discrepancy

The gftools-packager onboarding (commit `8e748d2e9`) originally recorded commit `22e2d855` from the upstream repo. However, this commit no longer exists in the upstream repo. The entire repository history was squashed into a single commit (`b58d268`, dated 2023-10-29, message "Eth, j, fj, fi updates"). This squash occurred 10 days after the font was onboarded to Google Fonts.

The current commit `b58d268` was set by the "[Batch 2/4] port info from fontc_crater targets list" commit (`4ad8ac68`, 2025-03-31), which also added the `config_yaml` field. This batch update sourced the commit hash from fontc_crater's target.json.

### Binary File Verification

The font binary `Kalnia[wdth,wght].ttf` in google/fonts exactly matches the one at `fonts/variable/Kalnia[wdth,wght].ttf` in the upstream repo at commit `b58d268`:
- SHA-256: `33685d0ec4abcca2736a51a10a6d4ee1aab2e608e6598c6926af9550b86731a4`

Since the upstream repo only has one commit and the binaries match, `b58d268` is effectively the correct reference even though it is not the original onboarding commit (which was squashed away).

### Upstream Repository

- **URL**: https://github.com/fridamedrano/Kalnia-Typeface
- **Single commit**: `b58d268` (2023-10-29, "Eth, j, fj, fi updates")
- **Source file**: `sources/Kalnia.glyphs` (Glyphs format)
- **Config**: `sources/config.yaml` (gftools-builder compatible)
- **Repo status**: Clean, up to date with origin

### Config.yaml Contents

The upstream `sources/config.yaml` contains a valid gftools-builder configuration:
- Source: `Kalnia.glyphs`
- Builds variable and static fonts
- Axis order: wght, wdth
- Family name: Kalnia

### Subsequent Changes in google/fonts

After onboarding, the kalnia directory received these changes:
- `738ee89a` (2023-10-19): METADATA.pb math subset + stroke and classification added
- `66f91f10` (2024-04-03): Merge upstream.yaml into METADATA.pb
- `f97d0f2e` (2025-01-14): Kalnia Glaze article adjustments (also touched kalnia)
- `9ece2689` (2025-01-16): Kalnia corrected (article corrections between kalnia and kalniaglaze)
- `4ad8ac68` (2025-03-31): Batch 2/4 - updated commit hash and added config_yaml

No override config.yaml exists in the google/fonts family directory, nor is one needed since the upstream repo contains a valid `sources/config.yaml`.

## Actions Taken

Read and analyzed METADATA.pb, upstream repo history, google/fonts commit history, and verified binary file integrity. No changes were needed.

## Final State

The source block in METADATA.pb is complete and correct. The repository URL points to a valid upstream repo, the commit hash references the only commit in the repo (the original was squashed but the binary matches), the config.yaml path is valid, and file mappings are correct.

## Source Block
```
source {
  repository_url: "https://github.com/fridamedrano/Kalnia-Typeface"
  commit: "b58d2689de548478ed6cee6937c37eabc4140958"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "documentation/DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/variable/Kalnia[wdth,wght].ttf"
    dest_file: "Kalnia[wdth,wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

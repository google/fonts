# Lora — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/cyrealtype/Lora-Cyrillic"
  commit: "c44a1dde19a3fcff5bf549677e08a64510837e9d"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Lora[wght].ttf"
    dest_file: "Lora[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Lora-Italic[wght].ttf"
    dest_file: "Lora-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

## Repository Analysis

- **Repository URL**: https://github.com/cyrealtype/Lora-Cyrillic (verified accessible, HTTP 200)
- **Repository owner**: Cyreal (cyrealtype)
- **Primary author**: Alexei Vanyashin (a+mygit@cyreal.org)
- **Other contributors**: Aaron Bell, Emma Marichal, Marc Foley, Denis Moyogo Jacquerye, Olga Karpushina, Richard Lipton, Jill Pichotta, CrystalType
- **Default branch**: main
- **Source files at commit `403b1a66`**: `sources/Lora.glyphs`, `sources/Lora-Italic.glyphs`
- **Config file at commit `403b1a66`**: `sources/config.yaml` (present and valid)
- **Build tool**: gftools-builder (config.yaml references Glyphs sources with STAT tables and weight axis)
- **Latest upstream commits (beyond what is in google/fonts)**:
  - `ed15b630` (2025-05-17): "addresses #69, fixed in sources"
  - `7dc32ea6` (2025-05-25): "cleanup"

The upstream repo has a well-structured layout with Glyphs sources, compiled font outputs in `fonts/` subdirectories (variable, ttf, otf, webfonts), and a proper `sources/config.yaml`.

## Onboarding History

Lora has a long history in Google Fonts, dating back to the initial commit (2011-07-06):

1. **v2.000** — PR #542, merged 2016-12-14. Added by Marc Foley (m4rc1e).
2. **v2.101** — PR #1288, merged 2017-10-29. Added by Marc Foley.
3. **v2.102** — PR #1398, merged 2017-12-18. Added by laerm0 (ttfautohinted). Immediately reverted in PR #1400.
4. **v3.000** — Commit `16a2ebfdf`, merged 2020-03-04 (PR #2377). Taken from upstream at commit `1063c5dd65157e00c561867ad7bf1c7985678f35`.
5. **v3.001** — PR #3641, merged 2021-08-03. STAT table fix.
6. **v3.004** — PR #4996, merged 2022-07-28. Taken from upstream commit `42418d965083aa5471c6d9aa5f5c4051cba29384`. This PR introduced the initial `source { }` block in METADATA.pb.
7. **v3.008** — PR #7103, merged 2024-01-09. Taken from upstream commit `403b1a66ca2e79f81d749c5299559e168591a4df`. Updated by Emma Marichal via gftools-packager. The commit message and PR body both reference this exact upstream commit.
8. **Batch 2/4** — Commit `4ad8ac680`, 2025-03-31. This batch update from fontc_crater targets changed the commit hash from `403b1a66` to `c44a1dde` and added `config_yaml: "sources/config.yaml"`.

## Build Configuration

- **Config file**: `sources/config.yaml` exists in the upstream repo at both the correct commit (`403b1a66`) and at HEAD.
- **Config content**: References two Glyphs sources (`Lora.glyphs` and `Lora-Italic.glyphs`), specifies `wght` axis order, family name "Lora", and STAT table definitions for both Roman and Italic variable font files.
- **Build method**: gftools-builder with Glyphs sources.
- **Config path in METADATA.pb**: `sources/config.yaml` — this is correct and points to the config in the upstream repo.

## Findings

### Critical Issue: Wrong Commit Hash

The commit hash currently in METADATA.pb (`c44a1dde19a3fcff5bf549677e08a64510837e9d`, "built fonts v3.11", 2024-11-06) is **incorrect**. It was introduced by the Batch 2/4 fontc_crater port (commit `4ad8ac680` in google/fonts, 2025-03-31), which sourced the hash from fontc_crater's target.json file.

The correct commit hash is `403b1a66ca2e79f81d749c5299559e168591a4df` ("Update Lora (#65)", 2023-12-14), which was:
- Referenced in the gftools-packager commit message for v3.008
- Referenced in the PR #7103 body
- **Verified by binary file comparison**: The SHA256 hashes of `Lora[wght].ttf` and `Lora-Italic[wght].ttf` in google/fonts match exactly with the files at upstream commit `403b1a66`, and differ from the files at `c44a1dde`.

**Binary verification**:
| File | google/fonts size | upstream @ `403b1a66` | upstream @ `c44a1dde` |
|------|------------------|-----------------------|-----------------------|
| `Lora[wght].ttf` | 212,196 bytes | 212,196 bytes (SHA256 match) | 209,044 bytes |
| `Lora-Italic[wght].ttf` | 221,232 bytes | 221,232 bytes (SHA256 match) | 222,528 bytes |

The fontc_crater target.json apparently pointed to a newer commit (`c44a1dde`, v3.11 from November 2024) that was not the one actually used for the last onboarding. Between the correct commit (`403b1a66`) and the incorrect one (`c44a1dde`), there were 6 upstream commits that introduced changes to the fonts:

- `3748b17d` (2024-01-26): "fixed sterling"
- `54e93242` (2024-02-05): "fixes #66"
- `5828caa8` (2024-10-21): "fixes #67"
- `d5e22b63` (2024-10-21): "generated fonts v3.010"
- `4be406e5` (2024-11-06): "updated registered sign"
- `c44a1dde` (2024-11-06): "built fonts v3.11"

These additional changes have NOT been reviewed or onboarded to Google Fonts. If they are to be incorporated, they would need a separate review process.

### Other Observations

- The `repository_url` is correct and accessible.
- The `branch` field ("main") is correct.
- The `files` mappings are correct.
- The `config_yaml` field ("sources/config.yaml") is correct — config.yaml exists at that path in the upstream repo at the correct commit.
- There are 2 even newer commits on upstream main (from May 2025) beyond `c44a1dde`.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/cyrealtype/Lora-Cyrillic"
  commit: "403b1a66ca2e79f81d749c5299559e168591a4df"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Lora[wght].ttf"
    dest_file: "Lora[wght].ttf"
  }
  files {
    source_file: "fonts/variable/Lora-Italic[wght].ttf"
    dest_file: "Lora-Italic[wght].ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yaml"
}
```

The only change from the current source block is reverting the commit hash from `c44a1dde19a3fcff5bf549677e08a64510837e9d` back to `403b1a66ca2e79f81d749c5299559e168591a4df`, which is the commit that actually matches the font binaries currently served in Google Fonts.

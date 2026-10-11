# Luxurious Roman — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/luxurious-roman"
  commit: "79ca0d1eececc94be7fe0e23f306043de77c7457"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LuxuriousRoman-Regular.ttf"
    dest_file: "LuxuriousRoman-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

## Repository Analysis

- **Repository**: https://github.com/googlefonts/luxurious-roman
- **Status**: Active, accessible
- **Designer**: Robert Leuschke
- **Source files**: `sources/Luxurious-Roman.glyphs` (Glyphs format)
- **Config file**: `sources/config.yml` (gftools-builder config)
- **Font outputs**: `fonts/ttf/LuxuriousRoman-Regular.ttf`, `fonts/otf/LuxuriousRoman-Regular.otf`, `fonts/webfonts/LuxuriousRoman-Regular.woff2`
- **Total commits**: 36 (from initial commit on 2021-11-03 to latest on 2021-11-25)
- **Latest commit**: `79ca0d1` ("sample image updated", 2021-11-25) — only changed `Documentation/image1.png`

### Config.yml Contents

```yaml
sources:
  - Luxurious-Roman.glyphs
familyName: "Luxurious Roman"
buildVariable: false
#autohintTTF: false
```

The config existed at `sources/config.yml` at both the onboarding commit and HEAD. It references a single Glyphs source with no variable font output.

## Onboarding History

The font was onboarded via PR [#4082](https://github.com/google/fonts/pull/4082), merged on 2021-11-26.

- **PR title**: "Luxurious Roman: Version 1.010; ttfautohint (v1.8.3) added"
- **Author**: Viviana Monsalve (viviana.monsalve.a@gmail.com)
- **Merge commit**: `8f6171bdb`
- **Tool used**: gftools-packager
- **Upstream commit referenced in PR**: `31c4f13d56c397cb8e0fb6992594cd4ec5b12ffd` ("Luxurious Roman copyright fix", 2021-11-18)

The PR body explicitly stated:
> "Luxurious Roman Version 1.010; ttfautohint (v1.8.3) taken from the upstream repo https://github.com/googlefonts/luxurious-roman at commit https://github.com/googlefonts/luxurious-roman/commit/31c4f13d56c397cb8e0fb6992594cd4ec5b12ffd."

### Commit Hash Discrepancy

The current METADATA.pb has commit `79ca0d1eececc94be7fe0e23f306043de77c7457`, which was set by the "[Batch 2/4] port info from fontc_crater targets list" commit (`4ad8ac680`, 2025-03-31). The fontc_crater targets list used HEAD of the upstream repo (`79ca0d1`) rather than the actual onboarding commit (`31c4f13d`).

### Binary File Verification

SHA-256 comparison of `LuxuriousRoman-Regular.ttf`:
- At commit `31c4f13d` (onboarding): `30d6bc4b25cf075560f0dd90a77a8ed8165bd280a863de1c3ab429fbf9ace58b`
- At commit `79ca0d1` (HEAD): `30d6bc4b25cf075560f0dd90a77a8ed8165bd280a863de1c3ab429fbf9ace58b`
- In google/fonts: `30d6bc4b25cf075560f0dd90a77a8ed8165bd280a863de1c3ab429fbf9ace58b`

All three are identical. The commit `79ca0d1` only changed `Documentation/image1.png` (a sample image), not any source or font files. Therefore, the font binary is the same at both commits.

## Build Configuration

- **Config file**: `sources/config.yml` (present in upstream repo)
- **Config path in METADATA.pb**: `sources/config.yml` (correct)
- **Override config.yaml**: None present in google/fonts family directory
- **Source format**: Glyphs (`.glyphs`)
- **Build type**: Static only (`buildVariable: false`)

## Findings

1. **Commit hash should be corrected**: The METADATA.pb currently references `79ca0d1` (HEAD, "sample image updated") instead of `31c4f13d` (the commit explicitly referenced during onboarding via gftools-packager). While both commits produce identical font binaries, the correct onboarding commit as documented in PR #4082 was `31c4f13d`. The fontc_crater targets list used HEAD rather than the actual onboarding commit.

2. **Repository URL is correct**: `https://github.com/googlefonts/luxurious-roman` is valid and accessible.

3. **Config path is correct**: `sources/config.yml` exists at both commits and contains valid gftools-builder configuration.

4. **No override config needed**: The upstream repo already has a proper `config.yml`.

5. **Note on functional equivalence**: Since `79ca0d1` only changed a documentation image and did not alter any source files, font binaries, or build configuration, the current commit hash is functionally correct for building purposes. However, for historical accuracy, `31c4f13d` should be preferred as it was the documented onboarding commit.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/googlefonts/luxurious-roman"
  commit: "31c4f13d56c397cb8e0fb6992594cd4ec5b12ffd"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "DESCRIPTION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  files {
    source_file: "fonts/ttf/LuxuriousRoman-Regular.ttf"
    dest_file: "LuxuriousRoman-Regular.ttf"
  }
  branch: "main"
  config_yaml: "sources/config.yml"
}
```

The only change from the current block is the commit hash: `79ca0d1eececc94be7fe0e23f306043de77c7457` should be corrected to `31c4f13d56c397cb8e0fb6992594cd4ec5b12ffd` to match the commit explicitly referenced during onboarding in PR #4082.

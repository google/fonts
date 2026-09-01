# Marhey — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: complete

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/namelatype/Marhey"
  commit: "535eeb5a3f4dee825fdaf13d84075b212d969f8d"
  config_yaml: "source/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Marhey[wght].ttf"
    dest_file: "Marhey[wght].ttf"
  }
  files {
    source_file: "DESCRITION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

The source block was largely populated during the upstream.yaml-to-METADATA.pb merge (commit `66f91f10f`, 2024-04-03). The `config_yaml` field was added later by the gfonts_agents project (commit `d9ad7cfd4`, 2025-09-18).

## Repository Analysis

- **Repository**: https://github.com/namelatype/Marhey
- **Owner**: namelatype (Nur Syamsi / Bustanul Arifin)
- **Cached at**: `upstream_repos/fontc_crater_cache/namelatype/Marhey`
- **Repository status**: Clean, up to date with origin/main
- **Default branch**: main
- **Total commits**: 54
- **Latest commit**: `535eeb5` (2022-10-07) — "Merge pull request #5 from yanone/main"

The repository contains:
- `source/Marhey.glyphs` — Glyphs source file
- `source/config.yaml` — gftools-builder configuration
- `fonts/variable/Marhey[wght].ttf` — Pre-built variable font binary
- `fonts/ttf/` — Pre-built static TTF instances
- `fonts/otf/` — Pre-built static OTF instances
- `fonts/webfonts/` — Pre-built WOFF2 files
- `DESCRITION.en_us.html` — Description file (note: typo in filename, missing "P" in "DESCRIPTION")
- `OFL.txt` — License file
- `documentation/` — Specimen images

The repository has not had any new commits since 2022-10-07. Commit `535eeb5` is both HEAD and `origin/main`.

## Onboarding History

The font was onboarded to Google Fonts on **2022-10-07** via **PR #5374** ("Marhey: Version 1.000 added"), authored by **Yanone** (font engineer).

### PR #5374 Timeline

The PR body stated the font was taken from commit `e5686e3` in the upstream repo. However, this was the gftools-packager initial hash, and additional work occurred upstream before the PR was merged:

1. **e5686e3** (2022-10-05): Merge PR #4 from yanone/main — "New fonts with kerning" — The commit referenced in the PR body
2. **d81f209** (2022-10-07): "rearrange font's weight"
3. **6cc6143** (2022-10-07): "Rearrange font's weight"
4. **7e75cfa** (2022-10-07): "Updated STAT table"
5. **f1574bf** (2022-10-07): "Updated binaries"
6. **535eeb5** (2022-10-07): Merge PR #5 from yanone/main — "Generated new font binaries after weight setup change"

The PR was merged at 2022-10-07T15:04:50Z. The final upstream commit `535eeb5` was made on the same day (2022-10-07 20:07:11 +0700 = 13:07 UTC), slightly before the google/fonts PR merge.

### Binary Verification

The variable font binary in google/fonts (`Marhey[wght].ttf`, 198,704 bytes) was verified against the upstream repo:

| Commit | File Size | SHA256 |
|--------|-----------|--------|
| `e5686e3` (PR body ref) | 198,764 bytes | (different) |
| `535eeb5` (METADATA.pb) | 198,704 bytes | `19c30686157ec965797fae8c8feb7bb142b082217227562d1a809c067df447e9` |
| google/fonts | 198,704 bytes | `19c30686157ec965797fae8c8feb7bb142b082217227562d1a809c067df447e9` |

The SHA256 hash matches exactly at commit `535eeb5`, confirming this is the correct onboarding commit. The gftools-packager hash `e5686e3` was a starting point; Yanone made additional upstream fixes (rearranging weight instances, updating the STAT table, and regenerating binaries) before the google/fonts PR was merged.

### google/fonts Commit History

| Commit | Date | Description |
|--------|------|-------------|
| `97004a80c` | 2022-10-07 | "Marhey: Version 1.000 added (#5374)" — Original onboarding |
| `1db714082` | 2023-08-16 | "The last batch of ~250 updated METADATA.pb files for stroke and classification" |
| `66f91f10f` | 2024-04-03 | "Merge upstream.yaml into METADATA.pb [skip ci]" — Added source block |
| `d9ad7cfd4` | 2025-09-18 | "sources info for Marhey" — Added config_yaml field |

## Build Configuration

The upstream repo has `source/config.yaml` at the referenced commit:

```yaml
sources:
  - Marhey.glyphs
axisOrder:
  - wght
familyName: Marhey
stat:
  Marhey[wght].ttf:
  - name: Weight
    tag: wght
    values:
    - name: Light
      value: 300
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

The config references `Marhey.glyphs` (relative to the `source/` directory), which is present as `source/Marhey.glyphs`. The configuration includes weight axis ordering and STAT table definitions for the five named instances (Light 300, Regular 400, Medium 500, SemiBold 600, Bold 700).

No override config.yaml exists in the google/fonts family directory. The `config_yaml` field in METADATA.pb correctly points to `source/config.yaml` in the upstream repo.

## Findings

1. **Source block is complete and correct**. All fields are properly populated:
   - `repository_url` points to a valid, accessible repository
   - `commit` hash `535eeb5` is verified as the correct onboarding commit (binary SHA256 match)
   - `config_yaml` correctly points to `source/config.yaml` in the upstream repo
   - `files` mappings are accurate (including the DESCRITION->DESCRIPTION filename correction)
   - `branch` is correctly set to "main"

2. **The gftools-packager commit hash was a hint, not the final truth**. The PR #5374 body referenced `e5686e3`, but the actual fonts shipped were from `535eeb5` — three commits later. This is a textbook case of the pattern described in the project memory: Yanone started work at one commit, then made additional upstream fixes before the google/fonts PR was merged.

3. **Typo in upstream filename**: The upstream repo has `DESCRITION.en_us.html` (missing the "P"). The METADATA.pb `files` block correctly maps this to `DESCRIPTION.en_us.html` in google/fonts.

4. **No activity since onboarding**: The upstream repo has had no new commits since `535eeb5` (2022-10-07). The commit referenced in METADATA.pb is the latest and final commit in the repository.

5. **No corrections needed**. The existing source block is accurate and complete.

## Recommended Source Block

The current source block is correct and complete. No changes needed:

```
source {
  repository_url: "https://github.com/namelatype/Marhey"
  commit: "535eeb5a3f4dee825fdaf13d84075b212d969f8d"
  config_yaml: "source/config.yaml"
  files {
    source_file: "OFL.txt"
    dest_file: "OFL.txt"
  }
  files {
    source_file: "fonts/variable/Marhey[wght].ttf"
    dest_file: "Marhey[wght].ttf"
  }
  files {
    source_file: "DESCRITION.en_us.html"
    dest_file: "DESCRIPTION.en_us.html"
  }
  branch: "main"
}
```

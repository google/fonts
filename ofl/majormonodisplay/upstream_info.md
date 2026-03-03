# Major Mono Display — Source Investigation

**Model**: Claude Opus 4.6
**Date**: 2026-03-03
**Status**: needs_correction

## METADATA.pb Source Block (current)

```
source {
  repository_url: "https://github.com/googlefonts/majormono"
  commit: "fae0bb9c728fe082097baedaf23604e290ddac16"
}
```

An override `config.yaml` exists in the google/fonts family directory (not referenced in METADATA.pb, which is correct behavior for local overrides).

## Repository Analysis

- **Repository**: https://github.com/googlefonts/majormono
- **Owner**: googlefonts
- **Default branch**: master
- **Total commits**: 33
- **Latest commit**: `fae0bb9` (2018-10-12) — "Updated description" (README-only change)
- **Repository appears inactive** — no commits since October 2018.

### Source Files

The upstream repo contains a UFO source at `sources/MajorMonoDisplay.ufo/` along with supporting files:
- `sources/MajorMonoDisplay.ufo/` — the primary UFO source
- `sources/MajorMonoDisplay.vfc` — FontLab VFC source
- `sources/MajorMonoDisplay.vfj` — FontLab VFJ source
- `sources/liga.fea` — ligature OpenType feature file
- `sources/encodings/` — encoding files
- `sources/mono-fix.py` — monospace fix script
- `fonts/MajorMonoDisplay-Regular.ttf` — pre-compiled binary

### Config.yaml in Upstream

No `config.yaml` was found in the upstream repository. An override `config.yaml` was created in the google/fonts family directory with the following content:

```yaml
buildVariable: false
sources:
  - sources/MajorMonoDisplay.ufo
```

## Onboarding History

The font was onboarded to Google Fonts on **2018-12-05** via PR #1710 by Marc Foley (m4rc1e).

### Key Commits in google/fonts

| Commit | Date | Author | Description |
|--------|------|--------|-------------|
| `a6169376b` | 2018-12-05 | Marc Foley | Original onboarding: "Add majormonodisplay (v2.000, #1710)" |
| `e75f82401` | 2023-12-14 | Simon Cozens | Added source block with repository_url (no commit hash) |
| `7ed21ec31` | 2025-12-01 | Felipe Sanches | Added commit hash `fae0bb9` and override config.yaml |

### PR #1710 Details

The PR body explicitly stated:

> "Taken from the upstream repo https://github.com/googlefonts/majormono at commit https://github.com/googlefonts/majormono/commit/ab4221e332ee158b314406b4ca01246290a9168b"

This means the **original onboarding commit was `ab4221e`**, not `fae0bb9` as currently recorded in METADATA.pb.

### Commit Hash Discrepancy Analysis

- **`ab4221e`** (2018-09-27) — "Updated ttf" — This was the commit explicitly cited in PR #1710. It updated the binary TTF file.
- **`fae0bb9`** (2018-10-12) — "Updated description" — This is HEAD of the repo. It only modified `README.md`.

Between these two commits, three intermediate commits occurred:
1. `4768f4b` (2018-10-02) — "Updated description text" (README change only)
2. `948c59c` (2018-10-02) — Merge branch (merge commit)
3. `fae0bb9` (2018-10-12) — "Updated description" (README change only)

**Binary verification**: The TTF file is identical at both commits (MD5: `46295860df2cad9c67a9501459838b7c`), and it matches the TTF in google/fonts exactly. The source files under `sources/` are also unchanged between the two commits.

While using `fae0bb9` (HEAD) is technically harmless since the font binary and sources are identical, the correct commit per the onboarding record is `ab4221e`. Per project policy, the commit hash should reflect the commit originally used for onboarding, not a later commit with unrelated changes.

## Build Configuration

- **No config.yaml in upstream**: The upstream repository does not contain a `config.yaml` file.
- **Override config.yaml in google/fonts**: An override was created at `ofl/majormonodisplay/config.yaml`.
- **Build type**: Static only (`buildVariable: false`)
- **Source**: `sources/MajorMonoDisplay.ufo` — a single-master UFO source for the Regular weight.
- **Note**: The `config_yaml` field is correctly omitted from METADATA.pb since google-fonts-sources auto-detects local overrides.

## Findings

1. **Commit hash needs correction**: The METADATA.pb currently records `fae0bb9c728fe082097baedaf23604e290ddac16` (HEAD of repo, a README-only change), but the original onboarding PR #1710 explicitly cited `ab4221e332ee158b314406b4ca01246290a9168b`. While the binary is identical at both commits, the commit should be corrected to match the documented onboarding point.

2. **Override config.yaml is correct**: The upstream repo has no config.yaml, so the override in google/fonts is necessary. The config references `sources/MajorMonoDisplay.ufo`, which exists in the upstream repo at both the cited commit and HEAD.

3. **Binary match confirmed**: The TTF in google/fonts (`46295860df2cad9c67a9501459838b7c`) matches the upstream binary at both `ab4221e` and `fae0bb9` exactly.

4. **Repository is inactive**: The upstream repo has not received any commits since October 2018. The designer is Emre Parlak, and the font engineer contributor was Mike LaGattuta (mjlagattuta).

5. **Single font family**: This is a single-weight (Regular 400) static font. No variable font axes are involved.

## Recommended Source Block

```
source {
  repository_url: "https://github.com/googlefonts/majormono"
  commit: "ab4221e332ee158b314406b4ca01246290a9168b"
}
```

The commit hash should be corrected from `fae0bb9c728fe082097baedaf23604e290ddac16` to `ab4221e332ee158b314406b4ca01246290a9168b` to match the commit explicitly cited in onboarding PR #1710. The `config_yaml` field should remain omitted since an override config.yaml exists in the google/fonts family directory.

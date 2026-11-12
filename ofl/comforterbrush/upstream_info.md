# Comforter Brush - Investigation Report

## Source Data

| Field | Value |
|-------|-------|
| Family Name | Comforter Brush |
| Designer | Robert Leuschke |
| Repository URL | https://github.com/googlefonts/comforter-brush |
| Commit | `4f308116699899ec59db6b7596e00912abd4ebef` |
| Branch | main |
| Config YAML | `sources/config.yaml` |
| Override Config | No |
| Date Added | 2021-09-17 |
| License | OFL |

## How URL Found

The repository URL `https://github.com/googlefonts/comforter-brush` is documented in the METADATA.pb source block. It was originally set via the `upstream.yaml` file created during onboarding (PR #3846) and later merged into METADATA.pb by Simon Cozens (commit `66f91f10f`, April 2024). The URL also appears in the copyright string.

## How Commit Determined

The commit hash `4f308116699899ec59db6b7596e00912abd4ebef` was ported from the fontc_crater targets list (commit `19cdcec59` in google/fonts, March 2025). This commit is the HEAD of the `main` branch in the upstream repo.

**Onboarding history:**
1. **Initial onboarding** (PR #3846, 2021-09-22): Used commit `b766cd284bccca94e617e03b167e3a1dc0582779` (Version 1.010)
2. **Update** (PR #3886, 2021-09-30): Used commit `f202772314cb1160cc65aef8cf2e932889a84782` (Version 1.013 with fina fix)
3. **Current METADATA.pb**: References `4f30811` which is the HEAD of the repo

The difference between the last font update commit (`f202772`) and HEAD (`4f30811`) consists only of:
- `README.md`: 2 lines added (sample image link)
- `documentation/image1.png`: minor image change

No source files or font files were modified between these commits, so using HEAD is acceptable for build reproducibility.

## Config YAML Status

The upstream repository has `sources/config.yaml` at the HEAD commit. The config file contains:

```yaml
sources:
  - ComforterBrush-Pro.glyphs
familyName: "Comforter Brush"
buildVariable: false
autohintTTF: false
```

## Verification

- **Commit exists in upstream**: Yes - it is the HEAD of `main` branch
- **Branch matches**: Yes - `main` branch, matches METADATA.pb
- **Config YAML exists at commit**: Yes - `sources/config.yaml` exists
- **Font files match**: The fonts were built from `ComforterBrush-Pro.glyphs` source
- **Repository accessible**: Yes, cached at `upstream_repos/fontc_crater_cache/googlefonts/comforter-brush/`

## Confidence Level

**HIGH** - All data is verified. While the METADATA.pb commit is HEAD rather than the exact onboarding commit, the difference is only non-font documentation changes. The font binaries in google/fonts correspond to Version 1.013 built from commit `f202772`, and HEAD (`4f30811`) contains identical source files.

## Open Questions

None. The minor discrepancy between the font update commit and METADATA.pb commit is cosmetic (only README/image changes), not affecting build reproducibility.

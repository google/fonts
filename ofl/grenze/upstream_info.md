# Investigation Report: Grenze

## Summary

Grenze is a serif font family designed by Omnibus-Type, added to Google Fonts on 2018-09-19. The upstream repository is `Omnibus-Type/Grenze` on GitHub. The original onboarding commit `00affb70f8e0bb8ab7c9adfd5b5067a5a2ae2d8d` (referenced in the google/fonts commit message) no longer exists in the upstream repo -- the repo was rewritten/squashed into a single commit `a2a182c7b828c3d6a1784ef08b22be8521b2b9a7` from 2021. The METADATA.pb currently references the newer commit `a2a182c`, which came from the fontc_crater targets list. The `config.yaml` exists at `sources/config.yaml` but has issues: it references `Grenze.glyphs` and `Grenze-Italic.glyphs` relative to its location, but `Grenze.glyphs` is in `Sources/` (capital S) while `Grenze-Italic.glyphs` is in `sources/` (lowercase s). The config also contains a STAT table referencing `Texturina[wght].ttf`, which appears to be a copy-paste error from another font family.

## Key Findings

| Field             | Value                                                              |
|-------------------|--------------------------------------------------------------------|
| Family Name       | Grenze                                                             |
| Repository URL    | https://github.com/Omnibus-Type/Grenze                             |
| Commit Hash       | `a2a182c7b828c3d6a1784ef08b22be8521b2b9a7` (only surviving commit) |
| Original Onboarding Hash | `00affb70f8e0bb8ab7c9adfd5b5067a5a2ae2d8d` (lost due to repo rewrite) |
| Config Path       | `sources/config.yaml`                                              |
| Source Files      | `Sources/Grenze.glyphs`, `sources/Grenze-Italic.glyphs`           |
| Status            | **needs_correction**                                               |
| Confidence        | **MEDIUM**                                                         |

## Investigation Details

### METADATA.pb Analysis

The current METADATA.pb source block contains:
- `repository_url`: `https://github.com/Omnibus-Type/Grenze`
- `commit`: `a2a182c7b828c3d6a1784ef08b22be8521b2b9a7`
- `config_yaml`: `sources/config.yaml`

No file mappings or branch field are present.

### Google Fonts Commit History

1. **`fda381241`** (2018-09-19) - "grenze: v1.002 added" by Marc Foley. Original onboarding commit. The commit message states: "Taken from the upstream repo https://github.com/Omnibus-Type/Grenze at commit https://github.com/Omnibus-Type/Grenze/commit/00affb70f8e0bb8ab7c9adfd5b5067a5a2ae2d8d". This added 18 TTF files (9 weights x 2 styles).
2. **`2423d2aef`** (2023-12-14) - "Update upstreams" by Simon Cozens. Added the source block with only `repository_url`.
3. **`19cdcec59`** (2025-03-31) - "[Batch 1/4] port info from fontc_crater targets list" by Felipe Sanches. Added `commit` and `config_yaml` fields.

### Upstream Repository Verification

The upstream repo at `Omnibus-Type/Grenze` is cached at `upstream_repos/fontc_crater_cache/Omnibus-Type/Grenze/`. Key observations:

- **Single commit**: The repo contains only one commit: `a2a182c` (2021-04-14, "Updated sources and added config.yaml file and requirements.txt" by Yorlmar Campos).
- **Original commit lost**: The onboarding commit `00affb70` referenced in the google/fonts commit message does not exist in any branch. The repository was evidently force-pushed/rewritten at some point after the 2018 onboarding, replacing all history with a single squashed commit from 2021.
- **Timeline mismatch**: The single surviving commit is from 2021-04-14, but the onboarding happened on 2018-09-19. The commit `a2a182c` post-dates the onboarding by nearly 3 years.
- **Branches**: Only `master` branch exists.
- **Clean state**: The repo is clean with no uncommitted changes.

### Config File Analysis

The config file at `sources/config.yaml` contains:
```yaml
    sources:
      - Grenze.glyphs
      - Grenze-Italic.glyphs
    axisOrder:
      - wght
      - ital
    familyName: Grenze
    stat:
      Texturina[wght].ttf:
      ...
```

**Issues identified:**

1. **Incorrect STAT table reference**: The STAT table section references `Texturina[wght].ttf` instead of `Grenze[wght].ttf`. This is clearly a copy-paste error from the Texturina font family (also by Omnibus-Type).

2. **Mixed-case directory problem**: The config references `Grenze.glyphs` and `Grenze-Italic.glyphs` relative to the `sources/` directory. However:
   - `Grenze-Italic.glyphs` is correctly in `sources/`
   - `Grenze.glyphs` is in `Sources/` (capital S), NOT in `sources/` (lowercase s)

   This means the config would fail on case-sensitive file systems (like Linux) because it cannot find `Grenze.glyphs` in the `sources/` directory.

### Source Files

The repo has two directories with source files:
- `Sources/` (capital S): Contains `Grenze.glyphs`, `Backup/` and `master_ufo/` directories
- `sources/` (lowercase s): Contains `config.yaml`, `Grenze-Italic.glyphs`, `Archived/`, `Backup/`, and `master_ufo/` directories

### Font Files in Upstream

The `fonts-/` directory contains pre-built font files in `gx/`, `otf/`, `ttf/`, and `webfonts/` subdirectories.

## Conclusion

The METADATA.pb source block has the correct repository URL. The commit hash `a2a182c` is the only available commit (the original `00affb70` was lost to a repo rewrite), so it is the best we can reference. However, important caveats apply:

1. **The commit `a2a182c` (2021) is NOT the original onboarding commit (2018)**. The fonts currently in google/fonts were built from the lost commit `00affb70`. The 2021 commit may contain different source files than what was originally used.
2. **The config.yaml has errors** (Texturina reference, mixed-case directory issue) that would prevent a clean build on Linux.
3. **The static TTF files in google/fonts were not rebuilt from this config** -- they were pre-compiled binaries taken directly from the upstream at the original 2018 commit.

Given these issues, the source block points to the only surviving commit but should be understood as an approximation. The config.yaml has known issues that would need fixing before any rebuild.

### Current METADATA.pb Source Block

```
source {
  repository_url: "https://github.com/Omnibus-Type/Grenze"
  commit: "a2a182c7b828c3d6a1784ef08b22be8521b2b9a7"
  config_yaml: "sources/config.yaml"
}
```

### Assessment

The current source block is the best available given the repo rewrite. The commit `a2a182c` is the only commit that exists, so while it is not the original onboarding commit, it is the only reference point available. The `config_yaml` field correctly points to the config file in the repo, though that config file itself has issues (wrong STAT reference, case-sensitivity problem). Status is **needs_correction** because the config.yaml in the upstream repo has errors that would prevent a clean build, and the original onboarding commit is lost.
